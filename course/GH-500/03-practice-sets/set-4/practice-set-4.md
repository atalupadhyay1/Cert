# Microsoft / GitHub Exam GH-500: GitHub Advanced Security — Full-Length Mock Exam 4

**Theme:** Code Security (CodeQL), SARIF 2.1.0 Ingestion, Matrix Build Modes, Taint Dataflow & Copilot Autofix  
**Credential:** `GitHub Advanced Security` *(Intermediate · **no prerequisite** · **2-year validity** transitioning to Microsoft Learn recertification)*  
**Study guide baseline:** `July 2026 (Last updated May 14, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-500 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Advanced Security documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Describe GitHub Security suites, features, and ecosystem (15–20% official weight · 18 questions)

### 1. PelagicGrid Offshore manages maritime routing repositories (`vessel-ais-router`, `ballast-control-swift`) on a standalone `GitHub Team` organization and wants `GitHub Secret Protection` today, deferring `GitHub Code Security` until Q3 budget sign-off. How does GitHub's SKU model support this?

- **A.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **B.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **C.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **D.** Standalone `GitHub Secret Protection` and `GitHub Code Security` SKUs (`purchasable separately or together on GitHub Team and GitHub Enterprise`, alongside legacy bundled GHAS)

### 2. PelagicGrid Offshore's NERC-CIP compliance lead is mapping controls for leaked SCADA MQTT broker credentials, command-injection bugs in `grid-dispatch-java`, and vulnerable Python ML libraries in `forecast-wave-ml`. Which GitHub Security pillars govern those three risk classes?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** `Secret Protection` (`secret scanning + push protection`), `Code Security` (`CodeQL/SARIF SAST + Copilot Autofix`), and `Supply Chain Security` (`Dependency Graph, Dependabot, Dependency Review & SBOMs`)

### 3. PelagicGrid Offshore's OT security board is reviewing feature entitlements across `GitHub Secret Protection` and `GitHub Code Security` before contracting seats for 70 offshore-wind repositories. Which two statements accurately describe each SKU? Select two.

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** `GitHub Secret Protection` prevents and detects leaked credentials via `Push Protection`, `secret scanning`, `validity checks`, custom patterns, and AI generic secret detection
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** `GitHub Code Security` finds and fixes code and dependency risks via `CodeQL` / `SARIF` code scanning, `Copilot Autofix`, `Dependency Review` on private repos, and `Security Campaigns`
- **E.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 4. PelagicGrid Offshore publishes an open-source IEC-61850 packet decoder (`open-iec61850-go`) in a `public` GitHub.com repo while running `substation-iec61850` inside a `private` GHEC organization. Which security capabilities run at zero license cost on the public decoder repo?

- **A.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Core features (`secret scanning, push protection, Dependency Graph, Dependabot, CodeQL default setup & Dependency Review`) are free on `public` GitHub.com repos; `private/internal` repos require licensed SKUs where applicable
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 5. PelagicGrid Offshore tagged 42 offshore substation repositories with custom property `ot_zone:hvdc_ring` and needs an executive rollup of scanner enablement coverage, open critical risk, and active campaign progress (`____`). Which native GitHub view provides this?

- **A.** `Security Overview` (`Organization & Enterprise Risk, Coverage, Campaigns, Code scanning, Secret scanning & Dependabot dashboards` filterable by team, topic, or custom property)
- **B.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **C.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **D.** `.github/codeql/codeql-config.yml` (`defining packs:, queries:, paths-ignore:, and threat-models: alongside YAML model-pack extensions`)

### 6. PelagicGrid Offshore acquired a subsea ROV inspection startup whose GitHub org has no paid security licenses yet and wants a free baseline count of leaked tokens plus sample CodeQL + Copilot Autofix findings across up to `20` active repos. Which Security Overview capability (`____`) runs this?

- **A.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **B.** Organization `free security risk assessment` (`scanning org repos for leaked secrets and up to 20 active repositories for CodeQL vulnerabilities + Copilot Autofix preview`)
- **C.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **D.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners

### 7. In `offshore-opcua-bridge`, Secret Protection flagged a base64 X.509 private key committed inside an `.env.staging` file, whereas CodeQL flagged an unvalidated OPC-UA node string flowing into `Runtime.getRuntime().exec()` in Java. What distinguishes how the two suites analyze repositories?

- **A.** `Secret Protection` matches structured/high-entropy/AI secret tokens across Git history & pushes, whereas `Code Security (CodeQL)` traces semantic AST/dataflow vulnerabilities (`including hardcoded-credential sinks`)
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 8. PelagicGrid Offshore wants every feature branch on `dayahead-bidding-svc` checked automatically for energy-exchange API keys at push time and for vulnerable Maven dependencies plus Java taint flaws on pull requests. Which combined architecture delivers this?

- **A.** Layer `Push Protection` (`pre-receive`), `actions/dependency-review-action` (`PR manifest/license gate`), and `CodeQL` PR checks (`with Copilot Autofix`) so secrets, vulnerable packages, and taint flaws fail pre-merge
- **B.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **C.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 9. PelagicGrid Offshore wants `rov-inspection-cv` (`Python + TypeScript`) protected so high-confidence cloud secrets never enter Git history and pull-request code vulnerabilities generate automated fix diffs before merge. Proposed solution: Enable `GitHub Secret Protection` (`with Push Protection`) and `GitHub Code Security` (`CodeQL Default Setup` with `Copilot Autofix`), enforcing CodeQL via an active branch ruleset. Does this satisfy all requirements?

- **A.** No — CodeQL `Default Setup` and custom `Advanced Setup` (`.github/workflows/codeql.yml`) cannot run active CodeQL management simultaneously (`switch to Advanced Setup with build-mode: manual`)
- **B.** No — `actions/dependency-review-action` forbids specifying `allow-licenses` and `deny-licenses` together, and fails to block merges unless marked as a required status check on `pull_request`
- **C.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **D.** No — `.github/secret_scanning.yml` `paths-ignore` only auto-closes post-push user alerts (`<=1,000` paths / `<=1 MB`) and neither revokes keys nor replaces Push Protection / public partner alerts

### 10. PelagicGrid Offshore is replacing a semi-annual maritime classification audit bottleneck on `turbine-pitch-plc` with a prevention-first DevSecOps pipeline. In what order should GitHub Security controls operate across the developer workflow?

- **A.** Apply Copilot Autofix before running CodeQL → run Push Protection only after merging to main → skip Dependency Review on lockfiles → delete Security Overview roles
- **B.** Block secrets pre-receive via Push Protection → run Dependency Review & CodeQL on the PR → apply Copilot Autofix or patch vulnerable packages before merge → monitor default-branch advisories in Security Overview
- **C.** Merge PRs without checks to main → run weekly manual secret scans → disable Push Protection to avoid developer friction → export CSVs quarterly without remediating open alerts
- **D.** Dismiss all PR alerts automatically → merge vulnerable dependencies → run Dependency Review only on archived branches → rely on gitignore to revoke leaked API tokens

### 11. Why does PelagicGrid Offshore's AppSec charter prioritize pre-receive Push Protection and PR-time CodeQL + Copilot Autofix over running a single security gate right before offshore vessel firmware deployment?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Prevention-first (`Push Protection + IDE/PR Dependency Review + PR CodeQL with Copilot Autofix`) stops defects before Git history/merge, whereas late release-only gates cause expensive rework

### 12. PelagicGrid Offshore needs eight SCADA engineering squads to remediate 520 legacy SSRF, path-traversal, and SQLi findings on default branches ahead of winter grid peak, backed by an AppSec advisor. Which native feature (`____`) coordinates this?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **C.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **D.** `Security Campaigns` (`targeted, time-bound initiatives grouping up to 1,000 default-branch alerts with a named security contact and Copilot Autofix support`)

### 13. On `ballast-control-swift`, an engineer wants to close a CodeQL alert inside an offline wave-tank simulator fixture as `Used in tests`. What governance trail does GitHub record when the alert is dismissed?

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Dismissing an alert requires a structured closure reason (`False positive`, `Used in tests`, `Won't fix`) plus an audit-logged justification comment—and never deletes commits or revokes keys
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 14. A telemetry contractor pushed a live maritime Inmarsat API key to `vessel-ais-router` and immediately received a Secret Protection alert. Proposed solution: Dismiss the alert as `False positive` so Security Overview risk counts clear while leaving the Inmarsat key unrotated. Does this eliminate the exposure?

- **A.** No — dismissing a Secret Protection alert or deleting the line in a new commit leaves the live credential active and exposed in prior Git history (`revoke & rotate first, then purge history`)
- **B.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **C.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)
- **D.** No — temporary private forks created inside a Repository Security Advisory (`GHSA`) intentionally **disable GitHub Actions** (`and pushing fixes to a public branch before release leaks the zero-day`)

### 15. PelagicGrid Offshore's NERC-CIP auditors require verifiable controls over any closed security alert that was not fixed in code. Which two practices satisfy this audit requirement? Select two.

- **A.** Monitor dismissed and open alert trends centrally in `Security Overview` and `Audit Logs` (`repository_vulnerability_alert`, `secret_scanning_alert`, `code_scanning_alert`)
- **B.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **E.** Require an accurate dismissal reason (`False positive`, `Used in tests`, or `Won't fix`) with a reviewer-auditable justification comment whenever dismissing an alert

### 16. How should PelagicGrid Offshore divide responsibilities across Enterprise Admins, OT Security Managers, and SCADA Software Engineers?

- **A.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **B.** Shared security model: `Admins` govern licensing/Security Configurations, `Security Managers` monitor Security Overview/campaigns/policies, and `Developers` remediate PR & campaign findings
- **C.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 17. On `subsea-hvdc-telemetry`, why should raw Secret Protection alert details remain restricted to privileged security roles while Push Protection uses `delegated bypass`?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **C.** Least-privilege alert access (`Write/Maintain/Admin/Security Manager` or custom roles) paired with `delegated bypass` so designated reviewers audit push-protection exceptions
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 18. PelagicGrid Offshore is ratifying an enterprise DevSecOps standard spanning role accountability, push-protection exception governance, and pre-merge pull-request supply-chain checks. Which three statements belong in that standard? Select three.

- **A.** Least-privilege alert access (`Write/Maintain/Admin/Security Manager` or custom roles) paired with `delegated bypass` so designated reviewers audit push-protection exceptions
- **B.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **C.** Shared security model: `Admins` govern licensing/Security Configurations, `Security Managers` monitor Security Overview/campaigns/policies, and `Developers` remediate PR & campaign findings
- **D.** `actions/dependency-review-action@v4` on `pull_request` (`with fail-on-severity, mutually exclusive allow-licenses OR deny-licenses SPDX lists, fail-on-scopes, and allow-ghsas`) enforced as a required check
- **E.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **F.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations

---

## Domain 2 — Configure and use Secret Protection (formerly secret scanning) (15–20% official weight · 18 questions)

### 19. PelagicGrid Offshore creates new offshore-wind microservice repositories weekly and wants `Secret scanning`, `Push Protection`, and `Validity checks` enabled automatically on all existing and future repos in `pelagicgrid-ot`. Which setting (`____`) achieves this?

- **A.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **B.** Enable `GitHub Secret Protection` (`secret scanning + push protection`) via Organization/Enterprise `Security Configurations` (`with Apply to new repositories`) or Repository `Settings -> Advanced Security`
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 20. Contrast what happens when a developer commits a Cloudflare API token to PelagicGrid's `public` `open-iec61850-go` repo versus committing one to the `private` `subsea-hvdc-telemetry` repo (`with Secret Protection enabled`).

- **A.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **B.** On `public` repos, partner patterns run free and auto-notify token providers for revocation; on `private/internal` repos (`with Secret Protection`), alerts notify repo/org users (`plus optional validity checks`)
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 21. PelagicGrid Offshore's Enterprise Owner disables `Repository administrators can enable or disable GitHub Secret Protection` to stop unplanned metered seat usage. What is the immediate impact on the 70 repositories already running Secret Protection?

- **A.** Enforce Enterprise Advanced Security policies (`restricting repo admins while preserving Org Owner/Security Manager control`), scope ruleset/push-protection bypass actors, and stream `security_configuration.*` / alert audit logs
- **B.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations

### 22. An offshore data engineer uses a custom Python script calling GitHub's `PUT /repos/{owner}/{repo}/contents/{path}` REST API to commit a config file containing a live Databricks token to `forecast-wave-ml`, and receives an HTTP `409 / GH013` secret block. Which control (`____`) intercepted the API commit?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** `Push Protection` intercepts supported high-confidence and published custom secrets pre-receive during `git push` (`CLI, IDE, web editor & REST API`), blocking the secret from entering Git history

### 23. On `dayahead-bidding-svc`, Secret Protection shows 2 `Active` AWS keys, 11 `Inactive` keys, and 5 non-provider generic PostgreSQL connection strings. Why should responders jump straight to the `Active` AWS keys—while still manually verifying the 5 PostgreSQL strings?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** `Validity checks` query partner token endpoints (`displaying Active, Inactive, or Unknown`) so responders prioritize live `Active` credentials first
- **C.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 24. PelagicGrid Offshore wants `offshore-opcua-bridge` protected against both standard cloud tokens at `git push` and unstructured SCADA PLC passwords in `.ini` files. Which two Secret Protection capabilities address both threats? Select two.

- **A.** `Non-provider / generic pattern scanning` (`private keys, DB connection strings`) plus `Copilot AI generic secret detection` (`unstructured passwords/keys`, consuming `Secret Protection AI credits` on push)
- **B.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **C.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **D.** `Push Protection` blocks high-confidence partner and published custom secrets pre-receive during `git push` before commits land on GitHub
- **E.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 25. Secret Protection raises an `Active` alert for a Grafana Cloud API token committed to `subsea-hvdc-telemetry` 20 minutes ago. In what chronological order must PelagicGrid Offshore execute incident remediation?

- **A.** Run git filter-repo first while leaving the production key active for 30 days → disable Secret Protection to clear UI banners → rotate the key only if an outage occurs → skip audit notes
- **B.** Add paths-ignore in .github/secret_scanning.yml to auto-close the live production key alert → keep the credential unrotated → merge to main → archive the audit log
- **C.** Confirm alert validity & blast radius → revoke and rotate the compromised credential at the provider → purge commit history (`git filter-repo`) & contact Support if cached PRs remain → resolve the alert as Revoked
- **D.** Dismiss the alert as Won't fix → delete the line in a new commit while keeping the live key active → add the file to .gitignore → assume old commits are unreadable

### 26. Why does GitHub's Secret Protection guidance state that any secret pushed to a remote repository must be considered **compromised** even if the repository is `private` and `git push --force` removed the commit within 60 seconds?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** Treat every committed secret as compromised: `revoke & rotate at the issuing provider immediately`, rewrite Git history (`git filter-repo`), purge cached views via Support if needed, and resolve as `Revoked`
- **C.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 27. During backlog cleanup on `rov-inspection-cv`, an AppSec analyst finds an alert triggered by a randomly generated test UUID in `tests/mock_auth.py` that matches a vendor prefix by coincidence. Which resolution reason (`____`) and practice should be used?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **D.** Dismissing an alert requires a structured closure reason (`False positive`, `Used in tests`, `Won't fix`) plus an audit-logged justification comment—and never deletes commits or revokes keys

### 28. PelagicGrid Offshore wants offshore field engineers who hit a false-positive Push Protection block on `turbine-pitch-plc` to request override approval from `@pelagicgrid/ot-cert-approvers` rather than self-bypassing. Which setting (`____`) enforces this workflow?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **C.** `Delegated bypass for push protection` (`granting Specific roles, visible teams, or custom roles with "Review and manage secret scanning bypass requests" authority—never secret teams`)
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 29. PelagicGrid Offshore wants to stop developers from pushing secrets to `vessel-ais-router` unless an OT Security Reviewer approves the exception, using a hidden **secret team** (`@pelagicgrid/hidden-soc`) as the approver list. Proposed solution: Add the secret team `@pelagicgrid/hidden-soc` to Push Protection delegated bypass (`or list them inside .github/secret_scanning.yml`). Does this work?

- **A.** No — CodeQL `Default Setup` and custom `Advanced Setup` (`.github/workflows/codeql.yml`) cannot run active CodeQL management simultaneously (`switch to Advanced Setup with build-mode: manual`)
- **B.** No — `.github/secret_scanning.yml` `paths-ignore` only auto-closes post-push user alerts (`<=1,000` paths / `<=1 MB`) and neither revokes keys nor replaces Push Protection / public partner alerts
- **C.** No — Code Scanning rejects gzip-compressed SARIF files larger than `10 MB` (`and overwrites prior alerts when multiple matrix uploads share an identical SARIF category on one commit`)
- **D.** Yes — this configuration satisfies every security, licensing, and governance requirement

### 30. PelagicGrid Offshore wants shift leads in Aberdeen and Stavanger to approve Push Protection bypass requests without giving them full `Security Manager` or `Organization Owner` privileges. Which two configuration rules apply? Select two.

- **A.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **B.** Assign `Specific roles, visible teams, or custom org roles` (`never secret teams`) to the Push Protection delegated bypass list to review and approve contributor bypass requests
- **C.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **D.** `Review and manage secret scanning bypass requests` (`fine-grained organization role permission for Push Protection delegated bypass`)
- **E.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 31. `substation-iec61850` stores 450 synthetic X.509 test certificates under `testdata/iec_certs/**`. Which exact repository file and YAML key (`____`) suppresses user Secret Protection alerts in that directory, and what are its two hard limits?

- **A.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **B.** `.github/codeql/codeql-config.yml` (`defining packs:, queries:, paths-ignore:, and threat-models: alongside YAML model-pack extensions`)
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`

### 32. On PelagicGrid Offshore's `public` `open-iec61850-go` repository, `.github/secret_scanning.yml` contains `paths-ignore: ["fixtures/**"]`. Why did AWS still email PelagicGrid revoking an IAM test key accidentally committed inside `fixtures/s3_sample.go`?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** `.github/secret_scanning.yml` with `paths-ignore:` (`up to 1,000 glob entries and <= 1 MB file size`) auto-closing user alerts in test/docs paths (`without suppressing public-repo partner revocation alerts`)
- **D.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config

### 33. PelagicGrid Offshore wants the lead maintainer of `ballast-control-swift` (`who holds Maintain access, not Admin`) to view and resolve Secret Protection alerts on that single repository. How can an admin grant this with least privilege?

- **A.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **B.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **C.** Separate `Enterprise/Org Owners` (`billing & global policy`), `Security Managers` (`org-wide alert read/write & security config management, without code-write`), and custom repository roles (`granular view/dismiss per tool`)
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 34. PelagicGrid Offshore's HVDC SCADA gateways authenticate with tokens formatted as `PGRID_HVDC_[0-9A-Z]{36}`. When an AppSec engineer drafts this custom org pattern (`optionally using Generate with AI`), why is the `Enable push protection` checkbox initially disabled?

- **A.** Custom regex patterns (`up to 100/repo or 500/org-or-enterprise`, optional `Generate with AI` & `before`/`after` context) validated via `Save and dry run` (`<=1,000` sample hits) before `Publish pattern` & Push Protection
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 35. PelagicGrid Offshore's original Enterprise Owner created an enterprise-level custom secret pattern last year and has now asked a second Enterprise Owner to modify its regex. What enterprise custom-pattern rule applies, and what happens to old alerts when a custom pattern is edited?

- **A.** Custom regex patterns (`up to 100/repo or 500/org-or-enterprise`, optional `Generate with AI` & `before`/`after` context) validated via `Save and dry run` (`<=1,000` sample hits) before `Publish pattern` & Push Protection
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 36. PelagicGrid Offshore is auditing its end-to-end Secret Protection posture across 70 maritime and grid repositories. Which three statements accurately reflect GitHub Secret Protection behavior? Select three.

- **A.** `Validity checks` verify supported partner tokens (`Active` vs `Inactive`) so responders remediate live exploitable credentials immediately
- **B.** Custom regex patterns (`up to 100/repo or 500/org-or-enterprise`, optional `Generate with AI` & `before`/`after` context) validated via `Save and dry run` (`<=1,000` sample hits) before `Publish pattern` & Push Protection
- **C.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **D.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **E.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **F.** `Push Protection` blocks high-confidence partner and published custom secrets pre-receive during `git push` before commits land on GitHub

---

## Domain 3 — Configure and use supply chain security (formerly Dependabot/Dependency Review) (15–20% official weight · 18 questions)

### 37. `grid-dispatch-java` resolves Gradle dynamic version ranges and custom shaded JARs during CI builds, while `turbine-pitch-plc` compiles C++ vcpkg libraries. How can PelagicGrid Offshore feed complete resolved transitive trees into GitHub's Dependency Graph?

- **A.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** `Dependency Graph` (`parsing committed manifests and lockfiles`, augmented by the `Dependency Submission API` for build-time resolved transitive graphs in Maven/Gradle/C++/containers)

### 38. European Cyber Resilience Act (`CRA`) compliance requires PelagicGrid Offshore to archive an `SPDX` JSON SBOM for every firmware release of `substation-iec61850`. Which REST API endpoint (`____`) exports this SBOM?

- **A.** `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`exporting the repository dependency inventory in SPDX JSON format`)
- **B.** `codeql github upload-results --repository=<org/repo> --ref=<refs/heads/main> --commit=<sha> --sarif=<results.sarif>`
- **C.** `POST /orgs/{org}/code-security/configurations/{configuration_id}/attach` (`attaching a Security Configuration across selected or all org repos via REST`)
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 39. Does exporting the Dependency Graph SBOM from PelagicGrid Offshore's shared `pelagic-modbus-lib` repository enumerate the 19 internal SCADA apps that import `pelagic-modbus-lib`?

- **A.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** Export an `SPDX` JSON Software Bill of Materials (`SBOM`) via `Insights -> Dependency graph -> Export SBOM`, `GET /repos/{owner}/{repo}/dependency-graph/sbom`, or `actions/attest-sbom` (`excluding dependents`)
- **D.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step

### 40. PelagicGrid Offshore wants `forecast-wave-ml` to auto-dismiss low-risk dev-only test dependencies before notifications fire while automatically opening Dependabot security PRs **only** for `Critical`/`High` runtime alerts with `EPSS >= 0.08`. What is the exact setup order?

- **A.** Enable Dependency Graph & Dependabot alerts → disable global `Dependabot security updates` where custom PR rules govern → create an org/repo auto-triage rule targeting EPSS/severity/scope → audit `resolution:auto-dismiss` & targeted PRs
- **B.** Disable Dependabot alerts completely → keep global Dependabot security updates enabled → create an `Open a pull request` rule for malware alerts → expect dismissed dev alerts never to reopen on runtime promotion
- **C.** Export an SPDX SBOM → delete package-lock.json so transitive packages disappear → enable `Dismiss package malware alerts` to block zero-days → skip reachability review
- **D.** Put auto-triage EPSS rules inside .github/secret_scanning.yml → expect repo rules to override enforced org rules → delete audit logs → manually email developers before rules evaluate

### 41. `dayahead-bidding-svc` has two `High`-severity Dependabot alerts: Package X has `EPSS 0.88` and `Reachable` (`2 call paths from BidController`), while Package Y has `EPSS 0.001` and `Unreachable`. How do `EPSS` and static `Reachability` work together?

- **A.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **B.** Prioritize `Dependabot alerts` combining `EPSS` (`30-day exploitation probability`), `CVSS` severity, `Reachability` call-path analysis (`Reachable` vs `Unreachable`), `runtime` scope, and `patch availability`
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 42. PelagicGrid Offshore's AppSec lead is reviewing Dependabot triage metrics with NERC-CIP auditors. Which two capabilities explain how alerts are prioritized and how auto-dismissed alerts are audited? Select two.

- **A.** Combine `EPSS` (`30-day exploitation probability`) and static `Reachability` call-path verdicts with `CVSS` severity and `runtime` dependency scope
- **B.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **E.** `resolution:auto-dismiss` (`alert filter matching findings automatically dismissed by preset or custom Dependabot auto-triage rules`)

### 43. On `vessel-ais-router`, why did enabling `Dependabot security updates` patch a vulnerable `golang.org/x/net` version to `v0.23.0` (`the minimum patched release`) rather than upgrading unrelated outdated packages in `go.mod`?

- **A.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **B.** `Dependabot security updates` (`alert-driven PRs patching vulnerable versions to the minimum fixed version`) vs `.github/dependabot.yml` `Dependabot version updates` (`scheduled ecosystem/Actions freshness PRs`)
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step

### 44. PelagicGrid Offshore wants Dependabot security pull requests on `rov-inspection-cv` opened **only** when a custom Dependabot auto-triage rule matches `CWE-502` deserialization flaws with `EPSS > 0.15`. Proposed solution: Keep repository-wide `Dependabot security updates` enabled in Settings alongside the custom `Open a pull request` rule. Does this limit PRs to that rule?

- **A.** No — temporary private forks created inside a Repository Security Advisory (`GHSA`) intentionally **disable GitHub Actions** (`and pushing fixes to a public branch before release leaks the zero-day`)
- **B.** No — Code Scanning rejects gzip-compressed SARIF files larger than `10 MB` (`and overwrites prior alerts when multiple matrix uploads share an identical SARIF category on one commit`)
- **C.** No — repository-wide `Dependabot security updates` must be **disabled** before a custom Dependabot auto-triage `Open a pull request` rule can selectively control which alerts open PRs
- **D.** Yes — this configuration satisfies every security, licensing, and governance requirement

### 45. What happens when a repository administrator on `offshore-opcua-bridge` disables an **organization-enforced** Dependabot auto-triage rule—or when a dependency previously auto-dismissed as `development` scope moves into `dependencies` (`runtime`) in `package.json`?

- **A.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** `Dependabot auto-triage rules` (`GitHub presets or custom rules on EPSS/CVE/CWE/scope/patch` setting `resolution:auto-dismiss` before notifications; disable global `Dependabot security updates` for custom PR-trigger rules)

### 46. PelagicGrid Offshore must prevent pull requests on private `grid-dispatch-java` from merging newly introduced `High`/`Critical` vulnerabilities or `GPL-3.0` / `AGPL-3.0` packages. What is the complete four-step configuration sequence?

- **A.** Add SPDX license names to `.github/dependabot.yml` → expect Dependabot version updates to block developer PR merges → skip required status checks → disable lockfiles
- **B.** Enable the Dependency Graph (`and Code Security on private repos`) → add an `on: pull_request` workflow running `actions/dependency-review-action@v4` → configure `fail-on-severity` & `deny-licenses` → mark the check required in a branch ruleset
- **C.** Trigger `dependency-review-action` only on weekly cron `schedule` → pass both `allow-licenses` and `deny-licenses` simultaneously → disable the Dependency Graph → leave main unprotected
- **D.** Run `dependency-review-action` on an unlicensed private Free repo → grant `write-all` permissions to untrusted fork code → ignore `fail-on-scopes` → merge failing checks freely

### 47. PelagicGrid Offshore wants `actions/dependency-review-action@v4` on `ballast-control-swift` to allow `Apache-2.0` and `MIT` while rejecting `LGPL-3.0`. Proposed solution: Configure both `allow-licenses: Apache-2.0, MIT` and `deny-licenses: LGPL-3.0` in the same `dependency-review-action@v4` step. Does this configuration succeed?

- **A.** No — `actions/dependency-review-action` forbids specifying `allow-licenses` and `deny-licenses` together, and fails to block merges unless marked as a required status check on `pull_request`
- **B.** No — CodeQL `Default Setup` and custom `Advanced Setup` (`.github/workflows/codeql.yml`) cannot run active CodeQL management simultaneously (`switch to Advanced Setup with build-mode: manual`)
- **C.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)
- **D.** Yes — this configuration satisfies every security, licensing, and governance requirement

### 48. PelagicGrid Offshore wants `dayahead-bidding-svc` pull requests gated strictly on runtime `High+` vulnerabilities and SPDX license compliance. Which two steps complete this pre-merge gate? Select two.

- **A.** Mark the `Dependency Review` workflow job as a **required status check** in a repository or organization Branch Ruleset targeting `main`
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **D.** `actions/dependency-review-action@v4` with `fail-on-severity: high`, `fail-on-scopes: runtime`, and `deny-licenses` (`or allow-licenses`, never both)
- **E.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 49. `forecast-wave-ml` pulls private Python wheels from an internal Cloudsmith PyPI registry and wants all `scipy`/`numpy`/`pandas` minor and patch updates combined into a single weekly PR. Which `.github/dependabot.yml` keys (`____`) achieve this?

- **A.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`
- **B.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **C.** `.github/codeql/codeql-config.yml` (`defining packs:, queries:, paths-ignore:, and threat-models: alongside YAML model-pack extensions`)
- **D.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)

### 50. On `grid-dispatch-java`, engineers froze `netty` major upgrades (`5.x`) due to IEC protocol compatibility while capping open version-update PRs at `8`. Which `.github/dependabot.yml` settings enforce both rules?

- **A.** Configure `.github/dependabot.yml` with `groups:` (`batching patch/minor updates into single PRs`), `ignore:` (`version/dependency exclusions`), `open-pull-requests-limit`, and `registries:` (`authenticated via Dependabot secrets`)
- **B.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **C.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 51. PelagicGrid Offshore pins third-party GitHub Actions by full 40-character commit SHA (`e.g., actions/checkout@11bd7190...`) for supply-chain hardening and wants Dependabot PRs updating those pinned SHAs when new tags ship. How does `.github/dependabot.yml` handle SHA-pinned Actions?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **C.** `Dependabot security updates` (`alert-driven PRs patching vulnerable versions to the minimum fixed version`) vs `.github/dependabot.yml` `Dependabot version updates` (`scheduled ecosystem/Actions freshness PRs`)
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 52. Why does GitHub provide a **read-only `GITHUB_TOKEN`** and block standard `Actions secrets` when a `pull_request` workflow runs on a branch created by `dependabot[bot]`?

- **A.** Govern Dependabot PR workflows (`read-only GITHUB_TOKEN` & `Dependabot secrets`), fine-grained alert roles, `dependabot_alert` webhooks, and production-context filters (`has:deployment`, `runtime-risk:internet-exposed`)
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 53. PelagicGrid Offshore feeds Azure AKS deployment records from Microsoft Defender for Cloud into GitHub Security Overview. Which search qualifiers (`____`) isolate alerts running in live internet-exposed energy-trading workloads?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`exporting the repository dependency inventory in SPDX JSON format`)
- **C.** `resolution:auto-dismiss` (`alert filter matching findings automatically dismissed by preset or custom Dependabot auto-triage rules`)
- **D.** `has:deployment runtime-risk:internet-exposed` (`Security Overview and alert search qualifiers powered by ingested deployment metadata`)

### 54. PelagicGrid Offshore's platform security team is reviewing Dependabot CI security boundaries and production telemetry integrations. Which two statements are accurate? Select two.

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **C.** Ingest deployment metadata (`from Microsoft Defender for Cloud, JFrog Artifactory, or CI/CD APIs`) to filter `has:deployment` and `runtime-risk:internet-exposed` alerts
- **D.** Workflows triggered by `dependabot` PRs receive a **read-only `GITHUB_TOKEN`** by default and access credentials stored in **`Dependabot secrets`** (`not standard Actions secrets on untrusted triggers`)
- **E.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

---

## Domain 4 — Configure and use Code Security (formerly Code Scanning with CodeQL) (10–15% official weight · 14 questions)

### 55. PelagicGrid Offshore runs `CodeQL` on `grid-dispatch-java` and `ballast-control-swift`, plus `Semgrep` and `tfsec` outputting `SARIF 2.1.0` for OT firewall Terraform templates. What architectural advantage does CodeQL's relational database have alongside third-party SARIF tools?

- **A.** `CodeQL` (`compiling/extracting code into a queryable relational AST/CFG/dataflow database`) paired with third-party SAST/IaC/container scanners uploading `SARIF 2.1.0` into unified Code Scanning alerts
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **D.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage

### 56. On `turbine-pitch-plc`, a firmware analyzer produces a `22 MB` gzip-compressed SARIF file containing `38,000` raw findings, and a second scanner uploads to the identical default `category`. Proposed solution: Upload both directly via `upload-sarif@v3` without filtering noisy rules or setting distinct categories. Will this succeed cleanly?

- **A.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **B.** No — Code Scanning rejects gzip-compressed SARIF files larger than `10 MB` (`and overwrites prior alerts when multiple matrix uploads share an identical SARIF category on one commit`)
- **C.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)
- **D.** No — repository-wide `Dependabot security updates` must be **disabled** before a custom Dependabot auto-triage `Open a pull request` rule can selectively control which alerts open PRs

### 57. PelagicGrid Offshore runs three SARIF scanners (`CodeQL`, `Trivy`, and an IEC-62443 C++ checker) across `substation-iec61850`. Which two SARIF ingestion rules keep alerts accurate across commits? Select two.

- **A.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **B.** Ensure each uploaded `SARIF 2.1.0` file is `<= 10 MB` gzip-compressed and `<= 25,000` results (`knowing GitHub displays only the top 5,000 results prioritized by severity`)
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** Assign a unique `category` per tool/language/monorepo target and preserve stable `ruleId` + `partialFingerprints` so alerts deduplicate cleanly without overwriting sibling scans
- **E.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts

### 58. `ballast-control-swift` compiles on dedicated macOS Xcode build servers managed by Buildkite outside GitHub Actions, and CodeQL results must publish to GitHub Code Scanning. What is the exact four-step `CodeQL CLI` lifecycle?

- **A.** Install the CodeQL CLI bundle on the CI agent → run `codeql database create` (`tracing compiled builds`) → run `codeql database analyze --format=sarif-latest` → run `codeql github upload-results` (`--sarif`, `--ref`, `--commit`)
- **B.** Enable Default Setup simultaneously for the same language/category → upload SARIF with a read-only `contents: read` token → strip `partialFingerprints` → expect >25,000 results to render without truncation
- **C.** Create one shared SARIF file without `--sarif-category` across 6 monorepo services → overwrite prior language alerts on every upload → disable GitHub Code Security on private repos → view alerts in Actions cache
- **D.** Run `codeql github upload-results` on raw `.java` source files → run `codeql database analyze` before `codeql database create` → upload an uncompressed 45 MB XML report → omit `--ref` and `--commit`

### 59. PelagicGrid Offshore has three repositories: `rov-inspection-cv` (`Python`), `grid-dispatch-java` (`pure Maven Java 21, zero Kotlin`), and `ballast-control-swift` (`Swift + C++` with custom `xcodebuild` schemes). Which CodeQL `build-mode` fits each repository?

- **A.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** CodeQL `build-mode` options: `none` (`JS/TS, Python, Ruby & buildless Java`), `autobuild` (`heuristic compiler detection`), and `manual` (`explicit custom build commands in CI for C/C++, C#, Go, Kotlin, Swift`)
- **D.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts

### 60. `turbine-pitch-plc` (`C++` with proprietary vendor RTOS headers) needs custom `cmake` pre-build script execution via `build-mode: manual` in `.github/workflows/codeql.yml`. Proposed solution: Keep CodeQL `Default Setup` enabled on `turbine-pitch-plc` and add `.github/workflows/codeql.yml` running `build-mode: manual` alongside it. Does this work?

- **A.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **B.** No — `actions/dependency-review-action` forbids specifying `allow-licenses` and `deny-licenses` together, and fails to block merges unless marked as a required status check on `pull_request`
- **C.** No — temporary private forks created inside a Repository Security Advisory (`GHSA`) intentionally **disable GitHub Actions** (`and pushing fixes to a public branch before release leaks the zero-day`)
- **D.** No — CodeQL `Default Setup` and custom `Advanced Setup` (`.github/workflows/codeql.yml`) cannot run active CodeQL management simultaneously (`switch to Advanced Setup with build-mode: manual`)

### 61. On `dayahead-bidding-svc`, CodeQL flags `Server-side request forgery (CWE-918)` tracing an untrusted `webhookUrl` query parameter (`source`) through `UrlBuilder.normalize()` (`step`) into `HttpClient.send()` (`sink`), accompanied by a `Copilot Autofix` allowlist patch. How does classic CodeQL `Copilot Autofix` work on PRs?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Inspect CodeQL `source -> step -> sink` path-problem dataflow traces and apply `Copilot Autofix` (`enabled by default on CodeQL PRs & default branch without requiring a Copilot seat for classic Autofix`)

### 62. On PelagicGrid Offshore's Buildkite macOS runner for `ballast-control-swift`, `codeql database analyze` wrote `swift-results.sarif`. Which exact `CodeQL CLI` command (`____`) uploads that SARIF report to GitHub Code Scanning?

- **A.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **B.** `POST /orgs/{org}/code-security/configurations/{configuration_id}/attach` (`attaching a Security Configuration across selected or all org repos via REST`)
- **C.** `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`exporting the repository dependency inventory in SPDX JSON format`)
- **D.** `codeql github upload-results --repository=<org/repo> --ref=<refs/heads/main> --commit=<sha> --sarif=<results.sarif>`

### 63. PelagicGrid Offshore is standardizing `.github/workflows/codeql.yml` permissions and `Copilot Autofix` review gates across 42 HVDC repositories. Which two rules belong in that workflow template? Select two.

- **A.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **B.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **C.** `permissions: { security-events: write, contents: read, actions: read }` on `github/codeql-action/upload-sarif@v3`
- **D.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **E.** Validate every `Copilot Autofix` suggestion by inspecting dataflow context, running full CI unit/integration tests + re-scanning with `CodeQL`, and completing human PR review

### 64. `substation-iec61850` builds both `armhf-gateway` and `x86_64-control-room` binaries from the same C++ tree in one matrix workflow. Which `codeql-action` input (`____`) prevents the second matrix leg from marking architecture-specific `#ifdef` alerts from the first leg as fixed?

- **A.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **B.** Distinguish `security-severity` (`Critical/High/Medium/Low` mapped from CVSS `0.0–10.0`) from rule `problem.severity` (`error/warning/note`), use `category` per matrix leg, and record audited dismissal reasons
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 65. Why did a CodeQL alert with `Rule severity: Error` **not** block a pull request on `vessel-ais-router` when the branch ruleset had `Security alerts: High or higher` and `All alerts: None`?

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** Distinguish `security-severity` (`Critical/High/Medium/Low` mapped from CVSS `0.0–10.0`) from rule `problem.severity` (`error/warning/note`), use `category` per matrix leg, and record audited dismissal reasons
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 66. In `.github/workflows/codeql.yml` on `turbine-pitch-plc`, `autobuild` picked up a tiny test Makefile instead of the main `cmake --preset offshore-rtos` firmware build, leaving 90% of C++ files unanalyzed. Which `init` configuration (`____`) fixes coverage?

- **A.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** `build-mode: manual` (`paired with explicit compiler commands prior to github/codeql-action/analyze@v3`)
- **D.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`

### 67. PelagicGrid Offshore uses a proprietary Java RPC bus (`com.pelagic.hvdc.RpcFrame.readUntrustedPayload()`) that CodeQL does not treat as an untrusted taint source out of the box. Where should AppSec register custom taint `sources`, `sinks`, and `summaries` without rewriting `.ql` queries (`____`)?

- **A.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **B.** `.github/codeql/codeql-config.yml` (`defining packs:, queries:, paths-ignore:, and threat-models: alongside YAML model-pack extensions`)
- **C.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **D.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`

### 68. CodeQL analysis on `grid-dispatch-java` times out at 360 minutes when scanning `Java`, `TypeScript`, and `C++` sequentially inside one job while also indexing `build/generated-sources/protobuf/`. What optimizations resolve this?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **D.** Customize `.github/codeql/codeql-config.yml` (`paths-ignore`, `packs`, `queries`, `threat-models`) & `CodeQL model packs` (`YAML data extensions`), and fix OOM/slow scans via Larger runners or split language matrices

---

## Domain 5 — Security operations: best practices, prioritization, and remediation (15–20% official weight · 18 questions)

### 69. PelagicGrid Offshore maintains `open-iec61850-go` publicly and wants external maritime researchers to submit zero-day packet-crash bugs confidentially into draft `GHSA` advisories. Which repository setting (`____`) enables this intake, and how do `CWE`, `CVE`, and `GHSA` interact?

- **A.** `CWE` classifies weakness types (`e.g., CWE-89 SQLi`), `CVE` identifies a publicly disclosed vulnerability instance, and `GHSA` (`Repository Security Advisories` + Private Reporting) coordinates private patches & CVEs
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions

### 70. Inside `open-iec61850-go`'s temporary private advisory fork (`open-iec61850-go-ghsa-39kq`), maintainers push commits fixing a stack-exhaustion bug (`CWE-674`). Proposed solution: Rely on GitHub Actions inside the temporary private advisory fork to run fuzzing suites automatically, or copy the exploit reproducer into a public PR on `open-iec61850-go` before release. Is this valid?

- **A.** No — repository-wide `Dependabot security updates` must be **disabled** before a custom Dependabot auto-triage `Open a pull request` rule can selectively control which alerts open PRs
- **B.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)
- **C.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **D.** No — temporary private forks created inside a Repository Security Advisory (`GHSA`) intentionally **disable GitHub Actions** (`and pushing fixes to a public branch before release leaks the zero-day`)

### 71. Why is specifying exact `Affected versions` (`>= 1.2.0, < 1.8.4`) and `Patched versions` (`1.8.4`) critical before PelagicGrid Offshore publishes its `open-iec61850-go` `GHSA`?

- **A.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** `CWE` classifies weakness types (`e.g., CWE-89 SQLi`), `CVE` identifies a publicly disclosed vulnerability instance, and `GHSA` (`Repository Security Advisories` + Private Reporting) coordinates private patches & CVEs
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 72. PelagicGrid Offshore has 1,100 open alerts across 70 repositories—half in decommissioned R&D prototypes and half in live North Sea substation gateways. How should AppSec prioritize remediation while preventing new severe debt?

- **A.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Prioritize using `has:deployment` + `runtime-risk:internet-exposed` (`Defender for Cloud / artifact registries`), `EPSS`, and `Reachability`, while blocking new regressions via `Require code scanning results` rulesets
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 73. On `grid-dispatch-java`, PelagicGrid Offshore's active ruleset sets `Require code scanning results` (`CodeQL: Security alerts High or higher`) AND `Trivy: Security alerts Critical`. When can a pull request merge?

- **A.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Enforce approved CodeQL scanning via Org/Enterprise `Rulesets` (`Require code scanning results` + Required Workflows) and automate governance via REST/GraphQL (`code-security/configurations`, org alert endpoints & billing APIs)

### 74. PelagicGrid Offshore wants zero surprise merge blocks when introducing cross-org severity rulesets across 70 SCADA repos while prioritizing live containerized workloads. Which two steps achieve this? Select two.

- **A.** Pilot cross-repository `Rulesets` in **`Evaluate` mode** to measure would-be blocked PRs via Ruleset Insights before switching enforcement to **`Active`**
- **B.** Ingest deployment metadata (`from Microsoft Defender for Cloud, JFrog Artifactory, or CI/CD APIs`) to filter `has:deployment` and `runtime-risk:internet-exposed` alerts
- **C.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **E.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 75. PelagicGrid Offshore's OT AppSec lead is launching a 4-week initiative to remediate 210 default-branch `CWE-78` OS command-injection and `CWE-918` SSRF findings across 14 maritime services. What is the end-to-end Security Campaign sequence?

- **A.** Filter high-risk default-branch alerts in Security Overview → create a Security Campaign (`<=1,000` alerts) with due date & contact → trigger Copilot Autofix (`or assign <=25 alerts to @copilot`) → verify CI checks & track burndown
- **B.** Export alerts to a static spreadsheet with no GitHub links → disable CodeQL so open counts fall to zero → bulk-dismiss every alert without comments → report 100% remediation
- **C.** Assign 500 alerts in one batch to `@copilot` without AI credits or branch protection → skip human PR review → disable Security Overview → expect secret campaigns to auto-rotate AWS IAM keys
- **D.** Create a campaign containing 50,000 unmerged fork-branch alerts with no contact owner → auto-merge Copilot suggestions bypassing CI tests → revoke developer write access → close the campaign with alerts still open

### 76. PelagicGrid Offshore's campaign manager selects alerts inside a Code Security Campaign to delegate to the `@copilot` cloud coding agent. What is the per-batch alert limit (`____`), what artifact does `@copilot` produce, and which credit pool is used?

- **A.** Run `Security Campaigns` (`<=1,000` default-branch alerts, named security lead, developer notifications, Copilot Autofix, or assigning `<=25` alerts per batch to `@copilot` cloud agent) with audited dismissal comments
- **B.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **C.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 77. During PelagicGrid Offshore's winter Security Campaign, an engineer dismisses 4 `CWE-918` alerts in `offshore-opcua-bridge` as `False positive` with a single-character comment `"ok"`. How should AppSec respond using GitHub's governance features?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** Dismissing an alert requires a structured closure reason (`False positive`, `Used in tests`, `Won't fix`) plus an audit-logged justification comment—and never deletes commits or revokes keys
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 78. PelagicGrid Offshore wants `substation-iec61850` (`critical HVDC infrastructure`) analyzed with broader medium-precision CodeQL security rules on top of `default` without noisy code-formatting or comment-style rules. Which query suite (`____`) should be configured?

- **A.** `has:deployment runtime-risk:internet-exposed` (`Security Overview and alert search qualifiers powered by ingested deployment metadata`)
- **B.** `queries: security-extended` (`executing default high-precision CodeQL security rules plus medium-precision security queries without style/quality rules`)
- **C.** `resolution:auto-dismiss` (`alert filter matching findings automatically dismissed by preset or custom Dependabot auto-triage rules`)
- **D.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage

### 79. After an external SCADA advisory reveals an unsafe Modbus CRC pointer-arithmetic bug, PelagicGrid Offshore writes a custom `.ql` query in VS Code and wants to scan all 70 org repositories simultaneously. Which capability (`____`) performs this?

- **A.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** Select CodeQL query suites (`default` high-precision, `security-extended` broader lower-confidence security, `security-and-quality` adds maintainability) and run `Multi-Repository Variant Analysis (MRVA)` in VS Code
- **D.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts

### 80. `turbine-pitch-plc` parses untrusted calibration files from local industrial SD cards (`FileInputStream` / `getenv`), which CodeQL's default `remote` threat model ignores. How should PelagicGrid Offshore expand CodeQL's threat model?

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** Customize `.github/codeql/codeql-config.yml` (`paths-ignore`, `packs`, `queries`, `threat-models`) & `CodeQL model packs` (`YAML data extensions`), and fix OOM/slow scans via Larger runners or split language matrices
- **D.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect

### 81. PelagicGrid Offshore wants one embedded-security champion inside each turbine squad to triage Code Scanning and Dependabot alerts on their squad's repositories without granting `Admin` rights to modify branch rulesets or delete repos. Which role model fits?

- **A.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **D.** Assign `Security Manager` org roles, custom repository alert roles, and per-alert `Assignees` (`noting secret-alert assignment temporarily elevates single-alert view access for repo writers until unassigned`)

### 82. When a Security Manager assigns a single leaked-credential alert (`inside a Secret scanning campaign`) on `vessel-ais-router` to a developer with standard `Write` access, does that developer gain visibility into all other Secret Protection alerts in `vessel-ais-router`?

- **A.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **B.** Assign `Security Manager` org roles, custom repository alert roles, and per-alert `Assignees` (`noting secret-alert assignment temporarily elevates single-alert view access for repo writers until unassigned`)
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 83. PelagicGrid Offshore is aligning OT Security Managers and maritime developers on exception approvals and alert triage. Which two governance rules apply? Select two.

- **A.** `Delegated bypass for push protection` (`granting Specific roles, visible teams, or custom roles with "Review and manage secret scanning bypass requests" authority—never secret teams`)
- **B.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **C.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **D.** Assign `Security Manager` org roles, custom repository alert roles, and per-alert `Assignees` (`noting secret-alert assignment temporarily elevates single-alert view access for repo writers until unassigned`)
- **E.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 84. PelagicGrid Offshore wants zero credentials in Git history, zero copyleft/vulnerable PR lockfile merges, and pre-merge taint fixes across `dayahead-bidding-svc`. Which three-control shift-left stack achieves this?

- **A.** Layer `Push Protection` (`pre-receive`), `actions/dependency-review-action` (`PR manifest/license gate`), and `CodeQL` PR checks (`with Copilot Autofix`) so secrets, vulnerable packages, and taint flaws fail pre-merge
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts

### 85. On a pull request to `rov-inspection-cv`, `actions/dependency-review-action@v4` fails because a transitive dependency carries an `Unknown` license not present in `allow-licenses: [MIT, Apache-2.0, BSD-3-Clause]`. What prerequisite must be active on this **private** repository for Dependency Review to run?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **C.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **D.** `actions/dependency-review-action@v4` on `pull_request` (`with fail-on-severity, mutually exclusive allow-licenses OR deny-licenses SPDX lists, fail-on-scopes, and allow-ghsas`) enforced as a required check

### 86. PelagicGrid Offshore's Engineering Security Baseline mandates three shift-left controls before code reaches `main` on any SCADA repository. Which three controls belong in that baseline? Select three.

- **A.** Validate every `Copilot Autofix` suggestion by inspecting dataflow context, running full CI unit/integration tests + re-scanning with `CodeQL`, and completing human PR review
- **B.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** `Push Protection` blocks high-confidence partner and published custom secrets pre-receive during `git push` before commits land on GitHub
- **E.** Configure `actions/dependency-review-action@v4` with `fail-on-severity`, `fail-on-scopes`, and either `allow-licenses` OR `deny-licenses` (`SPDX` IDs)
- **F.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses

---

## Domain 6 — GitHub Security suites administration (10–15% official weight · 14 questions)

### 87. PelagicGrid Offshore is standardizing Secret Protection, Dependabot, and CodeQL across 110 repositories grouped by `ot_zone` custom properties. What is the recommended four-step Security Configuration rollout sequence?

- **A.** Manually toggle Settings on 2,000 repositories one by one → grant every developer Organization Owner permissions → disable Push Protection globally → rely on `.gitignore` for enterprise governance
- **B.** Apply an `Enforced` configuration across 2,000 private repos with zero available committer seats → set every feature to `Not set` expecting strict locks → leave new repositories uncovered → disable audit logs
- **C.** Enable cloud-only Copilot Autofix on an air-gapped GHES instance with metered billing → skip GitHub Connect → expect transferred external repos to inherit new-repo defaults automatically without policy checks
- **D.** Verify committer license headroom (`or metered budget`) → create/select a Security Configuration → attach to tiered repos (`custom properties`) & enable `Apply to new repositories` → set `Enforced` to lock baseline controls

### 88. PelagicGrid Offshore hosts offshore substation control repos on an onshore `GitHub Enterprise Server (GHES)` instance and energy-trading microservices on `GitHub Enterprise Cloud (GHEC)`. How do licensing, AI features, and Advisory sync differ between `GHES` and `GHEC`?

- **A.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** Roll out org/enterprise `Security Configurations` (`GitHub-recommended` or custom, `Apply to new repositories`), contrasting `GHEC` (`metered or volume + cloud AI features`) with `GHES` (`volume-only + GitHub Connect Advisory sync`)
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 89. PelagicGrid Offshore transferred 6 private repositories from an acquired wind-turbine vendor org into `pelagicgrid-ot`, where `Apply to new repositories` is enabled on the `OT-Enforced` Security Configuration. Why did those 6 transferred repositories remain unattached?

- **A.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **B.** `Enforced` Security Configurations lock enabled/disabled settings (`except fields set to "Not set"`), while private/internal repos consume `90-day unique active committer` seats (`plus metered AI credits for AI Scan/generic secrets`)
- **C.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 90. PelagicGrid Offshore's Security Manager attaches an `Enforced` Security Configuration to `substation-iec61850` with `Push protection = Enabled` and `Dependabot alerts = Not set`, assuming repo admins cannot turn off Dependabot alerts. Proposed solution: Leave `Dependabot alerts` set to `"Not set"` inside the `Enforced` Security Configuration. Does this lock Dependabot alerts on?

- **A.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **B.** No — Code Scanning rejects gzip-compressed SARIF files larger than `10 MB` (`and overwrites prior alerts when multiple matrix uploads share an identical SARIF category on one commit`)
- **C.** No — repository-wide `Dependabot security updates` must be **disabled** before a custom Dependabot auto-triage `Open a pull request` rule can selectively control which alerts open PRs
- **D.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)

### 91. Across PelagicGrid Offshore's enterprise, 300 developers have `Read` access, 180 committed code to private GHAS-enabled repos 140 days ago (`none since`), 85 human engineers pushed commits within the last 90 days across 40 enabled repos, and `github-actions[bot]` pushed 200 release tags yesterday. How many active-committer seats are consumed (`____`)?

- **A.** `Enforced` Security Configurations lock enabled/disabled settings (`except fields set to "Not set"`), while private/internal repos consume `90-day unique active committer` seats (`plus metered AI credits for AI Scan/generic secrets`)
- **B.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **C.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 92. PelagicGrid Offshore's FinOps lead is configuring GHEC cost guardrails for `GitHub Secret Protection`, `GitHub Code Security`, and AI security credits. Which two billing and budget behaviors apply? Select two.

- **A.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **B.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **C.** Count `90-day unique active committers` across private/internal repos (`deduplicating each human user once across the enterprise, plus GitHub Connect sync between GHEC and GHES`)
- **D.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **E.** Monitor `Code Security AI credits` (`AI Scan / agentic autofix`) and `Secret Protection AI credits` (`AI push scanning`), setting **hard metered budgets** to cap spend

### 93. PelagicGrid Offshore's Enterprise Owner wants central governance so individual Repository Admins cannot enable metered `GitHub Code Security` on experimental repos, while allowing Organization Owners and `Security Managers` to attach Security Configurations freely. Which Enterprise policy accomplishes this without disrupting active repos?

- **A.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **B.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **C.** Enforce Enterprise Advanced Security policies (`restricting repo admins while preserving Org Owner/Security Manager control`), scope ruleset/push-protection bypass actors, and stream `security_configuration.*` / alert audit logs
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 94. For NERC-CIP compliance, PelagicGrid Offshore streams its Enterprise Audit Log to Azure Sentinel. Which security actions appear in that audit stream?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Enforce Enterprise Advanced Security policies (`restricting repo admins while preserving Org Owner/Security Manager control`), scope ruleset/push-protection bypass actors, and stream `security_configuration.*` / alert audit logs

### 95. If PelagicGrid Offshore switches an organization on subscription/volume licensing and hits `100%` seat utilization (`0 available seats`), what happens when `Apply to new repositories` tries to enable `GitHub Code Security` on a newly created private repository?

- **A.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **B.** `Enforced` Security Configurations lock enabled/disabled settings (`except fields set to "Not set"`), while private/internal repos consume `90-day unique active committer` seats (`plus metered AI credits for AI Scan/generic secrets`)
- **C.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 96. PelagicGrid Offshore's 6-member OT AppSec team (`@pelagicgrid/ot-appsec`) needs org-wide Security Overview access, Security Campaign ownership, and Security Configuration attachment rights across `pelagicgrid-ot`, with **zero** permission to push code or modify enterprise billing. Which built-in org role (`____`) fits?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Separate `Enterprise/Org Owners` (`billing & global policy`), `Security Managers` (`org-wide alert read/write & security config management, without code-write`), and custom repository roles (`granular view/dismiss per tool`)
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations

### 97. A maritime classification surveyor (`DNV`) requires temporary read-only access to inspect `Code Scanning` and `Dependabot` alerts on `ballast-control-swift` without viewing raw `Secret Protection` credentials, dismissing alerts, or pushing branches. Which role setup enforces this?

- **A.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **B.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **C.** Separate `Enterprise/Org Owners` (`billing & global policy`), `Security Managers` (`org-wide alert read/write & security config management, without code-write`), and custom repository roles (`granular view/dismiss per tool`)
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 98. PelagicGrid Offshore wants its 24/7 offshore NOC shift supervisors to review and approve/deny urgent Push Protection bypass requests across `pelagicgrid-ot` without granting them `Security Manager` power to change Security Configurations. Which custom organization role permission (`____`) grants just that capability?

- **A.** `permissions: { security-events: write, contents: read, actions: read }` on `github/codeql-action/upload-sarif@v3`
- **B.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **C.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **D.** `Review and manage secret scanning bypass requests` (`fine-grained organization role permission for Push Protection delegated bypass`)

### 99. PelagicGrid Offshore wants an organization-wide branch ruleset enforcing `Require code scanning results` (`High+` security severity) across all 70 SCADA repositories without causing unexpected PR deadlocks on day one. What is the four-step rollout sequence?

- **A.** Set an Org Ruleset to `Active` requiring `CodeQL` results before enabling CodeQL on any repo → grant `All repository writers` bypass access → set thresholds to `Note` style warnings → disable PR scans
- **B.** Configure branch protection individually in `.github/secret_scanning.yml` → allow Copilot Autofix comments to count as human PR approvals → skip `Evaluate` mode → delete Security Manager access
- **C.** Standardize CodeQL across target repos → create an Org Branch Ruleset in `Evaluate` mode with `Require code scanning results` (`High+` security severity) → audit Evaluate insights & scope bypass actors → switch enforcement to `Active`
- **D.** Disable `pull_request` triggers in `codeql.yml` so scans run only monthly on `main` → enforce `Require code scanning results` on feature PRs → expect instant green PR gates

### 100. PelagicGrid Offshore's platform automation attaches Security Configurations whenever a new microservice repo is provisioned and streams weekly org-wide alert counts into Grafana without polling 110 repos one by one. Which two API and workflow patterns enable this? Select two.

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **C.** `POST /orgs/{org}/code-security/configurations/{configuration_id}/attach` (`attaching a Security Configuration across selected or all org repos via REST`)
- **D.** Enforce approved CodeQL scanning via Org/Enterprise `Rulesets` (`Require code scanning results` + Required Workflows) and automate governance via REST/GraphQL (`code-security/configurations`, org alert endpoints & billing APIs)
- **E.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect

---

## Answer Key and Explanations

### Question 1 — `D` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: D (is correct). GitHub unbundles `GitHub Secret Protection` and `GitHub Code Security` as independent SKUs purchasable separately or together on both GitHub Team and GitHub Enterprise, billed per 90-day active committer. [Skill 1.1: Describe GitHub Security suite structure, navigation, and contrast Code Security, Secret Protection, and Supply Chain Security | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)]

- **A:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **B:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **C:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **D:** Correct. GitHub offers standalone Secret Protection and Code Security products on both GitHub Team and GitHub Enterprise, billed by unique 90-day active committers on private/internal repos

### Question 2 — `D` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: D (is correct). Secret Protection covers leaked credentials, Code Security (`CodeQL`/SARIF + Copilot Autofix) covers first-party source vulnerabilities, and Supply Chain Security covers open-source dependency and license exposure. [Skill 1.1: Describe GitHub Security suite structure, navigation, and contrast Code Security, Secret Protection, and Supply Chain Security | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Correct. each pillar targets a distinct risk surface: leaked credentials, first-party source vulnerabilities, and third-party open-source dependency/license exposure

### Question 3 — `B, D` (Describe GitHub Security suites, features, and ecosystem)

Correct answers: B and D (are correct). `GitHub Secret Protection` delivers Push Protection, secret scanning, validity checks, custom patterns, and AI generic detection, while `GitHub Code Security` delivers CodeQL/SARIF analysis, Copilot Autofix, private-repo Dependency Review, and Security Campaigns. [Skill 1.1: Describe GitHub Security suite structure, navigation, and contrast Code Security, Secret Protection, and Supply Chain Security | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Correct. Secret Protection focuses specifically on credential exposure in pushes and Git history
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Correct. Code Security covers first-party SAST, Copilot Autofix, and private-repository Dependency Review enforcement
- **E:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 4 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). Public GitHub.com repositories receive core secret scanning, Push Protection, Dependency Graph, Dependabot, CodeQL default setup, and Dependency Review free, whereas private/internal repositories require paid SKUs for advanced Secret Protection and Code Security coverage. [Skill 1.2: Differentiate security feature availability for public repositories vs. enterprise environments and explain Security Overview | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-overview/about-security-overview)]

- **A:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Correct. GitHub provides core security scanning free to open-source public repositories on GitHub.com while requiring Secret Protection / Code Security licenses for advanced private/internal repo coverage
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 5 — `A` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: A (is correct). Organization and Enterprise `Security Overview` surfaces `Risk`, `Coverage`, `Campaigns`, and tool-level dashboards filterable by custom properties such as `props.ot_zone:hvdc_ring`. [Skill 1.2: Differentiate security feature availability for public repositories vs. enterprise environments and explain Security Overview | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-overview/about-security-overview)]

- **A:** Correct. Security Overview aggregates posture, enablement gaps, alert trends, and campaign burndown across hundreds of repositories from a single org/enterprise plane
- **B:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **C:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **D:** Incorrect. codeql-config.yml centralizes custom query packs, path exclusions, threat models, and data-extension model packs for Advanced Setup

### Question 6 — `B` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: B (is correct). Triggering the free organization security risk assessment scans private org repositories for exposed secrets and previews CodeQL vulnerabilities with Copilot Autofix across up to 20 active repositories. [Skill 1.2: Differentiate security feature availability for public repositories vs. enterprise environments and explain Security Overview | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-overview/about-security-overview)]

- **A:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **B:** Correct. organizations on GitHub Team or Enterprise can run free secret and code risk assessments before purchasing full rollout licenses
- **C:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **D:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers

### Question 7 — `A` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: A (is correct). Secret Protection inspects text blobs and pushes for token formats, entropy, and AI generic secrets, whereas CodeQL compiles/extracts code into a relational AST/dataflow database to trace untrusted sources to dangerous execution sinks. [Skill 1.3: Explain differences and interplay between Secret Protection and Code Security across an end-to-end secure SDLC | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Correct. Secret Protection catches leaked tokens in any text/config file at push time, while CodeQL models how untrusted inputs or hardcoded values flow into sensitive code sinks
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 8 — `A` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: A (is correct). Combine pre-receive `Push Protection`, PR `actions/dependency-review-action@v4`, and PR `CodeQL` checks (`with Copilot Autofix`) enforced as required checks on protected branches. [Skill 1.3: Explain differences and interplay between Secret Protection and Code Security across an end-to-end secure SDLC | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Correct. combining all three shift-left controls prevents new security debt from ever landing on the default branch
- **B:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **C:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 9 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). Push Protection blocks secrets pre-receive before commits enter Git history, while CodeQL Default Setup with Copilot Autofix and an active ruleset detects and patches code flaws prior to merge. [Skill 1.3: Explain differences and interplay between Secret Protection and Code Security across an end-to-end secure SDLC | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Incorrect. enabling Advanced Setup disables Default Setup so custom workflow build steps, codeql-config.yml, or custom query suites govern scanning cleanly without duplicate conflicts
- **B:** Incorrect. allow-licenses and deny-licenses are mutually exclusive inputs in dependency-review-action, and branch rulesets must require the check to block merging
- **C:** Correct. every required GitHub Security suite setting, permission boundary, and enforcement rule is properly configured
- **D:** Incorrect. secret_scanning.yml suppresses user notifications in excluded folders rather than blocking pushes or cancelling public-repo partner revocations

### Question 10 — `B` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: B (is correct). Block secrets pre-receive via Push Protection, run Dependency Review and CodeQL on pull requests, apply Copilot Autofix or package upgrades before merge, and monitor default-branch advisories in Security Overview. [Skill 1.4: Compare prevention-first approaches vs. gate-based security strategies and explain security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/security-at-scale/about-security-campaigns)]

- **A:** Incorrect. Copilot Autofix requires an upstream CodeQL finding first, and Push Protection intercepts secrets during git push rather than post-merge
- **B:** Correct. a prevention-first secure SDLC stops secrets at git push, blocks vulnerable PR code/dependencies with pre-merge checks and Autofix, and continuously monitors post-merge advisories
- **C:** Incorrect. deferring secret and code checks until after merge exposes live credentials in Git history and turns security into high-cost reactive firefighting
- **D:** Incorrect. auto-dismissing unreviewed PR findings defeats shift-left prevention, and .gitignore never revokes already-exposed credentials

### Question 11 — `D` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: D (is correct). Pre-receive and PR-time prevention stops credentials from tainting Git history and resolves vulnerabilities while developers still hold active code context, avoiding late vessel-commissioning delays. [Skill 1.4: Compare prevention-first approaches vs. gate-based security strategies and explain security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/security-at-scale/about-security-campaigns)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Correct. shifting detection to git push and pull requests prevents secret sprawl and vulnerable merges before release cutoffs

### Question 12 — `D` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: D (is correct). `Security Campaigns` organize up to 1,000 default-branch alerts around a target date, named security contact, developer notifications, and Copilot Autofix remediation workflows. [Skill 1.4: Compare prevention-first approaches vs. gate-based security strategies and explain security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/security-at-scale/about-security-campaigns)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **C:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **D:** Correct. Security Campaigns turn overwhelming alert backlogs into manageable, developer-friendly remediation sprints with clear ownership

### Question 13 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). GitHub requires a structured dismissal reason (`False positive`, `Used in tests`, `Won't fix`), captures the justification comment, actor, and timestamp, and exposes the event across APIs, webhooks, and audit logs without altering Git commits. [Skill 1.5: Identify vulnerability and secret detection mechanisms, act on alerts, and govern ignoring or dismissing alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/vulnerability-exposure)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Correct. alert dismissals remain visible in REST/GraphQL APIs, webhooks, and audit logs, so teams must document rationale rather than hiding unverified risk
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 14 — `A` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: A (is correct). Dismissing the alert hides the UI banner while leaving the live Inmarsat credential active at the provider and readable inside Git commit history. [Skill 1.5: Identify vulnerability and secret detection mechanisms, act on alerts, and govern ignoring or dismissing alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/vulnerability-exposure)]

- **A:** Correct. alert dismissal only updates GitHub UI/API triage status; attackers can still extract unrotated keys from earlier commits, clones, or reflogs
- **B:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. Dismissing the alert hides the UI banner while leaving the live Inmarsat credential active at the provider and readable inside Git commit history.
- **C:** Incorrect. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories
- **D:** Incorrect. validate advisory patches locally or in an isolated private mirror without exposing exploit diffs publicly before publishing the coordinated GHSA release

### Question 15 — `A, E` (Describe GitHub Security suites, features, and ecosystem)

Correct answers: A and E (are correct). Enforce structured dismissal reasons paired with written justification comments, and continuously audit dismissal events through Security Overview, webhooks, REST APIs, and streamed enterprise audit logs. [Skill 1.5: Identify vulnerability and secret detection mechanisms, act on alerts, and govern ignoring or dismissing alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/vulnerability-exposure)]

- **A:** Correct. Security Overview and org audit logs surface anomalous dismissal spikes or unpatched high-risk repositories
- **B:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **E:** Correct. structured dismissal reasons and comments create an auditable compliance trail in webhooks and GraphQL/REST APIs

### Question 16 — `B` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: B (is correct). Enterprise/Org Admins govern licensing and Security Configurations, Security Managers oversee Security Overview, triage rules, and campaigns, and Developers remediate PR and campaign vulnerabilities in source code. [Skill 1.6: Describe developer, security, and admin responsibilities, alert access management, delegated bypass, and supply chain security concepts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)]

- **A:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **B:** Correct. effective DevSecOps distributes enablement, posture prioritization, and code-level patching cleanly across Admin, AppSec, and Developer roles
- **C:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 17 — `C` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: C (is correct). Secret alerts display actual credential values and commit paths, and delegated bypass prevents unilateral developer overrides by routing push exceptions to designated reviewers. [Skill 1.6: Describe developer, security, and admin responsibilities, alert access management, delegated bypass, and supply chain security concepts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **C:** Correct. restricting sensitive secret/vulnerability details and routing bypass requests through designated security reviewers preserves accountability without halting urgent releases
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 18 — `A, C, D` (Describe GitHub Security suites, features, and ecosystem)

Correct answers: A, C, and D (are correct). Separate Admin/Security Manager/Developer responsibilities, enforce least-privilege secret access with Push Protection delegated bypass, and gate PR manifest/license diffs using `actions/dependency-review-action@v4`. [Skill 1.6: Describe developer, security, and admin responsibilities, alert access management, delegated bypass, and supply chain security concepts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)]

- **A:** Correct. restricting sensitive secret/vulnerability details and routing bypass requests through designated security reviewers preserves accountability without halting urgent releases
- **B:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **C:** Correct. effective DevSecOps distributes enablement, posture prioritization, and code-level patching cleanly across Admin, AppSec, and Developer roles
- **D:** Correct. Dependency Review inspects PR manifest/lockfile diffs before merge and fails the check when newly introduced packages breach vulnerability or license policies
- **E:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **F:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges

### Question 19 — `B` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: B (is correct). Attaching an Organization Security Configuration with `Apply to new repositories` enabled turns on Secret Protection controls across current and newly created repositories automatically. [Skill 2.1: Enable and configure GitHub Secret Protection at repository and organization levels and contrast public vs. private/enterprise behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)]

- **A:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **B:** Correct. Security Configurations scale Secret Protection across existing and newly created repositories consistently, while single-repo toggles suit isolated pilots
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 20 — `B` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: B (is correct). On the public repo, partner scanning runs free and automatically forwards the exposed token to Cloudflare for partner handling/revocation; on the private repo, GitHub alerts authorized internal org/repo users (`plus optional validity checks`) without public partner revocation notices. [Skill 2.1: Enable and configure GitHub Secret Protection at repository and organization levels and contrast public vs. private/enterprise behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)]

- **A:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **B:** Correct. partner notification automatically reports exposed public-repo tokens to the issuing cloud/SaaS vendor, whereas private-repo findings stay internal unless validity checks query the provider
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 21 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). All 70 already-enabled repositories continue running Secret Protection uninterrupted, `Org Owners` and `Security Managers` keep full Security Configuration control, and individual Repository Admins can no longer toggle licensing. [Skill 2.1: Enable and configure GitHub Secret Protection at repository and organization levels and contrast public vs. private/enterprise behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)]

- **A:** Correct. enterprise policies prevent uncontrolled repo-admin license consumption while audit log streaming preserves tamper-evident compliance records across configuration and bypass events
- **B:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges

### Question 22 — `D` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: D (is correct). `Push Protection` inspects commits pre-receive across Git CLI, IDEs, web edits, and the GitHub Contents REST API before any secret blob is written to repository history. [Skill 2.2: Prevent secret exposure using Push Protection, validity checks, and prioritized high-confidence or generic secret detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Correct. blocking leaked credentials before the remote ref updates avoids costly key rotation, incident response, and Git history rewrites

### Question 23 — `B` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: B (is correct). `Active` confirms AWS verified those credentials are live right now, whereas non-provider generic PostgreSQL connection strings have no external SaaS partner API for validity checks (`so they must be verified directly against internal databases`). [Skill 2.2: Prevent secret exposure using Push Protection, validity checks, and prioritized high-confidence or generic secret detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Correct. knowing a leaked AWS, Stripe, or Slack token is still Active lets incident responders triage live compromises ahead of already-revoked tokens
- **C:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 24 — `A, D` (Configure and use Secret Protection (formerly secret scanning))

Correct answers: A and D (are correct). Enable `Push Protection` to block high-confidence secrets pre-receive, and enable `non-provider patterns` plus `Copilot AI generic secret detection` (`consuming Secret Protection AI credits` on push) for unstructured passwords. [Skill 2.2: Prevent secret exposure using Push Protection, validity checks, and prioritized high-confidence or generic secret detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection)]

- **A:** Correct. enabling non-provider and AI generic secret detection catches unstructured passwords and connection strings missed by vendor-prefix regexes (noting non-provider patterns lack partner validity checks)
- **B:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **C:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **D:** Correct. stopping secrets pre-receive prevents Git history contamination and emergency credential rotation
- **E:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 25 — `C` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: C (is correct). Confirm alert validity and blast radius, immediately revoke and rotate the Grafana token at the provider, purge Git history (`git filter-repo` and GitHub Support PR cache purge if needed), and resolve the alert as `Revoked`. [Skill 2.3: Manage the Secret Protection alert lifecycle, apply secret remediation actions, and govern alert dismissals | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts)]

- **A:** Incorrect. delaying credential revocation leaves attackers able to exploit copies harvested from webhooks, clones, or cached diffs while history is rewritten
- **B:** Incorrect. using secret_scanning.yml to silence an active production credential leak hides the alert without revoking or rotating the compromised secret
- **C:** Correct. once a secret reaches Git history, revoking/rotating the live key comes first, followed by history rewrite/cache purge and marking the alert Revoked for auditability
- **D:** Incorrect. deleting a secret in a follow-up commit leaves the active credential exposed in prior Git commits, reflogs, and clones without revoking access

### Question 26 — `B` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: B (is correct). Automated CI clones, webhook consumers, developer workstations, and cached GitHub object/PR views may have already captured the credential the instant the remote push landed, making provider rotation mandatory. [Skill 2.3: Manage the Secret Protection alert lifecycle, apply secret remediation actions, and govern alert dismissals | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Correct. merely deleting a secret in a later commit leaves it readable in earlier commits; immediate revocation and rotation is mandatory
- **C:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 27 — `D` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: D (is correct). Resolve the alert as `Used in tests` (`or False positive`) with an explanatory audit comment—and optionally exclude dedicated synthetic test folders in `.github/secret_scanning.yml`. [Skill 2.3: Manage the Secret Protection alert lifecycle, apply secret remediation actions, and govern alert dismissals | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **D:** Correct. alert dismissals remain visible in REST/GraphQL APIs, webhooks, and audit logs, so teams must document rationale rather than hiding unverified risk

### Question 28 — `C` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: C (is correct). Enabling `Delegated bypass for push protection` restricts bypass approvals to designated visible teams, roles, or custom roles while recording every request and reviewer decision. [Skill 2.4: Configure role-based and delegated bypass policies in Secret Protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **C:** Correct. delegated bypass replaces ad-hoc writer self-bypasses with a structured request-and-approval workflow audited via webhooks and logs
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 29 — `B` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: B (is correct). No—GitHub explicitly prohibits adding **secret teams** (`visible only to members`) to Push Protection delegated bypass lists, and `.github/secret_scanning.yml` only configures `paths-ignore` path exclusions. [Skill 2.4: Configure role-based and delegated bypass policies in Secret Protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection)]

- **A:** Incorrect. enabling Advanced Setup disables Default Setup so custom workflow build steps, codeql-config.yml, or custom query suites govern scanning cleanly without duplicate conflicts
- **B:** Correct. secret_scanning.yml suppresses user notifications in excluded folders rather than blocking pushes or cancelling public-repo partner revocations
- **C:** Incorrect. each gzipped SARIF upload must be <=10 MB with a distinct category per language/tool/component and security-events: write permission
- **D:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. No—GitHub explicitly prohibits adding **secret teams** (`visible only to members`) to Push Protection delegated bypass lists, and `.github/secret_scanning.yml` only configures `paths-ignore` path exclusions.

### Question 30 — `B, D` (Configure and use Secret Protection (formerly secret scanning))

Correct answers: B and D (are correct). Assign a **visible** organization team or custom role (`never a secret team`) to the delegated bypass list, and grant the custom organization role `Review and manage secret scanning bypass requests`. [Skill 2.4: Configure role-based and delegated bypass policies in Secret Protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection)]

- **A:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **B:** Correct. delegated bypass centralizes exception approvals in visible accountable security teams or roles
- **C:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **D:** Correct. granting Review and manage secret scanning bypass requests creates least-privilege Push Protection approvers without full Org Owner access
- **E:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 31 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). `.github/secret_scanning.yml` with `paths-ignore:` supports up to `1,000` glob entries and a maximum `1 MB` file size (`and target files > 1 MB still get scanned`). [Skill 2.5: Configure Secret Protection alert recipients and path exclusions (.github/secret_scanning.yml) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning)]

- **A:** Correct. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **B:** Incorrect. codeql-config.yml centralizes custom query packs, path exclusions, threat models, and data-extension model packs for Advanced Setup
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets

### Question 32 — `C` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: C (is correct). On public repositories, `paths-ignore` in `.github/secret_scanning.yml` suppresses user-facing repository alerts (`where enabled`) but **never** disables partner pattern scanning or automatic partner revocation notifications. [Skill 2.5: Configure Secret Protection alert recipients and path exclusions (.github/secret_scanning.yml) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Correct. secret_scanning.yml silences noisy user alerts in synthetic fixture directories up to 1,000 paths / 1 MB while keeping real code paths protected
- **D:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement

### Question 33 — `C` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: C (is correct). Create a custom repository role inheriting `Maintain` and add `View secret scanning alerts` and `Dismiss or resolve secret scanning alerts` on `ballast-control-swift`. [Skill 2.5: Configure Secret Protection alert recipients and path exclusions (.github/secret_scanning.yml) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning)]

- **A:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **B:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **C:** Correct. Security Manager and fine-grained custom repository roles grant AppSec and security champions exact triage permissions without over-provisioning Repository Admin or code-push rights
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 34 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). GitHub requires running `Save and dry run` (`inspecting up to 1,000 historical matches without creating live alerts`) and clicking `Publish pattern` before `Push Protection` can be enabled on a custom pattern. [Skill 2.6: Create, dry-run, and manage custom secret patterns (including Copilot regex generation and Push Protection) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning)]

- **A:** Correct. dry runs preview up to 1,000 historical matches without creating live alerts, and editing a published pattern automatically closes alerts generated by its previous version
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 35 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). Enterprise-level custom patterns can only be edited or removed by the specific user who created them (`unlike org/repo patterns editable by any org owner/security manager/repo admin`), and saving edits closes alerts created by the prior pattern version. [Skill 2.6: Create, dry-run, and manage custom secret patterns (including Copilot regex generation and Push Protection) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning)]

- **A:** Correct. dry runs preview up to 1,000 historical matches without creating live alerts, and editing a published pattern automatically closes alerts generated by its previous version
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 36 — `A, B, F` (Configure and use Secret Protection (formerly secret scanning))

Correct answers: A, B, and F (are correct). Custom patterns (`100/repo`, `500/org-or-ent`) validate via dry runs before publishing, Push Protection blocks supported partner and published custom patterns pre-receive, and partner validity checks identify `Active` live tokens for immediate rotation. [Skill 2.6: Create, dry-run, and manage custom secret patterns (including Copilot regex generation and Push Protection) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning)]

- **A:** Correct. Active validation status gives AppSec teams high-signal prioritization during incident triage
- **B:** Correct. dry runs preview up to 1,000 historical matches without creating live alerts, and editing a published pattern automatically closes alerts generated by its previous version
- **C:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **D:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **E:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **F:** Correct. stopping secrets pre-receive prevents Git history contamination and emergency credential rotation

### Question 37 — `D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: D (is correct). Use CI `Dependency Submission API` actions (`alongside committed gradle.lockfile / manifest lockfiles`) to upload build-time resolved dependency snapshots to `POST /repos/{owner}/{repo}/dependency-graph/snapshots`. [Skill 3.1: Generate and interpret the dependency graph, vulnerability databases, Dependency Submission API, and SPDX SBOM exports | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository)]

- **A:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Correct. committing lockfiles plus submitting build-resolved snapshots gives GitHub complete direct and transitive dependency visibility

### Question 38 — `A` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: A (is correct). Calling `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`or generating signed attestations with actions/attest-sbom`) exports the repository's direct and transitive dependency graph in SPDX JSON format. [Skill 3.1: Generate and interpret the dependency graph, vulnerability databases, Dependency Submission API, and SPDX SBOM exports | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository)]

- **A:** Correct. the Dependency Graph SBOM REST endpoint returns upstream direct and transitive packages in machine-readable SPDX JSON
- **B:** Incorrect. codeql github upload-results publishes externally generated SARIF 2.1.0 files to GitHub Code Scanning with exact ref and commit metadata
- **C:** Incorrect. the code-security configurations attach endpoint programmatically binds a Security Configuration to targeted or organization-wide repositories
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 39 — `C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: C (is correct). No—an exported `SPDX` SBOM inventories only the upstream direct and transitive dependencies consumed *by* `pelagic-modbus-lib`, never downstream `dependents`. [Skill 3.1: Generate and interpret the dependency graph, vulnerability databases, Dependency Submission API, and SPDX SBOM exports | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository)]

- **A:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Correct. GitHub exports dependency inventories, versions, licenses, and transitive relationships in standard SPDX JSON (and never includes downstream external dependents)
- **D:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure

### Question 40 — `A` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: A (is correct). Enable Dependency Graph and Dependabot alerts, disable global `Dependabot security updates` where custom PR rules govern, create an org/repo auto-triage rule targeting EPSS/severity/scope, and audit `resolution:auto-dismiss` plus targeted PRs. [Skill 3.2: Prioritize supply chain alerts (EPSS, CVSS, reachability) and configure Dependabot auto-triage (auto-dismiss) rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules)]

- **A:** Correct. custom Dependabot auto-triage rules run before notifications, and repository-wide Dependabot security updates must be off when using custom rules to selectively open security PRs
- **B:** Incorrect. auto-triage rules require Dependabot alerts enabled, global security updates override selective PR rules, malware alerts do not open PRs, and scope changes auto-reopen alerts
- **C:** Incorrect. deleting lockfiles blinds transitive vulnerability detection, and the Dismiss package malware alerts preset suppresses false-positive internal namespace collisions rather than blocking malware
- **D:** Incorrect. Dependabot auto-triage rules live in Dependabot settings (where org rules override conflicting repo rules and evaluate before notifications), not secret_scanning.yml

### Question 41 — `B` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: B (is correct). `EPSS` predicts 30-day exploitation probability in the wild while static `Reachability` (`showing up to 5 call paths`) confirms `BidController` invokes the vulnerable symbol—making Package X the urgent production fix. [Skill 3.2: Prioritize supply chain alerts (EPSS, CVSS, reachability) and configure Dependabot auto-triage (auto-dismiss) rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules)]

- **A:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **B:** Correct. combining EPSS exploit likelihood and static reachability with CVSS and runtime scope focuses engineering effort on genuinely exploitable dependencies
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 42 — `A, E` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answers: A and E (are correct). Rank alerts using `EPSS`, `Reachability`, CVSS, and `runtime` scope, and query `resolution:auto-dismiss` to audit findings suppressed by preset or custom Dependabot auto-triage rules. [Skill 3.2: Prioritize supply chain alerts (EPSS, CVSS, reachability) and configure Dependabot auto-triage (auto-dismiss) rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules)]

- **A:** Correct. high-EPSS reachable runtime vulnerabilities represent immediate real-world exploit risk compared with unreachable dev-only packages
- **B:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **E:** Correct. querying is:closed resolution:auto-dismiss audits every Dependabot alert suppressed by preset or custom auto-triage rules

### Question 43 — `B` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: B (is correct). `Dependabot security updates` react specifically to vulnerable default-branch dependencies in the GitHub Advisory Database (`patching to the minimum safe version`), whereas general freshness upgrades require `.github/dependabot.yml` `version updates`. [Skill 3.3: Remediate supply chain alerts through Dependabot security updates, version updates, and security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **B:** Correct. security updates react to GitHub Advisory Database alerts on default-branch dependencies, whereas dependabot.yml keeps dependencies and github-actions current on a schedule
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure

### Question 44 — `C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: C (is correct). No—repository-wide `Dependabot security updates` must be **disabled** first, otherwise Dependabot continues opening PRs for all patchable repository alerts regardless of selective custom PR rules. [Skill 3.3: Remediate supply chain alerts through Dependabot security updates, version updates, and security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. validate advisory patches locally or in an isolated private mirror without exposing exploit diffs publicly before publishing the coordinated GHSA release
- **B:** Incorrect. each gzipped SARIF upload must be <=10 MB with a distinct category per language/tool/component and security-events: write permission
- **C:** Correct. when global Dependabot security updates remain enabled, Dependabot attempts PRs for every patchable alert, overriding selective custom PR auto-triage rules
- **D:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. No—repository-wide `Dependabot security updates` must be **disabled** first, otherwise Dependabot continues opening PRs for all patchable repository alerts regardless of selective custom PR rules.

### Question 45 — `D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: D (is correct). Organization-enforced Dependabot auto-triage rules override conflicting repository settings, and any auto-dismissed alert automatically **reopens** whenever scope or advisory metadata changes so it no longer satisfies the dismissal rule. [Skill 3.3: Remediate supply chain alerts through Dependabot security updates, version updates, and security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Correct. auto-triage rules suppress low-risk noise before notifications fire, auto-reopen if metadata/scope changes, and defer to organization rules when repo rules conflict

### Question 46 — `B` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: B (is correct). Enable the Dependency Graph (`and Code Security on private repos`), add an `on: pull_request` workflow running `actions/dependency-review-action@v4`, configure `fail-on-severity` and `deny-licenses`, and enforce the check in an active branch ruleset. [Skill 3.4: Secure dependencies during development using pre-merge Dependency Review (dependency-review-action) for vulnerabilities and licenses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action)]

- **A:** Incorrect. dependabot.yml schedules dependency update PRs rather than gating developer PRs on license compliance; pre-merge gating requires dependency-review-action plus required checks
- **B:** Correct. Dependency Review compares PR base-vs-head manifests/lockfiles via the Dependency Graph and blocks vulnerable or non-compliant licenses when required on protected branches
- **C:** Incorrect. dependency-review-action requires pull_request base/head diffs and an active Dependency Graph, and allow-licenses / deny-licenses are mutually exclusive
- **D:** Incorrect. private repositories require GitHub Code Security / GHAS for Dependency Review, contents: read suffices, and unenforced checks do not block merges

### Question 47 — `A` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: A (is correct). No—`allow-licenses` and `deny-licenses` are mutually exclusive in `dependency-review-action@v4`; specifying `allow-licenses: Apache-2.0, MIT` alone already blocks `LGPL-3.0` and every other unlisted license. [Skill 3.4: Secure dependencies during development using pre-merge Dependency Review (dependency-review-action) for vulnerabilities and licenses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action)]

- **A:** Correct. allow-licenses and deny-licenses are mutually exclusive inputs in dependency-review-action, and branch rulesets must require the check to block merging
- **B:** Incorrect. enabling Advanced Setup disables Default Setup so custom workflow build steps, codeql-config.yml, or custom query suites govern scanning cleanly without duplicate conflicts
- **C:** Incorrect. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories
- **D:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. No—`allow-licenses` and `deny-licenses` are mutually exclusive in `dependency-review-action@v4`; specifying `allow-licenses: Apache-2.0, MIT` alone already blocks `LGPL-3.0` and every other unlisted license.

### Question 48 — `A, D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answers: A and D (are correct). Configure `actions/dependency-review-action@v4` with `fail-on-severity: high`, `fail-on-scopes: runtime`, and `deny-licenses` (`or allow-licenses`), and require that status check inside an enforced branch ruleset. [Skill 3.4: Secure dependencies during development using pre-merge Dependency Review (dependency-review-action) for vulnerabilities and licenses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action)]

- **A:** Correct. without a required status check rule, a failing Dependency Review workflow warns on the PR without blocking merge
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **D:** Correct. dependency-review-action@v4 gates pull requests on severity, dependency scope, and SPDX license policy using a single allow OR deny list
- **E:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 49 — `A` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: A (is correct). Define a `registries:` entry (`type: python-index` referencing `${{ secrets.CLOUDSMITH_TOKEN }}` in **Dependabot secrets**) and a `groups:` entry with `patterns` and `update-types: [minor, patch]`. [Skill 3.5: Configure advanced dependency update rules in dependabot.yml (grouping, ignore rules, update strategies, private registries) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference)]

- **A:** Correct. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets
- **B:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **C:** Incorrect. codeql-config.yml centralizes custom query packs, path exclusions, threat models, and data-extension model packs for Advanced Setup
- **D:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories

### Question 50 — `A` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: A (is correct). Configure `ignore:` (`dependency-name: "io.netty:*"`, `update-types: ["version-update:semver-major"]`) and `open-pull-requests-limit: 8`. [Skill 3.5: Configure advanced dependency update rules in dependabot.yml (grouping, ignore rules, update strategies, private registries) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference)]

- **A:** Correct. grouping related updates cuts CI/PR noise dramatically, while registries + Dependabot secrets authenticate Dependabot to private npm/NuGet/PyPI/Maven feeds
- **B:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **C:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 51 — `C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: C (is correct). Adding `package-ecosystem: "github-actions"` (`directory: "/"`) in `.github/dependabot.yml` automatically opens PRs updating both full commit SHAs and version comments whenever upstream Actions release updates. [Skill 3.5: Configure advanced dependency update rules in dependabot.yml (grouping, ignore rules, update strategies, private registries) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **C:** Correct. security updates react to GitHub Advisory Database alerts on default-branch dependencies, whereas dependabot.yml keeps dependencies and github-actions current on a schedule
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 52 — `A` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: A (is correct). If a compromised upstream dependency altered test hooks or build scripts inside a Dependabot PR, read-only `GITHUB_TOKEN` defaults and isolated `Dependabot secrets` prevent exfiltrating production deployment secrets or mutating repository contents. [Skill 3.6: Configure supply chain alert permissions, Dependabot workflows/runners, webhooks, and external production-context integrations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/automating-dependabot-with-github-actions)]

- **A:** Correct. understanding Dependabot token/secret isolation, webhook automation, and Defender for Cloud / artifact-registry deployment context integrates supply-chain security safely into operations
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 53 — `D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: D (is correct). Filtering by `has:deployment runtime-risk:internet-exposed` narrows alerts to artifacts actively running in internet-exposed production clusters. [Skill 3.6: Configure supply chain alert permissions, Dependabot workflows/runners, webhooks, and external production-context integrations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/automating-dependabot-with-github-actions)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Incorrect. the Dependency Graph SBOM REST endpoint returns upstream direct and transitive packages in machine-readable SPDX JSON
- **C:** Incorrect. querying is:closed resolution:auto-dismiss audits every Dependabot alert suppressed by preset or custom auto-triage rules
- **D:** Correct. filtering by has:deployment and runtime-risk:internet-exposed isolates alerts affecting live internet-reachable workloads

### Question 54 — `C, D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answers: C and D (are correct). Dependabot PR workflows receive a read-only `GITHUB_TOKEN` and read from `Dependabot secrets`, while Defender for Cloud / JFrog integrations enable `has:deployment` and `runtime-risk:internet-exposed` filtering. [Skill 3.6: Configure supply chain alert permissions, Dependabot workflows/runners, webhooks, and external production-context integrations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/automating-dependabot-with-github-actions)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **C:** Correct. production context pinpoints vulnerabilities actually running in internet-facing workloads rather than dead or archived repos
- **D:** Correct. isolating Dependabot secrets and read-only default tokens protects repository secrets if a compromised upstream package alters build scripts
- **E:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 55 — `A` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: A (is correct). CodeQL models complete AST, control-flow, and interprocedural dataflow graphs across files/packages, while `SARIF 2.1.0` ingestion unifies specialized IaC/protocol linters under identical PR annotations, rulesets, and Security Overview dashboards. [Skill 4.1: Compare CodeQL and third-party analysis tools and manage SARIF 2.1.0 ingestion, fingerprints, and limits | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning)]

- **A:** Correct. CodeQL excels at deep interprocedural taint tracking across supported languages while SARIF 2.1.0 lets specialized IaC/container/linter tools report into one PR interface
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **D:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)

### Question 56 — `B` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: B (is correct). No—Code Scanning rejects any SARIF file exceeding `10 MB` gzip-compressed (`or > 25,000 results per run, displaying at most top 5,000`) and overwrites sibling results when uploads share one `category` on the same commit. [Skill 4.1: Compare CodeQL and third-party analysis tools and manage SARIF 2.1.0 ingestion, fingerprints, and limits | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning)]

- **A:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. No—Code Scanning rejects any SARIF file exceeding `10 MB` gzip-compressed (`or > 25,000 results per run, displaying at most top 5,000`) and overwrites sibling results when uploads share one `category` on the same commit.
- **B:** Correct. each gzipped SARIF upload must be <=10 MB with a distinct category per language/tool/component and security-events: write permission
- **C:** Incorrect. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories
- **D:** Incorrect. when global Dependabot security updates remain enabled, Dependabot attempts PRs for every patchable alert, overriding selective custom PR auto-triage rules

### Question 57 — `B, D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answers: B and D (are correct). Keep each gzip-compressed SARIF file `<= 10 MB` (`<= 25,000` results, top `5,000` displayed by severity) and assign a distinct `category` per tool/target while preserving `ruleId` + `partialFingerprints`. [Skill 4.1: Compare CodeQL and third-party analysis tools and manage SARIF 2.1.0 ingestion, fingerprints, and limits | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning)]

- **A:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **B:** Correct. exceeding 10 MB gzipped rejects the upload outright, while noisy rule sets over 5,000 findings truncate lower-priority alerts
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Correct. distinct categories prevent multi-job uploads on the same commit from clobbering one another, while fingerprints track alerts across line shifts
- **E:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`

### Question 58 — `A` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: A (is correct). Install the CodeQL CLI bundle on the macOS build agent, run `codeql database create` (`tracing xcodebuild`), run `codeql database analyze --format=sarif-latest`, and upload via `codeql github upload-results` (`--sarif`, `--ref`, `--commit`). [Skill 4.2: Set up and configure Code Security via Default Setup, Advanced Setup workflows, matrix build-modes, and external CI (CodeQL CLI) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages)]

- **A:** Correct. external CI integrations create the semantic CodeQL database, execute query suites into SARIF 2.1.0 (`<=10 MB` gzipped), and upload results with `security_events` write auth
- **B:** Incorrect. Default Setup conflicts with custom/external CodeQL uploads, uploading SARIF requires security-events: write, and runs cap at 25,000 results (displaying top 5,000)
- **C:** Incorrect. omitting distinct SARIF categories causes subsequent uploads for the same commit to overwrite/mark prior component results stale, and private repos require Code Security
- **D:** Incorrect. CodeQL cannot upload raw source files or XML; a database must be created before analysis, and SARIF 2.1.0 uploads must be <=10 MB gzipped with target ref and commit SHA

### Question 59 — `C` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: C (is correct). `rov-inspection-cv` (`Python`) and pure-Java `grid-dispatch-java` can use `build-mode: none` (`or autobuild`), whereas `ballast-control-swift` (`Swift` and `C++`) **cannot** use `build-mode: none` and requires `build-mode: manual` (`or autobuild`). [Skill 4.2: Set up and configure Code Security via Default Setup, Advanced Setup workflows, matrix build-modes, and external CI (CodeQL CLI) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages)]

- **A:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Correct. selecting build-mode: manual when custom flags/codegen break autobuild—or build-mode: none where supported—eliminates build-wrapper failures cleanly
- **D:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`

### Question 60 — `D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: D (is correct). No—CodeQL `Default Setup` and custom `Advanced Setup` (`codeql.yml`) are mutually exclusive for active CodeQL management; switching to `Advanced Setup` disables Default Setup so custom `build-mode: manual` steps run without conflict. [Skill 4.2: Set up and configure Code Security via Default Setup, Advanced Setup workflows, matrix build-modes, and external CI (CodeQL CLI) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages)]

- **A:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. No—CodeQL `Default Setup` and custom `Advanced Setup` (`codeql.yml`) are mutually exclusive for active CodeQL management; switching to `Advanced Setup` disables Default Setup so custom `build-mode: manual` steps run without conflict.
- **B:** Incorrect. allow-licenses and deny-licenses are mutually exclusive inputs in dependency-review-action, and branch rulesets must require the check to block merging
- **C:** Incorrect. validate advisory patches locally or in an isolated private mirror without exposing exploit diffs publicly before publishing the coordinated GHSA release
- **D:** Correct. enabling Advanced Setup disables Default Setup so custom workflow build steps, codeql-config.yml, or custom query suites govern scanning cleanly without duplicate conflicts

### Question 61 — `D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: D (is correct). CodeQL exposes every `source -> step -> sink` node for taint verification, and `Copilot Autofix` generates context-aware code + dependency suggestions automatically under `GitHub Code Security` (`without requiring Copilot seats or AI credits`). [Skill 4.3: Review CodeQL dataflow analysis insights and remediate alerts using Copilot Autofix and pull request workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Correct. taint-flow paths pinpoint exact user-input sources and unvalidated sinks, while Copilot Autofix proposes context-aware diffs that must still pass CI and human review

### Question 62 — `D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: D (is correct). `codeql github upload-results --repository=pelagicgrid/ballast-control-swift --ref=refs/heads/main --commit=<sha> --sarif=swift-results.sarif` (`authenticated with security_events: write`) publishes the scan. [Skill 4.3: Review CodeQL dataflow analysis insights and remediate alerts using Copilot Autofix and pull request workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning)]

- **A:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **B:** Incorrect. the code-security configurations attach endpoint programmatically binds a Security Configuration to targeted or organization-wide repositories
- **C:** Incorrect. the Dependency Graph SBOM REST endpoint returns upstream direct and transitive packages in machine-readable SPDX JSON
- **D:** Correct. codeql github upload-results publishes externally generated SARIF 2.1.0 files to GitHub Code Scanning with exact ref and commit metadata

### Question 63 — `C, E` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answers: C and E (are correct). Grant job-level `permissions: { security-events: write, contents: read, actions: read }`, and require every `Copilot Autofix` patch to pass dataflow review, CI unit/integration tests, a clean CodeQL re-scan, and human PR approval. [Skill 4.3: Review CodeQL dataflow analysis insights and remediate alerts using Copilot Autofix and pull request workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning)]

- **A:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **B:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **C:** Correct. uploading CodeQL or third-party SARIF 2.1.0 findings from GitHub Actions requires least-privilege security-events: write permission
- **D:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **E:** Correct. LLM-generated security fixes lower remediation friction dramatically, yet still require automated test and human semantic verification before merge

### Question 64 — `B` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: B (is correct). Setting a unique `category:` (`for example category: "/language:cpp/arch:${{ matrix.arch }}"`) isolates alert lifecycles per build configuration on the same commit. [Skill 4.4: Manage code scanning alert lifecycles, dismissals, severity thresholds, and analysis categories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository)]

- **A:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **B:** Correct. branch protection rulesets filter security alerts by Critical/High/Medium/Low security-severity independently from non-security error/warning quality notes
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 65 — `B` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: B (is correct). Because that rule lacked a `@security-severity` score >= `7.0` (`making it a non-security quality Error rather than a High/Critical security alert`), and setting `All alerts: None` disables merge blocking on non-security `Error`/`Warning`/`Note` rules. [Skill 4.4: Manage code scanning alert lifecycles, dismissals, severity thresholds, and analysis categories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Correct. branch protection rulesets filter security alerts by Critical/High/Medium/Low security-severity independently from non-security error/warning quality notes
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 66 — `C` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: C (is correct). Switching `github/codeql-action/init@v3` to `build-mode: manual` and running the exact `cmake --preset offshore-rtos && cmake --build` step before `analyze` guarantees full compiler-traced extraction. [Skill 4.4: Manage code scanning alert lifecycles, dismissals, severity thresholds, and analysis categories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository)]

- **A:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Correct. build-mode: manual traces exact custom C/C++, C#, Go, Java/Kotlin, or Swift compiler invocations when autobuild heuristics fail
- **D:** Incorrect. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets

### Question 67 — `B` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: B (is correct). Author a YAML `CodeQL model pack` (`data extensions`) declaring `readUntrustedPayload()` as a remote taint `source` and load it via `packs:` in `.github/codeql/codeql-config.yml`. [Skill 4.5: Optimize and troubleshoot Code Security operations with custom configurations, model packs, and build/performance diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning)]

- **A:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **B:** Correct. codeql-config.yml centralizes custom query packs, path exclusions, threat models, and data-extension model packs for Advanced Setup
- **C:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **D:** Incorrect. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets

### Question 68 — `D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: D (is correct). Fan out languages into parallel `matrix` jobs, exclude generated directories via `paths-ignore` in `codeql-config.yml`, and run compiled `C++`/`Java` extraction on high-CPU/high-RAM Larger or self-hosted runners (`optionally setting --ram / --threads`). [Skill 4.5: Optimize and troubleshoot Code Security operations with custom configurations, model packs, and build/performance diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **D:** Correct. model packs teach CodeQL custom internal framework sources/sanitizers/sinks without forking queries, while Adequate RAM/CPU runners and scoped paths resolve timeout/OOM failures

### Question 69 — `A` (Security operations: best practices, prioritization, and remediation)

Correct answer: A (is correct). Enabling `Private vulnerability reporting` lets researchers open draft `GHSA` advisories where maintainers classify the `CWE` weakness, develop a silent patch in a temporary private fork, request a `CVE`, and publish coordinated semver advisory data. [Skill 5.1: Understand CVE, CWE, and GitHub Security Advisory (GHSA) concepts and execute end-to-end advisory remediation workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories)]

- **A:** Correct. maintainers triage private reports inside draft GHSAs, patch silently in temporary private forks (where Actions stay disabled), request a CVE, and publish coordinated advisories
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names

### Question 70 — `D` (Security operations: best practices, prioritization, and remediation)

Correct answer: D (is correct). No—GitHub Actions is intentionally disabled inside temporary private advisory forks, and opening a public PR with the exploit reproducer leaks the unpatched vulnerability before downstream operators can upgrade. [Skill 5.1: Understand CVE, CWE, and GitHub Security Advisory (GHSA) concepts and execute end-to-end advisory remediation workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories)]

- **A:** Incorrect. when global Dependabot security updates remain enabled, Dependabot attempts PRs for every patchable alert, overriding selective custom PR auto-triage rules
- **B:** Incorrect. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories
- **C:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. No—GitHub Actions is intentionally disabled inside temporary private advisory forks, and opening a public PR with the exploit reproducer leaks the unpatched vulnerability before downstream operators can upgrade.
- **D:** Correct. validate advisory patches locally or in an isolated private mirror without exposing exploit diffs publicly before publishing the coordinated GHSA release

### Question 71 — `C` (Security operations: best practices, prioritization, and remediation)

Correct answer: C (is correct). Once published to the GitHub Advisory Database (`Reviewed` tier), exact ecosystem and semver boundaries allow Dependabot to alert every downstream Go repository running `< 1.8.4` and automatically propose upgrading to `1.8.4`. [Skill 5.1: Understand CVE, CWE, and GitHub Security Advisory (GHSA) concepts and execute end-to-end advisory remediation workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories)]

- **A:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Correct. maintainers triage private reports inside draft GHSAs, patch silently in temporary private forks (where Actions stay disabled), request a CVE, and publish coordinated advisories
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 72 — `C` (Security operations: best practices, prioritization, and remediation)

Correct answer: C (is correct). Filter backlogs by `has:deployment`, `runtime-risk:internet-exposed`, `EPSS`, and `Reachability` to remediate live internet-facing grid workloads first, while enforcing `Require code scanning results` (`Critical/High`) on active default-branch rulesets. [Skill 5.2: Define, prioritize, and enforce severity rulesets and production-context prioritization at scale | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-vulnerabilities/alerts-in-production-code)]

- **A:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Correct. combining runtime deployment exposure with pre-merge High/Critical blocking stops alert growth while burning down real internet-exposed production risk first
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 73 — `D` (Security operations: best practices, prioritization, and remediation)

Correct answer: D (is correct). Only after **both** `CodeQL` and `Trivy` report scan results for the pull request ref with zero net-new alerts breaching their respective configured severity thresholds. [Skill 5.2: Define, prioritize, and enforce severity rulesets and production-context prioritization at scale | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-vulnerabilities/alerts-in-production-code)]

- **A:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Correct. combining Rulesets with REST/GraphQL security configuration and org-level alert APIs automates compliance reporting and zero-drift enforcement across thousands of repositories

### Question 74 — `A, B` (Security operations: best practices, prioritization, and remediation)

Correct answers: A and B (are correct). Ingest deployment telemetry from Defender for Cloud / JFrog (`has:deployment`, `runtime-risk:internet-exposed`), and run new organization rulesets in `Evaluate` mode before flipping enforcement to `Active`. [Skill 5.2: Define, prioritize, and enforce severity rulesets and production-context prioritization at scale | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-vulnerabilities/alerts-in-production-code)]

- **A:** Correct. Evaluate mode surfaces missing scans or noisy rules safely without halting production releases on day one
- **B:** Correct. production context pinpoints vulnerabilities actually running in internet-facing workloads rather than dead or archived repos
- **C:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **E:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 75 — `A` (Security operations: best practices, prioritization, and remediation)

Correct answer: A (is correct). PelagicGrid should filter default-branch `CWE-78`/`CWE-918` alerts in Security Overview, create a Security Campaign (`<=1,000` alerts) with a target date and OT AppSec contact, generate Copilot Autofix diffs (`or delegate <=25 alerts per batch to @copilot`), and validate CI before merging. [Skill 5.3: Execute campaign-based remediation strategies, bulk alert management, and audited alert dismissal documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/manage-security-alerts/best-practices-for-participating-in-a-security-campaign)]

- **A:** Correct. Security Campaigns group high-risk default-branch alerts around a dedicated security contact and accelerate developer burndown with Copilot Autofix or @copilot draft PRs
- **B:** Incorrect. disabling scanners or bulk-dismissing unreviewed findings hides real production vulnerabilities rather than remediating security debt
- **C:** Incorrect. agentic @copilot campaign assignments cap at 25 alerts per batch (opening a PR for human/CI verification), and Copilot cannot rotate external cloud provider IAM credentials
- **D:** Incorrect. code security campaigns target default-branch alerts (up to 1,000 per campaign) with a named contact, and developers need write access plus passing CI checks to merge fixes

### Question 76 — `A` (Security operations: best practices, prioritization, and remediation)

Correct answer: A (is correct). Managers can assign up to `25` alerts per batch to `@copilot` (`consuming Code Security AI credits`), which opens draft pull requests on the target repositories for CI validation and human code review. [Skill 5.3: Execute campaign-based remediation strategies, bulk alert management, and audited alert dismissal documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/manage-security-alerts/best-practices-for-participating-in-a-security-campaign)]

- **A:** Correct. grouping related CWEs into focused campaigns builds developer remediation momentum while Copilot Autofix and @copilot PR batches cut manual toil
- **B:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **C:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 77 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). Detect weak dismissal justifications via Security Overview campaign tracking, `code_scanning_alert` webhooks, or REST audits, reopen the unverified alerts, and require documented technical proof (`or a YAML model-pack sanitizer summary`). [Skill 5.3: Execute campaign-based remediation strategies, bulk alert management, and audited alert dismissal documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/manage-security-alerts/best-practices-for-participating-in-a-security-campaign)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Correct. alert dismissals remain visible in REST/GraphQL APIs, webhooks, and audit logs, so teams must document rationale rather than hiding unverified risk
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 78 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). Configuring `queries: security-extended` runs `default` high-precision plus medium-precision security queries while excluding the maintainability/quality queries found in `security-and-quality`. [Skill 5.4: Customize CodeQL query suites, multi-repository variant analysis, and risk-profile-tailored security detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites)]

- **A:** Incorrect. filtering by has:deployment and runtime-risk:internet-exposed isolates alerts affecting live internet-reachable workloads
- **B:** Correct. security-extended broadens vulnerability detection beyond default without adding non-security maintainability noise from security-and-quality
- **C:** Incorrect. querying is:closed resolution:auto-dismiss audits every Dependabot alert suppressed by preset or custom auto-triage rules
- **D:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)

### Question 79 — `C` (Security operations: best practices, prioritization, and remediation)

Correct answer: C (is correct). `Multi-Repository Variant Analysis (MRVA)` in the CodeQL VS Code extension executes custom `.ql` queries across up to 1,000 repositories via a controller GitHub Actions workflow. [Skill 5.4: Customize CodeQL query suites, multi-repository variant analysis, and risk-profile-tailored security detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites)]

- **A:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Correct. security-extended expands vulnerability coverage beyond high-precision default rules, while MRVA hunts novel zero-day patterns across up to 1,000 org repositories simultaneously
- **D:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`

### Question 80 — `C` (Security operations: best practices, prioritization, and remediation)

Correct answer: C (is correct). Add `threat-models: [remote, local]` inside `.github/codeql/codeql-config.yml` so local filesystem, CLI argument, and environment-variable inputs are tracked as taint sources. [Skill 5.4: Customize CodeQL query suites, multi-repository variant analysis, and risk-profile-tailored security detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Correct. model packs teach CodeQL custom internal framework sources/sanitizers/sinks without forking queries, while Adequate RAM/CPU runners and scoped paths resolve timeout/OOM failures
- **D:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)

### Question 81 — `D` (Security operations: best practices, prioritization, and remediation)

Correct answer: D (is correct). Assign a custom repository role (`inheriting Write`) granted fine-grained Code Scanning and Dependabot alert view/dismiss permissions, paired with org-level `Security Managers` governing rulesets and Security Configurations. [Skill 5.5: Collaborate across security roles, delegated exceptions, alert ownership, and cross-suite governance rulesets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)]

- **A:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **D:** Correct. clear alert ownership, delegated bypass reviewers, and Evaluate-first cross-suite rulesets align AppSec governance with engineering velocity

### Question 82 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). No—the developer receives temporary single-alert read/resolve access **only** for the specific secret alert(s) assigned to them, and loses that visibility once unassigned. [Skill 5.5: Collaborate across security roles, delegated exceptions, alert ownership, and cross-suite governance rulesets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)]

- **A:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **B:** Correct. clear alert ownership, delegated bypass reviewers, and Evaluate-first cross-suite rulesets align AppSec governance with engineering velocity
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 83 — `A, D` (Security operations: best practices, prioritization, and remediation)

Correct answers: A and D (are correct). Use `Security Manager` + fine-grained custom alert roles with explicit per-alert `Assignees`, and route Push Protection overrides through `delegated bypass` backed by visible teams or custom bypass-approver roles. [Skill 5.5: Collaborate across security roles, delegated exceptions, alert ownership, and cross-suite governance rulesets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)]

- **A:** Correct. delegated bypass replaces ad-hoc writer self-bypasses with a structured request-and-approval workflow audited via webhooks and logs
- **B:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **C:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **D:** Correct. clear alert ownership, delegated bypass reviewers, and Evaluate-first cross-suite rulesets align AppSec governance with engineering velocity
- **E:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 84 — `A` (Security operations: best practices, prioritization, and remediation)

Correct answer: A (is correct). Enable `Push Protection` (`pre-receive`), `actions/dependency-review-action@v4` (`PR dependency/license diff check`), and PR `CodeQL` scanning with `Copilot Autofix` gated by an active branch ruleset. [Skill 5.6: Shift left and strengthen preventive security through push protection, pre-merge dependency scanning, and PR CodeQL analysis | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Correct. combining all three shift-left controls prevents new security debt from ever landing on the default branch
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`

### Question 85 — `D` (Security operations: best practices, prioritization, and remediation)

Correct answer: D (is correct). `Dependency Graph` and `GitHub Code Security` (`or GHAS`) must be enabled on the private repository (`whereas Dependency Review runs free on public GitHub.com repositories`). [Skill 5.6: Shift left and strengthen preventive security through push protection, pre-merge dependency scanning, and PR CodeQL analysis | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **C:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **D:** Correct. Dependency Review inspects PR manifest/lockfile diffs before merge and fails the check when newly introduced packages breach vulnerability or license policies

### Question 86 — `A, D, E` (Security operations: best practices, prioritization, and remediation)

Correct answers: A, D, and E (are correct). Block high-confidence secrets pre-receive via Push Protection, gate PR vulnerabilities and SPDX licenses via `dependency-review-action@v4`, and verify CodeQL `Copilot Autofix` patches with full CI tests and human PR review. [Skill 5.6: Shift left and strengthen preventive security through push protection, pre-merge dependency scanning, and PR CodeQL analysis | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Correct. LLM-generated security fixes lower remediation friction dramatically, yet still require automated test and human semantic verification before merge
- **B:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Correct. stopping secrets pre-receive prevents Git history contamination and emergency credential rotation
- **E:** Correct. Dependency Review blocks both vulnerable package versions and prohibited copyleft/unknown licenses on pull requests
- **F:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions

### Question 87 — `D` (GitHub Security suites administration)

Correct answer: D (is correct). Verify committer license headroom (`or metered budget`), create/select a Security Configuration, attach it to tiered repos via custom properties with `Apply to new repositories` enabled, and set `Enforced` to lock baseline controls. [Skill 6.1: Roll out GitHub Security Suites at enterprise, organization, and repository scale and contrast GHEC vs. GHES capabilities | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/choosing-a-security-configuration-for-your-repositories)]

- **A:** Incorrect. manual per-repo changes do not scale or prevent configuration drift, and granting Organization Owner violates least privilege when Security Manager / Security Configurations exist
- **B:** Incorrect. exceeding volume committer licenses blocks enablement on additional/new private repos, and features left as Not set remain editable by repository admins even under Enforced configurations
- **C:** Incorrect. standalone GHES uses volume/subscription licensing (not metered billing) and requires GitHub Connect for Advisory DB sync, while transferred repos must be explicitly targeted by configurations
- **D:** Correct. rolling out Security Configurations verifies committer license capacity first, targets repo tiers via custom properties, covers newly created repos, and locks drift with Enforced mode

### Question 88 — `C` (GitHub Security suites administration)

Correct answer: C (is correct). `GHEC` offers metered or volume licensing plus cloud AI features (`Copilot Autofix`, AI push secret detection), whereas `GHES` uses volume/subscription licensing and requires `GitHub Connect` to sync the GitHub Advisory Database and deduplicate hybrid committer seats. [Skill 6.1: Roll out GitHub Security Suites at enterprise, organization, and repository scale and contrast GHEC vs. GHES capabilities | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/choosing-a-security-configuration-for-your-repositories)]

- **A:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Correct. Security Configurations eliminate manual repo drift on GHEC and GHES, while hybrid enterprises link GHES to GHEC via GitHub Connect for Advisory DB updates and committer seat deduplication
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 89 — `B` (GitHub Security suites administration)

Correct answer: B (is correct). `Apply to new repositories` triggers only for newly created or newly forked repositories inside the org; transferred repositories do not inherit that default automatically and must be attached explicitly via Security Configurations UI or REST API. [Skill 6.1: Roll out GitHub Security Suites at enterprise, organization, and repository scale and contrast GHEC vs. GHES capabilities | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/choosing-a-security-configuration-for-your-repositories)]

- **A:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **B:** Correct. understanding Enforced vs Unenforced inheritance, transferred-repo gaps, 90-day active committer deduplication, and hard budgets on metered SKUs/AI credits prevents surprise overages or lockouts
- **C:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 90 — `D` (GitHub Security suites administration)

Correct answer: D (is correct). No—even under `Enforced` mode, any row left as `"Not set"` remains unlocked and editable by repository administrators; set `Dependabot alerts = Enabled` explicitly to lock it. [Skill 6.2: Configure suite defaults, Enforced vs. Unenforced inheritance, 90-day active-committer licensing, and AI credit budgets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/billing/concepts/product-billing/github-advanced-security)]

- **A:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. No—even under `Enforced` mode, any row left as `"Not set"` remains unlocked and editable by repository administrators; set `Dependabot alerts = Enabled` explicitly to lock it.
- **B:** Incorrect. each gzipped SARIF upload must be <=10 MB with a distinct category per language/tool/component and security-events: write permission
- **C:** Incorrect. when global Dependabot security updates remain enabled, Dependabot attempts PRs for every patchable alert, overriding selective custom PR auto-triage rules
- **D:** Correct. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories

### Question 91 — `A` (GitHub Security suites administration)

Correct answer: A (is correct). Exactly **`85`** seats: licensing counts unique human users who authored/pushed commits to at least one enabled private/internal repository within the rolling **90-day** window (`deduplicated across the enterprise, excluding read-only users, >90-day inactive authors, and built-in bots`). [Skill 6.2: Configure suite defaults, Enforced vs. Unenforced inheritance, 90-day active-committer licensing, and AI credit budgets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/billing/concepts/product-billing/github-advanced-security)]

- **A:** Correct. understanding Enforced vs Unenforced inheritance, transferred-repo gaps, 90-day active committer deduplication, and hard budgets on metered SKUs/AI credits prevents surprise overages or lockouts
- **B:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **C:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 92 — `C, E` (GitHub Security suites administration)

Correct answers: C and E (are correct). Unique human committers over the rolling 90-day window deduplicate once across the enterprise (`including GHEC + GHES via GitHub Connect`), and administrators can set **hard metered budgets** capping `Code Security AI credits` and `Secret Protection AI credits`. [Skill 6.2: Configure suite defaults, Enforced vs. Unenforced inheritance, 90-day active-committer licensing, and AI credit budgets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/billing/concepts/product-billing/github-advanced-security)]

- **A:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **B:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **C:** Correct. a developer pushing to 50 GHAS-enabled repos in an enterprise consumes only one active-committer license seat over the rolling 90-day window
- **D:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **E:** Correct. classic CodeQL Copilot Autofix does not consume AI credits, whereas agentic autofix / AI Scan and AI push secret scanning draw from included or metered AI credit pools

### Question 93 — `C` (GitHub Security suites administration)

Correct answer: C (is correct). Disable `Repository administrators can enable or disable GitHub Code Security` in Enterprise settings—leaving all currently enabled repos active while restricting future repo-level toggles to Org/Enterprise Owners and Security Managers. [Skill 6.3: Define enterprise and organization security policies, enforcement boundaries, bypass permissions, and audit log governance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise)]

- **A:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **B:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **C:** Correct. enterprise policies prevent uncontrolled repo-admin license consumption while audit log streaming preserves tamper-evident compliance records across configuration and bypass events
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 94 — `D` (GitHub Security suites administration)

Correct answer: D (is correct). Security Configuration creation/attachment/detachment (`security_configuration.*`), Push Protection bypass approvals, ruleset edits/bypasses (`repository_ruleset.*`), custom secret pattern changes, and alert dismissal/resolution events all stream to the SIEM. [Skill 6.3: Define enterprise and organization security policies, enforcement boundaries, bypass permissions, and audit log governance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Correct. enterprise policies prevent uncontrolled repo-admin license consumption while audit log streaming preserves tamper-evident compliance records across configuration and bypass events

### Question 95 — `B` (GitHub Security suites administration)

Correct answer: B (is correct). GitHub cannot auto-enable paid `GitHub Code Security` features on the new private repository once volume seats hit 100% capacity, logging a license-exhaustion warning until seats free up or capacity is added. [Skill 6.3: Define enterprise and organization security policies, enforcement boundaries, bypass permissions, and audit log governance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise)]

- **A:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **B:** Correct. understanding Enforced vs Unenforced inheritance, transferred-repo gaps, 90-day active committer deduplication, and hard budgets on metered SKUs/AI credits prevents surprise overages or lockouts
- **C:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 96 — `B` (GitHub Security suites administration)

Correct answer: B (is correct). Granting the **`Security Manager`** organization role to `@pelagicgrid/ot-appsec` provides full org-wide security posture, alert triage, and Security Configuration management without code-write or billing-owner access. [Skill 6.4: Define administrator, Security Manager, developer, and fine-grained custom roles for viewing and dismissing security alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Correct. Security Manager and fine-grained custom repository roles grant AppSec and security champions exact triage permissions without over-provisioning Repository Admin or code-push rights
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges

### Question 97 — `C` (GitHub Security suites administration)

Correct answer: C (is correct). Create a custom repository role inheriting `Read` with only `View code scanning alerts` and `View Dependabot alerts` enabled. [Skill 6.4: Define administrator, Security Manager, developer, and fine-grained custom roles for viewing and dismissing security alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization)]

- **A:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **B:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **C:** Correct. Security Manager and fine-grained custom repository roles grant AppSec and security champions exact triage permissions without over-provisioning Repository Admin or code-push rights
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 98 — `D` (GitHub Security suites administration)

Correct answer: D (is correct). Assigning `Review and manage secret scanning bypass requests` in a custom organization role scopes delegated Push Protection bypass approvals cleanly. [Skill 6.4: Define administrator, Security Manager, developer, and fine-grained custom roles for viewing and dismissing security alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization)]

- **A:** Incorrect. uploading CodeQL or third-party SARIF 2.1.0 findings from GitHub Actions requires least-privilege security-events: write permission
- **B:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **C:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **D:** Correct. granting Review and manage secret scanning bypass requests creates least-privilege Push Protection approvers without full Org Owner access

### Question 99 — `C` (GitHub Security suites administration)

Correct answer: C (is correct). Standardize CodeQL across target repos, create an Organization Branch Ruleset in `Evaluate` mode with `Require code scanning results` (`High+`), audit Evaluate insights and scope bypass actors, then switch enforcement to `Active`. [Skill 6.5: Enforce default or approved custom CodeQL workflows and automate large-scale security governance via REST and GraphQL APIs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/rest/code-security/configurations)]

- **A:** Incorrect. requiring CodeQL results before CodeQL runs deadlocks every PR awaiting a missing scan, while granting broad writer bypass or blocking on Note hints breaks governance
- **B:** Incorrect. secret_scanning.yml only configures secret path exclusions, and AI suggestions never replace required human pull-request approvals
- **C:** Correct. piloting an Organization Ruleset in Evaluate mode confirms CodeQL check reporting and false-positive impact before switching Require code scanning results to Active merge blocking
- **D:** Incorrect. Require code scanning results blocks PR merges until the configured tool reports scan results for that pull request head/merge ref

### Question 100 — `C, D` (GitHub Security suites administration)

Correct answers: C and D (are correct). Enforce centrally governed Required Workflows + `Require code scanning results` rulesets, and call `POST /orgs/{org}/code-security/configurations/{configuration_id}/attach` plus org/enterprise alert REST/GraphQL endpoints (`GET /orgs/{org}/code-scanning/alerts`, `/secret-scanning/alerts`, `/dependabot/alerts`). [Skill 6.5: Enforce default or approved custom CodeQL workflows and automate large-scale security governance via REST and GraphQL APIs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/rest/code-security/configurations)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **C:** Correct. the code-security configurations attach endpoint programmatically binds a Security Configuration to targeted or organization-wide repositories
- **D:** Correct. combining Rulesets with REST/GraphQL security configuration and org-level alert APIs automates compliance reporting and zero-drift enforcement across thousands of repositories
- **E:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
