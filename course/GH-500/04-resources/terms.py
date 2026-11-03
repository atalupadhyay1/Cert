"""Canonical GH-500 term dictionary (atomic + multi-select + Proposed-solution + distractor traps + 40 sequence terms)."""

from sequences import SEQUENCE_TERMS

ATOMIC_TERMS = {
    # ===================== DOMAIN 1: Suites, Features & Ecosystem =====================
    'suite_unbundled_skus': (
        'Standalone `GitHub Secret Protection` and `GitHub Code Security` SKUs (`purchasable separately or together on GitHub Team and GitHub Enterprise`, alongside legacy bundled GHAS)',
        'GitHub offers standalone Secret Protection and Code Security products on both GitHub Team and GitHub Enterprise, billed by unique 90-day active committers on private/internal repos',
    ),
    'suite_three_pillars_contrast': (
        '`Secret Protection` (`secret scanning + push protection`), `Code Security` (`CodeQL/SARIF SAST + Copilot Autofix`), and `Supply Chain Security` (`Dependency Graph, Dependabot, Dependency Review & SBOMs`)',
        'each pillar targets a distinct risk surface: leaked credentials, first-party source vulnerabilities, and third-party open-source dependency/license exposure',
    ),
    'suite_public_vs_enterprise': (
        'Core features (`secret scanning, push protection, Dependency Graph, Dependabot, CodeQL default setup & Dependency Review`) are free on `public` GitHub.com repos; `private/internal` repos require licensed SKUs where applicable',
        'GitHub provides core security scanning free to open-source public repositories on GitHub.com while requiring Secret Protection / Code Security licenses for advanced private/internal repo coverage',
    ),
    'suite_security_overview_hub': (
        '`Security Overview` (`Organization & Enterprise Risk, Coverage, Campaigns, Code scanning, Secret scanning & Dependabot dashboards` filterable by team, topic, or custom property)',
        'Security Overview aggregates posture, enablement gaps, alert trends, and campaign burndown across hundreds of repositories from a single org/enterprise plane',
    ),
    'suite_free_risk_assessment': (
        'Organization `free security risk assessment` (`scanning org repos for leaked secrets and up to 20 active repositories for CodeQL vulnerabilities + Copilot Autofix preview`)',
        'organizations on GitHub Team or Enterprise can run free secret and code risk assessments before purchasing full rollout licenses',
    ),
    'suite_interplay_secret_vs_code': (
        '`Secret Protection` matches structured/high-entropy/AI secret tokens across Git history & pushes, whereas `Code Security (CodeQL)` traces semantic AST/dataflow vulnerabilities (`including hardcoded-credential sinks`)',
        'Secret Protection catches leaked tokens in any text/config file at push time, while CodeQL models how untrusted inputs or hardcoded values flow into sensitive code sinks',
    ),
    'suite_prevention_vs_gate': (
        'Prevention-first (`Push Protection + IDE/PR Dependency Review + PR CodeQL with Copilot Autofix`) stops defects before Git history/merge, whereas late release-only gates cause expensive rework',
        'shifting detection to git push and pull requests prevents secret sprawl and vulnerable merges before release cutoffs',
    ),
    'suite_campaigns_role': (
        '`Security Campaigns` (`targeted, time-bound initiatives grouping up to 1,000 default-branch alerts with a named security contact and Copilot Autofix support`)',
        'Security Campaigns turn overwhelming alert backlogs into manageable, developer-friendly remediation sprints with clear ownership',
    ),
    'suite_dismissal_governance': (
        'Dismissing an alert requires a structured closure reason (`False positive`, `Used in tests`, `Won\'t fix`) plus an audit-logged justification comment—and never deletes commits or revokes keys',
        'alert dismissals remain visible in REST/GraphQL APIs, webhooks, and audit logs, so teams must document rationale rather than hiding unverified risk',
    ),
    'suite_shared_responsibilities': (
        'Shared security model: `Admins` govern licensing/Security Configurations, `Security Managers` monitor Security Overview/campaigns/policies, and `Developers` remediate PR & campaign findings',
        'effective DevSecOps distributes enablement, posture prioritization, and code-level patching cleanly across Admin, AppSec, and Developer roles',
    ),
    'suite_access_delegated_bypass': (
        'Least-privilege alert access (`Write/Maintain/Admin/Security Manager` or custom roles) paired with `delegated bypass` so designated reviewers audit push-protection exceptions',
        'restricting sensitive secret/vulnerability details and routing bypass requests through designated security reviewers preserves accountability without halting urgent releases',
    ),

    # ===================== DOMAIN 2: Secret Protection =====================
    'sec_enable_repo_org': (
        'Enable `GitHub Secret Protection` (`secret scanning + push protection`) via Organization/Enterprise `Security Configurations` (`with Apply to new repositories`) or Repository `Settings -> Advanced Security`',
        'Security Configurations scale Secret Protection across existing and newly created repositories consistently, while single-repo toggles suit isolated pilots',
    ),
    'sec_public_partner_vs_private': (
        'On `public` repos, partner patterns run free and auto-notify token providers for revocation; on `private/internal` repos (`with Secret Protection`), alerts notify repo/org users (`plus optional validity checks`)',
        'partner notification automatically reports exposed public-repo tokens to the issuing cloud/SaaS vendor, whereas private-repo findings stay internal unless validity checks query the provider',
    ),
    'sec_push_protection_source': (
        '`Push Protection` intercepts supported high-confidence and published custom secrets pre-receive during `git push` (`CLI, IDE, web editor & REST API`), blocking the secret from entering Git history',
        'blocking leaked credentials before the remote ref updates avoids costly key rotation, incident response, and Git history rewrites',
    ),
    'sec_validity_checks_priority': (
        '`Validity checks` query partner token endpoints (`displaying Active, Inactive, or Unknown`) so responders prioritize live `Active` credentials first',
        'knowing a leaked AWS, Stripe, or Slack token is still Active lets incident responders triage live compromises ahead of already-revoked tokens',
    ),
    'sec_generic_ai_nonprovider': (
        '`Non-provider / generic pattern scanning` (`private keys, DB connection strings`) plus `Copilot AI generic secret detection` (`unstructured passwords/keys`, consuming `Secret Protection AI credits` on push)',
        'enabling non-provider and AI generic secret detection catches unstructured passwords and connection strings missed by vendor-prefix regexes (noting non-provider patterns lack partner validity checks)',
    ),
    'sec_alert_lifecycle_remediate': (
        'Treat every committed secret as compromised: `revoke & rotate at the issuing provider immediately`, rewrite Git history (`git filter-repo`), purge cached views via Support if needed, and resolve as `Revoked`',
        'merely deleting a secret in a later commit leaves it readable in earlier commits; immediate revocation and rotation is mandatory',
    ),
    'sec_delegated_bypass_policy': (
        '`Delegated bypass for push protection` (`granting Specific roles, visible teams, or custom roles with "Review and manage secret scanning bypass requests" authority—never secret teams`)',
        'delegated bypass replaces ad-hoc writer self-bypasses with a structured request-and-approval workflow audited via webhooks and logs',
    ),
    'sec_exclusions_yaml_recipients': (
        '`.github/secret_scanning.yml` with `paths-ignore:` (`up to 1,000 glob entries and <= 1 MB file size`) auto-closing user alerts in test/docs paths (`without suppressing public-repo partner revocation alerts`)',
        'secret_scanning.yml silences noisy user alerts in synthetic fixture directories up to 1,000 paths / 1 MB while keeping real code paths protected',
    ),
    'sec_custom_patterns_dryrun': (
        'Custom regex patterns (`up to 100/repo or 500/org-or-enterprise`, optional `Generate with AI` & `before`/`after` context) validated via `Save and dry run` (`<=1,000` sample hits) before `Publish pattern` & Push Protection',
        'dry runs preview up to 1,000 historical matches without creating live alerts, and editing a published pattern automatically closes alerts generated by its previous version',
    ),

    # ===================== DOMAIN 3: Supply Chain Security =====================
    'scs_dep_graph_submission': (
        '`Dependency Graph` (`parsing committed manifests and lockfiles`, augmented by the `Dependency Submission API` for build-time resolved transitive graphs in Maven/Gradle/C++/containers)',
        'committing lockfiles plus submitting build-resolved snapshots gives GitHub complete direct and transitive dependency visibility',
    ),
    'scs_sbom_spdx_export': (
        'Export an `SPDX` JSON Software Bill of Materials (`SBOM`) via `Insights -> Dependency graph -> Export SBOM`, `GET /repos/{owner}/{repo}/dependency-graph/sbom`, or `actions/attest-sbom` (`excluding dependents`)',
        'GitHub exports dependency inventories, versions, licenses, and transitive relationships in standard SPDX JSON (and never includes downstream external dependents)',
    ),
    'scs_epss_reachability_priority': (
        'Prioritize `Dependabot alerts` combining `EPSS` (`30-day exploitation probability`), `CVSS` severity, `Reachability` call-path analysis (`Reachable` vs `Unreachable`), `runtime` scope, and `patch availability`',
        'combining EPSS exploit likelihood and static reachability with CVSS and runtime scope focuses engineering effort on genuinely exploitable dependencies',
    ),
    'scs_autotriage_rules': (
        '`Dependabot auto-triage rules` (`GitHub presets or custom rules on EPSS/CVE/CWE/scope/patch` setting `resolution:auto-dismiss` before notifications; disable global `Dependabot security updates` for custom PR-trigger rules)',
        'auto-triage rules suppress low-risk noise before notifications fire, auto-reopen if metadata/scope changes, and defer to organization rules when repo rules conflict',
    ),
    'scs_dependabot_sec_vs_ver': (
        '`Dependabot security updates` (`alert-driven PRs patching vulnerable versions to the minimum fixed version`) vs `.github/dependabot.yml` `Dependabot version updates` (`scheduled ecosystem/Actions freshness PRs`)',
        'security updates react to GitHub Advisory Database alerts on default-branch dependencies, whereas dependabot.yml keeps dependencies and github-actions current on a schedule',
    ),
    'scs_dep_review_action': (
        '`actions/dependency-review-action@v4` on `pull_request` (`with fail-on-severity, mutually exclusive allow-licenses OR deny-licenses SPDX lists, fail-on-scopes, and allow-ghsas`) enforced as a required check',
        'Dependency Review inspects PR manifest/lockfile diffs before merge and fails the check when newly introduced packages breach vulnerability or license policies',
    ),
    'scs_dependabot_yml_advanced': (
        'Configure `.github/dependabot.yml` with `groups:` (`batching patch/minor updates into single PRs`), `ignore:` (`version/dependency exclusions`), `open-pull-requests-limit`, and `registries:` (`authenticated via Dependabot secrets`)',
        'grouping related updates cuts CI/PR noise dramatically, while registries + Dependabot secrets authenticate Dependabot to private npm/NuGet/PyPI/Maven feeds',
    ),
    'scs_workflows_webhooks_prod': (
        'Govern Dependabot PR workflows (`read-only GITHUB_TOKEN` & `Dependabot secrets`), fine-grained alert roles, `dependabot_alert` webhooks, and production-context filters (`has:deployment`, `runtime-risk:internet-exposed`)',
        'understanding Dependabot token/secret isolation, webhook automation, and Defender for Cloud / artifact-registry deployment context integrates supply-chain security safely into operations',
    ),

    # ===================== DOMAIN 4: Code Security (CodeQL & SARIF) =====================
    'code_codeql_vs_thirdparty': (
        '`CodeQL` (`compiling/extracting code into a queryable relational AST/CFG/dataflow database`) paired with third-party SAST/IaC/container scanners uploading `SARIF 2.1.0` into unified Code Scanning alerts',
        'CodeQL excels at deep interprocedural taint tracking across supported languages while SARIF 2.1.0 lets specialized IaC/container/linter tools report into one PR interface',
    ),
    'code_sarif_limits_fingerprints': (
        '`SARIF 2.1.0` ingestion rules: `<= 10 MB` gzip-compressed upload limit, `<= 25,000` results/run (`top 5,000` displayed by severity), `partialFingerprints` deduplication, distinct `category` tags, and `security-events: write`',
        'compressing SARIF under 10 MB, preserving ruleId + partialFingerprints across runs, and setting unique category strings per tool/language/monorepo slice prevents rejected or overwritten alerts',
    ),
    'code_default_vs_advanced_setup': (
        '`Default Setup` (`zero-YAML automatic language/trigger management`) vs `Advanced Setup` (`.github/workflows/codeql.yml` for custom build steps, `codeql-config.yml`, matrix `build-mode`s, or third-party SARIF—mutually exclusive)',
        'Default Setup is fastest for broad rollout, whereas Advanced Setup unlocks manual builds, custom query packs, and granular matrix control (disabling Default Setup automatically on switch)',
    ),
    'code_build_modes_matrix': (
        'CodeQL `build-mode` options: `none` (`JS/TS, Python, Ruby & buildless Java`), `autobuild` (`heuristic compiler detection`), and `manual` (`explicit custom build commands in CI for C/C++, C#, Go, Kotlin, Swift`)',
        'selecting build-mode: manual when custom flags/codegen break autobuild—or build-mode: none where supported—eliminates build-wrapper failures cleanly',
    ),
    'code_dataflow_taint_autofix': (
        'Inspect CodeQL `source -> step -> sink` path-problem dataflow traces and apply `Copilot Autofix` (`enabled by default on CodeQL PRs & default branch without requiring a Copilot seat for classic Autofix`)',
        'taint-flow paths pinpoint exact user-input sources and unvalidated sinks, while Copilot Autofix proposes context-aware diffs that must still pass CI and human review',
    ),
    'code_severity_category_dismiss': (
        'Distinguish `security-severity` (`Critical/High/Medium/Low` mapped from CVSS `0.0–10.0`) from rule `problem.severity` (`error/warning/note`), use `category` per matrix leg, and record audited dismissal reasons',
        'branch protection rulesets filter security alerts by Critical/High/Medium/Low security-severity independently from non-security error/warning quality notes',
    ),
    'code_config_models_troubleshoot': (
        'Customize `.github/codeql/codeql-config.yml` (`paths-ignore`, `packs`, `queries`, `threat-models`) & `CodeQL model packs` (`YAML data extensions`), and fix OOM/slow scans via Larger runners or split language matrices',
        'model packs teach CodeQL custom internal framework sources/sanitizers/sinks without forking queries, while Adequate RAM/CPU runners and scoped paths resolve timeout/OOM failures',
    ),

    # ===================== DOMAIN 5: Security Operations =====================
    'ops_cve_cwe_ghsa_advisory': (
        '`CWE` classifies weakness types (`e.g., CWE-89 SQLi`), `CVE` identifies a publicly disclosed vulnerability instance, and `GHSA` (`Repository Security Advisories` + Private Reporting) coordinates private patches & CVEs',
        'maintainers triage private reports inside draft GHSAs, patch silently in temporary private forks (where Actions stay disabled), request a CVE, and publish coordinated advisories',
    ),
    'ops_rulesets_prod_priority': (
        'Prioritize using `has:deployment` + `runtime-risk:internet-exposed` (`Defender for Cloud / artifact registries`), `EPSS`, and `Reachability`, while blocking new regressions via `Require code scanning results` rulesets',
        'combining runtime deployment exposure with pre-merge High/Critical blocking stops alert growth while burning down real internet-exposed production risk first',
    ),
    'ops_campaigns_bulk_remediate': (
        'Run `Security Campaigns` (`<=1,000` default-branch alerts, named security lead, developer notifications, Copilot Autofix, or assigning `<=25` alerts per batch to `@copilot` cloud agent) with audited dismissal comments',
        'grouping related CWEs into focused campaigns builds developer remediation momentum while Copilot Autofix and @copilot PR batches cut manual toil',
    ),
    'ops_query_suites_mrva': (
        'Select CodeQL query suites (`default` high-precision, `security-extended` broader lower-confidence security, `security-and-quality` adds maintainability) and run `Multi-Repository Variant Analysis (MRVA)` in VS Code',
        'security-extended expands vulnerability coverage beyond high-precision default rules, while MRVA hunts novel zero-day patterns across up to 1,000 org repositories simultaneously',
    ),
    'ops_roles_ownership_collab': (
        'Assign `Security Manager` org roles, custom repository alert roles, and per-alert `Assignees` (`noting secret-alert assignment temporarily elevates single-alert view access for repo writers until unassigned`)',
        'clear alert ownership, delegated bypass reviewers, and Evaluate-first cross-suite rulesets align AppSec governance with engineering velocity',
    ),
    'ops_shift_left_preventive': (
        'Layer `Push Protection` (`pre-receive`), `actions/dependency-review-action` (`PR manifest/license gate`), and `CodeQL` PR checks (`with Copilot Autofix`) so secrets, vulnerable packages, and taint flaws fail pre-merge',
        'combining all three shift-left controls prevents new security debt from ever landing on the default branch',
    ),

    # ===================== DOMAIN 6: Security Suites Administration =====================
    'adm_scale_configs_ghec_ghes': (
        'Roll out org/enterprise `Security Configurations` (`GitHub-recommended` or custom, `Apply to new repositories`), contrasting `GHEC` (`metered or volume + cloud AI features`) with `GHES` (`volume-only + GitHub Connect Advisory sync`)',
        'Security Configurations eliminate manual repo drift on GHEC and GHES, while hybrid enterprises link GHES to GHEC via GitHub Connect for Advisory DB updates and committer seat deduplication',
    ),
    'adm_defaults_inheritance_billing': (
        '`Enforced` Security Configurations lock enabled/disabled settings (`except fields set to "Not set"`), while private/internal repos consume `90-day unique active committer` seats (`plus metered AI credits for AI Scan/generic secrets`)',
        'understanding Enforced vs Unenforced inheritance, transferred-repo gaps, 90-day active committer deduplication, and hard budgets on metered SKUs/AI credits prevents surprise overages or lockouts',
    ),
    'adm_policies_bypass_audit': (
        'Enforce Enterprise Advanced Security policies (`restricting repo admins while preserving Org Owner/Security Manager control`), scope ruleset/push-protection bypass actors, and stream `security_configuration.*` / alert audit logs',
        'enterprise policies prevent uncontrolled repo-admin license consumption while audit log streaming preserves tamper-evident compliance records across configuration and bypass events',
    ),
    'adm_roles_custom_permissions': (
        'Separate `Enterprise/Org Owners` (`billing & global policy`), `Security Managers` (`org-wide alert read/write & security config management, without code-write`), and custom repository roles (`granular view/dismiss per tool`)',
        'Security Manager and fine-grained custom repository roles grant AppSec and security champions exact triage permissions without over-provisioning Repository Admin or code-push rights',
    ),
    'adm_codeql_workflows_apis': (
        'Enforce approved CodeQL scanning via Org/Enterprise `Rulesets` (`Require code scanning results` + Required Workflows) and automate governance via REST/GraphQL (`code-security/configurations`, org alert endpoints & billing APIs)',
        'combining Rulesets with REST/GraphQL security configuration and org-level alert APIs automates compliance reporting and zero-drift enforcement across thousands of repositories',
    ),

    # ===================== EXACT CLI / YAML / REST / FILTER COMPLETION KEYS =====================
    'cfg_secret_scanning_paths_ignore': (
        '`.github/secret_scanning.yml` containing `paths-ignore:` (`<= 1,000` glob entries and `<= 1 MB` total file size)',
        'secret_scanning.yml uses paths-ignore globs (up to 1,000 entries and 1 MB) to auto-close user alerts in fixture directories',
    ),
    'cfg_custom_role_bypass_perm': (
        '`Review and manage secret scanning bypass requests` (`fine-grained organization role permission for Push Protection delegated bypass`)',
        'granting Review and manage secret scanning bypass requests creates least-privilege Push Protection approvers without full Org Owner access',
    ),
    'cfg_dep_review_fail_severity': (
        '`actions/dependency-review-action@v4` with `fail-on-severity: high`, `fail-on-scopes: runtime`, and `deny-licenses` (`or allow-licenses`, never both)',
        'dependency-review-action@v4 gates pull requests on severity, dependency scope, and SPDX license policy using a single allow OR deny list',
    ),
    'cfg_dependabot_groups_registries': (
        '`.github/dependabot.yml` with `groups:` (`update-types: [minor, patch]`) and `registries:` referencing `${{ secrets.<TOKEN> }}` stored in `Dependabot secrets`',
        'dependabot.yml groups reduce PR noise and authenticate private feeds using credentials stored specifically in Dependabot secrets',
    ),
    'cfg_sbom_rest_endpoint': (
        '`GET /repos/{owner}/{repo}/dependency-graph/sbom` (`exporting the repository dependency inventory in SPDX JSON format`)',
        'the Dependency Graph SBOM REST endpoint returns upstream direct and transitive packages in machine-readable SPDX JSON',
    ),
    'cfg_autotriage_filter_query': (
        '`resolution:auto-dismiss` (`alert filter matching findings automatically dismissed by preset or custom Dependabot auto-triage rules`)',
        'querying is:closed resolution:auto-dismiss audits every Dependabot alert suppressed by preset or custom auto-triage rules',
    ),
    'cfg_sarif_upload_permissions': (
        '`permissions: { security-events: write, contents: read, actions: read }` on `github/codeql-action/upload-sarif@v3`',
        'uploading CodeQL or third-party SARIF 2.1.0 findings from GitHub Actions requires least-privilege security-events: write permission',
    ),
    'cfg_codeql_build_mode_manual': (
        '`build-mode: manual` (`paired with explicit compiler commands prior to github/codeql-action/analyze@v3`)',
        'build-mode: manual traces exact custom C/C++, C#, Go, Java/Kotlin, or Swift compiler invocations when autobuild heuristics fail',
    ),
    'cfg_codeql_config_packs_models': (
        '`.github/codeql/codeql-config.yml` (`defining packs:, queries:, paths-ignore:, and threat-models: alongside YAML model-pack extensions`)',
        'codeql-config.yml centralizes custom query packs, path exclusions, threat models, and data-extension model packs for Advanced Setup',
    ),
    'cfg_codeql_cli_upload_cmd': (
        '`codeql github upload-results --repository=<org/repo> --ref=<refs/heads/main> --commit=<sha> --sarif=<results.sarif>`',
        'codeql github upload-results publishes externally generated SARIF 2.1.0 files to GitHub Code Scanning with exact ref and commit metadata',
    ),
    'cfg_sec_overview_prod_qualifiers': (
        '`has:deployment runtime-risk:internet-exposed` (`Security Overview and alert search qualifiers powered by ingested deployment metadata`)',
        'filtering by has:deployment and runtime-risk:internet-exposed isolates alerts affecting live internet-reachable workloads',
    ),
    'cfg_query_suite_security_extended': (
        '`queries: security-extended` (`executing default high-precision CodeQL security rules plus medium-precision security queries without style/quality rules`)',
        'security-extended broadens vulnerability detection beyond default without adding non-security maintainability noise from security-and-quality',
    ),
    'cfg_rest_org_security_configs': (
        '`POST /orgs/{org}/code-security/configurations/{configuration_id}/attach` (`attaching a Security Configuration across selected or all org repos via REST`)',
        'the code-security configurations attach endpoint programmatically binds a Security Configuration to targeted or organization-wide repositories',
    ),

    # ===================== MULTI-SELECT ATOMIC PAIRINGS =====================
    'ms_d1_secret_protection_scope': (
        '`GitHub Secret Protection` prevents and detects leaked credentials via `Push Protection`, `secret scanning`, `validity checks`, custom patterns, and AI generic secret detection',
        'Secret Protection focuses specifically on credential exposure in pushes and Git history',
    ),
    'ms_d1_code_security_scope': (
        '`GitHub Code Security` finds and fixes code and dependency risks via `CodeQL` / `SARIF` code scanning, `Copilot Autofix`, `Dependency Review` on private repos, and `Security Campaigns`',
        'Code Security covers first-party SAST, Copilot Autofix, and private-repository Dependency Review enforcement',
    ),
    'ms_d1_dismiss_reason_comment': (
        'Require an accurate dismissal reason (`False positive`, `Used in tests`, or `Won\'t fix`) with a reviewer-auditable justification comment whenever dismissing an alert',
        'structured dismissal reasons and comments create an auditable compliance trail in webhooks and GraphQL/REST APIs',
    ),
    'ms_d1_alert_audit_monitoring': (
        'Monitor dismissed and open alert trends centrally in `Security Overview` and `Audit Logs` (`repository_vulnerability_alert`, `secret_scanning_alert`, `code_scanning_alert`)',
        'Security Overview and org audit logs surface anomalous dismissal spikes or unpatched high-risk repositories',
    ),
    'ms_d2_push_block_prereceive': (
        '`Push Protection` blocks high-confidence partner and published custom secrets pre-receive during `git push` before commits land on GitHub',
        'stopping secrets pre-receive prevents Git history contamination and emergency credential rotation',
    ),
    'ms_d2_validity_active_triage': (
        '`Validity checks` verify supported partner tokens (`Active` vs `Inactive`) so responders remediate live exploitable credentials immediately',
        'Active validation status gives AppSec teams high-signal prioritization during incident triage',
    ),
    'ms_d2_delegated_bypass_actors': (
        'Assign `Specific roles, visible teams, or custom org roles` (`never secret teams`) to the Push Protection delegated bypass list to review and approve contributor bypass requests',
        'delegated bypass centralizes exception approvals in visible accountable security teams or roles',
    ),
    'ms_d2_bypass_audit_webhook': (
        'Audit every Push Protection bypass request, approval, and exemption via `secret_scanning_push_protection_bypass` audit events, alert timelines, and webhooks',
        'every bypass leaves an immutable audit trail linking the actor, commit, justification, and approver',
    ),
    'ms_d3_epss_reachability': (
        'Combine `EPSS` (`30-day exploitation probability`) and static `Reachability` call-path verdicts with `CVSS` severity and `runtime` dependency scope',
        'high-EPSS reachable runtime vulnerabilities represent immediate real-world exploit risk compared with unreachable dev-only packages',
    ),
    'ms_d3_autotriage_before_notify': (
        'Use `Dependabot auto-triage rules` to auto-dismiss or snooze low-impact dev/unpatched alerts (`resolution:auto-dismiss`) **before** alert notifications fire',
        'evaluating auto-triage rules prior to notifications eliminates alert fatigue while keeping alerts auditable and auto-reopenable',
    ),
    'ms_d3_dep_review_severity_license': (
        'Configure `actions/dependency-review-action@v4` with `fail-on-severity`, `fail-on-scopes`, and either `allow-licenses` OR `deny-licenses` (`SPDX` IDs)',
        'Dependency Review blocks both vulnerable package versions and prohibited copyleft/unknown licenses on pull requests',
    ),
    'ms_d3_required_status_ruleset': (
        'Mark the `Dependency Review` workflow job as a **required status check** in a repository or organization Branch Ruleset targeting `main`',
        'without a required status check rule, a failing Dependency Review workflow warns on the PR without blocking merge',
    ),
    'ms_d3_dependabot_readonly_secrets': (
        'Workflows triggered by `dependabot` PRs receive a **read-only `GITHUB_TOKEN`** by default and access credentials stored in **`Dependabot secrets`** (`not standard Actions secrets on untrusted triggers`)',
        'isolating Dependabot secrets and read-only default tokens protects repository secrets if a compromised upstream package alters build scripts',
    ),
    'ms_d4_sarif_10mb_5000_cap': (
        'Ensure each uploaded `SARIF 2.1.0` file is `<= 10 MB` gzip-compressed and `<= 25,000` results (`knowing GitHub displays only the top 5,000 results prioritized by severity`)',
        'exceeding 10 MB gzipped rejects the upload outright, while noisy rule sets over 5,000 findings truncate lower-priority alerts',
    ),
    'ms_d4_category_partial_fingerprint': (
        'Assign a unique `category` per tool/language/monorepo target and preserve stable `ruleId` + `partialFingerprints` so alerts deduplicate cleanly without overwriting sibling scans',
        'distinct categories prevent multi-job uploads on the same commit from clobbering one another, while fingerprints track alerts across line shifts',
    ),
    'ms_d4_autofix_ci_human_review': (
        'Validate every `Copilot Autofix` suggestion by inspecting dataflow context, running full CI unit/integration tests + re-scanning with `CodeQL`, and completing human PR review',
        'LLM-generated security fixes lower remediation friction dramatically, yet still require automated test and human semantic verification before merge',
    ),
    'ms_d5_prod_context_mdc_jfrog': (
        'Ingest deployment metadata (`from Microsoft Defender for Cloud, JFrog Artifactory, or CI/CD APIs`) to filter `has:deployment` and `runtime-risk:internet-exposed` alerts',
        'production context pinpoints vulnerabilities actually running in internet-facing workloads rather than dead or archived repos',
    ),
    'ms_d5_ruleset_evaluate_to_active': (
        'Pilot cross-repository `Rulesets` in **`Evaluate` mode** to measure would-be blocked PRs via Ruleset Insights before switching enforcement to **`Active`**',
        'Evaluate mode surfaces missing scans or noisy rules safely without halting production releases on day one',
    ),
    'ms_d6_committer_90day_dedup': (
        'Count `90-day unique active committers` across private/internal repos (`deduplicating each human user once across the enterprise, plus GitHub Connect sync between GHEC and GHES`)',
        'a developer pushing to 50 GHAS-enabled repos in an enterprise consumes only one active-committer license seat over the rolling 90-day window',
    ),
    'ms_d6_ai_credits_hard_budget': (
        'Monitor `Code Security AI credits` (`AI Scan / agentic autofix`) and `Secret Protection AI credits` (`AI push scanning`), setting **hard metered budgets** to cap spend',
        'classic CodeQL Copilot Autofix does not consume AI credits, whereas agentic autofix / AI Scan and AI push secret scanning draw from included or metered AI credit pools',
    ),

    # ===================== PROPOSED SOLUTION: YES + 8 DISTINCT NO TRAPS =====================
    'sol_yes': (
        'Yes — this configuration satisfies every security, licensing, and governance requirement',
        'every required GitHub Security suite setting, permission boundary, and enforcement rule is properly configured',
    ),
    'sol_no_dismiss_not_revocation': (
        'No — dismissing a Secret Protection alert or deleting the line in a new commit leaves the live credential active and exposed in prior Git history (`revoke & rotate first, then purge history`)',
        'alert dismissal only updates GitHub UI/API triage status; attackers can still extract unrotated keys from earlier commits, clones, or reflogs',
    ),
    'sol_no_secret_yaml_not_push_block': (
        'No — `.github/secret_scanning.yml` `paths-ignore` only auto-closes post-push user alerts (`<=1,000` paths / `<=1 MB`) and neither revokes keys nor replaces Push Protection / public partner alerts',
        'secret_scanning.yml suppresses user notifications in excluded folders rather than blocking pushes or cancelling public-repo partner revocations',
    ),
    'sol_no_mutually_exclusive_licenses': (
        'No — `actions/dependency-review-action` forbids specifying `allow-licenses` and `deny-licenses` together, and fails to block merges unless marked as a required status check on `pull_request`',
        'allow-licenses and deny-licenses are mutually exclusive inputs in dependency-review-action, and branch rulesets must require the check to block merging',
    ),
    'sol_no_sec_updates_block_custom_pr': (
        'No — repository-wide `Dependabot security updates` must be **disabled** before a custom Dependabot auto-triage `Open a pull request` rule can selectively control which alerts open PRs',
        'when global Dependabot security updates remain enabled, Dependabot attempts PRs for every patchable alert, overriding selective custom PR auto-triage rules',
    ),
    'sol_no_default_conflicts_advanced': (
        'No — CodeQL `Default Setup` and custom `Advanced Setup` (`.github/workflows/codeql.yml`) cannot run active CodeQL management simultaneously (`switch to Advanced Setup with build-mode: manual`)',
        'enabling Advanced Setup disables Default Setup so custom workflow build steps, codeql-config.yml, or custom query suites govern scanning cleanly without duplicate conflicts',
    ),
    'sol_no_sarif_over_10mb_or_cat': (
        'No — Code Scanning rejects gzip-compressed SARIF files larger than `10 MB` (`and overwrites prior alerts when multiple matrix uploads share an identical SARIF category on one commit`)',
        'each gzipped SARIF upload must be <=10 MB with a distinct category per language/tool/component and security-events: write permission',
    ),
    'sol_no_not_set_unlocked_enforced': (
        'No — leaving a feature at `"Not set"` inside an `Enforced` Security Configuration leaves that specific setting editable by repository admins (`explicitly set Enabled or Disabled to lock it`)',
        'Enforced locks only explicitly configured Enabled/Disabled rows; Not set intentionally delegates control to individual repositories',
    ),
    'sol_no_advisory_fork_no_actions': (
        'No — temporary private forks created inside a Repository Security Advisory (`GHSA`) intentionally **disable GitHub Actions** (`and pushing fixes to a public branch before release leaks the zero-day`)',
        'validate advisory patches locally or in an isolated private mirror without exposing exploit diffs publicly before publishing the coordinated GHSA release',
    ),

    # ===================== DISTRACTOR-ONLY TRAPS (bad_* — never keyed correct) =====================
    'bad_dismiss_deletes_git_history': (
        'Dismiss the alert as `Won\'t fix` in the Security tab, which automatically rewrites Git commit history and revokes the live token at AWS/Stripe',
        'dismissing a GitHub alert never rewrites Git commits or contacts external cloud providers to revoke active credentials',
    ),
    'bad_gitignore_scans_retroactive': (
        'Add `.env` and `keys/` to `.gitignore` on `main`, which purges historical commits and blocks `git push` via Secret Protection automatically',
        '.gitignore only ignores untracked local working-tree files; it never purges committed Git history or enables Secret Protection Push Protection',
    ),
    'bad_secret_team_delegated_bypass': (
        'Add a hidden **secret organization team** (`visible only to team members`) to the Push Protection delegated bypass list so reviewers remain anonymous',
        'GitHub explicitly prohibits adding secret teams to Push Protection delegated bypass lists; only visible teams, roles, or custom roles are supported',
    ),
    'bad_nonprovider_partner_validity': (
        'Rely on automatic partner validity checks and Push Protection by default on all non-provider generic patterns (`such as PostgreSQL URLs and RSA keys`) without extra config',
        'non-provider patterns do not support partner validity checks (there is no single central SaaS vendor to query), and generic push protection requires explicit pattern enablement',
    ),
    'bad_sbom_includes_dependents': (
        'Export the repository SBOM from Dependency Graph to get a complete list of external downstream consumer repositories (`dependents`) that import your library',
        'an SPDX SBOM inventories upstream direct and transitive dependencies used BY your repository—it never lists downstream dependents',
    ),
    'bad_both_allow_and_deny_licenses': (
        'Specify both `allow-licenses: MIT, Apache-2.0` and `deny-licenses: GPL-3.0, AGPL-3.0` together in the same `actions/dependency-review-action@v4` step',
        'allow-licenses and deny-licenses are mutually exclusive in dependency-review-action; passing both causes a configuration validation failure',
    ),
    'bad_malware_preset_opens_fix_pr': (
        'Enable the `Dismiss package malware alerts` preset so Dependabot automatically opens pull requests upgrading malicious packages across all versions',
        'Dependabot never opens PRs for malware alerts, and Dismiss package malware alerts auto-dismisses all-version malware collisions for internal package names',
    ),
    'bad_sarif_50mb_xml_contents_read': (
        'Upload a `50 MB` uncompressed XML report using `actions/upload-artifact@v4` with only `contents: read` permissions so Code Scanning parses alerts',
        'Code Scanning requires valid SARIF 2.1.0 (`<=10 MB` gzipped) uploaded via `codeql-action/upload-sarif` or `codeql github upload-results` with `security-events: write`',
    ),
    'bad_build_mode_none_cpp_swift': (
        'Set `build-mode: none` for compiled `C/C++` and `Swift` repositories so CodeQL skips compilation while maintaining 100% semantic AST/type coverage',
        'C/C++ and Swift require traced compilation (`autobuild` or `manual`); `build-mode: none` is supported only for interpreted languages plus buildless Java (and preview C#/Python/JS/Ruby)',
    ),
    'bad_autofix_requires_copilot_ent': (
        'Purchase `GitHub Copilot Enterprise` (`$39/user/month`) seats for every developer first, because classic `CodeQL` Copilot Autofix refuses to run without individual Copilot licenses',
        'classic Copilot Autofix for CodeQL code scanning is included with GitHub Code Security (and public repos) without requiring individual GitHub Copilot subscriptions',
    ),
    'bad_ghes_metered_billing_default': (
        'Switch standalone air-gapped `GitHub Enterprise Server (GHES)` directly to pay-as-you-go metered billing without contacting Sales or configuring GitHub Connect',
        'standalone GitHub Enterprise Server instances use volume/subscription licenses exclusively; metered GHAS/Code Security/Secret Protection billing applies on GitHub.com (GHEC/Team)',
    ),
    'bad_disallowing_org_disables_active': (
        'Set Enterprise policy `Repository administrators can enable or disable GitHub Code Security = Disabled`, which immediately turns off CodeQL on all already-enabled repos and blocks Org Owners',
        'disallowing repository-admin enablement prevents repo admins from toggling additional repos, but leaves already-enabled repos active and never blocks Organization Owners or Security Managers',
    ),
    'bad_all_repo_contributors_seats': (
        'Count every historical Git author since repository creation (`plus read-only issue commenters`) toward `GitHub Secret Protection` active-committer license seats',
        'active-committer licensing counts only unique accounts that pushed commits to at least one enabled private/internal repository within the rolling last 90 days',
    ),
    'bad_security_manager_full_code_admin': (
        'Assign `Organization Owner` (`or Repository Admin`) to every AppSec analyst because `Security Manager` cannot view Security Overview or manage Security Configurations',
        'the built-in Security Manager organization role grants org-wide alert read/write, Security Overview, and Security Configuration management without granting code-write or billing-owner privileges',
    ),
}

TERMS = {**ATOMIC_TERMS, **SEQUENCE_TERMS}

assert len(ATOMIC_TERMS) == 102, f'Expected 102 atomic terms, got {len(ATOMIC_TERMS)}'
assert len(TERMS) == 142, f'Expected 142 total terms, got {len(TERMS)}'
for _k, (_lbl, _note) in TERMS.items():
    assert len(_lbl) <= 245, f'{_k} label len {len(_lbl)} > 245'
    assert len(_note) <= 200, f'{_k} note len {len(_note)} > 200'
