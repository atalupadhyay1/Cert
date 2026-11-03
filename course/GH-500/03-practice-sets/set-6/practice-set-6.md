# Microsoft / GitHub Exam GH-500: GitHub Advanced Security — Full-Length Mock Exam 6

**Theme:** Security Suites Administration, Security Configurations, GHEC vs GHES, Committer/AI Billing & REST APIs  
**Credential:** `GitHub Advanced Security` *(Intermediate · **no prerequisite** · **2-year validity** transitioning to Microsoft Learn recertification)*  
**Study guide baseline:** `July 2026 (Last updated May 14, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-500 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Advanced Security documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Describe GitHub Security suites, features, and ecosystem (15–20% official weight · 18 questions)

### 1. BaryonMed Genomics runs an academic-collab bioinformatics org on `GitHub Team` (`cryoem-reconstruct-py`, `clinvar-annotator`) and wants `GitHub Code Security` immediately while licensing `GitHub Secret Protection` across both `GitHub Team` and `GitHub Enterprise`. How does GitHub structure these SKUs?

- **A.** Standalone `GitHub Secret Protection` and `GitHub Code Security` SKUs (`purchasable separately or together on GitHub Team and GitHub Enterprise`, alongside legacy bundled GHAS)
- **B.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **C.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 2. BaryonMed Genomics' CAP/CLIA audit lead asks which GitHub Security pillar addresses leaked Illumina BaseSpace tokens, memory-corruption flaws in `fastq-aligner-cpp`, and vulnerable Biopython/Rails packages in `biobank-lims-rails`. Which mapping is accurate?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** `Secret Protection` (`secret scanning + push protection`), `Code Security` (`CodeQL/SARIF SAST + Copilot Autofix`), and `Supply Chain Security` (`Dependency Graph, Dependabot, Dependency Review & SBOMs`)
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 3. BaryonMed Genomics' research-computing steering committee is allocating FY27 funds between `GitHub Secret Protection` and `GitHub Code Security` across 75 private genomics repositories. Which two statements accurately define each SKU's scope? Select two.

- **A.** `GitHub Code Security` finds and fixes code and dependency risks via `CodeQL` / `SARIF` code scanning, `Copilot Autofix`, `Dependency Review` on private repos, and `Security Campaigns`
- **B.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** `GitHub Secret Protection` prevents and detects leaked credentials via `Push Protection`, `secret scanning`, `validity checks`, custom patterns, and AI generic secret detection
- **E.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 4. BaryonMed Genomics publishes an open-source VCF parser (`open-vcf-stream`) in a `public` GitHub.com repo while hosting `pharmacogenomics-kb` as a `private` GHEC repository. How do free versus licensed security features differ?

- **A.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** Core features (`secret scanning, push protection, Dependency Graph, Dependabot, CodeQL default setup & Dependency Review`) are free on `public` GitHub.com repos; `private/internal` repos require licensed SKUs where applicable
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 5. BaryonMed Genomics tagged 48 patient-cohort repositories with custom property `gdpr_genomic_data:yes` and needs one enterprise view comparing scanner enablement gaps, open critical alerts, and remediation campaign burndown (`____`). Which hub provides this?

- **A.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **B.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **C.** `Security Overview` (`Organization & Enterprise Risk, Coverage, Campaigns, Code scanning, Secret scanning & Dependabot dashboards` filterable by team, topic, or custom property)
- **D.** `.github/codeql/codeql-config.yml` (`defining packs:, queries:, paths-ignore:, and threat-models: alongside YAML model-pack extensions`)

### 6. BaryonMed Genomics acquired a proteomics spin-out running an unlicensed GitHub org and wants a free baseline scan of private repos for leaked AWS/GCP keys plus a CodeQL + Copilot Autofix preview on up to `20` active repos. Which Security Overview option (`____`) runs this?

- **A.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **B.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **C.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **D.** Organization `free security risk assessment` (`scanning org repos for leaked secrets and up to 20 active repositories for CodeQL vulnerabilities + Copilot Autofix preview`)

### 7. On `sequencer-instrument-cs`, Secret Protection intercepted an Azure Blob SAS token inside an `.xml` instrument manifest at `git push`, while CodeQL flagged an unsafe deserialization sink in `RunManifestLoader.cs` on the pull request. How do the two engines complement each other?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** `Secret Protection` matches structured/high-entropy/AI secret tokens across Git history & pushes, whereas `Code Security (CodeQL)` traces semantic AST/dataflow vulnerabilities (`including hardcoded-credential sinks`)

### 8. BaryonMed Genomics wants `consent-ledger-go` protected pre-merge against leaked biobank keys, copyleft or vulnerable Go modules, and Go SQL/path-injection bugs. Which combined developer-workflow controls achieve all three?

- **A.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **B.** Layer `Push Protection` (`pre-receive`), `actions/dependency-review-action` (`PR manifest/license gate`), and `CodeQL` PR checks (`with Copilot Autofix`) so secrets, vulnerable packages, and taint flaws fail pre-merge
- **C.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 9. BaryonMed Genomics wants `pedigree-cohort-ui` (`TypeScript`) configured so cloud tokens are rejected before entering Git history and XSS taint flows receive automated PR fix suggestions before merge. Proposed solution: Enable `GitHub Secret Protection` (`with Push Protection`) and `GitHub Code Security` (`CodeQL Default Setup` with `Copilot Autofix`), enforcing CodeQL in an active branch ruleset. Does this meet every requirement?

- **A.** No — `actions/dependency-review-action` forbids specifying `allow-licenses` and `deny-licenses` together, and fails to block merges unless marked as a required status check on `pull_request`
- **B.** No — dismissing a Secret Protection alert or deleting the line in a new commit leaves the live credential active and exposed in prior Git history (`revoke & rotate first, then purge history`)
- **C.** No — `.github/secret_scanning.yml` `paths-ignore` only auto-closes post-push user alerts (`<=1,000` paths / `<=1 MB`) and neither revokes keys nor replaces Push Protection / public partner alerts
- **D.** Yes — this configuration satisfies every security, licensing, and governance requirement

### 10. BaryonMed Genomics is replacing an annual biobank compliance freeze on `biobank-lims-rails` with a shift-left secure SDLC across GitHub Security suites. Which four-step chronological sequence implements prevention-first operations?

- **A.** Dismiss all PR alerts automatically → merge vulnerable dependencies → run Dependency Review only on archived branches → rely on gitignore to revoke leaked API tokens
- **B.** Apply Copilot Autofix before running CodeQL → run Push Protection only after merging to main → skip Dependency Review on lockfiles → delete Security Overview roles
- **C.** Block secrets pre-receive via Push Protection → run Dependency Review & CodeQL on the PR → apply Copilot Autofix or patch vulnerable packages before merge → monitor default-branch advisories in Security Overview
- **D.** Merge PRs without checks to main → run weekly manual secret scans → disable Push Protection to avoid developer friction → export CSVs quarterly without remediating open alerts

### 11. Why did BaryonMed Genomics' old practice of running static scans only on annual release branches cause far higher remediation cost than running Push Protection and PR-time CodeQL + Dependency Review on `variant-caller-java`?

- **A.** Prevention-first (`Push Protection + IDE/PR Dependency Review + PR CodeQL with Copilot Autofix`) stops defects before Git history/merge, whereas late release-only gates cause expensive rework
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 12. BaryonMed Genomics wants seven bioinformatics squads to burn down 380 legacy SQL-injection, command-injection, and path-traversal alerts on default branches ahead of ISO 27001 surveillance, guided by a named AppSec advisor. Which feature (`____`) coordinates this?

- **A.** `Security Campaigns` (`targeted, time-bound initiatives grouping up to 1,000 default-branch alerts with a named security contact and Copilot Autofix support`)
- **B.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 13. On `hla-typing-engine`, a senior developer dismisses a CodeQL alert triggered inside a synthetic benchmark harness as `Used in tests`. What audit metadata does GitHub retain for ISO 27001 assessors?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Dismissing an alert requires a structured closure reason (`False positive`, `Used in tests`, `Won't fix`) plus an audit-logged justification comment—and never deletes commits or revokes keys
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses

### 14. A pipeline researcher pushed a live AWS S3 genomics-bucket secret key to `cryoem-reconstruct-py` and received a Secret Protection alert. Proposed solution: Dismiss the alert as `Won't fix` and add `.aws/` to `.gitignore` on `main` without rotating the IAM key. Does this remediate the leak?

- **A.** No — CodeQL `Default Setup` and custom `Advanced Setup` (`.github/workflows/codeql.yml`) cannot run active CodeQL management simultaneously (`switch to Advanced Setup with build-mode: manual`)
- **B.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)
- **C.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **D.** No — dismissing a Secret Protection alert or deleting the line in a new commit leaves the live credential active and exposed in prior Git history (`revoke & rotate first, then purge history`)

### 15. BaryonMed Genomics' GDPR Data Protection Officer wants verifiable governance over every security alert dismissed without a code fix. Which two controls belong in BaryonMed's SOP? Select two.

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** Require an accurate dismissal reason (`False positive`, `Used in tests`, or `Won't fix`) with a reviewer-auditable justification comment whenever dismissing an alert
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **E.** Monitor dismissed and open alert trends centrally in `Security Overview` and `Audit Logs` (`repository_vulnerability_alert`, `secret_scanning_alert`, `code_scanning_alert`)

### 16. How should BaryonMed Genomics structure day-to-day responsibilities across Cloud Platform Admins, Genomics AppSec (`Security Managers`), and Bioinformatics Pipeline Developers?

- **A.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **B.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Shared security model: `Admins` govern licensing/Security Configurations, `Security Managers` monitor Security Overview/campaigns/policies, and `Developers` remediate PR & campaign findings

### 17. Why does BaryonMed Genomics restrict raw Secret Protection alert access on `biobank-lims-rails` to least-privilege roles while enforcing Push Protection `delegated bypass`?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Least-privilege alert access (`Write/Maintain/Admin/Security Manager` or custom roles) paired with `delegated bypass` so designated reviewers audit push-protection exceptions
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 18. BaryonMed Genomics' pharmaceutical partners require clear DevSecOps role boundaries, audited push-protection exceptions, and full transitive dependency tracking across Maven and C++ sequencing builds. Which three practices fulfill those requirements? Select three.

- **A.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **B.** `Dependency Graph` (`parsing committed manifests and lockfiles`, augmented by the `Dependency Submission API` for build-time resolved transitive graphs in Maven/Gradle/C++/containers)
- **C.** Shared security model: `Admins` govern licensing/Security Configurations, `Security Managers` monitor Security Overview/campaigns/policies, and `Developers` remediate PR & campaign findings
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **E.** Least-privilege alert access (`Write/Maintain/Admin/Security Manager` or custom roles) paired with `delegated bypass` so designated reviewers audit push-protection exceptions
- **F.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

---

## Domain 2 — Configure and use Secret Protection (formerly secret scanning) (15–20% official weight · 18 questions)

### 19. BaryonMed Genomics provisions 6 new cohort-analysis repositories monthly inside `baryonmed-genomics` and wants `Secret scanning`, `Push Protection`, and `Validity checks` enabled across all existing and newly created repositories automatically. Which feature (`____`) enforces this?

- **A.** Enable `GitHub Secret Protection` (`secret scanning + push protection`) via Organization/Enterprise `Security Configurations` (`with Apply to new repositories`) or Repository `Settings -> Advanced Security`
- **B.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 20. A postdoctoral fellow accidentally commits a Google Cloud service-account key to BaryonMed's `public` `open-vcf-stream` repo, while another commits a key to the `private` `clinvar-annotator` repo (`with Secret Protection enabled`). How does GitHub handle partner notifications?

- **A.** On `public` repos, partner patterns run free and auto-notify token providers for revocation; on `private/internal` repos (`with Secret Protection`), alerts notify repo/org users (`plus optional validity checks`)
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 21. BaryonMed Genomics' Enterprise Owner sets `Repository administrators can enable or disable GitHub Secret Protection = Disabled` at the enterprise level. Does that turn off Secret Protection on the 75 private repos already enabled, or block `Security Managers`?

- **A.** Enforce Enterprise Advanced Security policies (`restricting repo admins while preserving Org Owner/Security Manager control`), scope ruleset/push-protection bypass actors, and stream `security_configuration.*` / alert audit logs
- **B.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations

### 22. A bioinformatician pushes a Jupyter notebook commit from CLI containing an OpenAI live key inside `cryoem-reconstruct-py`, and GitHub rejects the push pre-receive with `GH013`. Which Secret Protection control (`____`) stopped the key from entering Git history?

- **A.** `Push Protection` intercepts supported high-confidence and published custom secrets pre-receive during `git push` (`CLI, IDE, web editor & REST API`), blocking the secret from entering Git history
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)

### 23. On `biobank-lims-rails`, Secret Protection displays `Validity: Active` on 3 Slack/AWS tokens, `Inactive` on 14 old tokens, and no validity badge on 4 non-provider generic MySQL URLs. Why do the MySQL URLs lack partner validity checks, and which alerts take top priority?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **C.** `Validity checks` query partner token endpoints (`displaying Active, Inactive, or Unknown`) so responders prioritize live `Active` credentials first
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 24. BaryonMed Genomics wants `sequencer-instrument-cs` protected against both standard cloud provider tokens at push time and unstructured laboratory LIMS passwords in `.config` files. Which two Secret Protection features should be enabled? Select two.

- **A.** `Non-provider / generic pattern scanning` (`private keys, DB connection strings`) plus `Copilot AI generic secret detection` (`unstructured passwords/keys`, consuming `Secret Protection AI credits` on push)
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **D.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **E.** `Push Protection` blocks high-confidence partner and published custom secrets pre-receive during `git push` before commits land on GitHub

### 25. Secret Protection reports an `Active` Okta admin API token committed 15 minutes ago to `consent-ledger-go`. In what chronological order must BaryonMed Genomics' incident response team act?

- **A.** Add paths-ignore in .github/secret_scanning.yml to auto-close the live production key alert → keep the credential unrotated → merge to main → archive the audit log
- **B.** Dismiss the alert as Won't fix → delete the line in a new commit while keeping the live key active → add the file to .gitignore → assume old commits are unreadable
- **C.** Confirm alert validity & blast radius → revoke and rotate the compromised credential at the provider → purge commit history (`git filter-repo`) & contact Support if cached PRs remain → resolve the alert as Revoked
- **D.** Run git filter-repo first while leaving the production key active for 30 days → disable Secret Protection to clear UI banners → rotate the key only if an outage occurs → skip audit notes

### 26. After revoking a leaked LIMS database password and rewriting branch history with `git filter-repo` on `biobank-lims-rails`, why might BaryonMed Genomics still contact GitHub Support during cleanup?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **D.** Treat every committed secret as compromised: `revoke & rotate at the issuing provider immediately`, rewrite Git history (`git filter-repo`), purge cached views via Support if needed, and resolve as `Revoked`

### 27. Once BaryonMed's cloud admin revokes an `Active` AWS access key flagged in `pharmacogenomics-kb`, how can the Security Manager verify revocation directly from the Secret Protection alert view before marking it `Revoked`?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** `Validity checks` query partner token endpoints (`displaying Active, Inactive, or Unknown`) so responders prioritize live `Active` credentials first
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config

### 28. BaryonMed Genomics wants researchers who trigger a false-positive Push Protection block on `clinvar-annotator` to submit a structured bypass request approved by `@baryonmed/genomics-sec-reviewers` rather than self-overriding. Which feature (`____`) implements this?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** `Delegated bypass for push protection` (`granting Specific roles, visible teams, or custom roles with "Review and manage secret scanning bypass requests" authority—never secret teams`)
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 29. BaryonMed Genomics wants Push Protection bypass requests on `biobank-lims-rails` approved exclusively by a hidden **secret team** (`@baryonmed/stealth-ir`) and configured via `.github/secret_scanning.yml`. Proposed solution: Add the secret team `@baryonmed/stealth-ir` to Push Protection delegated bypass (`or list them in .github/secret_scanning.yml`). Is this supported?

- **A.** No — Code Scanning rejects gzip-compressed SARIF files larger than `10 MB` (`and overwrites prior alerts when multiple matrix uploads share an identical SARIF category on one commit`)
- **B.** No — `.github/secret_scanning.yml` `paths-ignore` only auto-closes post-push user alerts (`<=1,000` paths / `<=1 MB`) and neither revokes keys nor replaces Push Protection / public partner alerts
- **C.** No — temporary private forks created inside a Repository Security Advisory (`GHSA`) intentionally **disable GitHub Actions** (`and pushing fixes to a public branch before release leaks the zero-day`)
- **D.** Yes — this configuration satisfies every security, licensing, and governance requirement

### 30. BaryonMed Genomics wants clinical biosecurity officers in Boston and Zurich to approve or deny Push Protection bypass requests without granting full `Security Manager` or `Organization Owner` privileges. Which two rules apply? Select two.

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Assign `Specific roles, visible teams, or custom org roles` (`never secret teams`) to the Push Protection delegated bypass list to review and approve contributor bypass requests
- **D.** `Review and manage secret scanning bypass requests` (`fine-grained organization role permission for Push Protection delegated bypass`)
- **E.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations

### 31. `pedigree-cohort-ui` stores 300 synthetic OAuth test fixtures inside `cypress/fixtures/mock_oauth/**`. Which repository file and YAML key (`____`) suppresses user Secret Protection alerts in that folder, and what limits apply?

- **A.** `.github/codeql/codeql-config.yml` (`defining packs:, queries:, paths-ignore:, and threat-models: alongside YAML model-pack extensions`)
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **D.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`

### 32. When BaryonMed Genomics commits `.github/secret_scanning.yml` adding `paths-ignore: ["test/synthetic_keys/**"]` to private `hla-typing-engine`, what happens to the 14 existing open user secret alerts inside `test/synthetic_keys/`—and would public-repo partner revocation alerts be suppressed?

- **A.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **B.** `.github/secret_scanning.yml` with `paths-ignore:` (`up to 1,000 glob entries and <= 1 MB file size`) auto-closing user alerts in test/docs paths (`without suppressing public-repo partner revocation alerts`)
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 33. BaryonMed Genomics wants two principal bioinformatics leads (`Maintain` access on `fastq-aligner-cpp`) to view and resolve Secret Protection alerts on `fastq-aligner-cpp` alone without making them Repository Admins or org-wide Security Managers. How is this configured?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Separate `Enterprise/Org Owners` (`billing & global policy`), `Security Managers` (`org-wide alert read/write & security config management, without code-write`), and custom repository roles (`granular view/dismiss per tool`)
- **C.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 34. BaryonMed Genomics issues sequencer run tokens formatted as `BMED_SEQ_[A-Z2-7]{32}` and uses `Generate with AI` in the organization custom-pattern editor to build the regex. Which step (`____`) must complete before `Publish pattern` and Push Protection become available?

- **A.** Custom regex patterns (`up to 100/repo or 500/org-or-enterprise`, optional `Generate with AI` & `before`/`after` context) validated via `Save and dry run` (`<=1,000` sample hits) before `Publish pattern` & Push Protection
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **D.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config

### 35. Compare custom secret pattern quotas (`repository` vs `organization/enterprise`), who can edit an **enterprise-level** custom pattern, and what happens to open alerts when a published custom pattern's regex is edited and saved.

- **A.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Custom regex patterns (`up to 100/repo or 500/org-or-enterprise`, optional `Generate with AI` & `before`/`after` context) validated via `Save and dry run` (`<=1,000` sample hits) before `Publish pattern` & Push Protection
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 36. BaryonMed Genomics is finalizing its Secret Protection architecture review across 75 biobank and sequencing repositories. Which three technical behaviors are accurate? Select three.

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Custom regex patterns (`up to 100/repo or 500/org-or-enterprise`, optional `Generate with AI` & `before`/`after` context) validated via `Save and dry run` (`<=1,000` sample hits) before `Publish pattern` & Push Protection
- **C.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **E.** `Push Protection` blocks high-confidence partner and published custom secrets pre-receive during `git push` before commits land on GitHub
- **F.** Audit every Push Protection bypass request, approval, and exemption via `secret_scanning_push_protection_bypass` audit events, alert timelines, and webhooks

---

## Domain 3 — Configure and use supply chain security (formerly Dependabot/Dependency Review) (15–20% official weight · 18 questions)

### 37. `fastq-aligner-cpp` compiles C++ HTSlib/zlib packages via Conan in CI, while `variant-caller-java` resolves Gradle BOMs dynamically at build time. How should BaryonMed Genomics populate complete transitive trees into GitHub's Dependency Graph?

- **A.** `Dependency Graph` (`parsing committed manifests and lockfiles`, augmented by the `Dependency Submission API` for build-time resolved transitive graphs in Maven/Gradle/C++/containers)
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 38. Clinical hospital customers require BaryonMed Genomics to attach a machine-readable `SPDX` JSON SBOM to every release of `sequencer-instrument-cs`. Which GitHub REST API endpoint (`____`) exports this SBOM?

- **A.** `POST /orgs/{org}/code-security/configurations/{configuration_id}/attach` (`attaching a Security Configuration across selected or all org repos via REST`)
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`exporting the repository dependency inventory in SPDX JSON format`)
- **D.** `codeql github upload-results --repository=<org/repo> --ref=<refs/heads/main> --commit=<sha> --sarif=<results.sarif>`

### 39. A product manager asks whether exporting the SPDX SBOM from `open-vcf-stream` will show which pharmaceutical companies' GitHub repositories depend on `open-vcf-stream`. Why is the answer no?

- **A.** Export an `SPDX` JSON Software Bill of Materials (`SBOM`) via `Insights -> Dependency graph -> Export SBOM`, `GET /repos/{owner}/{repo}/dependency-graph/sbom`, or `actions/attest-sbom` (`excluding dependents`)
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **D.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step

### 40. Frontend engineers on `pedigree-cohort-ui` at BaryonMed Genomics complain about noisy `devDependencies` pager alerts and unwanted low-probability upgrade PRs; leadership wants automated PRs triggered solely when `EPSS >= 0.07` with an available fix. In what chronological order should AppSec configure Dependabot?

- **A.** Enable Dependency Graph & Dependabot alerts → disable global `Dependabot security updates` where custom PR rules govern → create an org/repo auto-triage rule targeting EPSS/severity/scope → audit `resolution:auto-dismiss` & targeted PRs
- **B.** Put auto-triage EPSS rules inside .github/secret_scanning.yml → expect repo rules to override enforced org rules → delete audit logs → manually email developers before rules evaluate
- **C.** Disable Dependabot alerts completely → keep global Dependabot security updates enabled → create an `Open a pull request` rule for malware alerts → expect dismissed dev alerts never to reopen on runtime promotion
- **D.** Export an SPDX SBOM → delete package-lock.json so transitive packages disappear → enable `Dismiss package malware alerts` to block zero-days → skip reachability review

### 41. On `cryoem-reconstruct-py`, Dependabot shows `scipy` (`CVSS 8.4 High`, `EPSS 0.002`, `Unreachable`) and `aiohttp` (`CVSS 7.6 High`, `EPSS 0.86`, `Reachable` across 3 API upload endpoints in `runtime`). How do `EPSS` and `Reachability` prioritize these alerts?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **D.** Prioritize `Dependabot alerts` combining `EPSS` (`30-day exploitation probability`), `CVSS` severity, `Reachability` call-path analysis (`Reachable` vs `Unreachable`), `runtime` scope, and `patch availability`

### 42. BaryonMed Genomics' CAP/CLIA auditor asks how AppSec ranks Dependabot backlogs and verifies which alerts were automatically dismissed by policy. Which two capabilities answer both questions? Select two.

- **A.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** Combine `EPSS` (`30-day exploitation probability`) and static `Reachability` call-path verdicts with `CVSS` severity and `runtime` dependency scope
- **D.** `resolution:auto-dismiss` (`alert filter matching findings automatically dismissed by preset or custom Dependabot auto-triage rules`)
- **E.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step

### 43. BaryonMed Genomics wants a custom Dependabot auto-triage rule targeting only `manifest: services/legacy-qc/Gemfile.lock` inside `biobank-lims-rails`. Can `manifest` path conditions be configured in **organization-level** auto-triage rules or **repository-level** rules?

- **A.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** `Dependabot auto-triage rules` (`GitHub presets or custom rules on EPSS/CVE/CWE/scope/patch` setting `resolution:auto-dismiss` before notifications; disable global `Dependabot security updates` for custom PR-trigger rules)

### 44. BaryonMed Genomics wants Dependabot security pull requests on `clinvar-annotator` opened **only** for `Critical` alerts with `EPSS >= 0.10`. Proposed solution: Leave repository-wide `Dependabot security updates` enabled in Settings and create a custom auto-triage rule with `Open a pull request` for `Critical` + `EPSS >= 0.10`. Does this stop low-EPSS PRs?

- **A.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **B.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)
- **C.** No — Code Scanning rejects gzip-compressed SARIF files larger than `10 MB` (`and overwrites prior alerts when multiple matrix uploads share an identical SARIF category on one commit`)
- **D.** No — repository-wide `Dependabot security updates` must be **disabled** before a custom Dependabot auto-triage `Open a pull request` rule can selectively control which alerts open PRs

### 45. How do `Dependabot security updates` and `.github/dependabot.yml` `Dependabot version updates` complement each other on `consent-ledger-go`?

- **A.** `Dependabot security updates` (`alert-driven PRs patching vulnerable versions to the minimum fixed version`) vs `.github/dependabot.yml` `Dependabot version updates` (`scheduled ecosystem/Actions freshness PRs`)
- **B.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **C.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 46. BaryonMed Genomics wants pull requests on private `variant-caller-java` blocked before merge if a developer introduces a `High`/`Critical` vulnerability or an `AGPL-3.0` / `GPL-3.0` dependency. What is the complete four-step setup sequence?

- **A.** Add SPDX license names to `.github/dependabot.yml` → expect Dependabot version updates to block developer PR merges → skip required status checks → disable lockfiles
- **B.** Enable the Dependency Graph (`and Code Security on private repos`) → add an `on: pull_request` workflow running `actions/dependency-review-action@v4` → configure `fail-on-severity` & `deny-licenses` → mark the check required in a branch ruleset
- **C.** Run `dependency-review-action` on an unlicensed private Free repo → grant `write-all` permissions to untrusted fork code → ignore `fail-on-scopes` → merge failing checks freely
- **D.** Trigger `dependency-review-action` only on weekly cron `schedule` → pass both `allow-licenses` and `deny-licenses` simultaneously → disable the Dependency Graph → leave main unprotected

### 47. BaryonMed Genomics' IP counsel wants `actions/dependency-review-action@v4` on `hla-typing-engine` to permit `MIT` and `BSD-2-Clause` while blocking `GPL-2.0`. Proposed solution: Pass both `allow-licenses: MIT, BSD-2-Clause` and `deny-licenses: GPL-2.0` in the same `dependency-review-action@v4` step. Will this succeed?

- **A.** No — CodeQL `Default Setup` and custom `Advanced Setup` (`.github/workflows/codeql.yml`) cannot run active CodeQL management simultaneously (`switch to Advanced Setup with build-mode: manual`)
- **B.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **C.** No — `actions/dependency-review-action` forbids specifying `allow-licenses` and `deny-licenses` together, and fails to block merges unless marked as a required status check on `pull_request`
- **D.** No — temporary private forks created inside a Repository Security Advisory (`GHSA`) intentionally **disable GitHub Actions** (`and pushing fixes to a public branch before release leaks the zero-day`)

### 48. BaryonMed Genomics wants `pharmacogenomics-kb` pull requests gated strictly on runtime `High+` vulnerabilities and SPDX license compliance. Which two steps enforce that gate? Select two.

- **A.** `actions/dependency-review-action@v4` with `fail-on-severity: high`, `fail-on-scopes: runtime`, and `deny-licenses` (`or allow-licenses`, never both)
- **B.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **E.** Mark the `Dependency Review` workflow job as a **required status check** in a repository or organization Branch Ruleset targeting `main`

### 49. `variant-caller-java` authenticates to a private AWS CodeArtifact Maven repository and wants all `org.apache.spark.*` and `io.grpc.*` minor/patch bumps batched into a single weekly PR. Which `.github/dependabot.yml` configuration (`____`) achieves this?

- **A.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **B.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`
- **C.** `.github/codeql/codeql-config.yml` (`defining packs:, queries:, paths-ignore:, and threat-models: alongside YAML model-pack extensions`)
- **D.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step

### 50. Because `biobank-lims-rails` runs clinical validation protocols before major framework upgrades, engineers must prevent Dependabot from proposing `rails 8.x` major upgrades while still receiving `7.2.x` minor/patch and security updates, capped at `6` open version PRs. Which `.github/dependabot.yml` rules configure this?

- **A.** Configure `.github/dependabot.yml` with `groups:` (`batching patch/minor updates into single PRs`), `ignore:` (`version/dependency exclusions`), `open-pull-requests-limit`, and `registries:` (`authenticated via Dependabot secrets`)
- **B.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions

### 51. BaryonMed Genomics runs Nextflow/Docker bioinformatics containers and wants automated PRs whenever `ubuntu` or `nvidia/cuda` base tags in `Dockerfile` have newer digests/patches. Which `package-ecosystem` (`____`) in `.github/dependabot.yml` automates this?

- **A.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **B.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **C.** `Dependabot security updates` (`alert-driven PRs patching vulnerable versions to the minimum fixed version`) vs `.github/dependabot.yml` `Dependabot version updates` (`scheduled ecosystem/Actions freshness PRs`)
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 52. Why did a `pull_request` workflow on `sequencer-instrument-cs` triggered by `dependabot[bot]` fail with `403 Resource not accessible by integration` when attempting to write a PR deployment status using the default `GITHUB_TOKEN`?

- **A.** Govern Dependabot PR workflows (`read-only GITHUB_TOKEN` & `Dependabot secrets`), fine-grained alert roles, `dependabot_alert` webhooks, and production-context filters (`has:deployment`, `runtime-risk:internet-exposed`)
- **B.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **C.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 53. BaryonMed Genomics linked Microsoft Defender for Cloud and JFrog Artifactory to GitHub Enterprise so deployed container digests map back to source repositories. Which Security Overview filter (`____`) isolates alerts running in live internet-exposed clinical APIs?

- **A.** `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`exporting the repository dependency inventory in SPDX JSON format`)
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** `has:deployment runtime-risk:internet-exposed` (`Security Overview and alert search qualifiers powered by ingested deployment metadata`)
- **D.** `resolution:auto-dismiss` (`alert filter matching findings automatically dismissed by preset or custom Dependabot auto-triage rules`)

### 54. BaryonMed Genomics' DevSecOps team is documenting runner isolation for `dependabot` PRs, webhook automation, and runtime enrichment. Which two platform rules are accurate? Select two.

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Govern Dependabot PR workflows (`read-only GITHUB_TOKEN` & `Dependabot secrets`), fine-grained alert roles, `dependabot_alert` webhooks, and production-context filters (`has:deployment`, `runtime-risk:internet-exposed`)
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **E.** Workflows triggered by `dependabot` PRs receive a **read-only `GITHUB_TOKEN`** by default and access credentials stored in **`Dependabot secrets`** (`not standard Actions secrets on untrusted triggers`)

---

## Domain 4 — Configure and use Code Security (formerly Code Scanning with CodeQL) (10–15% official weight · 14 questions)

### 55. BaryonMed Genomics runs `CodeQL` across `C++`, `Java`, `C#`, `Go`, `Ruby`, and `Python` repos and imports `TerraScan` / `Trivy` `SARIF 2.1.0` reports for AWS Genomics Nextflow Terraform code. How do CodeQL and third-party SARIF tools complement each other?

- **A.** `CodeQL` (`compiling/extracting code into a queryable relational AST/CFG/dataflow database`) paired with third-party SAST/IaC/container scanners uploading `SARIF 2.1.0` into unified Code Scanning alerts
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts

### 56. What are GitHub Code Scanning's exact `SARIF 2.1.0` per-upload size limit (`gzip-compressed`), maximum results per run (`ingested` vs `displayed`), and maximum `threadFlowLocations` per dataflow path?

- **A.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **B.** `SARIF 2.1.0` ingestion rules: `<= 10 MB` gzip-compressed upload limit, `<= 25,000` results/run (`top 5,000` displayed by severity), `partialFingerprints` deduplication, distinct `category` tags, and `security-events: write`
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses

### 57. BaryonMed Genomics uploads SARIF outputs from `CodeQL`, `Clang-Tidy`, and `Trivy` on every commit to `fastq-aligner-cpp`. Which two SARIF practices prevent rejected uploads and overwritten alerts? Select two.

- **A.** Ensure each uploaded `SARIF 2.1.0` file is `<= 10 MB` gzip-compressed and `<= 25,000` results (`knowing GitHub displays only the top 5,000 results prioritized by severity`)
- **B.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **C.** Assign a unique `category` per tool/language/monorepo target and preserve stable `ruleId` + `partialFingerprints` so alerts deduplicate cleanly without overwriting sibling scans
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **E.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts

### 58. `fastq-aligner-cpp` (`AVX-512 C++`) compiles on an on-premises Slurm/Jenkins HPC cluster outside GitHub Actions, and CodeQL alerts must appear on GitHub pull requests and Security Overview. What is the exact four-step `CodeQL CLI` lifecycle?

- **A.** Create one shared SARIF file without `--sarif-category` across 6 monorepo services → overwrite prior language alerts on every upload → disable GitHub Code Security on private repos → view alerts in Actions cache
- **B.** Install the CodeQL CLI bundle on the CI agent → run `codeql database create` (`tracing compiled builds`) → run `codeql database analyze --format=sarif-latest` → run `codeql github upload-results` (`--sarif`, `--ref`, `--commit`)
- **C.** Enable Default Setup simultaneously for the same language/category → upload SARIF with a read-only `contents: read` token → strip `partialFingerprints` → expect >25,000 results to render without truncation
- **D.** Run `codeql github upload-results` on raw `.java` source files → run `codeql database analyze` before `codeql database create` → upload an uncompressed 45 MB XML report → omit `--ref` and `--commit`

### 59. BaryonMed Genomics manages `cryoem-reconstruct-py` (`Python`), `variant-caller-java` (`pure Gradle Java, no Kotlin`), and `fastq-aligner-cpp` (`C++` with custom Intel ICX compiler flags). How do CodeQL `build-mode` options apply across these three repos?

- **A.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **B.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **C.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **D.** CodeQL `build-mode` options: `none` (`JS/TS, Python, Ruby & buildless Java`), `autobuild` (`heuristic compiler detection`), and `manual` (`explicit custom build commands in CI for C/C++, C#, Go, Kotlin, Swift`)

### 60. `sequencer-instrument-cs` (`C#` requiring a private hardware SDK restore step before MSBuild) currently has CodeQL `Default Setup` enabled and fails to restore the private feed. Proposed solution: Keep `Default Setup` enabled and commit `.github/workflows/codeql.yml` (`Advanced Setup`) so both run together on `C#`. Is that supported?

- **A.** No — repository-wide `Dependabot security updates` must be **disabled** before a custom Dependabot auto-triage `Open a pull request` rule can selectively control which alerts open PRs
- **B.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **C.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)
- **D.** No — CodeQL `Default Setup` and custom `Advanced Setup` (`.github/workflows/codeql.yml`) cannot run active CodeQL management simultaneously (`switch to Advanced Setup with build-mode: manual`)

### 61. On `biobank-lims-rails`, CodeQL flags `Command injection` tracing `params[:sample_id]` (`source`) -> ` SampleNormalizer.tag()` (`step`) -> `Open3.capture2(cmd)` (`sink`) and posts a `Copilot Autofix` array-argument patch. How do dataflow review and classic Autofix licensing work?

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **D.** Inspect CodeQL `source -> step -> sink` path-problem dataflow traces and apply `Copilot Autofix` (`enabled by default on CodeQL PRs & default branch without requiring a Copilot seat for classic Autofix`)

### 62. On BaryonMed Genomics' HPC Jenkins node, `codeql database analyze` wrote `aligner.sarif` for commit `7d20a11` on `refs/heads/main`. Which exact `CodeQL CLI` command (`____`) uploads that file to GitHub Code Scanning?

- **A.** `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`exporting the repository dependency inventory in SPDX JSON format`)
- **B.** `POST /orgs/{org}/code-security/configurations/{configuration_id}/attach` (`attaching a Security Configuration across selected or all org repos via REST`)
- **C.** `codeql github upload-results --repository=<org/repo> --ref=<refs/heads/main> --commit=<sha> --sarif=<results.sarif>`
- **D.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts

### 63. BaryonMed Genomics is rolling out standardized `.github/workflows/codeql.yml` templates with `Copilot Autofix` across clinical sequencing services. Which two workflow permission and review requirements apply? Select two.

- **A.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** `permissions: { security-events: write, contents: read, actions: read }` on `github/codeql-action/upload-sarif@v3`
- **D.** Validate every `Copilot Autofix` suggestion by inspecting dataflow context, running full CI unit/integration tests + re-scanning with `CodeQL`, and completing human PR review
- **E.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses

### 64. `fastq-aligner-cpp` compiles both `avx512-linux` and `neon-arm64` SIMD code paths in a matrix workflow. Why must each matrix leg pass a distinct `category:` (`such as "/language:cpp/simd:${{ matrix.isa }}"`) to `codeql-action`?

- **A.** Distinguish `security-severity` (`Critical/High/Medium/Low` mapped from CVSS `0.0–10.0`) from rule `problem.severity` (`error/warning/note`), use `category` per matrix leg, and record audited dismissal reasons
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts

### 65. In BaryonMed Genomics' branch ruleset on `pharmacogenomics-kb`, `Require code scanning results` sets `Security alerts: Critical` and `All alerts: None`. Will a CodeQL alert with `Security severity: High (8.1)` and `Rule severity: Error` block the PR?

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Distinguish `security-severity` (`Critical/High/Medium/Low` mapped from CVSS `0.0–10.0`) from rule `problem.severity` (`error/warning/note`), use `category` per matrix leg, and record audited dismissal reasons
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 66. BaryonMed Genomics' custom bioinformatics memory-safety analyzer generated a `19 MB` gzip-compressed SARIF file (`31,000` results) on `fastq-aligner-cpp`. Proposed solution: Upload the `19 MB` `.sarif.gz` file directly via `upload-sarif@v3` without filtering low-value noise rules. Will Code Scanning accept the upload?

- **A.** No — Code Scanning rejects gzip-compressed SARIF files larger than `10 MB` (`and overwrites prior alerts when multiple matrix uploads share an identical SARIF category on one commit`)
- **B.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **C.** No — `actions/dependency-review-action` forbids specifying `allow-licenses` and `deny-licenses` together, and fails to block merges unless marked as a required status check on `pull_request`
- **D.** No — temporary private forks created inside a Repository Security Advisory (`GHSA`) intentionally **disable GitHub Actions** (`and pushing fixes to a public branch before release leaks the zero-day`)

### 67. BaryonMed Genomics uses an internal Java cohort-anonymization library (`org.baryonmed.deid.PatientMasker.redact()`) and wants CodeQL to recognize `redact()` as a taint sanitizer across 20 Java microservices without editing `.ql` queries. Which file and feature (`____`) enables this?

- **A.** `.github/codeql/codeql-config.yml` (`defining packs:, queries:, paths-ignore:, and threat-models: alongside YAML model-pack extensions`)
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **D.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`

### 68. CodeQL workflows on `sequencer-instrument-cs` (`C# + C++ + TypeScript`) hit runner memory exhaustion (`exit code 137`) while indexing `third_party/vendor_genomes/**`. Which three remediation actions resolve OOM crashes and cut runtime?

- **A.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **B.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **C.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **D.** Customize `.github/codeql/codeql-config.yml` (`paths-ignore`, `packs`, `queries`, `threat-models`) & `CodeQL model packs` (`YAML data extensions`), and fix OOM/slow scans via Larger runners or split language matrices

---

## Domain 5 — Security operations: best practices, prioritization, and remediation (15–20% official weight · 18 questions)

### 69. A genomics consortium discovers a heap-buffer-overflow (`CWE-122`) when `open-vcf-stream` parses malformed VCF headers and wants to report it privately to BaryonMed maintainers. Which feature (`____`) intakes the report, and how do `CWE`, `CVE`, and `GHSA` fit together?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **D.** `CWE` classifies weakness types (`e.g., CWE-89 SQLi`), `CVE` identifies a publicly disclosed vulnerability instance, and `GHSA` (`Repository Security Advisories` + Private Reporting) coordinates private patches & CVEs

### 70. Inside `open-vcf-stream`'s temporary private advisory fork (`open-vcf-stream-ghsa-55m9`), maintainers commit a heap-bounds check and want automated Linux/macOS CI matrix builds. Proposed solution: Trigger `.github/workflows/ci.yml` directly inside the temporary private advisory fork, or push the branch to a public `fix/heap-overflow` branch on `open-vcf-stream` a week before release. Is this valid and confidential?

- **A.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **B.** No — temporary private forks created inside a Repository Security Advisory (`GHSA`) intentionally **disable GitHub Actions** (`and pushing fixes to a public branch before release leaks the zero-day`)
- **C.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)
- **D.** No — repository-wide `Dependabot security updates` must be **disabled** before a custom Dependabot auto-triage `Open a pull request` rule can selectively control which alerts open PRs

### 71. Once BaryonMed Genomics merges the temporary private fork and publishes the `open-vcf-stream` `GHSA` (`marking < 3.1.2 vulnerable and 3.1.2 patched`), how do downstream clinical pipelines learn they are affected?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** `CWE` classifies weakness types (`e.g., CWE-89 SQLi`), `CVE` identifies a publicly disclosed vulnerability instance, and `GHSA` (`Repository Security Advisories` + Private Reporting) coordinates private patches & CVEs
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 72. BaryonMed Genomics has 950 open alerts across retired thesis repos and live clinical sequencing APIs alike. Which combined strategy halts net-new `Critical`/`High` PR merges while focusing sprints on internet-exposed clinical workloads first?

- **A.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **B.** Prioritize using `has:deployment` + `runtime-risk:internet-exposed` (`Defender for Cloud / artifact registries`), `EPSS`, and `Reachability`, while blocking new regressions via `Require code scanning results` rulesets
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 73. On `variant-caller-java`, an `Active` organization ruleset specifies `Require code scanning results` for tool `CodeQL`. What happens if a contributor submits a PR that modifies `.java` files while breaking the runner environment so `CodeQL` fails to upload SARIF results?

- **A.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **B.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Enforce approved CodeQL scanning via Org/Enterprise `Rulesets` (`Require code scanning results` + Required Workflows) and automate governance via REST/GraphQL (`code-security/configurations`, org alert endpoints & billing APIs)

### 74. BaryonMed Genomics is introducing organization-wide severity rulesets across 75 genomics repositories while prioritizing live clinical AKS clusters. Which two practices ensure smooth rollout and runtime focus? Select two.

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Ingest deployment metadata (`from Microsoft Defender for Cloud, JFrog Artifactory, or CI/CD APIs`) to filter `has:deployment` and `runtime-risk:internet-exposed` alerts
- **C.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **E.** Pilot cross-repository `Rulesets` in **`Evaluate` mode** to measure would-be blocked PRs via Ruleset Insights before switching enforcement to **`Active`**

### 75. BaryonMed Genomics' AppSec lead is launching a 30-day sprint to close 195 default-branch `CWE-89` SQLi and `CWE-22` path-traversal alerts across 12 biobank repositories. What is the end-to-end Security Campaign sequence?

- **A.** Filter high-risk default-branch alerts in Security Overview → create a Security Campaign (`<=1,000` alerts) with due date & contact → trigger Copilot Autofix (`or assign <=25 alerts to @copilot`) → verify CI checks & track burndown
- **B.** Export alerts to a static spreadsheet with no GitHub links → disable CodeQL so open counts fall to zero → bulk-dismiss every alert without comments → report 100% remediation
- **C.** Assign 500 alerts in one batch to `@copilot` without AI credits or branch protection → skip human PR review → disable Security Overview → expect secret campaigns to auto-rotate AWS IAM keys
- **D.** Create a campaign containing 50,000 unmerged fork-branch alerts with no contact owner → auto-merge Copilot suggestions bypassing CI tests → revoke developer write access → close the campaign with alerts still open

### 76. Inside BaryonMed Genomics' Code Security Campaign, what are the exact caps on total campaign alerts (`1,000`) and single-batch assignments to `@copilot` (`____`), and what credit pool funds `@copilot` campaign batches?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Run `Security Campaigns` (`<=1,000` default-branch alerts, named security lead, developer notifications, Copilot Autofix, or assigning `<=25` alerts per batch to `@copilot` cloud agent) with audited dismissal comments
- **C.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **D.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions

### 77. During BaryonMed's CAP/CLIA audit, assessors review 9 campaign alerts dismissed as `Won't fix` on `clinvar-annotator`. What governance evidence must accompany each dismissal, and how is unauthorized dismissal caught?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Dismissing an alert requires a structured closure reason (`False positive`, `Used in tests`, `Won't fix`) plus an audit-logged justification comment—and never deletes commits or revokes keys
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 78. BaryonMed Genomics wants `biobank-lims-rails` and `consent-ledger-go` (`GDPR genomic data`) scanned with medium-precision CodeQL security rules alongside `default` high-precision rules, without noisy non-security maintainability hints. Which suite (`queries: ____`) fits?

- **A.** `has:deployment runtime-risk:internet-exposed` (`Security Overview and alert search qualifiers powered by ingested deployment metadata`)
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** `resolution:auto-dismiss` (`alert filter matching findings automatically dismissed by preset or custom Dependabot auto-triage rules`)
- **D.** `queries: security-extended` (`executing default high-precision CodeQL security rules plus medium-precision security queries without style/quality rules`)

### 79. After discovering a custom BAM-file integer-overflow pattern in `fastq-aligner-cpp`, BaryonMed's security researcher writes a custom `.ql` query in VS Code to scan all 75 org repositories simultaneously. Which feature (`____`) powers this hunt?

- **A.** Select CodeQL query suites (`default` high-precision, `security-extended` broader lower-confidence security, `security-and-quality` adds maintainability) and run `Multi-Repository Variant Analysis (MRVA)` in VS Code
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 80. `cryoem-reconstruct-py` runs HPC batch workers that parse untrusted cryo-EM `.mrc` headers from shared local Lustre filesystems and CLI flags (`sys.argv`), which CodeQL's default `remote` threat model skips. Which `codeql-config.yml` option adds those sources?

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Customize `.github/codeql/codeql-config.yml` (`paths-ignore`, `packs`, `queries`, `threat-models`) & `CodeQL model packs` (`YAML data extensions`), and fix OOM/slow scans via Larger runners or split language matrices

### 81. BaryonMed Genomics wants principal scientists (`Write` access) designated as squad security leads to view and dismiss false-positive Code Scanning and Dependabot alerts on their squad repos without `Repository Admin` rights. How should permissions be granted?

- **A.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Assign `Security Manager` org roles, custom repository alert roles, and per-alert `Assignees` (`noting secret-alert assignment temporarily elevates single-alert view access for repo writers until unassigned`)
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 82. What happens to repository permissions when a BaryonMed `Security Manager` assigns Secret Protection alert `#29` (`via alert Assignee or a Secret scanning campaign`) on `pharmacogenomics-kb` to a backend developer with standard `Write` access?

- **A.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **D.** Assign `Security Manager` org roles, custom repository alert roles, and per-alert `Assignees` (`noting secret-alert assignment temporarily elevates single-alert view access for repo writers until unassigned`)

### 83. BaryonMed Genomics is formalizing cross-team triage and exception approvals between AppSec and 7 bioinformatics squads. Which two practices uphold least privilege and auditability? Select two.

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** `Delegated bypass for push protection` (`granting Specific roles, visible teams, or custom roles with "Review and manage secret scanning bypass requests" authority—never secret teams`)
- **C.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **E.** Assign `Security Manager` org roles, custom repository alert roles, and per-alert `Assignees` (`noting secret-alert assignment temporarily elevates single-alert view access for repo writers until unassigned`)

### 84. Which three-control shift-left pipeline protects BaryonMed Genomics' `consent-ledger-go` from credential exposure, vulnerable/unlicensed PR dependencies, and Go injection flaws before commits merge to `main`?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** Layer `Push Protection` (`pre-receive`), `actions/dependency-review-action` (`PR manifest/license gate`), and `CodeQL` PR checks (`with Copilot Autofix`) so secrets, vulnerable packages, and taint flaws fail pre-merge
- **C.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 85. Why does preventing an Illumina API token via pre-receive `Push Protection` save hours of incident toil compared with detecting it post-push on `clinvar-annotator`?

- **A.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** `Push Protection` intercepts supported high-confidence and published custom secrets pre-receive during `git push` (`CLI, IDE, web editor & REST API`), blocking the secret from entering Git history
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 86. BaryonMed Genomics' Clinical Software Quality Manual requires three preventive controls on every patient-facing repository before pull requests merge. Which three controls satisfy that requirement? Select three.

- **A.** Validate every `Copilot Autofix` suggestion by inspecting dataflow context, running full CI unit/integration tests + re-scanning with `CodeQL`, and completing human PR review
- **B.** `Push Protection` blocks high-confidence partner and published custom secrets pre-receive during `git push` before commits land on GitHub
- **C.** Configure `actions/dependency-review-action@v4` with `fail-on-severity`, `fail-on-scopes`, and either `allow-licenses` OR `deny-licenses` (`SPDX` IDs)
- **D.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **E.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **F.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step

---

## Domain 6 — GitHub Security suites administration (10–15% official weight · 14 questions)

### 87. BaryonMed Genomics is rolling out standardized Secret Protection, Dependabot, and CodeQL across 130 repositories across `clinical`, `biobank`, and `research` tiers. What is the recommended four-step Security Configuration rollout sequence?

- **A.** Manually toggle Settings on 2,000 repositories one by one → grant every developer Organization Owner permissions → disable Push Protection globally → rely on `.gitignore` for enterprise governance
- **B.** Verify committer license headroom (`or metered budget`) → create/select a Security Configuration → attach to tiered repos (`custom properties`) & enable `Apply to new repositories` → set `Enforced` to lock baseline controls
- **C.** Enable cloud-only Copilot Autofix on an air-gapped GHES instance with metered billing → skip GitHub Connect → expect transferred external repos to inherit new-repo defaults automatically without policy checks
- **D.** Apply an `Enforced` configuration across 2,000 private repos with zero available committer seats → set every feature to `Not set` expecting strict locks → leave new repositories uncovered → disable audit logs

### 88. BaryonMed Genomics operates sovereign hospital biobank repos on `GitHub Enterprise Server (GHES)` alongside global sequencing SaaS repos on `GitHub Enterprise Cloud (GHEC)`. How do billing models, cloud AI features, and `GitHub Connect` work across `GHEC` and `GHES`?

- **A.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **B.** Roll out org/enterprise `Security Configurations` (`GitHub-recommended` or custom, `Apply to new repositories`), contrasting `GHEC` (`metered or volume + cloud AI features`) with `GHES` (`volume-only + GitHub Connect Advisory sync`)
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 89. BaryonMed Genomics **transferred** 4 private repositories from a university lab org into `baryonmed-genomics`, where `Apply to new repositories` is enabled on the `GDPR-Clinical-Enforced` Security Configuration. Why weren't those 4 repos covered automatically?

- **A.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **B.** `Enforced` Security Configurations lock enabled/disabled settings (`except fields set to "Not set"`), while private/internal repos consume `90-day unique active committer` seats (`plus metered AI credits for AI Scan/generic secrets`)
- **C.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 90. BaryonMed Genomics' Security Manager attaches an `Enforced` Security Configuration to `biobank-lims-rails` with `Secret scanning = Enabled` and `CodeQL Default Setup = Not set`, assuming repo admins are locked out of changing CodeQL settings. Proposed solution: Leave `CodeQL Default Setup` as `"Not set"` expecting `Enforced` mode to freeze it. Does `"Not set"` lock repo admins out?

- **A.** No — repository-wide `Dependabot security updates` must be **disabled** before a custom Dependabot auto-triage `Open a pull request` rule can selectively control which alerts open PRs
- **B.** No — temporary private forks created inside a Repository Security Advisory (`GHSA`) intentionally **disable GitHub Actions** (`and pushing fixes to a public branch before release leaks the zero-day`)
- **C.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **D.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)

### 91. BaryonMed Genomics holds a fixed volume subscription of `100` `GitHub Code Security` seats, currently at `100 / 100` (`0` seats remaining). What happens when `Apply to new repositories` attempts to enable `GitHub Code Security` on a newly created private repository—and how does metered billing differ?

- **A.** `Enforced` Security Configurations lock enabled/disabled settings (`except fields set to "Not set"`), while private/internal repos consume `90-day unique active committer` seats (`plus metered AI credits for AI Scan/generic secrets`)
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **D.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners

### 92. BaryonMed Genomics' FinOps and AppSec leads are auditing monthly seat deduplication across `GHEC + GHES` and metered AI credit controls. Which two billing and budget rules apply? Select two.

- **A.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **B.** Monitor `Code Security AI credits` (`AI Scan / agentic autofix`) and `Secret Protection AI credits` (`AI push scanning`), setting **hard metered budgets** to cap spend
- **C.** Count `90-day unique active committers` across private/internal repos (`deduplicating each human user once across the enterprise, plus GitHub Connect sync between GHEC and GHES`)
- **D.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **E.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect

### 93. BaryonMed Genomics' Enterprise Owner sets `Repository administrators can enable or disable GitHub Code Security = Disabled`. What happens to existing enabled repos, and which roles can still attach Security Configurations?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Enforce Enterprise Advanced Security policies (`restricting repo admins while preserving Org Owner/Security Manager control`), scope ruleset/push-protection bypass actors, and stream `security_configuration.*` / alert audit logs
- **C.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **D.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners

### 94. For ISO 27001 and HIPAA long-term retention, BaryonMed Genomics streams its Enterprise Audit Log to Amazon S3 and Splunk. Which events verify governance over configurations, rulesets, bypasses, and dismissals?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Enforce Enterprise Advanced Security policies (`restricting repo admins while preserving Org Owner/Security Manager control`), scope ruleset/push-protection bypass actors, and stream `security_configuration.*` / alert audit logs
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 95. Visiting researcher Dr. Lin pushed commits to `cryoem-reconstruct-py` 91 days ago (`with zero commits to any private/internal enabled repo in the past 90 days`), and contractor Sam was removed from the enterprise yesterday. How many active-committer seats do Dr. Lin and Sam consume today (`____`)?

- **A.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **B.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** `Enforced` Security Configurations lock enabled/disabled settings (`except fields set to "Not set"`), while private/internal repos consume `90-day unique active committer` seats (`plus metered AI credits for AI Scan/generic secrets`)

### 96. BaryonMed Genomics created team `@baryonmed/clinical-secops` so five bioinformatics security analysts can triage alerts across every repo in `baryonmed-genomics` and govern rollout templates without modifying clinical source files or touching enterprise payment cards. Which organization role (`____`) should be granted?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **D.** Separate `Enterprise/Org Owners` (`billing & global policy`), `Security Managers` (`org-wide alert read/write & security config management, without code-write`), and custom repository roles (`granular view/dismiss per tool`)

### 97. An external CAP/CLIA laboratory inspector requires read-only visibility into `Dependabot` and `Code Scanning` alerts on `sequencer-instrument-cs` for 10 days—with **no** access to raw `Secret Protection` tokens, alert dismissal, or code edits. How should access be configured?

- **A.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **B.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **C.** Separate `Enterprise/Org Owners` (`billing & global policy`), `Security Managers` (`org-wide alert read/write & security config management, without code-write`), and custom repository roles (`granular view/dismiss per tool`)
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 98. BaryonMed Genomics wants two clinical data-custodian officers to approve or deny urgent Push Protection bypass requests across `baryonmed-genomics` without granting them `Security Manager` rights to modify Security Configurations. Which custom org role permission (`____`) grants only that authority?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** `permissions: { security-events: write, contents: read, actions: read }` on `github/codeql-action/upload-sarif@v3`
- **C.** `Review and manage secret scanning bypass requests` (`fine-grained organization role permission for Push Protection delegated bypass`)
- **D.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations

### 99. Before CAP/CLIA laboratory accreditation, BaryonMed Genomics must gate pull-request merges across 75 sequencing and biobank repos on clean `High`/`Critical` SAST checks—without halting clinical pipelines on unconfigured repos during week one. Which ordered sequence achieves a zero-disruption rollout?

- **A.** Disable `pull_request` triggers in `codeql.yml` so scans run only monthly on `main` → enforce `Require code scanning results` on feature PRs → expect instant green PR gates
- **B.** Set an Org Ruleset to `Active` requiring `CodeQL` results before enabling CodeQL on any repo → grant `All repository writers` bypass access → set thresholds to `Note` style warnings → disable PR scans
- **C.** Standardize CodeQL across target repos → create an Org Branch Ruleset in `Evaluate` mode with `Require code scanning results` (`High+` security severity) → audit Evaluate insights & scope bypass actors → switch enforcement to `Active`
- **D.** Configure branch protection individually in `.github/secret_scanning.yml` → allow Copilot Autofix comments to count as human PR approvals → skip `Evaluate` mode → delete Security Manager access

### 100. BaryonMed Genomics' platform engineering team automates Security Configuration attachment in Python and aggregates org-wide alert posture into BigQuery without making 130 per-repository API loops. Which two governance and API mechanisms enable this? Select two.

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Enforce approved CodeQL scanning via Org/Enterprise `Rulesets` (`Require code scanning results` + Required Workflows) and automate governance via REST/GraphQL (`code-security/configurations`, org alert endpoints & billing APIs)
- **C.** `POST /orgs/{org}/code-security/configurations/{configuration_id}/attach` (`attaching a Security Configuration across selected or all org repos via REST`)
- **D.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **E.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts

---

## Answer Key and Explanations

### Question 1 — `A` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: A (is correct). GitHub offers standalone `GitHub Secret Protection` and `GitHub Code Security` SKUs purchasable independently or together on both GitHub Team and GitHub Enterprise, billed per 90-day active committer on private/internal repositories. [Skill 1.1: Describe GitHub Security suite structure, navigation, and contrast Code Security, Secret Protection, and Supply Chain Security | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)]

- **A:** Correct. GitHub offers standalone Secret Protection and Code Security products on both GitHub Team and GitHub Enterprise, billed by unique 90-day active committers on private/internal repos
- **B:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **C:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 2 — `B` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: B (is correct). Secret Protection prevents and detects credential leaks, Code Security (`CodeQL`/SARIF + Copilot Autofix) analyzes first-party code flaws, and Supply Chain Security governs third-party dependency and license risks. [Skill 1.1: Describe GitHub Security suite structure, navigation, and contrast Code Security, Secret Protection, and Supply Chain Security | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Correct. each pillar targets a distinct risk surface: leaked credentials, first-party source vulnerabilities, and third-party open-source dependency/license exposure
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 3 — `A, D` (Describe GitHub Security suites, features, and ecosystem)

Correct answers: A and D (are correct). `GitHub Secret Protection` covers Push Protection, secret scanning, validity checks, custom patterns, and AI generic detection, while `GitHub Code Security` covers CodeQL/SARIF scanning, Copilot Autofix, private-repo Dependency Review, and Security Campaigns. [Skill 1.1: Describe GitHub Security suite structure, navigation, and contrast Code Security, Secret Protection, and Supply Chain Security | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)]

- **A:** Correct. Code Security covers first-party SAST, Copilot Autofix, and private-repository Dependency Review enforcement
- **B:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Correct. Secret Protection focuses specifically on credential exposure in pushes and Git history
- **E:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 4 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). Public GitHub.com repositories receive core secret scanning, Push Protection, Dependency Graph, Dependabot, CodeQL default setup, and Dependency Review free of charge, whereas private/internal repositories require Secret Protection / Code Security licenses for advanced features. [Skill 1.2: Differentiate security feature availability for public repositories vs. enterprise environments and explain Security Overview | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-overview/about-security-overview)]

- **A:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Correct. GitHub provides core security scanning free to open-source public repositories on GitHub.com while requiring Secret Protection / Code Security licenses for advanced private/internal repo coverage
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 5 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). Organization and Enterprise `Security Overview` surfaces `Risk`, `Coverage`, `Campaigns`, and tool-specific dashboards filterable by custom properties, teams, and topics. [Skill 1.2: Differentiate security feature availability for public repositories vs. enterprise environments and explain Security Overview | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-overview/about-security-overview)]

- **A:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **B:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **C:** Correct. Security Overview aggregates posture, enablement gaps, alert trends, and campaign burndown across hundreds of repositories from a single org/enterprise plane
- **D:** Incorrect. codeql-config.yml centralizes custom query packs, path exclusions, threat models, and data-extension model packs for Advanced Setup

### Question 6 — `D` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: D (is correct). Running the free organization security risk assessment in Security Overview scans private repositories for leaked secrets and previews CodeQL findings with Copilot Autofix across up to 20 active repositories. [Skill 1.2: Differentiate security feature availability for public repositories vs. enterprise environments and explain Security Overview | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-overview/about-security-overview)]

- **A:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **B:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **C:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **D:** Correct. organizations on GitHub Team or Enterprise can run free secret and code risk assessments before purchasing full rollout licenses

### Question 7 — `D` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: D (is correct). Secret Protection matches structured tokens, entropy, and AI generic credentials across pushed blobs and Git history, whereas CodeQL builds a relational AST/CFG/dataflow database to trace untrusted sources into dangerous code sinks. [Skill 1.3: Explain differences and interplay between Secret Protection and Code Security across an end-to-end secure SDLC | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Correct. Secret Protection catches leaked tokens in any text/config file at push time, while CodeQL models how untrusted inputs or hardcoded values flow into sensitive code sinks

### Question 8 — `B` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: B (is correct). Layer pre-receive `Push Protection`, PR `actions/dependency-review-action@v4`, and PR `CodeQL` checks (`with Copilot Autofix`) enforced as required checks on protected branches. [Skill 1.3: Explain differences and interplay between Secret Protection and Code Security across an end-to-end secure SDLC | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **B:** Correct. combining all three shift-left controls prevents new security debt from ever landing on the default branch
- **C:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 9 — `D` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: D (is correct). Push Protection blocks high-confidence secrets pre-receive before Git history updates, while CodeQL Default Setup with Copilot Autofix and an active ruleset blocks and patches XSS taint flaws pre-merge. [Skill 1.3: Explain differences and interplay between Secret Protection and Code Security across an end-to-end secure SDLC | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Incorrect. allow-licenses and deny-licenses are mutually exclusive inputs in dependency-review-action, and branch rulesets must require the check to block merging
- **B:** Incorrect. alert dismissal only updates GitHub UI/API triage status; attackers can still extract unrotated keys from earlier commits, clones, or reflogs
- **C:** Incorrect. secret_scanning.yml suppresses user notifications in excluded folders rather than blocking pushes or cancelling public-repo partner revocations
- **D:** Correct. every required GitHub Security suite setting, permission boundary, and enforcement rule is properly configured

### Question 10 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). Block secrets pre-receive via Push Protection, evaluate PR dependencies and code via Dependency Review and CodeQL, apply Copilot Autofix or dependency upgrades before merge, and monitor default-branch advisories in Security Overview. [Skill 1.4: Compare prevention-first approaches vs. gate-based security strategies and explain security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/security-at-scale/about-security-campaigns)]

- **A:** Incorrect. auto-dismissing unreviewed PR findings defeats shift-left prevention, and .gitignore never revokes already-exposed credentials
- **B:** Incorrect. Copilot Autofix requires an upstream CodeQL finding first, and Push Protection intercepts secrets during git push rather than post-merge
- **C:** Correct. a prevention-first secure SDLC stops secrets at git push, blocks vulnerable PR code/dependencies with pre-merge checks and Autofix, and continuously monitors post-merge advisories
- **D:** Incorrect. deferring secret and code checks until after merge exposes live credentials in Git history and turns security into high-cost reactive firefighting

### Question 11 — `A` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: A (is correct). Catching secrets pre-receive and fixing vulnerabilities inside small feature PRs (`with Copilot Autofix`) avoids multi-repo Git history purges, emergency biobank credential rotations, and release-week deadlocks. [Skill 1.4: Compare prevention-first approaches vs. gate-based security strategies and explain security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/security-at-scale/about-security-campaigns)]

- **A:** Correct. shifting detection to git push and pull requests prevents secret sprawl and vulnerable merges before release cutoffs
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 12 — `A` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: A (is correct). `Security Campaigns` group up to 1,000 default-branch alerts with a target deadline, designated security contact, developer notifications, and Copilot Autofix support. [Skill 1.4: Compare prevention-first approaches vs. gate-based security strategies and explain security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/security-at-scale/about-security-campaigns)]

- **A:** Correct. Security Campaigns turn overwhelming alert backlogs into manageable, developer-friendly remediation sprints with clear ownership
- **B:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 13 — `B` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: B (is correct). GitHub records the structured dismissal reason (`False positive`, `Used in tests`, `Won't fix`), mandatory justification comment, actor, and timestamp across timelines, REST/GraphQL APIs, webhooks, and audit logs without altering Git history. [Skill 1.5: Identify vulnerability and secret detection mechanisms, act on alerts, and govern ignoring or dismissing alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/vulnerability-exposure)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Correct. alert dismissals remain visible in REST/GraphQL APIs, webhooks, and audit logs, so teams must document rationale rather than hiding unverified risk
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions

### Question 14 — `D` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: D (is correct). Neither dismissing the alert nor editing `.gitignore` revokes the compromised AWS IAM key or purges historical Git commit blobs where the key remains readable. [Skill 1.5: Identify vulnerability and secret detection mechanisms, act on alerts, and govern ignoring or dismissing alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/vulnerability-exposure)]

- **A:** Incorrect. enabling Advanced Setup disables Default Setup so custom workflow build steps, codeql-config.yml, or custom query suites govern scanning cleanly without duplicate conflicts
- **B:** Incorrect. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories
- **C:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. Neither dismissing the alert nor editing `.gitignore` revokes the compromised AWS IAM key or purges historical Git commit blobs where the key remains readable.
- **D:** Correct. alert dismissal only updates GitHub UI/API triage status; attackers can still extract unrotated keys from earlier commits, clones, or reflogs

### Question 15 — `B, E` (Describe GitHub Security suites, features, and ecosystem)

Correct answers: B and E (are correct). Require structured dismissal reasons accompanied by written comments, and audit dismissal events continuously via Security Overview, webhooks, REST APIs, and enterprise audit log streams. [Skill 1.5: Identify vulnerability and secret detection mechanisms, act on alerts, and govern ignoring or dismissing alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/vulnerability-exposure)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Correct. structured dismissal reasons and comments create an auditable compliance trail in webhooks and GraphQL/REST APIs
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **E:** Correct. Security Overview and org audit logs surface anomalous dismissal spikes or unpatched high-risk repositories

### Question 16 — `D` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: D (is correct). Enterprise/Org Admins manage licensing and baseline Security Configurations, Security Managers oversee Security Overview, triage policies, and campaigns, and Developers fix PR and campaign findings in source code. [Skill 1.6: Describe developer, security, and admin responsibilities, alert access management, delegated bypass, and supply chain security concepts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)]

- **A:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **B:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Correct. effective DevSecOps distributes enablement, posture prioritization, and code-level patching cleanly across Admin, AppSec, and Developer roles

### Question 17 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). Raw secret alerts reveal live biobank credentials, and delegated bypass forces push override requests through designated security reviewers rather than unreviewed contributor self-bypasses. [Skill 1.6: Describe developer, security, and admin responsibilities, alert access management, delegated bypass, and supply chain security concepts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Correct. restricting sensitive secret/vulnerability details and routing bypass requests through designated security reviewers preserves accountability without halting urgent releases
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 18 — `B, C, E` (Describe GitHub Security suites, features, and ecosystem)

Correct answers: B, C, and E (are correct). Separate Admin/Security Manager/Developer duties, govern Push Protection exceptions via least-privilege delegated bypass reviewers, and combine lockfiles with CI `Dependency Submission API` snapshots for full transitive dependency visibility. [Skill 1.6: Describe developer, security, and admin responsibilities, alert access management, delegated bypass, and supply chain security concepts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)]

- **A:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **B:** Correct. committing lockfiles plus submitting build-resolved snapshots gives GitHub complete direct and transitive dependency visibility
- **C:** Correct. effective DevSecOps distributes enablement, posture prioritization, and code-level patching cleanly across Admin, AppSec, and Developer roles
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **E:** Correct. restricting sensitive secret/vulnerability details and routing bypass requests through designated security reviewers preserves accountability without halting urgent releases
- **F:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 19 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). Attaching an Organization or Enterprise Security Configuration with `Apply to new repositories` enabled activates Secret Protection controls across current and newly created repositories consistently. [Skill 2.1: Enable and configure GitHub Secret Protection at repository and organization levels and contrast public vs. private/enterprise behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)]

- **A:** Correct. Security Configurations scale Secret Protection across existing and newly created repositories consistently, while single-repo toggles suit isolated pilots
- **B:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 20 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). On the public repo, partner scanning runs free and automatically forwards the exposed key to Google Cloud for partner handling/revocation; on the private repo, GitHub raises internal repo/org alerts (`plus optional validity checks`) without public partner revocation notices. [Skill 2.1: Enable and configure GitHub Secret Protection at repository and organization levels and contrast public vs. private/enterprise behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)]

- **A:** Correct. partner notification automatically reports exposed public-repo tokens to the issuing cloud/SaaS vendor, whereas private-repo findings stay internal unless validity checks query the provider
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 21 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). Neither—already-enabled repositories remain active, `Enterprise Owners`, `Organization Owners`, and `Security Managers` keep full Security Configuration authority, and only individual Repository Admins are prevented from toggling licensing. [Skill 2.1: Enable and configure GitHub Secret Protection at repository and organization levels and contrast public vs. private/enterprise behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)]

- **A:** Correct. enterprise policies prevent uncontrolled repo-admin license consumption while audit log streaming preserves tamper-evident compliance records across configuration and bypass events
- **B:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges

### Question 22 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). `Push Protection` evaluates pushed commits pre-receive across CLI, IDEs, web edits, and REST APIs, blocking supported high-confidence secrets before refs update in Git history. [Skill 2.2: Prevent secret exposure using Push Protection, validity checks, and prioritized high-confidence or generic secret detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection)]

- **A:** Correct. blocking leaked credentials before the remote ref updates avoids costly key rotation, incident response, and Git history rewrites
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories

### Question 23 — `C` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: C (is correct). Rotate the `Active` partner tokens immediately (`and manually verify the MySQL URLs against internal servers`), because non-provider generic patterns have no external SaaS partner API endpoint for automatic validity verification. [Skill 2.2: Prevent secret exposure using Push Protection, validity checks, and prioritized high-confidence or generic secret detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **C:** Correct. knowing a leaked AWS, Stripe, or Slack token is still Active lets incident responders triage live compromises ahead of already-revoked tokens
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 24 — `A, E` (Configure and use Secret Protection (formerly secret scanning))

Correct answers: A and E (are correct). BaryonMed should enable `Push Protection` for pre-receive cloud-token blocking alongside `non-provider patterns` and `Copilot AI generic secret detection` (`using Secret Protection AI credits`) to catch unstructured LIMS `.config` passwords. [Skill 2.2: Prevent secret exposure using Push Protection, validity checks, and prioritized high-confidence or generic secret detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection)]

- **A:** Correct. enabling non-provider and AI generic secret detection catches unstructured passwords and connection strings missed by vendor-prefix regexes (noting non-provider patterns lack partner validity checks)
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **D:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **E:** Correct. stopping secrets pre-receive prevents Git history contamination and emergency credential rotation

### Question 25 — `C` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: C (is correct). Confirm alert validity and blast radius, immediately revoke and rotate the Okta token at the provider, purge Git commit history (`git filter-repo` plus GitHub Support cache purge if needed), and resolve the alert as `Revoked`. [Skill 2.3: Manage the Secret Protection alert lifecycle, apply secret remediation actions, and govern alert dismissals | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts)]

- **A:** Incorrect. using secret_scanning.yml to silence an active production credential leak hides the alert without revoking or rotating the compromised secret
- **B:** Incorrect. deleting a secret in a follow-up commit leaves the active credential exposed in prior Git commits, reflogs, and clones without revoking access
- **C:** Correct. once a secret reaches Git history, revoking/rotating the live key comes first, followed by history rewrite/cache purge and marking the alert Revoked for auditability
- **D:** Incorrect. delaying credential revocation leaves attackers able to exploit copies harvested from webhooks, clones, or cached diffs while history is rewritten

### Question 26 — `D` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: D (is correct). Rewriting branch commits does not immediately purge unreachable Git blobs cached in closed/merged pull requests or GitHub's object cache; GitHub Support can purge cached PR views when sensitive raw material must be evicted immediately. [Skill 2.3: Manage the Secret Protection alert lifecycle, apply secret remediation actions, and govern alert dismissals | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **D:** Correct. merely deleting a secret in a later commit leaves it readable in earlier commits; immediate revocation and rotation is mandatory

### Question 27 — `B` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: B (is correct). Trigger an on-demand validity check on the alert so GitHub re-queries the partner endpoint and confirms the badge transitions from `Active` to `Inactive`. [Skill 2.3: Manage the Secret Protection alert lifecycle, apply secret remediation actions, and govern alert dismissals | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Correct. knowing a leaked AWS, Stripe, or Slack token is still Active lets incident responders triage live compromises ahead of already-revoked tokens
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement

### Question 28 — `B` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: B (is correct). Enabling `Delegated bypass for push protection` removes writer self-bypass and routes requests (`with reason and comment`) to designated visible teams, roles, or custom roles. [Skill 2.4: Configure role-based and delegated bypass policies in Secret Protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Correct. delegated bypass replaces ad-hoc writer self-bypasses with a structured request-and-approval workflow audited via webhooks and logs
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 29 — `B` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: B (is correct). No—GitHub rejects **secret teams** on Push Protection delegated bypass lists (`only visible teams, roles, or custom roles are allowed`), and `.github/secret_scanning.yml` only configures `paths-ignore` path exclusions. [Skill 2.4: Configure role-based and delegated bypass policies in Secret Protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection)]

- **A:** Incorrect. each gzipped SARIF upload must be <=10 MB with a distinct category per language/tool/component and security-events: write permission
- **B:** Correct. secret_scanning.yml suppresses user notifications in excluded folders rather than blocking pushes or cancelling public-repo partner revocations
- **C:** Incorrect. validate advisory patches locally or in an isolated private mirror without exposing exploit diffs publicly before publishing the coordinated GHSA release
- **D:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. No—GitHub rejects **secret teams** on Push Protection delegated bypass lists (`only visible teams, roles, or custom roles are allowed`), and `.github/secret_scanning.yml` only configures `paths-ignore` path exclusions.

### Question 30 — `C, D` (Configure and use Secret Protection (formerly secret scanning))

Correct answers: C and D (are correct). Assign **visible** organization teams or custom roles (`never secret teams`) to the delegated bypass list, and grant the custom organization role `Review and manage secret scanning bypass requests`. [Skill 2.4: Configure role-based and delegated bypass policies in Secret Protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Correct. delegated bypass centralizes exception approvals in visible accountable security teams or roles
- **D:** Correct. granting Review and manage secret scanning bypass requests creates least-privilege Push Protection approvers without full Org Owner access
- **E:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges

### Question 31 — `C` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: C (is correct). `.github/secret_scanning.yml` with `paths-ignore: ["cypress/fixtures/mock_oauth/**"]` supports up to `1,000` glob entries and `<= 1 MB` file size (`while target files > 1 MB still get scanned`). [Skill 2.5: Configure Secret Protection alert recipients and path exclusions (.github/secret_scanning.yml) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning)]

- **A:** Incorrect. codeql-config.yml centralizes custom query packs, path exclusions, threat models, and data-extension model packs for Advanced Setup
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Correct. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **D:** Incorrect. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets

### Question 32 — `B` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: B (is correct). Existing open user alerts inside `test/synthetic_keys/` are automatically closed as excluded, whereas on public repositories `paths-ignore` never suppresses partner revocation notifications to token vendors. [Skill 2.5: Configure Secret Protection alert recipients and path exclusions (.github/secret_scanning.yml) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning)]

- **A:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **B:** Correct. secret_scanning.yml silences noisy user alerts in synthetic fixture directories up to 1,000 paths / 1 MB while keeping real code paths protected
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 33 — `B` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: B (is correct). Create a custom repository role inheriting `Maintain` and add `View secret scanning alerts` and `Dismiss or resolve secret scanning alerts` scoped to `fastq-aligner-cpp`. [Skill 2.5: Configure Secret Protection alert recipients and path exclusions (.github/secret_scanning.yml) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Correct. Security Manager and fine-grained custom repository roles grant AppSec and security champions exact triage permissions without over-provisioning Repository Admin or code-push rights
- **C:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 34 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). Run `Save and dry run` (`previewing up to 1,000 historical matches across org repos—or up to 10 selected repos at Enterprise scope—without generating live alerts`) before `Publish pattern` and Push Protection unlock. [Skill 2.6: Create, dry-run, and manage custom secret patterns (including Copilot regex generation and Push Protection) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning)]

- **A:** Correct. dry runs preview up to 1,000 historical matches without creating live alerts, and editing a published pattern automatically closes alerts generated by its previous version
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **D:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement

### Question 35 — `C` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: C (is correct). Quotas are `100` custom patterns per repository and `500` per organization or enterprise; only the original creator can edit an enterprise custom pattern; and saving edits to a published pattern automatically closes alerts from its prior version. [Skill 2.6: Create, dry-run, and manage custom secret patterns (including Copilot regex generation and Push Protection) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning)]

- **A:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Correct. dry runs preview up to 1,000 historical matches without creating live alerts, and editing a published pattern automatically closes alerts generated by its previous version
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 36 — `B, E, F` (Configure and use Secret Protection (formerly secret scanning))

Correct answers: B, E, and F (are correct). Custom patterns validate via dry run (`<=1,000` sample hits) before publishing, Push Protection intercepts published custom and high-confidence partner secrets pre-receive, and bypass events stream to webhooks and audit logs. [Skill 2.6: Create, dry-run, and manage custom secret patterns (including Copilot regex generation and Push Protection) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Correct. dry runs preview up to 1,000 historical matches without creating live alerts, and editing a published pattern automatically closes alerts generated by its previous version
- **C:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **E:** Correct. stopping secrets pre-receive prevents Git history contamination and emergency credential rotation
- **F:** Correct. every bypass leaves an immutable audit trail linking the actor, commit, justification, and approver

### Question 37 — `A` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: A (is correct). Upload build-resolved dependency snapshots from CI via the `Dependency Submission API` (`alongside committed lockfiles`) so GitHub's Dependency Graph tracks both direct and transitive dependencies. [Skill 3.1: Generate and interpret the dependency graph, vulnerability databases, Dependency Submission API, and SPDX SBOM exports | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository)]

- **A:** Correct. committing lockfiles plus submitting build-resolved snapshots gives GitHub complete direct and transitive dependency visibility
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 38 — `C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: C (is correct). `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`or actions/attest-sbom` for signed SPDX build provenance) exports the repository's direct and transitive dependency inventory in SPDX JSON format. [Skill 3.1: Generate and interpret the dependency graph, vulnerability databases, Dependency Submission API, and SPDX SBOM exports | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository)]

- **A:** Incorrect. the code-security configurations attach endpoint programmatically binds a Security Configuration to targeted or organization-wide repositories
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Correct. the Dependency Graph SBOM REST endpoint returns upstream direct and transitive packages in machine-readable SPDX JSON
- **D:** Incorrect. codeql github upload-results publishes externally generated SARIF 2.1.0 files to GitHub Code Scanning with exact ref and commit metadata

### Question 39 — `A` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: A (is correct). An exported Dependency Graph `SPDX` SBOM lists only upstream direct and transitive dependencies consumed *by* `open-vcf-stream` (`packages, versions, PURLs, licenses`), never downstream external `dependents`. [Skill 3.1: Generate and interpret the dependency graph, vulnerability databases, Dependency Submission API, and SPDX SBOM exports | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository)]

- **A:** Correct. GitHub exports dependency inventories, versions, licenses, and transitive relationships in standard SPDX JSON (and never includes downstream external dependents)
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **D:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure

### Question 40 — `A` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: A (is correct). Enable Dependency Graph and Dependabot alerts, disable global `Dependabot security updates` so selective PR rules govern, create an org/repo auto-triage rule on scope/EPSS/patch, and audit `resolution:auto-dismiss` plus targeted PRs. [Skill 3.2: Prioritize supply chain alerts (EPSS, CVSS, reachability) and configure Dependabot auto-triage (auto-dismiss) rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules)]

- **A:** Correct. custom Dependabot auto-triage rules run before notifications, and repository-wide Dependabot security updates must be off when using custom rules to selectively open security PRs
- **B:** Incorrect. Dependabot auto-triage rules live in Dependabot settings (where org rules override conflicting repo rules and evaluate before notifications), not secret_scanning.yml
- **C:** Incorrect. auto-triage rules require Dependabot alerts enabled, global security updates override selective PR rules, malware alerts do not open PRs, and scope changes auto-reopen alerts
- **D:** Incorrect. deleting lockfiles blinds transitive vulnerability detection, and the Dismiss package malware alerts preset suppresses false-positive internal namespace collisions rather than blocking malware

### Question 41 — `D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: D (is correct). `aiohttp`'s `0.86` `EPSS` 30-day exploitation probability combined with static `Reachability` call-path proof (`up to 5 call paths`) confirms live exploitable runtime exposure—making `aiohttp` the immediate remediation target. [Skill 3.2: Prioritize supply chain alerts (EPSS, CVSS, reachability) and configure Dependabot auto-triage (auto-dismiss) rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **D:** Correct. combining EPSS exploit likelihood and static reachability with CVSS and runtime scope focuses engineering effort on genuinely exploitable dependencies

### Question 42 — `C, D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answers: C and D (are correct). Prioritize alerts by `EPSS`, `Reachability`, CVSS, and `runtime` scope, and filter closed alerts with `resolution:auto-dismiss` to audit preset and custom Dependabot auto-triage dismissals. [Skill 3.2: Prioritize supply chain alerts (EPSS, CVSS, reachability) and configure Dependabot auto-triage (auto-dismiss) rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules)]

- **A:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Correct. high-EPSS reachable runtime vulnerabilities represent immediate real-world exploit risk compared with unreachable dev-only packages
- **D:** Correct. querying is:closed resolution:auto-dismiss audits every Dependabot alert suppressed by preset or custom auto-triage rules
- **E:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure

### Question 43 — `D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: D (is correct). Targeting a specific `manifest` path is supported in **repository-level** custom auto-triage rules (`whereas org-level custom rules match ecosystem, package, CVE, CWE, EPSS, severity, scope, and patch availability across repos, and override conflicting repo rules`). [Skill 3.3: Remediate supply chain alerts through Dependabot security updates, version updates, and security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Correct. auto-triage rules suppress low-risk noise before notifications fire, auto-reopen if metadata/scope changes, and defer to organization rules when repo rules conflict

### Question 44 — `D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: D (is correct). No—repository-wide `Dependabot security updates` must be **disabled** first so selective custom `Open a pull request` auto-triage rules control PR creation rather than opening PRs for every patchable alert. [Skill 3.3: Remediate supply chain alerts through Dependabot security updates, version updates, and security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. No—repository-wide `Dependabot security updates` must be **disabled** first so selective custom `Open a pull request` auto-triage rules control PR creation rather than opening PRs for every patchable alert.
- **B:** Incorrect. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories
- **C:** Incorrect. each gzipped SARIF upload must be <=10 MB with a distinct category per language/tool/component and security-events: write permission
- **D:** Correct. when global Dependabot security updates remain enabled, Dependabot attempts PRs for every patchable alert, overriding selective custom PR auto-triage rules

### Question 45 — `A` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: A (is correct). `Dependabot security updates` open urgent PRs upgrading vulnerable default-branch dependencies to the minimum patched release, while `.github/dependabot.yml` `version updates` keep `gomod`, `docker`, and `github-actions` dependencies current on a recurring schedule. [Skill 3.3: Remediate supply chain alerts through Dependabot security updates, version updates, and security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Correct. security updates react to GitHub Advisory Database alerts on default-branch dependencies, whereas dependabot.yml keeps dependencies and github-actions current on a schedule
- **B:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **C:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 46 — `B` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: B (is correct). Enable the Dependency Graph (`and Code Security on private repos`), add an `on: pull_request` workflow running `actions/dependency-review-action@v4`, configure `fail-on-severity` and `deny-licenses`, and enforce that check in an active branch ruleset. [Skill 3.4: Secure dependencies during development using pre-merge Dependency Review (dependency-review-action) for vulnerabilities and licenses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action)]

- **A:** Incorrect. dependabot.yml schedules dependency update PRs rather than gating developer PRs on license compliance; pre-merge gating requires dependency-review-action plus required checks
- **B:** Correct. Dependency Review compares PR base-vs-head manifests/lockfiles via the Dependency Graph and blocks vulnerable or non-compliant licenses when required on protected branches
- **C:** Incorrect. private repositories require GitHub Code Security / GHAS for Dependency Review, contents: read suffices, and unenforced checks do not block merges
- **D:** Incorrect. dependency-review-action requires pull_request base/head diffs and an active Dependency Graph, and allow-licenses / deny-licenses are mutually exclusive

### Question 47 — `C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: C (is correct). No—`allow-licenses` and `deny-licenses` are mutually exclusive inputs in `dependency-review-action@v4`; passing `allow-licenses: MIT, BSD-2-Clause` alone already blocks `GPL-2.0` and all other unlisted SPDX licenses. [Skill 3.4: Secure dependencies during development using pre-merge Dependency Review (dependency-review-action) for vulnerabilities and licenses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action)]

- **A:** Incorrect. enabling Advanced Setup disables Default Setup so custom workflow build steps, codeql-config.yml, or custom query suites govern scanning cleanly without duplicate conflicts
- **B:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. No—`allow-licenses` and `deny-licenses` are mutually exclusive inputs in `dependency-review-action@v4`; passing `allow-licenses: MIT, BSD-2-Clause` alone already blocks `GPL-2.0` and all other unlisted SPDX licenses.
- **C:** Correct. allow-licenses and deny-licenses are mutually exclusive inputs in dependency-review-action, and branch rulesets must require the check to block merging
- **D:** Incorrect. validate advisory patches locally or in an isolated private mirror without exposing exploit diffs publicly before publishing the coordinated GHSA release

### Question 48 — `A, E` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answers: A and E (are correct). Configure `actions/dependency-review-action@v4` with `fail-on-severity: high`, `fail-on-scopes: runtime`, and `deny-licenses` (`or allow-licenses`), and mark that workflow check required inside an active branch ruleset. [Skill 3.4: Secure dependencies during development using pre-merge Dependency Review (dependency-review-action) for vulnerabilities and licenses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action)]

- **A:** Correct. dependency-review-action@v4 gates pull requests on severity, dependency scope, and SPDX license policy using a single allow OR deny list
- **B:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **E:** Correct. without a required status check rule, a failing Dependency Review workflow warns on the PR without blocking merge

### Question 49 — `B` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: B (is correct). Configure `registries:` (`type: maven-repository` referencing `${{ secrets.CODEARTIFACT_TOKEN }}` in **Dependabot secrets**) and `groups:` (`matching patterns with update-types: [minor, patch]`). [Skill 3.5: Configure advanced dependency update rules in dependabot.yml (grouping, ignore rules, update strategies, private registries) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference)]

- **A:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **B:** Correct. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets
- **C:** Incorrect. codeql-config.yml centralizes custom query packs, path exclusions, threat models, and data-extension model packs for Advanced Setup
- **D:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure

### Question 50 — `A` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: A (is correct). Add `ignore:` (`dependency-name: "rails"`, `update-types: ["version-update:semver-major"]`) and set `open-pull-requests-limit: 6`. [Skill 3.5: Configure advanced dependency update rules in dependabot.yml (grouping, ignore rules, update strategies, private registries) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference)]

- **A:** Correct. grouping related updates cuts CI/PR noise dramatically, while registries + Dependabot secrets authenticate Dependabot to private npm/NuGet/PyPI/Maven feeds
- **B:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names

### Question 51 — `C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: C (is correct). Adding `package-ecosystem: "docker"` (`pointing directory to each Dockerfile folder`) in `.github/dependabot.yml` schedules automated container base-image update pull requests. [Skill 3.5: Configure advanced dependency update rules in dependabot.yml (grouping, ignore rules, update strategies, private registries) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference)]

- **A:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **B:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **C:** Correct. security updates react to GitHub Advisory Database alerts on default-branch dependencies, whereas dependabot.yml keeps dependencies and github-actions current on a schedule
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 52 — `A` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: A (is correct). Workflows triggered by `dependabot` pull requests receive a **read-only `GITHUB_TOKEN`** by default (`and read credentials only from Dependabot secrets`) to isolate untrusted dependency build scripts. [Skill 3.6: Configure supply chain alert permissions, Dependabot workflows/runners, webhooks, and external production-context integrations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/automating-dependabot-with-github-actions)]

- **A:** Correct. understanding Dependabot token/secret isolation, webhook automation, and Defender for Cloud / artifact-registry deployment context integrates supply-chain security safely into operations
- **B:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **C:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 53 — `C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: C (is correct). Querying `has:deployment runtime-risk:internet-exposed` filters Dependabot and Code Scanning backlogs down to vulnerabilities actively deployed on internet-reachable infrastructure. [Skill 3.6: Configure supply chain alert permissions, Dependabot workflows/runners, webhooks, and external production-context integrations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/automating-dependabot-with-github-actions)]

- **A:** Incorrect. the Dependency Graph SBOM REST endpoint returns upstream direct and transitive packages in machine-readable SPDX JSON
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Correct. filtering by has:deployment and runtime-risk:internet-exposed isolates alerts affecting live internet-reachable workloads
- **D:** Incorrect. querying is:closed resolution:auto-dismiss audits every Dependabot alert suppressed by preset or custom auto-triage rules

### Question 54 — `C, E` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answers: C and E (are correct). Dependabot PR workflows run with a read-only `GITHUB_TOKEN` and isolated `Dependabot secrets`, while `dependabot_alert` webhooks, custom alert roles, and deployment-context qualifiers (`has:deployment`, `runtime-risk:internet-exposed`) drive operational triage. [Skill 3.6: Configure supply chain alert permissions, Dependabot workflows/runners, webhooks, and external production-context integrations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/automating-dependabot-with-github-actions)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Correct. understanding Dependabot token/secret isolation, webhook automation, and Defender for Cloud / artifact-registry deployment context integrates supply-chain security safely into operations
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **E:** Correct. isolating Dependabot secrets and read-only default tokens protects repository secrets if a compromised upstream package alters build scripts

### Question 55 — `A` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: A (is correct). CodeQL constructs a relational AST/CFG/dataflow database for deep cross-function taint analysis in application code, while `SARIF 2.1.0` unifies specialized IaC and container scanners inside one Code Scanning interface and ruleset engine. [Skill 4.1: Compare CodeQL and third-party analysis tools and manage SARIF 2.1.0 ingestion, fingerprints, and limits | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning)]

- **A:** Correct. CodeQL excels at deep interprocedural taint tracking across supported languages while SARIF 2.1.0 lets specialized IaC/container/linter tools report into one PR interface
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`

### Question 56 — `B` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: B (is correct). Each uploaded SARIF 2.1.0 file must be `<= 10 MB` gzip-compressed with `<= 25,000` results (`retaining/displaying the top 5,000 prioritized by severity`) and `<= 1,000` `threadFlowLocations` per code-flow result (`requiring security-events: write`). [Skill 4.1: Compare CodeQL and third-party analysis tools and manage SARIF 2.1.0 ingestion, fingerprints, and limits | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning)]

- **A:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **B:** Correct. compressing SARIF under 10 MB, preserving ruleId + partialFingerprints across runs, and setting unique category strings per tool/language/monorepo slice prevents rejected or overwritten alerts
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions

### Question 57 — `A, C` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answers: A and C (are correct). Keep each gzip-compressed SARIF file `<= 10 MB` (`<= 25,000` results, top `5,000` displayed) and set a distinct `category` per tool/matrix target while preserving `ruleId` + `partialFingerprints`. [Skill 4.1: Compare CodeQL and third-party analysis tools and manage SARIF 2.1.0 ingestion, fingerprints, and limits | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning)]

- **A:** Correct. exceeding 10 MB gzipped rejects the upload outright, while noisy rule sets over 5,000 findings truncate lower-priority alerts
- **B:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **C:** Correct. distinct categories prevent multi-job uploads on the same commit from clobbering one another, while fingerprints track alerts across line shifts
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **E:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`

### Question 58 — `B` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: B (is correct). Install the CodeQL CLI bundle on the HPC build node, run `codeql database create` (`tracing the C++ build`), run `codeql database analyze --format=sarif-latest`, and upload via `codeql github upload-results` (`--sarif`, `--ref`, `--commit`). [Skill 4.2: Set up and configure Code Security via Default Setup, Advanced Setup workflows, matrix build-modes, and external CI (CodeQL CLI) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages)]

- **A:** Incorrect. omitting distinct SARIF categories causes subsequent uploads for the same commit to overwrite/mark prior component results stale, and private repos require Code Security
- **B:** Correct. external CI integrations create the semantic CodeQL database, execute query suites into SARIF 2.1.0 (`<=10 MB` gzipped), and upload results with `security_events` write auth
- **C:** Incorrect. Default Setup conflicts with custom/external CodeQL uploads, uploading SARIF requires security-events: write, and runs cap at 25,000 results (displaying top 5,000)
- **D:** Incorrect. CodeQL cannot upload raw source files or XML; a database must be created before analysis, and SARIF 2.1.0 uploads must be <=10 MB gzipped with target ref and commit SHA

### Question 59 — `D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: D (is correct). `Python` (`and pure Java without Kotlin`) supports `build-mode: none`, standard builds can use `autobuild`, and custom Intel ICX `C++` requires `build-mode: manual` (`since C/C++ and Swift never support build-mode: none`). [Skill 4.2: Set up and configure Code Security via Default Setup, Advanced Setup workflows, matrix build-modes, and external CI (CodeQL CLI) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages)]

- **A:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **B:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **C:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **D:** Correct. selecting build-mode: manual when custom flags/codegen break autobuild—or build-mode: none where supported—eliminates build-wrapper failures cleanly

### Question 60 — `D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: D (is correct). No—CodeQL `Default Setup` and custom `Advanced Setup` (`codeql.yml`) cannot actively manage CodeQL together; switching to `Advanced Setup` disables Default Setup so custom authentication and `build-mode: manual` steps run cleanly. [Skill 4.2: Set up and configure Code Security via Default Setup, Advanced Setup workflows, matrix build-modes, and external CI (CodeQL CLI) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages)]

- **A:** Incorrect. when global Dependabot security updates remain enabled, Dependabot attempts PRs for every patchable alert, overriding selective custom PR auto-triage rules
- **B:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. No—CodeQL `Default Setup` and custom `Advanced Setup` (`codeql.yml`) cannot actively manage CodeQL together; switching to `Advanced Setup` disables Default Setup so custom authentication and `build-mode: manual` steps run cleanly.
- **C:** Incorrect. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories
- **D:** Correct. enabling Advanced Setup disables Default Setup so custom workflow build steps, codeql-config.yml, or custom query suites govern scanning cleanly without duplicate conflicts

### Question 61 — `D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: D (is correct). Developers inspect each `source -> step -> sink` step to confirm shell metacharacters cannot reach execution, and classic CodeQL `Copilot Autofix` runs under `GitHub Code Security` without requiring paid GitHub Copilot seats or AI credits. [Skill 4.3: Review CodeQL dataflow analysis insights and remediate alerts using Copilot Autofix and pull request workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **D:** Correct. taint-flow paths pinpoint exact user-input sources and unvalidated sinks, while Copilot Autofix proposes context-aware diffs that must still pass CI and human review

### Question 62 — `C` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: C (is correct). `codeql github upload-results --repository=baryonmed/fastq-aligner-cpp --ref=refs/heads/main --commit=7d20a11... --sarif=aligner.sarif` (`using a GitHub App token or PAT with security_events: write`) publishes the findings. [Skill 4.3: Review CodeQL dataflow analysis insights and remediate alerts using Copilot Autofix and pull request workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning)]

- **A:** Incorrect. the Dependency Graph SBOM REST endpoint returns upstream direct and transitive packages in machine-readable SPDX JSON
- **B:** Incorrect. the code-security configurations attach endpoint programmatically binds a Security Configuration to targeted or organization-wide repositories
- **C:** Correct. codeql github upload-results publishes externally generated SARIF 2.1.0 files to GitHub Code Scanning with exact ref and commit metadata
- **D:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`

### Question 63 — `C, D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answers: C and D (are correct). Declare least-privilege `permissions: { security-events: write, contents: read, actions: read }`, and validate every `Copilot Autofix` patch with dataflow review, full CI test suites, a clean CodeQL re-scan, and human PR approval. [Skill 4.3: Review CodeQL dataflow analysis insights and remediate alerts using Copilot Autofix and pull request workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning)]

- **A:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Correct. uploading CodeQL or third-party SARIF 2.1.0 findings from GitHub Actions requires least-privilege security-events: write permission
- **D:** Correct. LLM-generated security fixes lower remediation friction dramatically, yet still require automated test and human semantic verification before merge
- **E:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions

### Question 64 — `A` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: A (is correct). Distinct `category` strings prevent multiple same-language SARIF uploads on one commit from overwriting one another and falsely closing architecture-specific SIMD alerts. [Skill 4.4: Manage code scanning alert lifecycles, dismissals, severity thresholds, and analysis categories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository)]

- **A:** Correct. branch protection rulesets filter security alerts by Critical/High/Medium/Low security-severity independently from non-security error/warning quality notes
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`

### Question 65 — `C` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: C (is correct). No—with `All alerts: None`, non-security rule severity (`Error`) does not block merges, and `Security alerts: Critical` blocks only `@security-severity >= 9.0` (`Critical`), allowing `High (8.1)` through unless changed to `High or higher`. [Skill 4.4: Manage code scanning alert lifecycles, dismissals, severity thresholds, and analysis categories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Correct. branch protection rulesets filter security alerts by Critical/High/Medium/Low security-severity independently from non-security error/warning quality notes
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 66 — `A` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: A (is correct). No—Code Scanning enforces hard ingestion limits of `<= 10 MB` gzip-compressed size and `<= 25,000` results per run (`displaying top 5,000 by severity`), rejecting oversized uploads outright. [Skill 4.4: Manage code scanning alert lifecycles, dismissals, severity thresholds, and analysis categories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository)]

- **A:** Correct. each gzipped SARIF upload must be <=10 MB with a distinct category per language/tool/component and security-events: write permission
- **B:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. No—Code Scanning enforces hard ingestion limits of `<= 10 MB` gzip-compressed size and `<= 25,000` results per run (`displaying top 5,000 by severity`), rejecting oversized uploads outright.
- **C:** Incorrect. allow-licenses and deny-licenses are mutually exclusive inputs in dependency-review-action, and branch rulesets must require the check to block merging
- **D:** Incorrect. validate advisory patches locally or in an isolated private mirror without exposing exploit diffs publicly before publishing the coordinated GHSA release

### Question 67 — `A` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: A (is correct). Define a YAML data-extension `CodeQL model pack` marking `PatientMasker.redact()` as a sanitizer/neutral summary and load it via `packs:` in `.github/codeql/codeql-config.yml`. [Skill 4.5: Optimize and troubleshoot Code Security operations with custom configurations, model packs, and build/performance diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning)]

- **A:** Correct. codeql-config.yml centralizes custom query packs, path exclusions, threat models, and data-extension model packs for Advanced Setup
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **D:** Incorrect. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets

### Question 68 — `D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: D (is correct). Split languages into parallel `matrix` jobs, exclude vendored/generated directories via `paths-ignore` in `codeql-config.yml`, and run compiled `C++`/`C#` jobs on Larger runners (`16–32+ GB RAM`). [Skill 4.5: Optimize and troubleshoot Code Security operations with custom configurations, model packs, and build/performance diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning)]

- **A:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **B:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **C:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **D:** Correct. model packs teach CodeQL custom internal framework sources/sanitizers/sinks without forking queries, while Adequate RAM/CPU runners and scoped paths resolve timeout/OOM failures

### Question 69 — `D` (Security operations: best practices, prioritization, and remediation)

Correct answer: D (is correct). `Private vulnerability reporting` opens a confidential draft `GHSA` where maintainers tag `CWE-122`, build a fix inside a temporary private fork, request a `CVE` (`via GitHub as CNA`), and publish coordinated semver advisory metadata. [Skill 5.1: Understand CVE, CWE, and GitHub Security Advisory (GHSA) concepts and execute end-to-end advisory remediation workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **D:** Correct. maintainers triage private reports inside draft GHSAs, patch silently in temporary private forks (where Actions stay disabled), request a CVE, and publish coordinated advisories

### Question 70 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). No—temporary private advisory forks disable GitHub Actions by design, and pushing a `fix/heap-overflow` branch to the public repository leaks the zero-day exploit surface before downstream clinics can patch. [Skill 5.1: Understand CVE, CWE, and GitHub Security Advisory (GHSA) concepts and execute end-to-end advisory remediation workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories)]

- **A:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. No—temporary private advisory forks disable GitHub Actions by design, and pushing a `fix/heap-overflow` branch to the public repository leaks the zero-day exploit surface before downstream clinics can patch.
- **B:** Correct. validate advisory patches locally or in an isolated private mirror without exposing exploit diffs publicly before publishing the coordinated GHSA release
- **C:** Incorrect. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories
- **D:** Incorrect. when global Dependabot security updates remain enabled, Dependabot attempts PRs for every patchable alert, overriding selective custom PR auto-triage rules

### Question 71 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). Publishing the reviewed `GHSA` updates the global GitHub Advisory Database, automatically triggering `Dependabot alerts` (`and security update PRs to 3.1.2`) across repositories whose Dependency Graph includes `< 3.1.2`. [Skill 5.1: Understand CVE, CWE, and GitHub Security Advisory (GHSA) concepts and execute end-to-end advisory remediation workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Correct. maintainers triage private reports inside draft GHSAs, patch silently in temporary private forks (where Actions stay disabled), request a CVE, and publish coordinated advisories
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 72 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). Enforce an active organization branch ruleset (`Require code scanning results` at `High or higher`) to block regressions on PRs, and prioritize default-branch backlogs using `has:deployment`, `runtime-risk:internet-exposed`, `EPSS`, and `Reachability`. [Skill 5.2: Define, prioritize, and enforce severity rulesets and production-context prioritization at scale | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-vulnerabilities/alerts-in-production-code)]

- **A:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **B:** Correct. combining runtime deployment exposure with pre-merge High/Critical blocking stops alert growth while burning down real internet-exposed production risk first
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 73 — `D` (Security operations: best practices, prioritization, and remediation)

Correct answer: D (is correct). The pull request remains **blocked from merging**, because `Require code scanning results` requires `CodeQL` to complete and report compliant results for that PR commit before merge is allowed. [Skill 5.2: Define, prioritize, and enforce severity rulesets and production-context prioritization at scale | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-vulnerabilities/alerts-in-production-code)]

- **A:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **B:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Correct. combining Rulesets with REST/GraphQL security configuration and org-level alert APIs automates compliance reporting and zero-drift enforcement across thousands of repositories

### Question 74 — `B, E` (Security operations: best practices, prioritization, and remediation)

Correct answers: B and E (are correct). Ingest deployment telemetry from Defender for Cloud / JFrog (`has:deployment`, `runtime-risk:internet-exposed`), and pilot new organization rulesets in `Evaluate` mode (`auditing Ruleset Insights`) before switching to `Active`. [Skill 5.2: Define, prioritize, and enforce severity rulesets and production-context prioritization at scale | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-vulnerabilities/alerts-in-production-code)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Correct. production context pinpoints vulnerabilities actually running in internet-facing workloads rather than dead or archived repos
- **C:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **E:** Correct. Evaluate mode surfaces missing scans or noisy rules safely without halting production releases on day one

### Question 75 — `A` (Security operations: best practices, prioritization, and remediation)

Correct answer: A (is correct). BaryonMed should filter those 195 default-branch biobank alerts in Security Overview, create a Security Campaign (`<=1,000` alerts) with deadline and AppSec lead, apply Copilot Autofix (`or assign <=25 alerts per batch to @copilot`), and verify CI tests before merge. [Skill 5.3: Execute campaign-based remediation strategies, bulk alert management, and audited alert dismissal documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/manage-security-alerts/best-practices-for-participating-in-a-security-campaign)]

- **A:** Correct. Security Campaigns group high-risk default-branch alerts around a dedicated security contact and accelerate developer burndown with Copilot Autofix or @copilot draft PRs
- **B:** Incorrect. disabling scanners or bulk-dismissing unreviewed findings hides real production vulnerabilities rather than remediating security debt
- **C:** Incorrect. agentic @copilot campaign assignments cap at 25 alerts per batch (opening a PR for human/CI verification), and Copilot cannot rotate external cloud provider IAM credentials
- **D:** Incorrect. code security campaigns target default-branch alerts (up to 1,000 per campaign) with a named contact, and developers need write access plus passing CI checks to merge fixes

### Question 76 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). A Security Campaign groups up to `1,000` default-branch alerts, and managers can assign up to `25` alerts per batch to `@copilot` (`consuming Code Security AI credits`) to open draft remediation pull requests. [Skill 5.3: Execute campaign-based remediation strategies, bulk alert management, and audited alert dismissal documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/manage-security-alerts/best-practices-for-participating-in-a-security-campaign)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Correct. grouping related CWEs into focused campaigns builds developer remediation momentum while Copilot Autofix and @copilot PR batches cut manual toil
- **C:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **D:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names

### Question 77 — `C` (Security operations: best practices, prioritization, and remediation)

Correct answer: C (is correct). Every dismissal requires a documented technical rationale comment (`retained with actor/timestamp in APIs and audit logs`), and `code_scanning_alert` webhooks / Security Overview campaign views let AppSec review and reopen unjustified closures. [Skill 5.3: Execute campaign-based remediation strategies, bulk alert management, and audited alert dismissal documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/manage-security-alerts/best-practices-for-participating-in-a-security-campaign)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Correct. alert dismissals remain visible in REST/GraphQL APIs, webhooks, and audit logs, so teams must document rationale rather than hiding unverified risk
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 78 — `D` (Security operations: best practices, prioritization, and remediation)

Correct answer: D (is correct). Configuring `queries: security-extended` runs `default` plus medium-precision security queries while omitting the maintainability/code-hygiene rules in `security-and-quality`. [Skill 5.4: Customize CodeQL query suites, multi-repository variant analysis, and risk-profile-tailored security detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites)]

- **A:** Incorrect. filtering by has:deployment and runtime-risk:internet-exposed isolates alerts affecting live internet-reachable workloads
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Incorrect. querying is:closed resolution:auto-dismiss audits every Dependabot alert suppressed by preset or custom auto-triage rules
- **D:** Correct. security-extended broadens vulnerability detection beyond default without adding non-security maintainability noise from security-and-quality

### Question 79 — `A` (Security operations: best practices, prioritization, and remediation)

Correct answer: A (is correct). `Multi-Repository Variant Analysis (MRVA)` in the CodeQL VS Code extension dispatches custom `.ql` queries via a controller repository's GitHub Actions workflow across up to 1,000 repositories. [Skill 5.4: Customize CodeQL query suites, multi-repository variant analysis, and risk-profile-tailored security detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites)]

- **A:** Correct. security-extended expands vulnerability coverage beyond high-precision default rules, while MRVA hunts novel zero-day patterns across up to 1,000 org repositories simultaneously
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 80 — `D` (Security operations: best practices, prioritization, and remediation)

Correct answer: D (is correct). Configuring `threat-models: [remote, local]` inside `.github/codeql/codeql-config.yml` includes local file reads, CLI arguments, and environment variables as untrusted taint sources. [Skill 5.4: Customize CodeQL query suites, multi-repository variant analysis, and risk-profile-tailored security detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Correct. model packs teach CodeQL custom internal framework sources/sanitizers/sinks without forking queries, while Adequate RAM/CPU runners and scoped paths resolve timeout/OOM failures

### Question 81 — `C` (Security operations: best practices, prioritization, and remediation)

Correct answer: C (is correct). Assign a custom repository role (`inheriting Write`) with fine-grained permissions to view and dismiss Code Scanning and Dependabot alerts, keeping org-wide rulesets and Security Configurations with `Security Managers`. [Skill 5.5: Collaborate across security roles, delegated exceptions, alert ownership, and cross-suite governance rulesets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)]

- **A:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Correct. clear alert ownership, delegated bypass reviewers, and Evaluate-first cross-suite rulesets align AppSec governance with engineering velocity
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 82 — `D` (Security operations: best practices, prioritization, and remediation)

Correct answer: D (is correct). That developer receives temporary single-alert visibility to view and resolve **only** alert `#29` (`not other secret alerts in pharmacogenomics-kb`), which automatically revokes if they are unassigned. [Skill 5.5: Collaborate across security roles, delegated exceptions, alert ownership, and cross-suite governance rulesets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)]

- **A:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **D:** Correct. clear alert ownership, delegated bypass reviewers, and Evaluate-first cross-suite rulesets align AppSec governance with engineering velocity

### Question 83 — `B, E` (Security operations: best practices, prioritization, and remediation)

Correct answers: B and E (are correct). Combine `Security Manager`, granular custom alert roles, and explicit alert `Assignees`, and enforce Push Protection `delegated bypass` backed by visible reviewer teams or custom bypass-approver roles. [Skill 5.5: Collaborate across security roles, delegated exceptions, alert ownership, and cross-suite governance rulesets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Correct. delegated bypass replaces ad-hoc writer self-bypasses with a structured request-and-approval workflow audited via webhooks and logs
- **C:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **E:** Correct. clear alert ownership, delegated bypass reviewers, and Evaluate-first cross-suite rulesets align AppSec governance with engineering velocity

### Question 84 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). Combine pre-receive `Push Protection`, PR `actions/dependency-review-action@v4`, and PR `CodeQL` analysis with `Copilot Autofix` gated by an active branch ruleset. [Skill 5.6: Shift left and strengthen preventive security through push protection, pre-merge dependency scanning, and PR CodeQL analysis | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Correct. combining all three shift-left controls prevents new security debt from ever landing on the default branch
- **C:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 85 — `C` (Security operations: best practices, prioritization, and remediation)

Correct answer: C (is correct). Pre-receive Push Protection rejects the push before the secret ever lands in remote Git objects, webhooks, clones, or PR caches—eliminating mandatory credential rotation and `git filter-repo` history rewrites. [Skill 5.6: Shift left and strengthen preventive security through push protection, pre-merge dependency scanning, and PR CodeQL analysis | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Correct. blocking leaked credentials before the remote ref updates avoids costly key rotation, incident response, and Git history rewrites
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 86 — `A, B, C` (Security operations: best practices, prioritization, and remediation)

Correct answers: A, B, and C (are correct). Block high-confidence secrets pre-receive via Push Protection, gate pull-request dependency vulnerabilities and SPDX licenses via `dependency-review-action@v4`, and verify CodeQL `Copilot Autofix` patches with CI tests and human review. [Skill 5.6: Shift left and strengthen preventive security through push protection, pre-merge dependency scanning, and PR CodeQL analysis | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Correct. LLM-generated security fixes lower remediation friction dramatically, yet still require automated test and human semantic verification before merge
- **B:** Correct. stopping secrets pre-receive prevents Git history contamination and emergency credential rotation
- **C:** Correct. Dependency Review blocks both vulnerable package versions and prohibited copyleft/unknown licenses on pull requests
- **D:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **E:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **F:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure

### Question 87 — `B` (GitHub Security suites administration)

Correct answer: B (is correct). BaryonMed should verify active-committer seat capacity (`or metered budget`), build Security Configurations for `clinical`/`biobank`/`research`, attach via custom properties with `Apply to new repositories` enabled, and enforce baseline locks with `Enforced`. [Skill 6.1: Roll out GitHub Security Suites at enterprise, organization, and repository scale and contrast GHEC vs. GHES capabilities | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/choosing-a-security-configuration-for-your-repositories)]

- **A:** Incorrect. manual per-repo changes do not scale or prevent configuration drift, and granting Organization Owner violates least privilege when Security Manager / Security Configurations exist
- **B:** Correct. rolling out Security Configurations verifies committer license capacity first, targets repo tiers via custom properties, covers newly created repos, and locks drift with Enforced mode
- **C:** Incorrect. standalone GHES uses volume/subscription licensing (not metered billing) and requires GitHub Connect for Advisory DB sync, while transferred repos must be explicitly targeted by configurations
- **D:** Incorrect. exceeding volume committer licenses blocks enablement on additional/new private repos, and features left as Not set remain editable by repository admins even under Enforced configurations

### Question 88 — `B` (GitHub Security suites administration)

Correct answer: B (is correct). `GHEC` supports metered or volume billing plus cloud AI features (`Copilot Autofix`, AI push secret detection), whereas `GHES` uses volume/subscription licensing and relies on `GitHub Connect` to sync the GitHub Advisory Database and deduplicate hybrid 90-day active committers. [Skill 6.1: Roll out GitHub Security Suites at enterprise, organization, and repository scale and contrast GHEC vs. GHES capabilities | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/choosing-a-security-configuration-for-your-repositories)]

- **A:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **B:** Correct. Security Configurations eliminate manual repo drift on GHEC and GHES, while hybrid enterprises link GHES to GHEC via GitHub Connect for Advisory DB updates and committer seat deduplication
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 89 — `B` (GitHub Security suites administration)

Correct answer: B (is correct). `Apply to new repositories` applies only to newly created or newly forked repositories inside the org; transferred repositories do not inherit new-repo defaults automatically and must have the Security Configuration explicitly attached. [Skill 6.1: Roll out GitHub Security Suites at enterprise, organization, and repository scale and contrast GHEC vs. GHES capabilities | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/choosing-a-security-configuration-for-your-repositories)]

- **A:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **B:** Correct. understanding Enforced vs Unenforced inheritance, transferred-repo gaps, 90-day active committer deduplication, and hard budgets on metered SKUs/AI credits prevents surprise overages or lockouts
- **C:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 90 — `D` (GitHub Security suites administration)

Correct answer: D (is correct). No—even inside an `Enforced` Security Configuration, any feature left as `"Not set"` stays unlocked and editable by repository administrators (`which is useful when letting specific repos configure custom Advanced Setup, or set Enabled/Disabled explicitly to lock`). [Skill 6.2: Configure suite defaults, Enforced vs. Unenforced inheritance, 90-day active-committer licensing, and AI credit budgets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/billing/concepts/product-billing/github-advanced-security)]

- **A:** Incorrect. when global Dependabot security updates remain enabled, Dependabot attempts PRs for every patchable alert, overriding selective custom PR auto-triage rules
- **B:** Incorrect. validate advisory patches locally or in an isolated private mirror without exposing exploit diffs publicly before publishing the coordinated GHSA release
- **C:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. No—even inside an `Enforced` Security Configuration, any feature left as `"Not set"` stays unlocked and editable by repository administrators (`which is useful when letting specific repos configure custom Advanced Setup, or set Enabled/Disabled explicitly to lock`).
- **D:** Correct. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories

### Question 91 — `A` (GitHub Security suites administration)

Correct answer: A (is correct). At `100%` volume-seat utilization (`0` available seats), GitHub prevents automatic enablement of paid GHAS / Code Security features on new private repositories, whereas pay-as-you-go metered billing on GitHub.com scales elastically up to configured hard spending budgets. [Skill 6.2: Configure suite defaults, Enforced vs. Unenforced inheritance, 90-day active-committer licensing, and AI credit budgets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/billing/concepts/product-billing/github-advanced-security)]

- **A:** Correct. understanding Enforced vs Unenforced inheritance, transferred-repo gaps, 90-day active committer deduplication, and hard budgets on metered SKUs/AI credits prevents surprise overages or lockouts
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **D:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers

### Question 92 — `B, C` (GitHub Security suites administration)

Correct answers: B and C (are correct). Active-committer seats count unique human committers over the rolling 90-day window deduplicated across the enterprise (`syncing GHEC + GHES via GitHub Connect`), and **hard metered budgets** cap overage spend on `Code Security AI credits` and `Secret Protection AI credits`. [Skill 6.2: Configure suite defaults, Enforced vs. Unenforced inheritance, 90-day active-committer licensing, and AI credit budgets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/billing/concepts/product-billing/github-advanced-security)]

- **A:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **B:** Correct. classic CodeQL Copilot Autofix does not consume AI credits, whereas agentic autofix / AI Scan and AI push secret scanning draw from included or metered AI credit pools
- **C:** Correct. a developer pushing to 50 GHAS-enabled repos in an enterprise consumes only one active-committer license seat over the rolling 90-day window
- **D:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **E:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)

### Question 93 — `B` (GitHub Security suites administration)

Correct answer: B (is correct). Existing enabled repositories stay active without interruption, and `Enterprise Owners`, `Organization Owners`, and `Security Managers` retain full authority to attach or update Security Configurations while individual Repository Admins cannot toggle licensing. [Skill 6.3: Define enterprise and organization security policies, enforcement boundaries, bypass permissions, and audit log governance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Correct. enterprise policies prevent uncontrolled repo-admin license consumption while audit log streaming preserves tamper-evident compliance records across configuration and bypass events
- **C:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **D:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers

### Question 94 — `C` (GitHub Security suites administration)

Correct answer: C (is correct). Streaming `security_configuration.*`, `repository_ruleset.*`, `secret_scanning_push_protection_bypass`, `secret_scanning_custom_pattern.*`, and alert `dismiss`/`resolve` audit events provides tamper-evident compliance records. [Skill 6.3: Define enterprise and organization security policies, enforcement boundaries, bypass permissions, and audit log governance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Correct. enterprise policies prevent uncontrolled repo-admin license consumption while audit log streaming preserves tamper-evident compliance records across configuration and bypass events
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 95 — `D` (GitHub Security suites administration)

Correct answer: D (is correct). **`0`** seats: seats automatically free up once a user has zero pushes to enabled private/internal repositories over the rolling last **90 days** (`Dr. Lin`), or immediately upon removal from the organization/enterprise (`Sam`). [Skill 6.3: Define enterprise and organization security policies, enforcement boundaries, bypass permissions, and audit log governance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise)]

- **A:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **B:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Correct. understanding Enforced vs Unenforced inheritance, transferred-repo gaps, 90-day active committer deduplication, and hard budgets on metered SKUs/AI credits prevents surprise overages or lockouts

### Question 96 — `D` (GitHub Security suites administration)

Correct answer: D (is correct). Assigning the **`Security Manager`** organization role to `@baryonmed/appsec` provides org-wide alert read/write, campaign management, and Security Configuration governance without source-write or billing-owner rights. [Skill 6.4: Define administrator, Security Manager, developer, and fine-grained custom roles for viewing and dismissing security alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **D:** Correct. Security Manager and fine-grained custom repository roles grant AppSec and security champions exact triage permissions without over-provisioning Repository Admin or code-push rights

### Question 97 — `C` (GitHub Security suites administration)

Correct answer: C (is correct). Create a custom repository role inheriting `Read` and enable only `View Dependabot alerts` and `View code scanning alerts`. [Skill 6.4: Define administrator, Security Manager, developer, and fine-grained custom roles for viewing and dismissing security alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization)]

- **A:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **B:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **C:** Correct. Security Manager and fine-grained custom repository roles grant AppSec and security champions exact triage permissions without over-provisioning Repository Admin or code-push rights
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 98 — `C` (GitHub Security suites administration)

Correct answer: C (is correct). Granting `Review and manage secret scanning bypass requests` in a custom organization role scopes Push Protection delegated-bypass approval rights with least privilege. [Skill 6.4: Define administrator, Security Manager, developer, and fine-grained custom roles for viewing and dismissing security alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Incorrect. uploading CodeQL or third-party SARIF 2.1.0 findings from GitHub Actions requires least-privilege security-events: write permission
- **C:** Correct. granting Review and manage secret scanning bypass requests creates least-privilege Push Protection approvers without full Org Owner access
- **D:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges

### Question 99 — `C` (GitHub Security suites administration)

Correct answer: C (is correct). BaryonMed should standardize CodeQL across all 75 genomics repos first, create the Organization Branch Ruleset in `Evaluate` mode requiring `High+` CodeQL results, inspect Ruleset Insights and scope break-glass bypasses, then flip enforcement to `Active`. [Skill 6.5: Enforce default or approved custom CodeQL workflows and automate large-scale security governance via REST and GraphQL APIs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/rest/code-security/configurations)]

- **A:** Incorrect. Require code scanning results blocks PR merges until the configured tool reports scan results for that pull request head/merge ref
- **B:** Incorrect. requiring CodeQL results before CodeQL runs deadlocks every PR awaiting a missing scan, while granting broad writer bypass or blocking on Note hints breaks governance
- **C:** Correct. piloting an Organization Ruleset in Evaluate mode confirms CodeQL check reporting and false-positive impact before switching Require code scanning results to Active merge blocking
- **D:** Incorrect. secret_scanning.yml only configures secret path exclusions, and AI suggestions never replace required human pull-request approvals

### Question 100 — `B, C` (GitHub Security suites administration)

Correct answers: B and C (are correct). BaryonMed combines Required Workflows + `Require code scanning results` rulesets with `POST /orgs/{org}/code-security/configurations/{configuration_id}/attach` and single-stream org/enterprise alert endpoints (`GET /orgs/{org}/code-scanning/alerts`, `/secret-scanning/alerts`, `/dependabot/alerts`) for BigQuery ingestion. [Skill 6.5: Enforce default or approved custom CodeQL workflows and automate large-scale security governance via REST and GraphQL APIs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/rest/code-security/configurations)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Correct. combining Rulesets with REST/GraphQL security configuration and org-level alert APIs automates compliance reporting and zero-drift enforcement across thousands of repositories
- **C:** Correct. the code-security configurations attach endpoint programmatically binds a Security Configuration to targeted or organization-wide repositories
- **D:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **E:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
