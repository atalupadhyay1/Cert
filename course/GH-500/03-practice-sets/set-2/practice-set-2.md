# Microsoft / GitHub Exam GH-500: GitHub Advanced Security — Full-Length Mock Exam 2

**Theme:** GitHub Secret Protection, Push Protection, Validity Checks, Delegated Bypass & Custom Patterns  
**Credential:** `GitHub Advanced Security` *(Intermediate · **no prerequisite** · **2-year validity** transitioning to Microsoft Learn recertification)*  
**Study guide baseline:** `July 2026 (Last updated May 14, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-500 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Advanced Security documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Describe GitHub Security suites, features, and ecosystem (15–20% official weight · 18 questions)

### 1. AetherNav Aerospace operates a dedicated ground-tools organization on `GitHub Team` (`groundstation-cli`, `mission-planner-ui`) and wants `CodeQL` + `Copilot Autofix` without purchasing Secret Protection for that org yet. How does GitHub license its Security suites?

- **A.** Standalone `GitHub Secret Protection` and `GitHub Code Security` SKUs (`purchasable separately or together on GitHub Team and GitHub Enterprise`, alongside legacy bundled GHAS)
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **D.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect

### 2. During an AS9100 aerospace audit at AetherNav Aerospace, assessors ask which native GitHub Security pillar addresses ground-antenna TLS private keys in Git, buffer-overflow bugs in `flightdeck-guidance-cpp`, and vulnerable Go modules in `orbital-downlink-go`. Which mapping is accurate?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** `Secret Protection` (`secret scanning + push protection`), `Code Security` (`CodeQL/SARIF SAST + Copilot Autofix`), and `Supply Chain Security` (`Dependency Graph, Dependabot, Dependency Review & SBOMs`)

### 3. AetherNav Aerospace's procurement team is comparing feature entitlements between `GitHub Secret Protection` and `GitHub Code Security` for 65 private avionics repositories. Which two statements accurately match features to SKUs? Select two.

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** `GitHub Secret Protection` prevents and detects leaked credentials via `Push Protection`, `secret scanning`, `validity checks`, custom patterns, and AI generic secret detection
- **E.** `GitHub Code Security` finds and fixes code and dependency risks via `CodeQL` / `SARIF` code scanning, `Copilot Autofix`, `Dependency Review` on private repos, and `Security Campaigns`

### 4. AetherNav Aerospace publishes open-source ephemeris parsers in a `public` GitHub.com repo (`open-rinex-tools`) while keeping `star-tracker-dsp` in a `private` GHEC repository. How does built-in security availability differ across the two visibility tiers?

- **A.** Core features (`secret scanning, push protection, Dependency Graph, Dependabot, CodeQL default setup & Dependency Review`) are free on `public` GitHub.com repos; `private/internal` repos require licensed SKUs where applicable
- **B.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners

### 5. AetherNav Aerospace's Flight Safety CISO wants to filter alert trends across 90 satellite repositories tagged with custom property `flight_tier:critical` and inspect scanner coverage gaps on a single dashboard (`____`). Which view provides this?

- **A.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **B.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **C.** `.github/codeql/codeql-config.yml` (`defining packs:, queries:, paths-ignore:, and threat-models: alongside YAML model-pack extensions`)
- **D.** `Security Overview` (`Organization & Enterprise Risk, Coverage, Campaigns, Code scanning, Secret scanning & Dependabot dashboards` filterable by team, topic, or custom property)

### 6. Before committing enterprise seats for an acquired propulsion lab, AetherNav Aerospace wants a zero-cost scan of historical secret leaks across that org plus sample CodeQL findings on up to `____` (`20`) repositories. Which native feature supports this?

- **A.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **B.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **C.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **D.** Organization `free security risk assessment` (`scanning org repos for leaked secrets and up to 20 active repositories for CodeQL vulnerabilities + Copilot Autofix preview`)

### 7. On `transponder-bus-c`, Secret Protection blocked a Space-Track API token inside a YAML manifest at push time, while CodeQL flagged an unvalidated telemetry packet length flowing into `memcpy()` on the pull request. How do the two engines complement each other?

- **A.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** `Secret Protection` matches structured/high-entropy/AI secret tokens across Git history & pushes, whereas `Code Security (CodeQL)` traces semantic AST/dataflow vulnerabilities (`including hardcoded-credential sinks`)

### 8. AetherNav Aerospace wants to prevent ground-station credentials, copyleft telemetry libraries, and memory-safety bugs from ever merging into `gnss-ephemeris-rust` `main`. Which combined SDLC architecture meets all three goals?

- **A.** Layer `Push Protection` (`pre-receive`), `actions/dependency-review-action` (`PR manifest/license gate`), and `CodeQL` PR checks (`with Copilot Autofix`) so secrets, vulnerable packages, and taint flaws fail pre-merge
- **B.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts

### 9. AetherNav Aerospace must block live satellite-uplink keys at `git push` on `orbital-downlink-go` and detect Go SQL/command-injection taint flows on every pull request. Proposed solution: Enable `GitHub Secret Protection` with `Push Protection` and enable `GitHub Code Security` (`CodeQL Default Setup`) enforced via an active branch ruleset on `main`. Does this meet the goal?

- **A.** No — dismissing a Secret Protection alert or deleting the line in a new commit leaves the live credential active and exposed in prior Git history (`revoke & rotate first, then purge history`)
- **B.** No — CodeQL `Default Setup` and custom `Advanced Setup` (`.github/workflows/codeql.yml`) cannot run active CodeQL management simultaneously (`switch to Advanced Setup with build-mode: manual`)
- **C.** No — `.github/secret_scanning.yml` `paths-ignore` only auto-closes post-push user alerts (`<=1,000` paths / `<=1 MB`) and neither revokes keys nor replaces Push Protection / public partner alerts
- **D.** Yes — this configuration satisfies every security, licensing, and governance requirement

### 10. AetherNav Aerospace is modernizing its `autopilot-sim-suite` pipeline from a late pre-flight freeze audit to a shift-left GitHub Security model. Which four-step execution sequence represents prevention-first operations?

- **A.** Apply Copilot Autofix before running CodeQL → run Push Protection only after merging to main → skip Dependency Review on lockfiles → delete Security Overview roles
- **B.** Block secrets pre-receive via Push Protection → run Dependency Review & CodeQL on the PR → apply Copilot Autofix or patch vulnerable packages before merge → monitor default-branch advisories in Security Overview
- **C.** Merge PRs without checks to main → run weekly manual secret scans → disable Push Protection to avoid developer friction → export CSVs quarterly without remediating open alerts
- **D.** Dismiss all PR alerts automatically → merge vulnerable dependencies → run Dependency Review only on archived branches → rely on gitignore to revoke leaked API tokens

### 11. Why did AetherNav Aerospace's legacy "scan only release candidates once per quarter" gate cost 10x more engineering hours than enabling Push Protection and PR CodeQL checks on `telemetry-ingest-kotlin`?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Prevention-first (`Push Protection + IDE/PR Dependency Review + PR CodeQL with Copilot Autofix`) stops defects before Git history/merge, whereas late release-only gates cause expensive rework
- **C.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 12. AetherNav Aerospace wants six avionics squads to burn down 420 legacy path-traversal and integer-overflow findings on default branches before Q4 flight certification, with an assigned AppSec point of contact. Which feature (`____`) organizes this?

- **A.** `Security Campaigns` (`targeted, time-bound initiatives grouping up to 1,000 default-branch alerts with a named security contact and Copilot Autofix support`)
- **B.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **C.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 13. A flight-sim developer on `autopilot-sim-suite` dismisses a mock telemetry credential alert inside a synthetic bench harness as `Used in tests`. What audit metadata does GitHub preserve for DO-178C traceability?

- **A.** Dismissing an alert requires a structured closure reason (`False positive`, `Used in tests`, `Won't fix`) plus an audit-logged justification comment—and never deletes commits or revokes keys
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses

### 14. An engineer committed a live ground-relay SSH private key to `groundstation-cli` yesterday. Proposed solution: Dismiss the Secret Protection alert as `False positive` with a comment and add `*.pem` to `.gitignore` on `main`. Does this remediate the incident?

- **A.** No — temporary private forks created inside a Repository Security Advisory (`GHSA`) intentionally **disable GitHub Actions** (`and pushing fixes to a public branch before release leaks the zero-day`)
- **B.** No — dismissing a Secret Protection alert or deleting the line in a new commit leaves the live credential active and exposed in prior Git history (`revoke & rotate first, then purge history`)
- **C.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **D.** No — repository-wide `Dependabot security updates` must be **disabled** before a custom Dependabot auto-triage `Open a pull request` rule can selectively control which alerts open PRs

### 15. AetherNav Aerospace's quality assurance lead needs strict controls over alert dismissals across `radhard-hal-sdk`. Which two governance controls ensure dismissals are justified and auditable? Select two.

- **A.** Require an accurate dismissal reason (`False positive`, `Used in tests`, or `Won't fix`) with a reviewer-auditable justification comment whenever dismissing an alert
- **B.** Monitor dismissed and open alert trends centrally in `Security Overview` and `Audit Logs` (`repository_vulnerability_alert`, `secret_scanning_alert`, `code_scanning_alert`)
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **E.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 16. How should AetherNav Aerospace partition day-to-day GitHub Security duties across Enterprise Administrators, Avionics AppSec (`Security Managers`), and Flight Software Developers?

- **A.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **B.** Shared security model: `Admins` govern licensing/Security Configurations, `Security Managers` monitor Security Overview/campaigns/policies, and `Developers` remediate PR & campaign findings
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners

### 17. Why does AetherNav Aerospace pair restricted Secret Protection alert visibility with Push Protection `delegated bypass` on `orbital-downlink-go`?

- **A.** Least-privilege alert access (`Write/Maintain/Admin/Security Manager` or custom roles) paired with `delegated bypass` so designated reviewers audit push-protection exceptions
- **B.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 18. AetherNav Aerospace's government customer requires clear DevSecOps role separation, audited push-protection exceptions, and machine-readable SPDX SBOMs for every satellite release. Which three capabilities satisfy those contract terms? Select three.

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Export an `SPDX` JSON Software Bill of Materials (`SBOM`) via `Insights -> Dependency graph -> Export SBOM`, `GET /repos/{owner}/{repo}/dependency-graph/sbom`, or `actions/attest-sbom` (`excluding dependents`)
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** Shared security model: `Admins` govern licensing/Security Configurations, `Security Managers` monitor Security Overview/campaigns/policies, and `Developers` remediate PR & campaign findings
- **E.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **F.** Least-privilege alert access (`Write/Maintain/Admin/Security Manager` or custom roles) paired with `delegated bypass` so designated reviewers audit push-protection exceptions

---

## Domain 2 — Configure and use Secret Protection (formerly secret scanning) (15–20% official weight · 18 questions)

### 19. AetherNav Aerospace is onboarding 55 private repositories in its `aethernav-satcom` organization and wants Secret Protection + Push Protection turned on immediately and inherited by every newly created repo. Which administrative mechanism (`____`) should be used?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Enable `GitHub Secret Protection` (`secret scanning + push protection`) via Organization/Enterprise `Security Configurations` (`with Apply to new repositories`) or Repository `Settings -> Advanced Security`
- **C.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 20. A contractor accidentally pushes a GitHub Personal Access Token (`ghp_...`) to AetherNav's public `open-rinex-tools` repo, while another contractor pushes a token to the private `star-tracker-dsp` repo. How does automatic revocation/alerting differ?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** On `public` repos, partner patterns run free and auto-notify token providers for revocation; on `private/internal` repos (`with Secret Protection`), alerts notify repo/org users (`plus optional validity checks`)
- **C.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 21. AetherNav Aerospace's subsidiary `aethernav-drones` has not yet enabled Secret Protection seats and wants to know how many historical partner secrets exist across its 30 private repos before buying licenses. Which zero-cost Organization Security Overview feature (`____`) provides that count?

- **A.** Organization `free security risk assessment` (`scanning org repos for leaked secrets and up to 20 active repositories for CodeQL vulnerabilities + Copilot Autofix preview`)
- **B.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **C.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **D.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses

### 22. An avionics engineer edits `config/uplink.yaml` directly in the GitHub.com web editor on `mission-planner-ui`, pastes a live Azure Storage SAS token, and attempts to commit—receiving an immediate block before the commit saves. Which feature stopped the commit (`____`)?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **C.** `Push Protection` intercepts supported high-confidence and published custom secrets pre-receive during `git push` (`CLI, IDE, web editor & REST API`), blocking the secret from entering Git history
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 23. AetherNav Aerospace enabled `Automatically verify if a secret is valid by sending it to the relevant partner` on `orbital-downlink-go`. What three validity states (`____`) appear on partner alerts, and why can non-provider generic RSA key alerts never show `Active`?

- **A.** `Validity checks` query partner token endpoints (`displaying Active, Inactive, or Unknown`) so responders prioritize live `Active` credentials first
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config

### 24. AetherNav Aerospace wants `telemetry-ingest-kotlin` protected against both standard cloud provider keys at `git push` and unstructured telemetry broker passwords pasted into `.conf` files. Which two Secret Protection capabilities should be enabled? Select two.

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **D.** `Push Protection` blocks high-confidence partner and published custom secrets pre-receive during `git push` before commits land on GitHub
- **E.** `Non-provider / generic pattern scanning` (`private keys, DB connection strings`) plus `Copilot AI generic secret detection` (`unstructured passwords/keys`, consuming `Secret Protection AI credits` on push)

### 25. A Secret Protection alert on `flightdeck-guidance-cpp` shows `Validity: Active` for an AWS IAM access key committed to a feature branch 45 minutes ago. In what sequence must AetherNav Aerospace's SOC respond?

- **A.** Dismiss the alert as Won't fix → delete the line in a new commit while keeping the live key active → add the file to .gitignore → assume old commits are unreadable
- **B.** Run git filter-repo first while leaving the production key active for 30 days → disable Secret Protection to clear UI banners → rotate the key only if an outage occurs → skip audit notes
- **C.** Add paths-ignore in .github/secret_scanning.yml to auto-close the live production key alert → keep the credential unrotated → merge to main → archive the audit log
- **D.** Confirm alert validity & blast radius → revoke and rotate the compromised credential at the provider → purge commit history (`git filter-repo`) & contact Support if cached PRs remain → resolve the alert as Revoked

### 26. After rotating a leaked ground-control API token and running `git filter-repo --force` on `groundstation-cli`, an engineer notices the commit SHA is still reachable via a closed pull request URL on GitHub.com. What additional remediation step is required?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Treat every committed secret as compromised: `revoke & rotate at the issuing provider immediately`, rewrite Git history (`git filter-repo`), purge cached views via Support if needed, and resolve as `Revoked`
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 27. Which Secret Protection closure resolution (`____`) should an AetherNav Security Manager select for a synthetic RFC-example token inside `docs/protocol-spec.md`, versus a real production token that has just been invalidated at the cloud provider?

- **A.** Dismissing an alert requires a structured closure reason (`False positive`, `Used in tests`, `Won't fix`) plus an audit-logged justification comment—and never deletes commits or revokes keys
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config

### 28. Without delegated bypass configured on `star-tracker-dsp`, who can bypass a Push Protection block by default, and how does enabling `Delegated bypass` change that behavior?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **C.** `Delegated bypass for push protection` (`granting Specific roles, visible teams, or custom roles with "Review and manage secret scanning bypass requests" authority—never secret teams`)
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 29. AetherNav Aerospace wants to prevent secret teams from being added to Push Protection bypass lists while ensuring only the `satcom-sec-reviewers` team approves push exceptions on `orbital-downlink-go`. Proposed solution: Leave Push Protection disabled and list `@aethernav/satcom-sec-reviewers` inside `.github/secret_scanning.yml`. Does this meet the goal?

- **A.** No — `actions/dependency-review-action` forbids specifying `allow-licenses` and `deny-licenses` together, and fails to block merges unless marked as a required status check on `pull_request`
- **B.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)
- **C.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **D.** No — `.github/secret_scanning.yml` `paths-ignore` only auto-closes post-push user alerts (`<=1,000` paths / `<=1 MB`) and neither revokes keys nor replaces Push Protection / public partner alerts

### 30. AetherNav Aerospace is designing least-privilege Push Protection exception reviewers across its US and EU satellite divisions. Which two platform rules apply when configuring delegated bypass reviewers? Select two.

- **A.** `Review and manage secret scanning bypass requests` (`fine-grained organization role permission for Push Protection delegated bypass`)
- **B.** Assign `Specific roles, visible teams, or custom org roles` (`never secret teams`) to the Push Protection delegated bypass list to review and approve contributor bypass requests
- **C.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **E.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 31. `autopilot-sim-suite` stores 320 mock JWT strings under `sim/testdata/**` and `benchmarks/mock_tokens/**`. Which file and key (`____`) prevents user Secret Protection alerts on those paths, and what happens if a fixture file grows to `1.8 MB`?

- **A.** `.github/codeql/codeql-config.yml` (`defining packs:, queries:, paths-ignore:, and threat-models: alongside YAML model-pack extensions`)
- **B.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)

### 32. After committing a new `.github/secret_scanning.yml` adding `paths-ignore: ["legacy_fixtures/**"]` to `transponder-bus-c`, what happens to the 18 existing open user secret alerts located inside `legacy_fixtures/`?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **C.** `.github/secret_scanning.yml` with `paths-ignore:` (`up to 1,000 glob entries and <= 1 MB file size`) auto-closing user alerts in test/docs paths (`without suppressing public-repo partner revocation alerts`)
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 33. AetherNav Aerospace wants three mission-reliability engineers (`who hold Write access on radhard-hal-sdk`) to receive and view Secret Protection alerts on that single repository without making them Repository Admins or org-wide Security Managers. How should access be granted?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **C.** Separate `Enterprise/Org Owners` (`billing & global policy`), `Security Managers` (`org-wide alert read/write & security config management, without code-write`), and custom repository roles (`granular view/dismiss per tool`)
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 34. AetherNav Aerospace wants to detect internal telemetry signing tokens (`ANAV_SIG_[0-9a-f]{40}`) across all 90 org repositories and uses `Generate with AI` in the custom pattern builder to draft the regex and `before`/`after` context. What step (`____`) is mandatory before `Publish pattern` and Push Protection unlock?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Custom regex patterns (`up to 100/repo or 500/org-or-enterprise`, optional `Generate with AI` & `before`/`after` context) validated via `Save and dry run` (`<=1,000` sample hits) before `Publish pattern` & Push Protection
- **C.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 35. What are the maximum published custom secret pattern quotas at the **repository** level versus the **organization / enterprise** level (`____`), and who can edit an **enterprise-level** custom pattern after creation?

- **A.** Custom regex patterns (`up to 100/repo or 500/org-or-enterprise`, optional `Generate with AI` & `before`/`after` context) validated via `Save and dry run` (`<=1,000` sample hits) before `Publish pattern` & Push Protection
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 36. AetherNav Aerospace is rolling out custom secret patterns for mission command keys across its GHEC organization. Which three technical behaviors should AppSec expect? Select three.

- **A.** Audit every Push Protection bypass request, approval, and exemption via `secret_scanning_push_protection_bypass` audit events, alert timelines, and webhooks
- **B.** Custom regex patterns (`up to 100/repo or 500/org-or-enterprise`, optional `Generate with AI` & `before`/`after` context) validated via `Save and dry run` (`<=1,000` sample hits) before `Publish pattern` & Push Protection
- **C.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **E.** `Push Protection` blocks high-confidence partner and published custom secrets pre-receive during `git push` before commits land on GitHub
- **F.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

---

## Domain 3 — Configure and use supply chain security (formerly Dependabot/Dependency Review) (15–20% official weight · 18 questions)

### 37. `flightdeck-guidance-cpp` resolves C++ Conan and CMake third-party libraries dynamically at compile time in GitHub Actions, leaving the static Dependency Graph empty. Which API (`____`) lets the CI build submit resolved dependency snapshots so Dependabot alerts work?

- **A.** `Dependency Graph` (`parsing committed manifests and lockfiles`, augmented by the `Dependency Submission API` for build-time resolved transitive graphs in Maven/Gradle/C++/containers)
- **B.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **C.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 38. AetherNav Aerospace's defense compliance pipeline archives a signed SBOM on every release tag of `orbital-downlink-go`. Which REST endpoint (`____`) or GitHub Action exports the Dependency Graph in `SPDX` JSON format?

- **A.** `POST /orgs/{org}/code-security/configurations/{configuration_id}/attach` (`attaching a Security Configuration across selected or all org repos via REST`)
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** `codeql github upload-results --repository=<org/repo> --ref=<refs/heads/main> --commit=<sha> --sarif=<results.sarif>`
- **D.** `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`exporting the repository dependency inventory in SPDX JSON format`)

### 39. Why did an internal shared Rust crate (`aethernav-coord-math`) show `0` external consuming apps inside its exported SPDX SBOM even though GitHub's `Insights -> Dependency graph -> Dependents` tab shows 24 internal repos importing it?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** Export an `SPDX` JSON Software Bill of Materials (`SBOM`) via `Insights -> Dependency graph -> Export SBOM`, `GET /repos/{owner}/{repo}/dependency-graph/sbom`, or `actions/attest-sbom` (`excluding dependents`)
- **D.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions

### 40. AetherNav Aerospace wants `mission-planner-ui` to auto-dismiss low-impact `development`-scope alerts silently before Slack/email notifications fire while opening Dependabot PRs **only** when `EPSS >= 0.05` and a patch exists. What is the exact configuration sequence?

- **A.** Enable Dependency Graph & Dependabot alerts → disable global `Dependabot security updates` where custom PR rules govern → create an org/repo auto-triage rule targeting EPSS/severity/scope → audit `resolution:auto-dismiss` & targeted PRs
- **B.** Disable Dependabot alerts completely → keep global Dependabot security updates enabled → create an `Open a pull request` rule for malware alerts → expect dismissed dev alerts never to reopen on runtime promotion
- **C.** Put auto-triage EPSS rules inside .github/secret_scanning.yml → expect repo rules to override enforced org rules → delete audit logs → manually email developers before rules evaluate
- **D.** Export an SPDX SBOM → delete package-lock.json so transitive packages disappear → enable `Dismiss package malware alerts` to block zero-days → skip reachability review

### 41. In `telemetry-ingest-kotlin`, Dependabot displays an alert with `CVSS 7.5 (High)`, `EPSS 0.84`, and `Unreachable` (`0 call paths found in static analysis`), alongside a `CVSS 8.1` alert with `EPSS 0.62` and `Reachable` (`3 call paths shown`). How do `EPSS` and `Reachability` guide triage?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **C.** Prioritize `Dependabot alerts` combining `EPSS` (`30-day exploitation probability`), `CVSS` severity, `Reachability` call-path analysis (`Reachable` vs `Unreachable`), `runtime` scope, and `patch availability`
- **D.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step

### 42. AetherNav Aerospace's vulnerability management lead is standardizing Dependabot auto-triage rules across 90 repositories. Which two platform behaviors govern rule precedence, notifications, and scope changes? Select two.

- **A.** Combine `EPSS` (`30-day exploitation probability`) and static `Reachability` call-path verdicts with `CVSS` severity and `runtime` dependency scope
- **B.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** Use `Dependabot auto-triage rules` to auto-dismiss or snooze low-impact dev/unpatched alerts (`resolution:auto-dismiss`) **before** alert notifications fire
- **E.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions

### 43. An AppSec engineer at AetherNav Aerospace wants to write a Dependabot custom auto-triage rule scoped specifically to `manifest_path: apps/simulator/package-lock.json`. At which level (`repository` vs `organization`) is `manifest` path targeting supported?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** `Dependabot auto-triage rules` (`GitHub presets or custom rules on EPSS/CVE/CWE/scope/patch` setting `resolution:auto-dismiss` before notifications; disable global `Dependabot security updates` for custom PR-trigger rules)
- **D.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions

### 44. `gnss-ephemeris-rust` has `Dependabot security updates` enabled in Settings, yet `Cargo.toml` dependencies without CVEs stay 18 months behind upstream releases. Why, and what fixes this?

- **A.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** `Dependabot security updates` (`alert-driven PRs patching vulnerable versions to the minimum fixed version`) vs `.github/dependabot.yml` `Dependabot version updates` (`scheduled ecosystem/Actions freshness PRs`)
- **D.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step

### 45. How can AetherNav Aerospace drive coordinated multi-squad remediation of high-severity supply-chain and code alerts across 35 avionics microservices with tracked burndown metrics in Security Overview?

- **A.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** `Security Campaigns` (`targeted, time-bound initiatives grouping up to 1,000 default-branch alerts with a named security contact and Copilot Autofix support`)

### 46. AetherNav Aerospace's export-compliance team requires pull requests on private `star-tracker-dsp` to fail automatically if a developer adds a `Moderate+` runtime vulnerability or a `GPL-3.0-only` library. What is the exact implementation sequence?

- **A.** Run `dependency-review-action` on an unlicensed private Free repo → grant `write-all` permissions to untrusted fork code → ignore `fail-on-scopes` → merge failing checks freely
- **B.** Trigger `dependency-review-action` only on weekly cron `schedule` → pass both `allow-licenses` and `deny-licenses` simultaneously → disable the Dependency Graph → leave main unprotected
- **C.** Add SPDX license names to `.github/dependabot.yml` → expect Dependabot version updates to block developer PR merges → skip required status checks → disable lockfiles
- **D.** Enable the Dependency Graph (`and Code Security on private repos`) → add an `on: pull_request` workflow running `actions/dependency-review-action@v4` → configure `fail-on-severity` & `deny-licenses` → mark the check required in a branch ruleset

### 47. Which exact `actions/dependency-review-action@v4` configuration (`____`) blocks `High`/`Critical` vulnerabilities **only** in production `runtime` dependencies (`ignoring dev-only test linters`) while rejecting `AGPL-3.0` licenses?

- **A.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **B.** `actions/dependency-review-action@v4` with `fail-on-severity: high`, `fail-on-scopes: runtime`, and `deny-licenses` (`or allow-licenses`, never both)
- **C.** `.github/codeql/codeql-config.yml` (`defining packs:, queries:, paths-ignore:, and threat-models: alongside YAML model-pack extensions`)
- **D.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step

### 48. Why did a developer on `groundstation-cli` manage to merge a PR introducing a `Critical` CVE even though `.github/workflows/dep-review.yml` ran `actions/dependency-review-action@v4`? Which two controls ensure both detection and merge blocking? Select two.

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** Configure `actions/dependency-review-action@v4` with `fail-on-severity`, `fail-on-scopes`, and either `allow-licenses` OR `deny-licenses` (`SPDX` IDs)
- **C.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **D.** Mark the `Dependency Review` workflow job as a **required status check** in a repository or organization Branch Ruleset targeting `main`
- **E.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions

### 49. `telemetry-ingest-kotlin` pulls internal artifacts from AetherNav's private Maven Nexus registry and wants all `org.springframework.*` minor/patch updates batched into one weekly PR. Which `.github/dependabot.yml` blocks (`____`) configure this?

- **A.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`
- **D.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)

### 50. In `mission-planner-ui`, AetherNav Aerospace wants Dependabot to update `package.json` range specifiers only when a new version falls outside the existing semver range (`rather than rewriting ^1.2.0 on every patch`). Which `.github/dependabot.yml` option (`versioning-strategy: ____`) controls manifest edits?

- **A.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **B.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **C.** Configure `.github/dependabot.yml` with `groups:` (`batching patch/minor updates into single PRs`), `ignore:` (`version/dependency exclusions`), `open-pull-requests-limit`, and `registries:` (`authenticated via Dependabot secrets`)
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 51. AetherNav Aerospace wants `actions/dependency-review-action@v4` on `orbital-downlink-go` to allow `MIT` and `BSD-3-Clause` while explicitly denying `SSPL-1.0`, plus temporarily waiving one vendor advisory `GHSA-9999-aaaa-bbbb`. Proposed solution: Pass `allow-licenses: MIT, BSD-3-Clause`, `deny-licenses: SSPL-1.0`, and `allow-ghsas: GHSA-9999-aaaa-bbbb` in the same step. Does this succeed?

- **A.** No — temporary private forks created inside a Repository Security Advisory (`GHSA`) intentionally **disable GitHub Actions** (`and pushing fixes to a public branch before release leaks the zero-day`)
- **B.** No — CodeQL `Default Setup` and custom `Advanced Setup` (`.github/workflows/codeql.yml`) cannot run active CodeQL management simultaneously (`switch to Advanced Setup with build-mode: manual`)
- **C.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **D.** No — `actions/dependency-review-action` forbids specifying `allow-licenses` and `deny-licenses` together, and fails to block merges unless marked as a required status check on `pull_request`

### 52. AetherNav Aerospace runs self-hosted Linux Actions runners for `radhard-hal-sdk` and wants real-time PagerDuty tickets whenever a `Critical` runtime Dependabot alert opens across any org repository. How should runner security and event automation be configured?

- **A.** Govern Dependabot PR workflows (`read-only GITHUB_TOKEN` & `Dependabot secrets`), fine-grained alert roles, `dependabot_alert` webhooks, and production-context filters (`has:deployment`, `runtime-risk:internet-exposed`)
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 53. After integrating JFrog Artifactory and Microsoft Defender for Cloud with AetherNav Aerospace's GitHub Enterprise org, which Security Overview search query (`____`) filters Dependabot alerts down to artifacts actively deployed to internet-exposed ground gateways?

- **A.** `resolution:auto-dismiss` (`alert filter matching findings automatically dismissed by preset or custom Dependabot auto-triage rules`)
- **B.** `has:deployment runtime-risk:internet-exposed` (`Security Overview and alert search qualifiers powered by ingested deployment metadata`)
- **C.** `queries: security-extended` (`executing default high-precision CodeQL security rules plus medium-precision security queries without style/quality rules`)
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 54. AetherNav Aerospace's CI security architect is auditing `dependabot` pull-request workflows and alert access governance on `orbital-downlink-go`. Which two platform rules apply? Select two.

- **A.** Workflows triggered by `dependabot` PRs receive a **read-only `GITHUB_TOKEN`** by default and access credentials stored in **`Dependabot secrets`** (`not standard Actions secrets on untrusted triggers`)
- **B.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **C.** Govern Dependabot PR workflows (`read-only GITHUB_TOKEN` & `Dependabot secrets`), fine-grained alert roles, `dependabot_alert` webhooks, and production-context filters (`has:deployment`, `runtime-risk:internet-exposed`)
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **E.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

---

## Domain 4 — Configure and use Code Security (formerly Code Scanning with CodeQL) (10–15% official weight · 14 questions)

### 55. AetherNav Aerospace uses `CodeQL` alongside a MISRA-C aerospace verifier (`PC-lint / Polyspace`) that exports `SARIF 2.1.0` on `transponder-bus-c`. Why run both inside GitHub Code Scanning?

- **A.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** `CodeQL` (`compiling/extracting code into a queryable relational AST/CFG/dataflow database`) paired with third-party SAST/IaC/container scanners uploading `SARIF 2.1.0` into unified Code Scanning alerts

### 56. AetherNav Aerospace's MISRA-C scanner generated `19,000` raw `SARIF 2.1.0` findings (`6 MB` gzipped) in a single run on `flightdeck-guidance-cpp`. Will `upload-sarif` accept the file, and how many findings will Code Scanning display?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** `SARIF 2.1.0` ingestion rules: `<= 10 MB` gzip-compressed upload limit, `<= 25,000` results/run (`top 5,000` displayed by severity), `partialFingerprints` deduplication, distinct `category` tags, and `security-events: write`
- **C.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **D.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts

### 57. AetherNav Aerospace uploads SARIF reports from `Clang-Tidy`, `CodeQL`, and `Trivy` in parallel jobs on every commit to `flightdeck-guidance-cpp`. Which two SARIF practices prevent rejected uploads and alert clobbering? Select two.

- **A.** Assign a unique `category` per tool/language/monorepo target and preserve stable `ruleId` + `partialFingerprints` so alerts deduplicate cleanly without overwriting sibling scans
- **B.** Ensure each uploaded `SARIF 2.1.0` file is `<= 10 MB` gzip-compressed and `<= 25,000` results (`knowing GitHub displays only the top 5,000 results prioritized by severity`)
- **C.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **D.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **E.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 58. `radhard-hal-sdk` compiles inside an air-cooled vendor FPGA build appliance using GitLab Runner rather than GitHub Actions, and results must appear in GitHub Code Scanning. What is the exact `CodeQL CLI` workflow?

- **A.** Enable Default Setup simultaneously for the same language/category → upload SARIF with a read-only `contents: read` token → strip `partialFingerprints` → expect >25,000 results to render without truncation
- **B.** Install the CodeQL CLI bundle on the CI agent → run `codeql database create` (`tracing compiled builds`) → run `codeql database analyze --format=sarif-latest` → run `codeql github upload-results` (`--sarif`, `--ref`, `--commit`)
- **C.** Run `codeql github upload-results` on raw `.java` source files → run `codeql database analyze` before `codeql database create` → upload an uncompressed 45 MB XML report → omit `--ref` and `--commit`
- **D.** Create one shared SARIF file without `--sarif-category` across 6 monorepo services → overwrite prior language alerts on every upload → disable GitHub Code Security on private repos → view alerts in Actions cache

### 59. When should AetherNav Aerospace choose CodeQL `Default Setup` (`mission-planner-ui` TypeScript/Python) versus switching to `Advanced Setup` (`flightdeck-guidance-cpp` custom RTOS C++ cross-compile)?

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** `Default Setup` (`zero-YAML automatic language/trigger management`) vs `Advanced Setup` (`.github/workflows/codeql.yml` for custom build steps, `codeql-config.yml`, matrix `build-mode`s, or third-party SARIF—mutually exclusive)
- **D.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts

### 60. AetherNav Aerospace's polyglot repository contains `Python` scripts, a standard `Maven Java` service (`no Kotlin`), and an embedded `C++` module requiring custom `bazel build //avionics/...` flags. How do CodeQL `build-mode` options (`none`, `autobuild`, `manual`) map across these languages?

- **A.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **B.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **C.** CodeQL `build-mode` options: `none` (`JS/TS, Python, Ruby & buildless Java`), `autobuild` (`heuristic compiler detection`), and `manual` (`explicit custom build commands in CI for C/C++, C#, Go, Kotlin, Swift`)
- **D.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)

### 61. On a pull request to `orbital-downlink-go`, CodeQL highlights `Untrusted network packet -> parseHeader() -> exec.Command()` and posts a `Copilot Autofix` comment parameterized safely without shell invocation. How should the developer evaluate the trace and fix?

- **A.** Inspect CodeQL `source -> step -> sink` path-problem dataflow traces and apply `Copilot Autofix` (`enabled by default on CodeQL PRs & default branch without requiring a Copilot seat for classic Autofix`)
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 62. On AetherNav Aerospace's external Jenkins server, `codeql database analyze` just wrote `avionics.sarif` for commit `9f3c12a` on `refs/heads/main`. Which exact `CodeQL CLI` command (`____`) uploads that file using `GITHUB_TOKEN` (`GitHub App or PAT with security_events: write`)?

- **A.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **B.** `POST /orgs/{org}/code-security/configurations/{configuration_id}/attach` (`attaching a Security Configuration across selected or all org repos via REST`)
- **C.** `codeql github upload-results --repository=<org/repo> --ref=<refs/heads/main> --commit=<sha> --sarif=<results.sarif>`
- **D.** `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`exporting the repository dependency inventory in SPDX JSON format`)

### 63. AetherNav Aerospace is rolling out `Advanced Setup` CodeQL PR workflows with `Copilot Autofix` across `telemetry-ingest-kotlin`. Which two workflow permission and review practices are required? Select two.

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** Validate every `Copilot Autofix` suggestion by inspecting dataflow context, running full CI unit/integration tests + re-scanning with `CodeQL`, and completing human PR review
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **E.** `permissions: { security-events: write, contents: read, actions: read }` on `github/codeql-action/upload-sarif@v3`

### 64. `flightdeck-guidance-cpp` compiles two matrix targets (`linux-x86_64` and `vxworks-arm64`) in `.github/workflows/codeql.yml`. Why did alerts specific to `vxworks-arm64` vanish whenever the `linux-x86_64` job finished second until `category: "/language:cpp/target:${{ matrix.os }}"` was added?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **D.** Distinguish `security-severity` (`Critical/High/Medium/Low` mapped from CVSS `0.0–10.0`) from rule `problem.severity` (`error/warning/note`), use `category` per matrix leg, and record audited dismissal reasons

### 65. AetherNav Aerospace wants `telemetry-ingest-kotlin` (`mixed Java + Kotlin`) analyzed without running Gradle builds by leaving `Default Setup` enabled while also committing `.github/workflows/codeql.yml` set to `build-mode: none`. Proposed solution: Run both Default Setup and `codeql.yml` (`build-mode: none`) for Java+Kotlin simultaneously. Does this work?

- **A.** No — CodeQL `Default Setup` and custom `Advanced Setup` (`.github/workflows/codeql.yml`) cannot run active CodeQL management simultaneously (`switch to Advanced Setup with build-mode: manual`)
- **B.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)
- **C.** No — `actions/dependency-review-action` forbids specifying `allow-licenses` and `deny-licenses` together, and fails to block merges unless marked as a required status check on `pull_request`
- **D.** Yes — this configuration satisfies every security, licensing, and governance requirement

### 66. How does CodeQL map numeric `@security-severity` query tags (`0.0–10.0`) into the four security severity labels shown in GitHub Security Overview (`____`)?

- **A.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **B.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Distinguish `security-severity` (`Critical/High/Medium/Low` mapped from CVSS `0.0–10.0`) from rule `problem.severity` (`error/warning/note`), use `category` per matrix leg, and record audited dismissal reasons

### 67. AetherNav Aerospace wraps SQL queries inside an internal Kotlin DAO library (`aero.db.SafeQuery`) and wants CodeQL to recognize its taint-propagating methods and sanitizers across 25 microservices without maintaining forked `.ql` files. Which configuration mechanism (`____`) accomplishes this?

- **A.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **B.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)
- **C.** `.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`
- **D.** `.github/codeql/codeql-config.yml` (`defining packs:, queries:, paths-ignore:, and threat-models: alongside YAML model-pack extensions`)

### 68. On `autopilot-sim-suite`, CodeQL takes 78 minutes because `sim/recorded_flights/` contains 4 GB of auto-generated TypeScript telemetry fixtures. How can AetherNav Aerospace cut scan runtime without disabling CodeQL on real application code?

- **A.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **B.** Customize `.github/codeql/codeql-config.yml` (`paths-ignore`, `packs`, `queries`, `threat-models`) & `CodeQL model packs` (`YAML data extensions`), and fix OOM/slow scans via Larger runners or split language matrices
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage

---

## Domain 5 — Security operations: best practices, prioritization, and remediation (15–20% official weight · 18 questions)

### 69. A university aerospace lab wants to privately report an integer-underflow bug (`CWE-191`) in AetherNav's public `open-rinex-tools` repo without posting a public GitHub Issue. Which repository setting (`____`) enables direct encrypted intake into a draft `GHSA`?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** `CWE` classifies weakness types (`e.g., CWE-89 SQLi`), `CVE` identifies a publicly disclosed vulnerability instance, and `GHSA` (`Repository Security Advisories` + Private Reporting) coordinates private patches & CVEs
- **C.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 70. While patching a critical RCE inside `open-rinex-tools`'s draft `GHSA` temporary private fork (`open-rinex-tools-ghsa-1234`), maintainers notice `.github/workflows/test.yml` never triggers. Proposed solution: Open a pull request from the temporary fork straight to the public `main` branch 5 days before the embargo lifts so public GitHub Actions can test the patch. Does this preserve embargo confidentiality?

- **A.** No — repository-wide `Dependabot security updates` must be **disabled** before a custom Dependabot auto-triage `Open a pull request` rule can selectively control which alerts open PRs
- **B.** No — temporary private forks created inside a Repository Security Advisory (`GHSA`) intentionally **disable GitHub Actions** (`and pushing fixes to a public branch before release leaks the zero-day`)
- **C.** No — Code Scanning rejects gzip-compressed SARIF files larger than `10 MB` (`and overwrites prior alerts when multiple matrix uploads share an identical SARIF category on one commit`)
- **D.** Yes — this configuration satisfies every security, licensing, and governance requirement

### 71. Once AetherNav Aerospace publishes a `GHSA` with affected (`< 2.4.3`) and patched (`2.4.3`) semver metadata and requests a `CVE` through GitHub (`acting as a CVE Numbering Authority`), what happens downstream after GitHub reviews the advisory?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** `CWE` classifies weakness types (`e.g., CWE-89 SQLi`), `CVE` identifies a publicly disclosed vulnerability instance, and `GHSA` (`Repository Security Advisories` + Private Reporting) coordinates private patches & CVEs
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 72. AetherNav Aerospace's Security Overview shows 900 open findings across retired prototype repos and active satellite uplinks alike. How should AppSec combine runtime prioritization and pre-merge gating so engineers fix live risk first while stopping backlog growth?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Prioritize using `has:deployment` + `runtime-risk:internet-exposed` (`Defender for Cloud / artifact registries`), `EPSS`, and `Reachability`, while blocking new regressions via `Require code scanning results` rulesets
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect

### 73. Which exact Security Overview filter expression (`____`) narrows AetherNav Aerospace's alert queue down to vulnerabilities running in deployed, internet-reachable ground-control workloads?

- **A.** `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`exporting the repository dependency inventory in SPDX JSON format`)
- **B.** `has:deployment runtime-risk:internet-exposed` (`Security Overview and alert search qualifiers powered by ingested deployment metadata`)
- **C.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **D.** `resolution:auto-dismiss` (`alert filter matching findings automatically dismissed by preset or custom Dependabot auto-triage rules`)

### 74. AetherNav Aerospace wants to introduce an organization-wide `Require code scanning results` ruleset across 65 avionics repos without unexpectedly freezing release branches, while prioritizing active orbital services. Which two steps accomplish this? Select two.

- **A.** Pilot cross-repository `Rulesets` in **`Evaluate` mode** to measure would-be blocked PRs via Ruleset Insights before switching enforcement to **`Active`**
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **D.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **E.** Ingest deployment metadata (`from Microsoft Defender for Cloud, JFrog Artifactory, or CI/CD APIs`) to filter `has:deployment` and `runtime-risk:internet-exposed` alerts

### 75. AetherNav Aerospace's AppSec team wants to remediate 240 default-branch `CWE-22` path-traversal and `CWE-78` command-injection alerts across 15 ground-station services before a defense audit. What is the end-to-end Security Campaign execution flow?

- **A.** Create a campaign containing 50,000 unmerged fork-branch alerts with no contact owner → auto-merge Copilot suggestions bypassing CI tests → revoke developer write access → close the campaign with alerts still open
- **B.** Assign 500 alerts in one batch to `@copilot` without AI credits or branch protection → skip human PR review → disable Security Overview → expect secret campaigns to auto-rotate AWS IAM keys
- **C.** Export alerts to a static spreadsheet with no GitHub links → disable CodeQL so open counts fall to zero → bulk-dismiss every alert without comments → report 100% remediation
- **D.** Filter high-risk default-branch alerts in Security Overview → create a Security Campaign (`<=1,000` alerts) with due date & contact → trigger Copilot Autofix (`or assign <=25 alerts to @copilot`) → verify CI checks & track burndown

### 76. What happens to alert access when an AetherNav Security Manager creates a **Secret scanning campaign** and assigns specific leaked-token alerts to repository `Write` developers who do not normally have Secret Protection view permissions?

- **A.** Run `Security Campaigns` (`<=1,000` default-branch alerts, named security lead, developer notifications, Copilot Autofix, or assigning `<=25` alerts per batch to `@copilot` cloud agent) with audited dismissal comments
- **B.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **C.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 77. During a Security Campaign review on `orbital-downlink-go`, a squad lead wants to bulk-close 12 alerts inside `cmd/mock-uplink-test/` as `Used in tests`. What documentation rule should AppSec enforce?

- **A.** Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions
- **B.** Dismissing an alert requires a structured closure reason (`False positive`, `Used in tests`, `Won't fix`) plus an audit-logged justification comment—and never deletes commits or revokes keys
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 78. AetherNav Aerospace classifies `flightdeck-guidance-cpp` as DAL-A safety-critical and wants broader CodeQL security detection (`including lower-confidence taint queries`) without flooding PRs with code-smell formatting notes. Which CodeQL query suite (`____`) fits best?

- **A.** `queries: security-extended` (`executing default high-precision CodeQL security rules plus medium-precision security queries without style/quality rules`)
- **B.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage
- **C.** `resolution:auto-dismiss` (`alert filter matching findings automatically dismissed by preset or custom Dependabot auto-triage rules`)
- **D.** `.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)

### 79. AetherNav Aerospace discovered an unsafe custom ASN.1 parser pattern in `transponder-bus-c` and wants to hunt for identical AST patterns across all 90 C/C++ and Go org repositories from VS Code. How does `Multi-Repository Variant Analysis (MRVA)` execute this at scale?

- **A.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **B.** Select CodeQL query suites (`default` high-precision, `security-extended` broader lower-confidence security, `security-and-quality` adds maintainability) and run `Multi-Repository Variant Analysis (MRVA)` in VS Code
- **C.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **D.** Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage

### 80. Why should AetherNav Aerospace assign `default` CodeQL queries to internal hackathon sandboxes, `security-extended` to internet-facing ground APIs, and `security-and-quality` only to greenfield SDK repos requesting code-hygiene lints?

- **A.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **B.** Select CodeQL query suites (`default` high-precision, `security-extended` broader lower-confidence security, `security-and-quality` adds maintainability) and run `Multi-Repository Variant Analysis (MRVA)` in VS Code
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect

### 81. How can AetherNav Aerospace allow avionics tech leads to dismiss verified false-positive Code Scanning alerts on their squad's repositories while preventing junior contractors (`Write`) from dismissing alerts?

- **A.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **B.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **C.** Assign `Security Manager` org roles, custom repository alert roles, and per-alert `Assignees` (`noting secret-alert assignment temporarily elevates single-alert view access for repo writers until unassigned`)
- **D.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners

### 82. An avionics release manager used emergency ruleset bypass permissions during a live orbital window on `orbital-downlink-go`. Where can AetherNav Aerospace's compliance team inspect every ruleset and Push Protection bypass across the organization?

- **A.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **B.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **C.** Enforce Enterprise Advanced Security policies (`restricting repo admins while preserving Org Owner/Security Manager control`), scope ruleset/push-protection bypass actors, and stream `security_configuration.*` / alert audit logs
- **D.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

### 83. AetherNav Aerospace is codifying collaborative exception handling between its central AppSec team and 12 flight-software squads. Which two controls preserve engineering velocity without losing security accountability? Select two.

- **A.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **B.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **C.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **D.** Assign `Security Manager` org roles, custom repository alert roles, and per-alert `Assignees` (`noting secret-alert assignment temporarily elevates single-alert view access for repo writers until unassigned`)
- **E.** `Delegated bypass for push protection` (`granting Specific roles, visible teams, or custom roles with "Review and manage secret scanning bypass requests" authority—never secret teams`)

### 84. Which three-stage developer feedback loop gives AetherNav Aerospace engineers pre-merge protection across secrets, third-party dependencies, and custom C++/Go source code?

- **A.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** Layer `Push Protection` (`pre-receive`), `actions/dependency-review-action` (`PR manifest/license gate`), and `CodeQL` PR checks (`with Copilot Autofix`) so secrets, vulnerable packages, and taint flaws fail pre-merge
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 85. Why is blocking a Space-Track API secret via Push Protection during `git push` dramatically safer than catching the same secret 90 seconds later via a post-push GitHub Actions scanner?

- **A.** Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config
- **B.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **C.** `Push Protection` intercepts supported high-confidence and published custom secrets pre-receive during `git push` (`CLI, IDE, web editor & REST API`), blocking the secret from entering Git history
- **D.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe

### 86. AetherNav Aerospace's CISO wants every new microservice repository born with automated preventive guardrails across Secret Protection, Supply Chain Security, and Code Security. Which three practices belong in that blueprint? Select three.

- **A.** Configure `actions/dependency-review-action@v4` with `fail-on-severity`, `fail-on-scopes`, and either `allow-licenses` OR `deny-licenses` (`SPDX` IDs)
- **B.** Validate every `Copilot Autofix` suggestion by inspecting dataflow context, running full CI unit/integration tests + re-scanning with `CodeQL`, and completing human PR review
- **C.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **D.** `Push Protection` blocks high-confidence partner and published custom secrets pre-receive during `git push` before commits land on GitHub
- **E.** Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step
- **F.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically

---

## Domain 6 — GitHub Security suites administration (10–15% official weight · 14 questions)

### 87. AetherNav Aerospace is onboarding 150 repositories across three organizations onto standardized Secret Protection, Dependabot, and CodeQL policies. In which sequence should Enterprise/Org administrators execute the rollout?

- **A.** Verify committer license headroom (`or metered budget`) → create/select a Security Configuration → attach to tiered repos (`custom properties`) & enable `Apply to new repositories` → set `Enforced` to lock baseline controls
- **B.** Apply an `Enforced` configuration across 2,000 private repos with zero available committer seats → set every feature to `Not set` expecting strict locks → leave new repositories uncovered → disable audit logs
- **C.** Enable cloud-only Copilot Autofix on an air-gapped GHES instance with metered billing → skip GitHub Connect → expect transferred external repos to inherit new-repo defaults automatically without policy checks
- **D.** Manually toggle Settings on 2,000 repositories one by one → grant every developer Organization Owner permissions → disable Push Protection globally → rely on `.gitignore` for enterprise governance

### 88. AetherNav Aerospace runs classified propulsion code on `GitHub Enterprise Server (GHES)` alongside commercial satcom repos on `GitHub Enterprise Cloud (GHEC)`. Why should administrators enable `GitHub Connect` between `GHES` and `GHEC`?

- **A.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **B.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** Roll out org/enterprise `Security Configurations` (`GitHub-recommended` or custom, `Apply to new repositories`), contrasting `GHEC` (`metered or volume + cloud AI features`) with `GHES` (`volume-only + GitHub Connect Advisory sync`)

### 89. What is the difference between attaching GitHub's built-in `GitHub-recommended` Security Configuration versus creating a **custom** Security Configuration at AetherNav Aerospace?

- **A.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **B.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **C.** Roll out org/enterprise `Security Configurations` (`GitHub-recommended` or custom, `Apply to new repositories`), contrasting `GHEC` (`metered or volume + cloud AI features`) with `GHES` (`volume-only + GitHub Connect Advisory sync`)
- **D.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners

### 90. AetherNav Aerospace purchased a fixed volume pool of `150` `GitHub Secret Protection` seats, and all `150` seats are currently consumed (`100%` utilization), while `Apply to new repositories` is enabled on its Security Configuration. What happens when an engineer creates a brand-new private repository today?

- **A.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **B.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **C.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **D.** `Enforced` Security Configurations lock enabled/disabled settings (`except fields set to "Not set"`), while private/internal repos consume `90-day unique active committer` seats (`plus metered AI credits for AI Scan/generic secrets`)

### 91. AetherNav Aerospace wants repository admins on `mission-planner-ui` prevented from turning off `Private vulnerability reporting` or enabling `Dependabot security updates`, using an `Enforced` Security Configuration. Proposed solution: Set both rows to `"Not set"` inside the `Enforced` Security Configuration. Does this lock repository admins out of changing them?

- **A.** No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)
- **B.** Yes — this configuration satisfies every security, licensing, and governance requirement
- **C.** No — repository-wide `Dependabot security updates` must be **disabled** before a custom Dependabot auto-triage `Open a pull request` rule can selectively control which alerts open PRs
- **D.** No — temporary private forks created inside a Repository Security Advisory (`GHSA`) intentionally **disable GitHub Actions** (`and pushing fixes to a public branch before release leaks the zero-day`)

### 92. AetherNav Aerospace's IT Finance director is reviewing monthly invoices for `GitHub Code Security` and `GitHub Secret Protection` on GHEC. Which two billing mechanics govern active-committer seats and AI credit consumption? Select two.

- **A.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **B.** Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses
- **C.** Monitor `Code Security AI credits` (`AI Scan / agentic autofix`) and `Secret Protection AI credits` (`AI push scanning`), setting **hard metered budgets** to cap spend
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **E.** Count `90-day unique active committers` across private/internal repos (`deduplicating each human user once across the enterprise, plus GitHub Connect sync between GHEC and GHES`)

### 93. AetherNav Aerospace's Enterprise Owner sets `Repository administrators can enable or disable GitHub Code Security = Disabled` at the enterprise policy level. Who **retains** permission to attach Security Configurations across org repositories, and what happens to currently enabled repos?

- **A.** Enforce Enterprise Advanced Security policies (`restricting repo admins while preserving Org Owner/Security Manager control`), scope ruleset/push-protection bypass actors, and stream `security_configuration.*` / alert audit logs
- **B.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **C.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 94. Which audit log event prefixes (`____`) should AetherNav Aerospace's SIEM team alert on in Microsoft Sentinel to detect unauthorized detachment of Security Configurations or emergency Push Protection bypasses?

- **A.** Enforce Enterprise Advanced Security policies (`restricting repo admins while preserving Org Owner/Security Manager control`), scope ruleset/push-protection bypass actors, and stream `security_configuration.*` / alert audit logs
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically
- **D.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous

### 95. When an engineer leaves AetherNav Aerospace and is removed from the GitHub Enterprise organization, how quickly does the `GitHub Code Security` committer seat they consumed on `orbital-downlink-go` free up?

- **A.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **B.** Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners
- **C.** `Enforced` Security Configurations lock enabled/disabled settings (`except fields set to "Not set"`), while private/internal repos consume `90-day unique active committer` seats (`plus metered AI credits for AI Scan/generic secrets`)
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library

### 96. AetherNav Aerospace wants its 5-person Central AppSec team (`@aethernav/appsec`) to view Security Overview, run Security Campaigns, and manage Security Configurations across all 65 repositories in `aethernav-satcom`, without granting code-push or billing rights. Which org role (`____`) should be assigned to `@aethernav/appsec`?

- **A.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **B.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **C.** Separate `Enterprise/Org Owners` (`billing & global policy`), `Security Managers` (`org-wide alert read/write & security config management, without code-write`), and custom repository roles (`granular view/dismiss per tool`)
- **D.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats

### 97. How many custom repository roles can AetherNav Aerospace define on GitHub Enterprise Cloud, and which base role should a read-only external AS9100 compliance assessor inherit to inspect Dependabot and Code Scanning alerts?

- **A.** Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats
- **B.** Dismiss the alert as `Won't fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe
- **C.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **D.** Separate `Enterprise/Org Owners` (`billing & global policy`), `Security Managers` (`org-wide alert read/write & security config management, without code-write`), and custom repository roles (`granular view/dismiss per tool`)

### 98. AetherNav Aerospace wants two duty officers in Europe to approve urgent Push Protection bypass requests across `aethernav-satcom` without granting full `Security Manager` access to manage Security Configurations. Which custom organization role permission (`____`) achieves this?

- **A.** `permissions: { security-events: write, contents: read, actions: read }` on `github/codeql-action/upload-sarif@v3`
- **B.** Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous
- **C.** Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations
- **D.** `Review and manage secret scanning bypass requests` (`fine-grained organization role permission for Push Protection delegated bypass`)

### 99. AetherNav Aerospace wants an organization-wide branch ruleset blocking pull requests with `High` or `Critical` CodeQL findings across 65 avionics repos without causing day-one deadlocks on repos missing workflows. What is the safe rollout sequence?

- **A.** Set an Org Ruleset to `Active` requiring `CodeQL` results before enabling CodeQL on any repo → grant `All repository writers` bypass access → set thresholds to `Note` style warnings → disable PR scans
- **B.** Disable `pull_request` triggers in `codeql.yml` so scans run only monthly on `main` → enforce `Require code scanning results` on feature PRs → expect instant green PR gates
- **C.** Standardize CodeQL across target repos → create an Org Branch Ruleset in `Evaluate` mode with `Require code scanning results` (`High+` security severity) → audit Evaluate insights & scope bypass actors → switch enforcement to `Active`
- **D.** Configure branch protection individually in `.github/secret_scanning.yml` → allow Copilot Autofix comments to count as human PR approvals → skip `Evaluate` mode → delete Security Manager access

### 100. AetherNav Aerospace's platform engineering team automates repository onboarding in Go and enforces tamper-proof CodeQL checks across custom C++ builds. Which two governance and API mechanisms support this architecture? Select two.

- **A.** `POST /orgs/{org}/code-security/configurations/{configuration_id}/attach` (`attaching a Security Configuration across selected or all org repos via REST`)
- **B.** Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts
- **C.** Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect
- **D.** Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library
- **E.** Enforce approved CodeQL scanning via Org/Enterprise `Rulesets` (`Require code scanning results` + Required Workflows) and automate governance via REST/GraphQL (`code-security/configurations`, org alert endpoints & billing APIs)

---

## Answer Key and Explanations

### Question 1 — `A` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: A (is correct). GitHub offers standalone `GitHub Code Security` and `GitHub Secret Protection` SKUs on both GitHub Team and GitHub Enterprise, allowing organizations to license either SKU independently or together per 90-day active committer. [Skill 1.1: Describe GitHub Security suite structure, navigation, and contrast Code Security, Secret Protection, and Supply Chain Security | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)]

- **A:** Correct. GitHub offers standalone Secret Protection and Code Security products on both GitHub Team and GitHub Enterprise, billed by unique 90-day active committers on private/internal repos
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **D:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)

### Question 2 — `D` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: D (is correct). Secret Protection guards against leaked keys/tokens, Code Security (`CodeQL`/SARIF + Copilot Autofix) detects source-code defects like buffer overflows, and Supply Chain Security governs third-party Go/Maven/npm vulnerabilities and licenses. [Skill 1.1: Describe GitHub Security suite structure, navigation, and contrast Code Security, Secret Protection, and Supply Chain Security | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Correct. each pillar targets a distinct risk surface: leaked credentials, first-party source vulnerabilities, and third-party open-source dependency/license exposure

### Question 3 — `D, E` (Describe GitHub Security suites, features, and ecosystem)

Correct answers: D and E (are correct). `GitHub Secret Protection` covers secret scanning, Push Protection, validity checks, custom patterns, and AI generic secret detection, whereas `GitHub Code Security` covers CodeQL/SARIF scanning, Copilot Autofix, private-repo Dependency Review, and Security Campaigns. [Skill 1.1: Describe GitHub Security suite structure, navigation, and contrast Code Security, Secret Protection, and Supply Chain Security | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Correct. Secret Protection focuses specifically on credential exposure in pushes and Git history
- **E:** Correct. Code Security covers first-party SAST, Copilot Autofix, and private-repository Dependency Review enforcement

### Question 4 — `A` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: A (is correct). Public GitHub.com repositories receive core secret scanning, Push Protection, Dependency Graph, Dependabot, CodeQL default setup, and Dependency Review free of charge, whereas private/internal repositories require licensed SKUs for advanced Secret Protection and Code Security features. [Skill 1.2: Differentiate security feature availability for public repositories vs. enterprise environments and explain Security Overview | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-overview/about-security-overview)]

- **A:** Correct. GitHub provides core security scanning free to open-source public repositories on GitHub.com while requiring Secret Protection / Code Security licenses for advanced private/internal repo coverage
- **B:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers

### Question 5 — `D` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: D (is correct). Organization and Enterprise `Security Overview` provides `Risk`, `Coverage`, `Campaigns`, and tool-level dashboards filterable by repository custom properties, teams, and topics. [Skill 1.2: Differentiate security feature availability for public repositories vs. enterprise environments and explain Security Overview | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-overview/about-security-overview)]

- **A:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **B:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **C:** Incorrect. codeql-config.yml centralizes custom query packs, path exclusions, threat models, and data-extension model packs for Advanced Setup
- **D:** Correct. Security Overview aggregates posture, enablement gaps, alert trends, and campaign burndown across hundreds of repositories from a single org/enterprise plane

### Question 6 — `D` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: D (is correct). Running an organization `free security risk assessment` in Security Overview scans private repositories for leaked secrets and analyzes up to 20 active repositories with CodeQL and Copilot Autofix previews. [Skill 1.2: Differentiate security feature availability for public repositories vs. enterprise environments and explain Security Overview | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-overview/about-security-overview)]

- **A:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **B:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **C:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **D:** Correct. organizations on GitHub Team or Enterprise can run free secret and code risk assessments before purchasing full rollout licenses

### Question 7 — `D` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: D (is correct). Secret Protection matches token patterns and entropy across text/history/pushes regardless of programming language, while CodeQL constructs a semantic AST/CFG/dataflow database to trace untrusted input sources to vulnerable code sinks. [Skill 1.3: Explain differences and interplay between Secret Protection and Code Security across an end-to-end secure SDLC | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Correct. Secret Protection catches leaked tokens in any text/config file at push time, while CodeQL models how untrusted inputs or hardcoded values flow into sensitive code sinks

### Question 8 — `A` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: A (is correct). Layer pre-receive `Push Protection`, PR `actions/dependency-review-action@v4`, and PR `CodeQL`/SARIF checks (`with Copilot Autofix`) enforced as required ruleset gates prior to merge. [Skill 1.3: Explain differences and interplay between Secret Protection and Code Security across an end-to-end secure SDLC | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Correct. combining all three shift-left controls prevents new security debt from ever landing on the default branch
- **B:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`

### Question 9 — `D` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: D (is correct). Enabling Push Protection intercepts secrets pre-receive before Git history updates, while CodeQL Default Setup plus an enforced ruleset blocks pull-request code vulnerabilities pre-merge. [Skill 1.3: Explain differences and interplay between Secret Protection and Code Security across an end-to-end secure SDLC | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Incorrect. alert dismissal only updates GitHub UI/API triage status; attackers can still extract unrotated keys from earlier commits, clones, or reflogs
- **B:** Incorrect. enabling Advanced Setup disables Default Setup so custom workflow build steps, codeql-config.yml, or custom query suites govern scanning cleanly without duplicate conflicts
- **C:** Incorrect. secret_scanning.yml suppresses user notifications in excluded folders rather than blocking pushes or cancelling public-repo partner revocations
- **D:** Correct. every required GitHub Security suite setting, permission boundary, and enforcement rule is properly configured

### Question 10 — `B` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: B (is correct). Block leaked secrets pre-receive via Push Protection, evaluate PR dependencies and code with Dependency Review and CodeQL, apply Copilot Autofix or package patches before merge, and monitor post-merge advisories in Security Overview. [Skill 1.4: Compare prevention-first approaches vs. gate-based security strategies and explain security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/security-at-scale/about-security-campaigns)]

- **A:** Incorrect. Copilot Autofix requires an upstream CodeQL finding first, and Push Protection intercepts secrets during git push rather than post-merge
- **B:** Correct. a prevention-first secure SDLC stops secrets at git push, blocks vulnerable PR code/dependencies with pre-merge checks and Autofix, and continuously monitors post-merge advisories
- **C:** Incorrect. deferring secret and code checks until after merge exposes live credentials in Git history and turns security into high-cost reactive firefighting
- **D:** Incorrect. auto-dismissing unreviewed PR findings defeats shift-left prevention, and .gitignore never revokes already-exposed credentials

### Question 11 — `B` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: B (is correct). Late release-gate discovery forces Git history scrubbing, multi-branch backports, and emergency credential rotations after defects have already propagated across downstream branches. [Skill 1.4: Compare prevention-first approaches vs. gate-based security strategies and explain security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/security-at-scale/about-security-campaigns)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Correct. shifting detection to git push and pull requests prevents secret sprawl and vulnerable merges before release cutoffs
- **C:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 12 — `A` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: A (is correct). `Security Campaigns` group up to 1,000 default-branch alerts with a due date, named security lead, developer notifications, and Copilot Autofix support. [Skill 1.4: Compare prevention-first approaches vs. gate-based security strategies and explain security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/security-at-scale/about-security-campaigns)]

- **A:** Correct. Security Campaigns turn overwhelming alert backlogs into manageable, developer-friendly remediation sprints with clear ownership
- **B:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **C:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 13 — `A` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: A (is correct). GitHub records the actor, timestamp, closure reason (`False positive`, `Used in tests`, `Won't fix`), and justification comment across the alert timeline, REST/GraphQL APIs, webhooks, and audit logs—without modifying Git commits. [Skill 1.5: Identify vulnerability and secret detection mechanisms, act on alerts, and govern ignoring or dismissing alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/vulnerability-exposure)]

- **A:** Correct. alert dismissals remain visible in REST/GraphQL APIs, webhooks, and audit logs, so teams must document rationale rather than hiding unverified risk
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions

### Question 14 — `B` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: B (is correct). Neither dismissing the alert nor updating `.gitignore` revokes the compromised SSH key or purges historical Git commits where the key remains readable. [Skill 1.5: Identify vulnerability and secret detection mechanisms, act on alerts, and govern ignoring or dismissing alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/vulnerability-exposure)]

- **A:** Incorrect. validate advisory patches locally or in an isolated private mirror without exposing exploit diffs publicly before publishing the coordinated GHSA release
- **B:** Correct. alert dismissal only updates GitHub UI/API triage status; attackers can still extract unrotated keys from earlier commits, clones, or reflogs
- **C:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. Neither dismissing the alert nor updating `.gitignore` revokes the compromised SSH key or purges historical Git commits where the key remains readable.
- **D:** Incorrect. when global Dependabot security updates remain enabled, Dependabot attempts PRs for every patchable alert, overriding selective custom PR auto-triage rules

### Question 15 — `A, B` (Describe GitHub Security suites, features, and ecosystem)

Correct answers: A and B (are correct). Enforce structured dismissal reasons paired with mandatory written comments, and audit dismissal events continuously via Security Overview, `code_scanning_alert`/`secret_scanning_alert` webhooks, REST APIs, and audit logs. [Skill 1.5: Identify vulnerability and secret detection mechanisms, act on alerts, and govern ignoring or dismissing alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/vulnerability-exposure)]

- **A:** Correct. structured dismissal reasons and comments create an auditable compliance trail in webhooks and GraphQL/REST APIs
- **B:** Correct. Security Overview and org audit logs surface anomalous dismissal spikes or unpatched high-risk repositories
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **E:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 16 — `B` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: B (is correct). Enterprise/Org Administrators govern billing and Security Configurations, Security Managers oversee Security Overview, campaigns, and policies, and Developers remediate PR and campaign alerts in source code. [Skill 1.6: Describe developer, security, and admin responsibilities, alert access management, delegated bypass, and supply chain security concepts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)]

- **A:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **B:** Correct. effective DevSecOps distributes enablement, posture prioritization, and code-level patching cleanly across Admin, AppSec, and Developer roles
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers

### Question 17 — `A` (Describe GitHub Security suites, features, and ecosystem)

Correct answer: A (is correct). Raw secret alerts expose live credential strings, and delegated bypass ensures any developer requesting to push a flagged token receives documented review from an authorized security group. [Skill 1.6: Describe developer, security, and admin responsibilities, alert access management, delegated bypass, and supply chain security concepts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)]

- **A:** Correct. restricting sensitive secret/vulnerability details and routing bypass requests through designated security reviewers preserves accountability without halting urgent releases
- **B:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 18 — `B, D, F` (Describe GitHub Security suites, features, and ecosystem)

Correct answers: B, D, and F (are correct). Separating Admin/Security Manager/Developer responsibilities, routing Push Protection exceptions through delegated bypass reviewers, and exporting `SPDX` JSON SBOMs via Dependency Graph UI/REST/`actions/attest-sbom` fulfill all three requirements. [Skill 1.6: Describe developer, security, and admin responsibilities, alert access management, delegated bypass, and supply chain security concepts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Correct. GitHub exports dependency inventories, versions, licenses, and transitive relationships in standard SPDX JSON (and never includes downstream external dependents)
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Correct. effective DevSecOps distributes enablement, posture prioritization, and code-level patching cleanly across Admin, AppSec, and Developer roles
- **E:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **F:** Correct. restricting sensitive secret/vulnerability details and routing bypass requests through designated security reviewers preserves accountability without halting urgent releases

### Question 19 — `B` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: B (is correct). Applying an Organization Security Configuration (`GitHub-recommended` or custom) with `Apply to new repositories` enabled activates Secret Protection and Push Protection consistently across existing and new repositories. [Skill 2.1: Enable and configure GitHub Secret Protection at repository and organization levels and contrast public vs. private/enterprise behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Correct. Security Configurations scale Secret Protection across existing and newly created repositories consistently, while single-repo toggles suit isolated pilots
- **C:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 20 — `B` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: B (is correct). On public repositories, partner scanning runs free and notifies the token partner (`here GitHub immediately revokes leaked GitHub tokens`), whereas private-repository secret scanning creates internal org/repo alerts (`plus optional partner validity checks`). [Skill 2.1: Enable and configure GitHub Secret Protection at repository and organization levels and contrast public vs. private/enterprise behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Correct. partner notification automatically reports exposed public-repo tokens to the issuing cloud/SaaS vendor, whereas private-repo findings stay internal unless validity checks query the provider
- **C:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 21 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). Running the free organization secret risk assessment in Security Overview scans private repositories for leaked partner secrets and reports exposure counts prior to full Secret Protection purchase. [Skill 2.1: Enable and configure GitHub Secret Protection at repository and organization levels and contrast public vs. private/enterprise behavior | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning)]

- **A:** Correct. organizations on GitHub Team or Enterprise can run free secret and code risk assessments before purchasing full rollout licenses
- **B:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **C:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **D:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions

### Question 22 — `C` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: C (is correct). Push Protection intercepts high-confidence secrets across `git push` CLI, IDEs, the GitHub web editor, and REST file-commit APIs before commits enter Git history. [Skill 2.2: Prevent secret exposure using Push Protection, validity checks, and prioritized high-confidence or generic secret detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **C:** Correct. blocking leaked credentials before the remote ref updates avoids costly key rotation, incident response, and Git history rewrites
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 23 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). Partner validity checks display `Active`, `Inactive`, or `Unknown`, whereas non-provider patterns (`like standalone PEM RSA private keys or generic DB URLs`) have no central SaaS vendor endpoint for GitHub to query. [Skill 2.2: Prevent secret exposure using Push Protection, validity checks, and prioritized high-confidence or generic secret detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection)]

- **A:** Correct. knowing a leaked AWS, Stripe, or Slack token is still Active lets incident responders triage live compromises ahead of already-revoked tokens
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement

### Question 24 — `D, E` (Configure and use Secret Protection (formerly secret scanning))

Correct answers: D and E (are correct). Push Protection blocks high-confidence partner/published custom secrets pre-receive, while non-provider pattern scanning plus Copilot AI generic secret push detection (`using Secret Protection AI credits`) catches unstructured passwords and connection strings. [Skill 2.2: Prevent secret exposure using Push Protection, validity checks, and prioritized high-confidence or generic secret detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **D:** Correct. stopping secrets pre-receive prevents Git history contamination and emergency credential rotation
- **E:** Correct. enabling non-provider and AI generic secret detection catches unstructured passwords and connection strings missed by vendor-prefix regexes (noting non-provider patterns lack partner validity checks)

### Question 25 — `D` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: D (is correct). Verify alert details and blast radius, immediately revoke and rotate the IAM key in AWS, purge commit history (`git filter-repo` and GitHub Support PR cache purge if needed), and mark the alert `Revoked`. [Skill 2.3: Manage the Secret Protection alert lifecycle, apply secret remediation actions, and govern alert dismissals | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts)]

- **A:** Incorrect. deleting a secret in a follow-up commit leaves the active credential exposed in prior Git commits, reflogs, and clones without revoking access
- **B:** Incorrect. delaying credential revocation leaves attackers able to exploit copies harvested from webhooks, clones, or cached diffs while history is rewritten
- **C:** Incorrect. using secret_scanning.yml to silence an active production credential leak hides the alert without revoking or rotating the compromised secret
- **D:** Correct. once a secret reaches Git history, revoking/rotating the live key comes first, followed by history rewrite/cache purge and marking the alert Revoked for auditability

### Question 26 — `B` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: B (is correct). Rewriting branch refs does not immediately evict cached pull-request commit views on GitHub; administrators must delete sensitive PR refs or contact GitHub Support to purge cached unreachable Git objects, even though token revocation already neutralized live access. [Skill 2.3: Manage the Secret Protection alert lifecycle, apply secret remediation actions, and govern alert dismissals | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Correct. merely deleting a secret in a later commit leaves it readable in earlier commits; immediate revocation and rotation is mandatory
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 27 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). Select `False positive` (`or Used in tests` for test fixtures) with an audit comment for non-live sample strings, and select `Revoked` once a real credential has been invalidated and rotated. [Skill 2.3: Manage the Secret Protection alert lifecycle, apply secret remediation actions, and govern alert dismissals | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts)]

- **A:** Correct. alert dismissals remain visible in REST/GraphQL APIs, webhooks, and audit logs, so teams must document rationale rather than hiding unverified risk
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement

### Question 28 — `C` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: C (is correct). By default any user with push (`Write`) access can self-bypass Push Protection after selecting a reason; enabling `Delegated bypass` removes writer self-bypass and forces requests through designated approver roles or visible teams. [Skill 2.4: Configure role-based and delegated bypass policies in Secret Protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **C:** Correct. delegated bypass replaces ad-hoc writer self-bypasses with a structured request-and-approval workflow audited via webhooks and logs
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 29 — `D` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: D (is correct). `.github/secret_scanning.yml` only defines `paths-ignore` exclusions for post-receive user alerts; enforcing approver-gated push blocks requires enabling Push Protection and configuring a visible team or role under `Delegated bypass`. [Skill 2.4: Configure role-based and delegated bypass policies in Secret Protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection)]

- **A:** Incorrect. allow-licenses and deny-licenses are mutually exclusive inputs in dependency-review-action, and branch rulesets must require the check to block merging
- **B:** Incorrect. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories
- **C:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. `.github/secret_scanning.yml` only defines `paths-ignore` exclusions for post-receive user alerts; enforcing approver-gated push blocks requires enabling Push Protection and configuring a visible team or role under `Delegated bypass`.
- **D:** Correct. secret_scanning.yml suppresses user notifications in excluded folders rather than blocking pushes or cancelling public-repo partner revocations

### Question 30 — `A, B` (Configure and use Secret Protection (formerly secret scanning))

Correct answers: A and B (are correct). Bypass lists accept visible organization teams, standard admin/maintain roles, or custom roles (`never secret teams`), and custom org roles can be scoped specifically with `Review and manage secret scanning bypass requests`. [Skill 2.4: Configure role-based and delegated bypass policies in Secret Protection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection)]

- **A:** Correct. granting Review and manage secret scanning bypass requests creates least-privilege Push Protection approvers without full Org Owner access
- **B:** Correct. delegated bypass centralizes exception approvals in visible accountable security teams or roles
- **C:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **E:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 31 — `D` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: D (is correct). Defining `paths-ignore:` (`<= 1,000` globs, file `<= 1 MB`) in `.github/secret_scanning.yml` suppresses user alerts in matched paths, though Secret Protection ignores `secret_scanning.yml` rules for target files larger than `1 MB` (`or if secret_scanning.yml itself exceeds 1 MB`). [Skill 2.5: Configure Secret Protection alert recipients and path exclusions (.github/secret_scanning.yml) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning)]

- **A:** Incorrect. codeql-config.yml centralizes custom query packs, path exclusions, threat models, and data-extension model packs for Advanced Setup
- **B:** Incorrect. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Correct. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories

### Question 32 — `C` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: C (is correct). GitHub automatically resolves/closes existing open user secret alerts in paths newly matched by `paths-ignore` in `.github/secret_scanning.yml` as excluded by configuration. [Skill 2.5: Configure Secret Protection alert recipients and path exclusions (.github/secret_scanning.yml) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **C:** Correct. secret_scanning.yml silences noisy user alerts in synthetic fixture directories up to 1,000 paths / 1 MB while keeping real code paths protected
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 33 — `C` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: C (is correct). Create a custom repository role inheriting `Write` and add the fine-grained `View secret scanning alerts` (`and optionally Dismiss/resolve secret scanning alerts`) permission on `radhard-hal-sdk`. [Skill 2.5: Configure Secret Protection alert recipients and path exclusions (.github/secret_scanning.yml) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **C:** Correct. Security Manager and fine-grained custom repository roles grant AppSec and security champions exact triage permissions without over-provisioning Repository Admin or code-push rights
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 34 — `B` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: B (is correct). Administrators must run `Save and dry run` (`returning up to 1,000 sample matches across the org, or across up to 10 selected repos at Enterprise scope, without creating live alerts`) before `Publish pattern` and Push Protection can be enabled. [Skill 2.6: Create, dry-run, and manage custom secret patterns (including Copilot regex generation and Push Protection) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Correct. dry runs preview up to 1,000 historical matches without creating live alerts, and editing a published pattern automatically closes alerts generated by its previous version
- **C:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 35 — `A` (Configure and use Secret Protection (formerly secret scanning))

Correct answer: A (is correct). GitHub supports up to `100` custom patterns per repository and up to `500` per organization or enterprise, and an enterprise-level custom pattern can only be edited or deleted by the specific enterprise owner who originally created it. [Skill 2.6: Create, dry-run, and manage custom secret patterns (including Copilot regex generation and Push Protection) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning)]

- **A:** Correct. dry runs preview up to 1,000 historical matches without creating live alerts, and editing a published pattern automatically closes alerts generated by its previous version
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 36 — `A, B, E` (Configure and use Secret Protection (formerly secret scanning))

Correct answers: A, B, and E (are correct). Dry-run testing previews up to 1,000 matches before publishing (`and editing a published pattern closes prior-version alerts`), Push Protection can block published custom patterns pre-receive, and bypass events emit webhook and audit-log records. [Skill 2.6: Create, dry-run, and manage custom secret patterns (including Copilot regex generation and Push Protection) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning)]

- **A:** Correct. every bypass leaves an immutable audit trail linking the actor, commit, justification, and approver
- **B:** Correct. dry runs preview up to 1,000 historical matches without creating live alerts, and editing a published pattern automatically closes alerts generated by its previous version
- **C:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **E:** Correct. stopping secrets pre-receive prevents Git history contamination and emergency credential rotation
- **F:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 37 — `A` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: A (is correct). Posting a build-time dependency snapshot to the `Dependency Submission API` (`POST /repos/{owner}/{repo}/dependency-graph/snapshots` or official detector actions) populates the Dependency Graph for ecosystems lacking static lockfiles. [Skill 3.1: Generate and interpret the dependency graph, vulnerability databases, Dependency Submission API, and SPDX SBOM exports | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository)]

- **A:** Correct. committing lockfiles plus submitting build-resolved snapshots gives GitHub complete direct and transitive dependency visibility
- **B:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **C:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 38 — `D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: D (is correct). `GET /repos/{owner}/{repo}/dependency-graph/sbom` (`or actions/attest-sbom` for cryptographically attested SPDX provenance) exports the repository's direct and transitive dependency graph. [Skill 3.1: Generate and interpret the dependency graph, vulnerability databases, Dependency Submission API, and SPDX SBOM exports | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository)]

- **A:** Incorrect. the code-security configurations attach endpoint programmatically binds a Security Configuration to targeted or organization-wide repositories
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Incorrect. codeql github upload-results publishes externally generated SARIF 2.1.0 files to GitHub Code Scanning with exact ref and commit metadata
- **D:** Correct. the Dependency Graph SBOM REST endpoint returns upstream direct and transitive packages in machine-readable SPDX JSON

### Question 39 — `C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: C (is correct). An SPDX SBOM documents only upstream packages consumed *by* `aethernav-coord-math`, whereas downstream consumers appear separately in the `Dependents` view and are excluded from SBOM exports. [Skill 3.1: Generate and interpret the dependency graph, vulnerability databases, Dependency Submission API, and SPDX SBOM exports | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Correct. GitHub exports dependency inventories, versions, licenses, and transitive relationships in standard SPDX JSON (and never includes downstream external dependents)
- **D:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names

### Question 40 — `A` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: A (is correct). Enable Dependency Graph and Dependabot alerts, disable global `Dependabot security updates` so custom PR rules govern, configure org/repo Dependabot auto-triage rules on scope/EPSS/patch, and audit `resolution:auto-dismiss` plus targeted PRs. [Skill 3.2: Prioritize supply chain alerts (EPSS, CVSS, reachability) and configure Dependabot auto-triage (auto-dismiss) rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules)]

- **A:** Correct. custom Dependabot auto-triage rules run before notifications, and repository-wide Dependabot security updates must be off when using custom rules to selectively open security PRs
- **B:** Incorrect. auto-triage rules require Dependabot alerts enabled, global security updates override selective PR rules, malware alerts do not open PRs, and scope changes auto-reopen alerts
- **C:** Incorrect. Dependabot auto-triage rules live in Dependabot settings (where org rules override conflicting repo rules and evaluate before notifications), not secret_scanning.yml
- **D:** Incorrect. deleting lockfiles blinds transitive vulnerability detection, and the Dismiss package malware alerts preset suppresses false-positive internal namespace collisions rather than blocking malware

### Question 41 — `C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: C (is correct). `EPSS` estimates the 30-day probability of wild exploitation while static `Reachability` (`up to 5 call paths`) proves `telemetry-ingest-kotlin` actually invokes the vulnerable function—making the reachable high-EPSS alert the immediate patch priority. [Skill 3.2: Prioritize supply chain alerts (EPSS, CVSS, reachability) and configure Dependabot auto-triage (auto-dismiss) rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **C:** Correct. combining EPSS exploit likelihood and static reachability with CVSS and runtime scope focuses engineering effort on genuinely exploitable dependencies
- **D:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure

### Question 42 — `A, D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answers: A and D (are correct). Prioritize alerts by `EPSS` + `Reachability` + `runtime` scope, and remember auto-triage rules apply `resolution:auto-dismiss` *before* notifications (`with org rules overriding repo conflicts and alerts auto-reopening if promoted to runtime`). [Skill 3.2: Prioritize supply chain alerts (EPSS, CVSS, reachability) and configure Dependabot auto-triage (auto-dismiss) rules | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules)]

- **A:** Correct. high-EPSS reachable runtime vulnerabilities represent immediate real-world exploit risk compared with unreachable dev-only packages
- **B:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Correct. evaluating auto-triage rules prior to notifications eliminates alert fatigue while keeping alerts auditable and auto-reopenable
- **E:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names

### Question 43 — `C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: C (is correct). Filtering custom Dependabot auto-triage rules by specific `manifest` path is supported at the **repository** level (`whereas CVE, CWE, EPSS, severity, scope, ecosystem, package, and patch availability work at both repo and org levels`). [Skill 3.3: Remediate supply chain alerts through Dependabot security updates, version updates, and security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Correct. auto-triage rules suppress low-risk noise before notifications fire, auto-reopen if metadata/scope changes, and defer to organization rules when repo rules conflict
- **D:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names

### Question 44 — `C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: C (is correct). `Dependabot security updates` only open PRs when a GitHub Advisory Database vulnerability affects the default branch; keeping non-vulnerable packages fresh requires adding a scheduled `.github/dependabot.yml` (`Dependabot version updates`). [Skill 3.3: Remediate supply chain alerts through Dependabot security updates, version updates, and security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Correct. security updates react to GitHub Advisory Database alerts on default-branch dependencies, whereas dependabot.yml keeps dependencies and github-actions current on a schedule
- **D:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure

### Question 45 — `D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: D (is correct). Coordinate targeted upgrades using Dependabot grouped updates and Security Overview dashboards/campaigns alongside owner notifications and ruleset gates so squads remediate production-exposed repositories systematically. [Skill 3.3: Remediate supply chain alerts through Dependabot security updates, version updates, and security campaigns | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates)]

- **A:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Correct. Security Campaigns turn overwhelming alert backlogs into manageable, developer-friendly remediation sprints with clear ownership

### Question 46 — `D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: D (is correct). Enable Dependency Graph (`with GitHub Code Security on private repos`), configure an `on: pull_request` workflow running `actions/dependency-review-action@v4` with `fail-on-severity` and `deny-licenses`, and enforce it as a required check in a branch ruleset. [Skill 3.4: Secure dependencies during development using pre-merge Dependency Review (dependency-review-action) for vulnerabilities and licenses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action)]

- **A:** Incorrect. private repositories require GitHub Code Security / GHAS for Dependency Review, contents: read suffices, and unenforced checks do not block merges
- **B:** Incorrect. dependency-review-action requires pull_request base/head diffs and an active Dependency Graph, and allow-licenses / deny-licenses are mutually exclusive
- **C:** Incorrect. dependabot.yml schedules dependency update PRs rather than gating developer PRs on license compliance; pre-merge gating requires dependency-review-action plus required checks
- **D:** Correct. Dependency Review compares PR base-vs-head manifests/lockfiles via the Dependency Graph and blocks vulnerable or non-compliant licenses when required on protected branches

### Question 47 — `B` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: B (is correct). Configuring `fail-on-severity: high`, `fail-on-scopes: runtime`, and `deny-licenses: AGPL-3.0` (`without setting allow-licenses simultaneously`) enforces runtime-only severity gating and SPDX license denial. [Skill 3.4: Secure dependencies during development using pre-merge Dependency Review (dependency-review-action) for vulnerabilities and licenses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action)]

- **A:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **B:** Correct. dependency-review-action@v4 gates pull requests on severity, dependency scope, and SPDX license policy using a single allow OR deny list
- **C:** Incorrect. codeql-config.yml centralizes custom query packs, path exclusions, threat models, and data-extension model packs for Advanced Setup
- **D:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure

### Question 48 — `B, D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answers: B and D (are correct). `dependency-review-action@v4` must be configured with appropriate `fail-on-severity` / `allow-licenses` OR `deny-licenses` thresholds on `pull_request`, and its job must be marked **required** in an active branch protection rule or ruleset on `main`. [Skill 3.4: Secure dependencies during development using pre-merge Dependency Review (dependency-review-action) for vulnerabilities and licenses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Correct. Dependency Review blocks both vulnerable package versions and prohibited copyleft/unknown licenses on pull requests
- **C:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **D:** Correct. without a required status check rule, a failing Dependency Review workflow warns on the PR without blocking merge
- **E:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names

### Question 49 — `C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: C (is correct). Declare a `registries:` block (`type: maven-repository` referencing `${{ secrets.NEXUS_TOKEN }}` in **Dependabot secrets**) and a `groups:` block matching `patterns: ["org.springframework*"]` with `update-types: ["minor", "patch"]`. [Skill 3.5: Configure advanced dependency update rules in dependabot.yml (grouping, ignore rules, update strategies, private registries) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference)]

- **A:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Correct. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets
- **D:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories

### Question 50 — `C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: C (is correct). Configuring `versioning-strategy` (`such as auto / increase-if-necessary` vs `increase` or `lockfile-only`) alongside `ignore:` and `groups:` in `.github/dependabot.yml` controls how Dependabot modifies manifests versus lockfiles. [Skill 3.5: Configure advanced dependency update rules in dependabot.yml (grouping, ignore rules, update strategies, private registries) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference)]

- **A:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **B:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **C:** Correct. grouping related updates cuts CI/PR noise dramatically, while registries + Dependabot secrets authenticate Dependabot to private npm/NuGet/PyPI/Maven feeds
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 51 — `D` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: D (is correct). While `allow-ghsas` validly waives a specific advisory ID, passing both `allow-licenses` and `deny-licenses` in the same step fails because the two license parameters are mutually exclusive (`allow-licenses` alone already rejects unlisted licenses like `SSPL-1.0`). [Skill 3.5: Configure advanced dependency update rules in dependabot.yml (grouping, ignore rules, update strategies, private registries) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference)]

- **A:** Incorrect. validate advisory patches locally or in an isolated private mirror without exposing exploit diffs publicly before publishing the coordinated GHSA release
- **B:** Incorrect. enabling Advanced Setup disables Default Setup so custom workflow build steps, codeql-config.yml, or custom query suites govern scanning cleanly without duplicate conflicts
- **C:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. While `allow-ghsas` validly waives a specific advisory ID, passing both `allow-licenses` and `deny-licenses` in the same step fails because the two license parameters are mutually exclusive (`allow-licenses` alone already rejects unlisted licenses like `SSPL-1.0`).
- **D:** Correct. allow-licenses and deny-licenses are mutually exclusive inputs in dependency-review-action, and branch rulesets must require the check to block merging

### Question 52 — `A` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: A (is correct). Subscribe an organization webhook to `dependabot_alert` events (`created`, `reopened`, `auto_reopened`) and isolate untrusted/fork or Dependabot workloads on ephemeral runners using read-only `GITHUB_TOKEN` defaults and scoped `Dependabot secrets`. [Skill 3.6: Configure supply chain alert permissions, Dependabot workflows/runners, webhooks, and external production-context integrations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/automating-dependabot-with-github-actions)]

- **A:** Correct. understanding Dependabot token/secret isolation, webhook automation, and Defender for Cloud / artifact-registry deployment context integrates supply-chain security safely into operations
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 53 — `B` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answer: B (is correct). Querying `has:deployment runtime-risk:internet-exposed` filters supply-chain and code alerts down to artifacts mapped to live internet-facing production deployments. [Skill 3.6: Configure supply chain alert permissions, Dependabot workflows/runners, webhooks, and external production-context integrations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/automating-dependabot-with-github-actions)]

- **A:** Incorrect. querying is:closed resolution:auto-dismiss audits every Dependabot alert suppressed by preset or custom auto-triage rules
- **B:** Correct. filtering by has:deployment and runtime-risk:internet-exposed isolates alerts affecting live internet-reachable workloads
- **C:** Incorrect. security-extended broadens vulnerability detection beyond default without adding non-security maintainability noise from security-and-quality
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 54 — `A, C` (Configure and use supply chain security (formerly Dependabot/Dependency Review))

Correct answers: A and C (are correct). Dependabot PR workflows run with a read-only `GITHUB_TOKEN` and read credentials from `Dependabot secrets`, while `dependabot_alert` webhooks, granular custom alert roles, and deployment-context integrations govern downstream operations. [Skill 3.6: Configure supply chain alert permissions, Dependabot workflows/runners, webhooks, and external production-context integrations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/dependabot/working-with-dependabot/automating-dependabot-with-github-actions)]

- **A:** Correct. isolating Dependabot secrets and read-only default tokens protects repository secrets if a compromised upstream package alters build scripts
- **B:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **C:** Correct. understanding Dependabot token/secret isolation, webhook automation, and Defender for Cloud / artifact-registry deployment context integrates supply-chain security safely into operations
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **E:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 55 — `D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: D (is correct). CodeQL performs deep interprocedural AST/dataflow taint analysis across source repositories, while importing MISRA-C `SARIF 2.1.0` consolidates specialized avionics compliance checks into the same PR annotations and ruleset gates. [Skill 4.1: Compare CodeQL and third-party analysis tools and manage SARIF 2.1.0 ingestion, fingerprints, and limits | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning)]

- **A:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Correct. CodeQL excels at deep interprocedural taint tracking across supported languages while SARIF 2.1.0 lets specialized IaC/container/linter tools report into one PR interface

### Question 56 — `B` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: B (is correct). Yes—the file is within the `<= 10 MB` gzipped and `<= 25,000` results-per-run ingestion limits, and GitHub retains/displays the top `5,000` results prioritized by severity (`plus up to 1,000 threadFlowLocations per path`). [Skill 4.1: Compare CodeQL and third-party analysis tools and manage SARIF 2.1.0 ingestion, fingerprints, and limits | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Correct. compressing SARIF under 10 MB, preserving ruleId + partialFingerprints across runs, and setting unique category strings per tool/language/monorepo slice prevents rejected or overwritten alerts
- **C:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **D:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`

### Question 57 — `A, B` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answers: A and B (are correct). Keep each gzip-compressed SARIF payload `<= 10 MB` (`<= 25,000` results, top `5,000` displayed) and set a distinct `category` per tool/target while preserving `ruleId` + `partialFingerprints`. [Skill 4.1: Compare CodeQL and third-party analysis tools and manage SARIF 2.1.0 ingestion, fingerprints, and limits | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning)]

- **A:** Correct. distinct categories prevent multi-job uploads on the same commit from clobbering one another, while fingerprints track alerts across line shifts
- **B:** Correct. exceeding 10 MB gzipped rejects the upload outright, while noisy rule sets over 5,000 findings truncate lower-priority alerts
- **C:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **D:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **E:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 58 — `B` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: B (is correct). Install the CodeQL CLI bundle on the external runner, execute `codeql database create` (`tracing the compiled build`), run `codeql database analyze --format=sarif-latest`, and upload via `codeql github upload-results` (`--sarif`, `--ref`, `--commit`). [Skill 4.2: Set up and configure Code Security via Default Setup, Advanced Setup workflows, matrix build-modes, and external CI (CodeQL CLI) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages)]

- **A:** Incorrect. Default Setup conflicts with custom/external CodeQL uploads, uploading SARIF requires security-events: write, and runs cap at 25,000 results (displaying top 5,000)
- **B:** Correct. external CI integrations create the semantic CodeQL database, execute query suites into SARIF 2.1.0 (`<=10 MB` gzipped), and upload results with `security_events` write auth
- **C:** Incorrect. CodeQL cannot upload raw source files or XML; a database must be created before analysis, and SARIF 2.1.0 uploads must be <=10 MB gzipped with target ref and commit SHA
- **D:** Incorrect. omitting distinct SARIF categories causes subsequent uploads for the same commit to overwrite/mark prior component results stale, and private repos require Code Security

### Question 59 — `C` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: C (is correct). `Default Setup` provides zero-YAML automatic onboarding for standard repositories and buildless languages, whereas `Advanced Setup` (`.github/workflows/codeql.yml`, mutually exclusive with Default Setup) is required when custom compiler wrappers, `codeql-config.yml` model packs, or custom matrix steps are needed. [Skill 4.2: Set up and configure Code Security via Default Setup, Advanced Setup workflows, matrix build-modes, and external CI (CodeQL CLI) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Correct. Default Setup is fastest for broad rollout, whereas Advanced Setup unlocks manual builds, custom query packs, and granular matrix control (disabling Default Setup automatically on switch)
- **D:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`

### Question 60 — `C` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: C (is correct). `build-mode: none` analyzes Python (`and buildless Java when no Kotlin is present`) without compilation, `autobuild` heuristically builds standard projects, and `build-mode: manual` is required for custom `bazel` C++ builds (`since C/C++ and Swift never support build-mode: none`). [Skill 4.2: Set up and configure Code Security via Default Setup, Advanced Setup workflows, matrix build-modes, and external CI (CodeQL CLI) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages)]

- **A:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **B:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **C:** Correct. selecting build-mode: manual when custom flags/codegen break autobuild—or build-mode: none where supported—eliminates build-wrapper failures cleanly
- **D:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories

### Question 61 — `A` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: A (is correct). Inspect each `source -> step -> sink` node in the CodeQL path viewer to confirm the untrusted telemetry input cannot still reach `exec.Command()`, apply or refine the Copilot Autofix patch, and verify unit tests plus the PR CodeQL re-scan pass. [Skill 4.3: Review CodeQL dataflow analysis insights and remediate alerts using Copilot Autofix and pull request workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning)]

- **A:** Correct. taint-flow paths pinpoint exact user-input sources and unvalidated sinks, while Copilot Autofix proposes context-aware diffs that must still pass CI and human review
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 62 — `C` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: C (is correct). Running `codeql github upload-results --repository=aethernav/radhard-hal-sdk --ref=refs/heads/main --commit=9f3c12a... --sarif=avionics.sarif` authenticates via `GITHUB_TOKEN` and publishes findings to Code Scanning. [Skill 4.3: Review CodeQL dataflow analysis insights and remediate alerts using Copilot Autofix and pull request workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning)]

- **A:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **B:** Incorrect. the code-security configurations attach endpoint programmatically binds a Security Configuration to targeted or organization-wide repositories
- **C:** Correct. codeql github upload-results publishes externally generated SARIF 2.1.0 files to GitHub Code Scanning with exact ref and commit metadata
- **D:** Incorrect. the Dependency Graph SBOM REST endpoint returns upstream direct and transitive packages in machine-readable SPDX JSON

### Question 63 — `B, E` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answers: B and E (are correct). Configure job permissions with `security-events: write`, `contents: read`, and `actions: read`, and require CI test verification, CodeQL re-scanning, and human PR review on every Copilot Autofix commit. [Skill 4.3: Review CodeQL dataflow analysis insights and remediate alerts using Copilot Autofix and pull request workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Correct. LLM-generated security fixes lower remediation friction dramatically, yet still require automated test and human semantic verification before merge
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **E:** Correct. uploading CodeQL or third-party SARIF 2.1.0 findings from GitHub Actions requires least-privilege security-events: write permission

### Question 64 — `D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: D (is correct). Without a unique `category` per matrix build target, Code Scanning treats same-language uploads on one commit as replacements for the same analysis target, marking findings absent from the second target as fixed. [Skill 4.4: Manage code scanning alert lifecycles, dismissals, severity thresholds, and analysis categories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **D:** Correct. branch protection rulesets filter security alerts by Critical/High/Medium/Low security-severity independently from non-security error/warning quality notes

### Question 65 — `A` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: A (is correct). Default Setup and custom `codeql.yml` CodeQL workflows cannot actively manage the same language together, and `build-mode: none` for Java does **not** analyze `Kotlin` (`which requires compiled extraction via autobuild or manual`). [Skill 4.4: Manage code scanning alert lifecycles, dismissals, severity thresholds, and analysis categories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository)]

- **A:** Correct. enabling Advanced Setup disables Default Setup so custom workflow build steps, codeql-config.yml, or custom query suites govern scanning cleanly without duplicate conflicts
- **B:** Incorrect. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories
- **C:** Incorrect. allow-licenses and deny-licenses are mutually exclusive inputs in dependency-review-action, and branch rulesets must require the check to block merging
- **D:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. Default Setup and custom `codeql.yml` CodeQL workflows cannot actively manage the same language together, and `build-mode: none` for Java does **not** analyze `Kotlin` (`which requires compiled extraction via autobuild or manual`).

### Question 66 — `D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: D (is correct). CodeQL maps `@security-severity` scores using CVSS thresholds: `9.0–10.0 = Critical`, `7.0–8.9 = High`, `4.0–6.9 = Medium`, and `0.1–3.9 = Low`, independent of `Error`/`Warning`/`Note` rule severity. [Skill 4.4: Manage code scanning alert lifecycles, dismissals, severity thresholds, and analysis categories | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository)]

- **A:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **B:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Correct. branch protection rulesets filter security alerts by Critical/High/Medium/Low security-severity independently from non-security error/warning quality notes

### Question 67 — `D` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: D (is correct). Publishing a `CodeQL model pack` (`YAML data extensions`) and referencing it under `packs:` in `.github/codeql/codeql-config.yml` extends CodeQL's knowledge of internal framework sources, summaries, and sinks cleanly. [Skill 4.5: Optimize and troubleshoot Code Security operations with custom configurations, model packs, and build/performance diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning)]

- **A:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **B:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories
- **C:** Incorrect. dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets
- **D:** Correct. codeql-config.yml centralizes custom query packs, path exclusions, threat models, and data-extension model packs for Advanced Setup

### Question 68 — `B` (Configure and use Code Security (formerly Code Scanning with CodeQL))

Correct answer: B (is correct). Add `paths-ignore: ["sim/recorded_flights/**"]` inside `.github/codeql/codeql-config.yml` (`or custom Default Setup path filters`), split languages into parallel jobs, and allocate higher-CPU/RAM runners where needed. [Skill 4.5: Optimize and troubleshoot Code Security operations with custom configurations, model packs, and build/performance diagnostics | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning)]

- **A:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **B:** Correct. model packs teach CodeQL custom internal framework sources/sanitizers/sinks without forking queries, while Adequate RAM/CPU runners and scoped paths resolve timeout/OOM failures
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)

### Question 69 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). Enabling `Private vulnerability reporting` on the public repository adds a `Report a vulnerability` workflow in the Security tab that creates a confidential draft Repository Security Advisory (`GHSA`) for maintainer triage. [Skill 5.1: Understand CVE, CWE, and GitHub Security Advisory (GHSA) concepts and execute end-to-end advisory remediation workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Correct. maintainers triage private reports inside draft GHSAs, patch silently in temporary private forks (where Actions stay disabled), request a CVE, and publish coordinated advisories
- **C:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 70 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). Temporary advisory forks intentionally disable GitHub Actions, and opening a PR against the public repository immediately leaks the exploit regression test and vulnerable code path to the public before patched packages ship. [Skill 5.1: Understand CVE, CWE, and GitHub Security Advisory (GHSA) concepts and execute end-to-end advisory remediation workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories)]

- **A:** Incorrect. when global Dependabot security updates remain enabled, Dependabot attempts PRs for every patchable alert, overriding selective custom PR auto-triage rules
- **B:** Correct. validate advisory patches locally or in an isolated private mirror without exposing exploit diffs publicly before publishing the coordinated GHSA release
- **C:** Incorrect. each gzipped SARIF upload must be <=10 MB with a distinct category per language/tool/component and security-events: write permission
- **D:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. Temporary advisory forks intentionally disable GitHub Actions, and opening a PR against the public repository immediately leaks the exploit regression test and vulnerable code path to the public before patched packages ship.

### Question 71 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). GitHub assigns the `CVE` (`when eligible`), curates the `GHSA` into the global GitHub Advisory Database, and automatically triggers `Dependabot alerts` (`and security updates`) for repositories using `< 2.4.3`. [Skill 5.1: Understand CVE, CWE, and GitHub Security Advisory (GHSA) concepts and execute end-to-end advisory remediation workflows | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Correct. maintainers triage private reports inside draft GHSAs, patch silently in temporary private forks (where Actions stay disabled), request a CVE, and publish coordinated advisories
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 72 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). Triage backlogs using `has:deployment` + `runtime-risk:internet-exposed` (`from Defender for Cloud / artifact registries`), `EPSS`, and `Reachability`, while enforcing `Require code scanning results` (`Critical/High`) on active default-branch rulesets. [Skill 5.2: Define, prioritize, and enforce severity rulesets and production-context prioritization at scale | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-vulnerabilities/alerts-in-production-code)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Correct. combining runtime deployment exposure with pre-merge High/Critical blocking stops alert growth while burning down real internet-exposed production risk first
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)

### Question 73 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). Using `has:deployment runtime-risk:internet-exposed` leverages ingested cloud/artifact deployment records to isolate live internet-exposed assets. [Skill 5.2: Define, prioritize, and enforce severity rulesets and production-context prioritization at scale | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-vulnerabilities/alerts-in-production-code)]

- **A:** Incorrect. the Dependency Graph SBOM REST endpoint returns upstream direct and transitive packages in machine-readable SPDX JSON
- **B:** Correct. filtering by has:deployment and runtime-risk:internet-exposed isolates alerts affecting live internet-reachable workloads
- **C:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **D:** Incorrect. querying is:closed resolution:auto-dismiss audits every Dependabot alert suppressed by preset or custom auto-triage rules

### Question 74 — `A, E` (Security operations: best practices, prioritization, and remediation)

Correct answers: A and E (are correct). Connect Defender for Cloud / JFrog deployment telemetry (`has:deployment`, `runtime-risk:internet-exposed`), and deploy the organization ruleset in `Evaluate` mode first to audit Ruleset Insights before switching to `Active`. [Skill 5.2: Define, prioritize, and enforce severity rulesets and production-context prioritization at scale | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-vulnerabilities/alerts-in-production-code)]

- **A:** Correct. Evaluate mode surfaces missing scans or noisy rules safely without halting production releases on day one
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **D:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **E:** Correct. production context pinpoints vulnerabilities actually running in internet-facing workloads rather than dead or archived repos

### Question 75 — `D` (Security operations: best practices, prioritization, and remediation)

Correct answer: D (is correct). Filter priority default-branch alerts in Security Overview, create a Security Campaign (`<=1,000` alerts) with a due date and security contact, trigger Copilot Autofix (`or assign batches of <=25 alerts to @copilot`), and verify CI checks while tracking burndown. [Skill 5.3: Execute campaign-based remediation strategies, bulk alert management, and audited alert dismissal documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/manage-security-alerts/best-practices-for-participating-in-a-security-campaign)]

- **A:** Incorrect. code security campaigns target default-branch alerts (up to 1,000 per campaign) with a named contact, and developers need write access plus passing CI checks to merge fixes
- **B:** Incorrect. agentic @copilot campaign assignments cap at 25 alerts per batch (opening a PR for human/CI verification), and Copilot cannot rotate external cloud provider IAM credentials
- **C:** Incorrect. disabling scanners or bulk-dismissing unreviewed findings hides real production vulnerabilities rather than remediating security debt
- **D:** Correct. Security Campaigns group high-risk default-branch alerts around a dedicated security contact and accelerate developer burndown with Copilot Autofix or @copilot draft PRs

### Question 76 — `A` (Security operations: best practices, prioritization, and remediation)

Correct answer: A (is correct). Assigning a repository writer (`or including them on assigned secret campaign items`) temporarily elevates their access to view **only** those specifically assigned secret alerts (`not other secret alerts in the repo`) until unassigned or removed. [Skill 5.3: Execute campaign-based remediation strategies, bulk alert management, and audited alert dismissal documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/manage-security-alerts/best-practices-for-participating-in-a-security-campaign)]

- **A:** Correct. grouping related CWEs into focused campaigns builds developer remediation momentum while Copilot Autofix and @copilot PR batches cut manual toil
- **B:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **C:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 77 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). Require an explicit justification comment citing the non-production test harness path alongside the `Used in tests` dismissal reason, and verify closures via Security Overview campaign audit metrics. [Skill 5.3: Execute campaign-based remediation strategies, bulk alert management, and audited alert dismissal documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/manage-security-alerts/best-practices-for-participating-in-a-security-campaign)]

- **A:** Incorrect. Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names
- **B:** Correct. alert dismissals remain visible in REST/GraphQL APIs, webhooks, and audit logs, so teams must document rationale rather than hiding unverified risk
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 78 — `A` (Security operations: best practices, prioritization, and remediation)

Correct answer: A (is correct). Setting `queries: security-extended` adds medium-precision security queries on top of `default` while excluding maintainability/style rules included in `security-and-quality`. [Skill 5.4: Customize CodeQL query suites, multi-repository variant analysis, and risk-profile-tailored security detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites)]

- **A:** Correct. security-extended broadens vulnerability detection beyond default without adding non-security maintainability noise from security-and-quality
- **B:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)
- **C:** Incorrect. querying is:closed resolution:auto-dismiss audits every Dependabot alert suppressed by preset or custom auto-triage rules
- **D:** Incorrect. secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories

### Question 79 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). The VS Code CodeQL extension dispatches the custom `.ql` query to a designated controller repository where GitHub Actions fans out analysis across up to 1,000 repositories' CodeQL databases and streams matches back to VS Code. [Skill 5.4: Customize CodeQL query suites, multi-repository variant analysis, and risk-profile-tailored security detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites)]

- **A:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **B:** Correct. security-extended expands vulnerability coverage beyond high-precision default rules, while MRVA hunts novel zero-day patterns across up to 1,000 org repositories simultaneously
- **C:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **D:** Incorrect. C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)

### Question 80 — `B` (Security operations: best practices, prioritization, and remediation)

Correct answer: B (is correct). Tailoring CodeQL query suites to each repository's custom-property risk profile balances false-positive signal-to-noise ratio for developers against deeper vulnerability coverage on critical assets. [Skill 5.4: Customize CodeQL query suites, multi-repository variant analysis, and risk-profile-tailored security detection | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites)]

- **A:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **B:** Correct. security-extended expands vulnerability coverage beyond high-precision default rules, while MRVA hunts novel zero-day patterns across up to 1,000 org repositories simultaneously
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)

### Question 81 — `C` (Security operations: best practices, prioritization, and remediation)

Correct answer: C (is correct). Configure fine-grained custom repository roles so standard `Write` contributors can view PR alerts and apply fixes while restricting alert `Dismiss/resolve` permissions to tech leads and `Security Managers`. [Skill 5.5: Collaborate across security roles, delegated exceptions, alert ownership, and cross-suite governance rulesets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)]

- **A:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **B:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **C:** Correct. clear alert ownership, delegated bypass reviewers, and Evaluate-first cross-suite rulesets align AppSec governance with engineering velocity
- **D:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers

### Question 82 — `C` (Security operations: best practices, prioritization, and remediation)

Correct answer: C (is correct). Organization Ruleset `RuleInsights` / bypass views, Push Protection bypass request logs, webhooks, and the Enterprise/Organization Audit Log (`streamed to SIEM`) record the actor, commit, repository, and stated justification. [Skill 5.5: Collaborate across security roles, delegated exceptions, alert ownership, and cross-suite governance rulesets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)]

- **A:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **B:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **C:** Correct. enterprise policies prevent uncontrolled repo-admin license consumption while audit log streaming preserves tamper-evident compliance records across configuration and bypass events
- **D:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 83 — `D, E` (Security operations: best practices, prioritization, and remediation)

Correct answers: D and E (are correct). Pair `Security Manager` and custom repository alert roles with clear per-alert `Assignees`, and enforce Push Protection `delegated bypass` backed by visible reviewer teams or custom bypass-approver roles. [Skill 5.5: Collaborate across security roles, delegated exceptions, alert ownership, and cross-suite governance rulesets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)]

- **A:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **B:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **C:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **D:** Correct. clear alert ownership, delegated bypass reviewers, and Evaluate-first cross-suite rulesets align AppSec governance with engineering velocity
- **E:** Correct. delegated bypass replaces ad-hoc writer self-bypasses with a structured request-and-approval workflow audited via webhooks and logs

### Question 84 — `C` (Security operations: best practices, prioritization, and remediation)

Correct answer: C (is correct). Intercept secrets during `git push` via Push Protection, block vulnerable/unlicensed PR dependencies via `actions/dependency-review-action@v4`, and run PR CodeQL checks with `Copilot Autofix` before merge. [Skill 5.6: Shift left and strengthen preventive security through push protection, pre-merge dependency scanning, and PR CodeQL analysis | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Correct. combining all three shift-left controls prevents new security debt from ever landing on the default branch
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 85 — `C` (Security operations: best practices, prioritization, and remediation)

Correct answer: C (is correct). Post-push Actions scanners run *after* the commit blob has already landed on the remote Git server (`triggering webhooks, clones, and history persistence`), whereas Push Protection rejects the packfile pre-receive so the secret never enters remote Git history. [Skill 5.6: Shift left and strengthen preventive security through push protection, pre-merge dependency scanning, and PR CodeQL analysis | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Incorrect. non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement
- **B:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **C:** Correct. blocking leaked credentials before the remote ref updates avoids costly key rotation, incident response, and Git history rewrites
- **D:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials

### Question 86 — `A, B, D` (Security operations: best practices, prioritization, and remediation)

Correct answers: A, B, and D (are correct). Block high-confidence secrets pre-receive with Push Protection, gate pull-request dependency and license diffs with `dependency-review-action@v4`, and verify CodeQL `Copilot Autofix` suggestions through CI tests and human review prior to merge. [Skill 5.6: Shift left and strengthen preventive security through push protection, pre-merge dependency scanning, and PR CodeQL analysis | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats)]

- **A:** Correct. Dependency Review blocks both vulnerable package versions and prohibited copyleft/unknown licenses on pull requests
- **B:** Correct. LLM-generated security fixes lower remediation friction dramatically, yet still require automated test and human semantic verification before merge
- **C:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **D:** Correct. stopping secrets pre-receive prevents Git history contamination and emergency credential rotation
- **E:** Incorrect. allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure
- **F:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection

### Question 87 — `A` (GitHub Security suites administration)

Correct answer: A (is correct). Verify committer license headroom (`or metered budget`), create/select a Security Configuration, attach it to tiered repositories via custom properties with `Apply to new repositories` enabled, and lock baseline drift with `Enforced`. [Skill 6.1: Roll out GitHub Security Suites at enterprise, organization, and repository scale and contrast GHEC vs. GHES capabilities | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/choosing-a-security-configuration-for-your-repositories)]

- **A:** Correct. rolling out Security Configurations verifies committer license capacity first, targets repo tiers via custom properties, covers newly created repos, and locks drift with Enforced mode
- **B:** Incorrect. exceeding volume committer licenses blocks enablement on additional/new private repos, and features left as Not set remain editable by repository admins even under Enforced configurations
- **C:** Incorrect. standalone GHES uses volume/subscription licensing (not metered billing) and requires GitHub Connect for Advisory DB sync, while transferred repos must be explicitly targeted by configurations
- **D:** Incorrect. manual per-repo changes do not scale or prevent configuration drift, and granting Organization Owner violates least privilege when Security Manager / Security Configurations exist

### Question 88 — `D` (GitHub Security suites administration)

Correct answer: D (is correct). `GitHub Connect` syncs the GitHub Advisory Database to `GHES` for Dependabot alerts and deduplicates `90-day active committer` seat counts across `GHES` and `GHEC` (`whereas standalone GHES uses volume licensing and lacks cloud-only metered billing`). [Skill 6.1: Roll out GitHub Security Suites at enterprise, organization, and repository scale and contrast GHEC vs. GHES capabilities | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/choosing-a-security-configuration-for-your-repositories)]

- **A:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **B:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Correct. Security Configurations eliminate manual repo drift on GHEC and GHES, while hybrid enterprises link GHES to GHEC via GitHub Connect for Advisory DB updates and committer seat deduplication

### Question 89 — `C` (GitHub Security suites administration)

Correct answer: C (is correct). `GitHub-recommended` provides an opinionated turnkey preset of core security features for fast onboarding, whereas custom Security Configurations let admins tailor individual toggles (`Push Protection, validity checks, auto-triage, Default Setup query suite, Enforced vs Unenforced`) per repository tier. [Skill 6.1: Roll out GitHub Security Suites at enterprise, organization, and repository scale and contrast GHEC vs. GHES capabilities | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/choosing-a-security-configuration-for-your-repositories)]

- **A:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **B:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **C:** Correct. Security Configurations eliminate manual repo drift on GHEC and GHES, while hybrid enterprises link GHES to GHEC via GitHub Connect for Advisory DB updates and committer seat deduplication
- **D:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers

### Question 90 — `D` (GitHub Security suites administration)

Correct answer: D (is correct). When a volume/subscription license pool reaches `100%` capacity with zero available seats, GitHub blocks automatic enablement of paid Secret Protection / Code Security features on newly created private repositories (`whereas metered billing scales elastically up to configured budget caps`). [Skill 6.2: Configure suite defaults, Enforced vs. Unenforced inheritance, 90-day active-committer licensing, and AI credit budgets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/billing/concepts/product-billing/github-advanced-security)]

- **A:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **B:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **C:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **D:** Correct. understanding Enforced vs Unenforced inheritance, transferred-repo gaps, 90-day active committer deduplication, and hard budgets on metered SKUs/AI credits prevents surprise overages or lockouts

### Question 91 — `A` (GitHub Security suites administration)

Correct answer: A (is correct). Leaving a row as `"Not set"` delegates control to repository administrators even when the overall Security Configuration policy mode is set to `Enforced`; rows must be explicitly set to `Enabled` or `Disabled` to lock them. [Skill 6.2: Configure suite defaults, Enforced vs. Unenforced inheritance, 90-day active-committer licensing, and AI credit budgets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/billing/concepts/product-billing/github-advanced-security)]

- **A:** Correct. Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories
- **B:** Incorrect. The proposed GitHub Security configuration or workflow violates at least one stated security, licensing, or governance requirement. Leaving a row as `"Not set"` delegates control to repository administrators even when the overall Security Configuration policy mode is set to `Enforced`; rows must be explicitly set to `Enabled` or `Disabled` to lock them.
- **C:** Incorrect. when global Dependabot security updates remain enabled, Dependabot attempts PRs for every patchable alert, overriding selective custom PR auto-triage rules
- **D:** Incorrect. validate advisory patches locally or in an isolated private mirror without exposing exploit diffs publicly before publishing the coordinated GHSA release

### Question 92 — `C, E` (GitHub Security suites administration)

Correct answers: C and E (are correct). Each unique human committer pushing to private/internal enabled repos over the rolling 90-day window consumes one deduplicated seat across the enterprise, and metered `Code Security AI credits` (`AI Scan / @copilot batches`) plus `Secret Protection AI credits` (`AI push detection`) respect hard spending budgets. [Skill 6.2: Configure suite defaults, Enforced vs. Unenforced inheritance, 90-day active-committer licensing, and AI credit budgets | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/billing/concepts/product-billing/github-advanced-security)]

- **A:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **B:** Incorrect. classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions
- **C:** Correct. classic CodeQL Copilot Autofix does not consume AI credits, whereas agentic autofix / AI Scan and AI push secret scanning draw from included or metered AI credit pools
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **E:** Correct. a developer pushing to 50 GHAS-enabled repos in an enterprise consumes only one active-committer license seat over the rolling 90-day window

### Question 93 — `A` (GitHub Security suites administration)

Correct answer: A (is correct). Already-enabled repositories stay active, and `Enterprise Owners`, `Organization Owners`, and `Security Managers` retain full authority to attach or detach Security Configurations while individual Repository Admins can no longer toggle licensing. [Skill 6.3: Define enterprise and organization security policies, enforcement boundaries, bypass permissions, and audit log governance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise)]

- **A:** Correct. enterprise policies prevent uncontrolled repo-admin license consumption while audit log streaming preserves tamper-evident compliance records across configuration and bypass events
- **B:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **C:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 94 — `A` (GitHub Security suites administration)

Correct answer: A (is correct). Monitoring `security_configuration.*` (`detach/update`), `secret_scanning_push_protection_bypass`, `secret_scanning_alert.resolve`, `code_scanning_alert.dismiss`, and `repository_ruleset.*` via Enterprise Audit Log streaming provides real-time tampering detection. [Skill 6.3: Define enterprise and organization security policies, enforcement boundaries, bypass permissions, and audit log governance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise)]

- **A:** Correct. enterprise policies prevent uncontrolled repo-admin license consumption while audit log streaming preserves tamper-evident compliance records across configuration and bypass events
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. .gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection
- **D:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported

### Question 95 — `C` (GitHub Security suites administration)

Correct answer: C (is correct). Removing a user from the organization/enterprise releases their consumed GHAS/Code Security/Secret Protection seat (`and for remaining inactive users, seats automatically release once 90 days pass since their last push to any enabled private/internal repo`). [Skill 6.3: Define enterprise and organization security policies, enforcement boundaries, bypass permissions, and audit log governance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise)]

- **A:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **B:** Incorrect. disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers
- **C:** Correct. understanding Enforced vs Unenforced inheritance, transferred-repo gaps, 90-day active committer deduplication, and hard budgets on metered SKUs/AI credits prevents surprise overages or lockouts
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents

### Question 96 — `C` (GitHub Security suites administration)

Correct answer: C (is correct). Assigning the organization `Security Manager` role to `@aethernav/appsec` grants org-wide alert read/write, campaign management, and Security Configuration governance without code-write or Organization Owner privileges. [Skill 6.4: Define administrator, Security Manager, developer, and fine-grained custom roles for viewing and dismissing security alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization)]

- **A:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **B:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **C:** Correct. Security Manager and fine-grained custom repository roles grant AppSec and security champions exact triage permissions without over-provisioning Repository Admin or code-push rights
- **D:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days

### Question 97 — `D` (GitHub Security suites administration)

Correct answer: D (is correct). Create a custom repository role inheriting `Read` and add only the `View Dependabot alerts` and `View code scanning alerts` fine-grained permissions (`omitting write, admin, dismiss, and raw secret-viewing rights`). [Skill 6.4: Define administrator, Security Manager, developer, and fine-grained custom roles for viewing and dismissing security alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization)]

- **A:** Incorrect. active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days
- **B:** Incorrect. dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials
- **C:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **D:** Correct. Security Manager and fine-grained custom repository roles grant AppSec and security champions exact triage permissions without over-provisioning Repository Admin or code-push rights

### Question 98 — `D` (GitHub Security suites administration)

Correct answer: D (is correct). Creating a custom organization role with `Review and manage secret scanning bypass requests` grants targeted Push Protection delegated-bypass approval rights without broader Security Configuration authority. [Skill 6.4: Define administrator, Security Manager, developer, and fine-grained custom roles for viewing and dismissing security alerts | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization)]

- **A:** Incorrect. uploading CodeQL or third-party SARIF 2.1.0 findings from GitHub Actions requires least-privilege security-events: write permission
- **B:** Incorrect. GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported
- **C:** Incorrect. the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges
- **D:** Correct. granting Review and manage secret scanning bypass requests creates least-privilege Push Protection approvers without full Org Owner access

### Question 99 — `C` (GitHub Security suites administration)

Correct answer: C (is correct). Standardize CodeQL across target repos, create an Organization Branch Ruleset in `Evaluate` mode with `Require code scanning results` (`High+` security severity), review Evaluate insights and scope bypass actors, then switch enforcement to `Active`. [Skill 6.5: Enforce default or approved custom CodeQL workflows and automate large-scale security governance via REST and GraphQL APIs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/rest/code-security/configurations)]

- **A:** Incorrect. requiring CodeQL results before CodeQL runs deadlocks every PR awaiting a missing scan, while granting broad writer bypass or blocking on Note hints breaks governance
- **B:** Incorrect. Require code scanning results blocks PR merges until the configured tool reports scan results for that pull request head/merge ref
- **C:** Correct. piloting an Organization Ruleset in Evaluate mode confirms CodeQL check reporting and false-positive impact before switching Require code scanning results to Active merge blocking
- **D:** Incorrect. secret_scanning.yml only configures secret path exclusions, and AI suggestions never replace required human pull-request approvals

### Question 100 — `A, E` (GitHub Security suites administration)

Correct answers: A and E (are correct). Enforce organization `Rulesets` (`Require code scanning results` + centrally stored Required Workflows) and automate attachment/reporting via `POST /orgs/{org}/code-security/configurations/{configuration_id}/attach` plus org-level alert REST/GraphQL APIs. [Skill 6.5: Enforce default or approved custom CodeQL workflows and automate large-scale security governance via REST and GraphQL APIs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500 | Reference: GitHub Security Documentation (https://docs.github.com/en/rest/code-security/configurations)]

- **A:** Correct. the code-security configurations attach endpoint programmatically binds a Security Configuration to targeted or organization-wide repositories
- **B:** Incorrect. Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`
- **C:** Incorrect. standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)
- **D:** Incorrect. an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents
- **E:** Correct. combining Rulesets with REST/GraphQL security configuration and org-level alert APIs automates compliance reporting and zero-drift enforcement across thousands of repositories
