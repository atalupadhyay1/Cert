"""10 four-step sequence families (40 entries) for Exam GH-500: GitHub Advanced Security."""

SEQUENCE_TERMS = {
    # 1. Domain 1 (1.4): Prevention-first end-to-end SDLC workflow
    'seq_sdlc_shift_left_ok': (
        'Block secrets pre-receive via Push Protection → run Dependency Review & CodeQL on the PR → apply Copilot Autofix or patch vulnerable packages before merge → monitor default-branch advisories in Security Overview',
        'a prevention-first secure SDLC stops secrets at git push, blocks vulnerable PR code/dependencies with pre-merge checks and Autofix, and continuously monitors post-merge advisories',
    ),
    'seq_sdlc_shift_left_w1': (
        'Merge PRs without checks to main → run weekly manual secret scans → disable Push Protection to avoid developer friction → export CSVs quarterly without remediating open alerts',
        'deferring secret and code checks until after merge exposes live credentials in Git history and turns security into high-cost reactive firefighting',
    ),
    'seq_sdlc_shift_left_w2': (
        'Apply Copilot Autofix before running CodeQL → run Push Protection only after merging to main → skip Dependency Review on lockfiles → delete Security Overview roles',
        'Copilot Autofix requires an upstream CodeQL finding first, and Push Protection intercepts secrets during git push rather than post-merge',
    ),
    'seq_sdlc_shift_left_w3': (
        'Dismiss all PR alerts automatically → merge vulnerable dependencies → run Dependency Review only on archived branches → rely on gitignore to revoke leaked API tokens',
        'auto-dismissing unreviewed PR findings defeats shift-left prevention, and .gitignore never revokes already-exposed credentials',
    ),

    # 2. Domain 2 (2.3): Secret Protection leak incident response & Git history purge
    'seq_secret_leak_remediate_ok': (
        'Confirm alert validity & blast radius → revoke and rotate the compromised credential at the provider → purge commit history (`git filter-repo`) & contact Support if cached PRs remain → resolve the alert as Revoked',
        'once a secret reaches Git history, revoking/rotating the live key comes first, followed by history rewrite/cache purge and marking the alert Revoked for auditability',
    ),
    'seq_secret_leak_remediate_w1': (
        'Dismiss the alert as Won\'t fix → delete the line in a new commit while keeping the live key active → add the file to .gitignore → assume old commits are unreadable',
        'deleting a secret in a follow-up commit leaves the active credential exposed in prior Git commits, reflogs, and clones without revoking access',
    ),
    'seq_secret_leak_remediate_w2': (
        'Run git filter-repo first while leaving the production key active for 30 days → disable Secret Protection to clear UI banners → rotate the key only if an outage occurs → skip audit notes',
        'delaying credential revocation leaves attackers able to exploit copies harvested from webhooks, clones, or cached diffs while history is rewritten',
    ),
    'seq_secret_leak_remediate_w3': (
        'Add paths-ignore in .github/secret_scanning.yml to auto-close the live production key alert → keep the credential unrotated → merge to main → archive the audit log',
        'using secret_scanning.yml to silence an active production credential leak hides the alert without revoking or rotating the compromised secret',
    ),

    # 3. Domain 2 (2.6 — odd sets): Custom secret pattern creation, dry run, publish & Push Protection
    'seq_custom_secret_pattern_ok': (
        'Define pattern name, regex & test strings (`or Generate with AI`) → run `Save and dry run` across representative repos → refine regex/context to eliminate false positives → `Publish pattern` & enable Push Protection',
        'custom secret patterns require dry-run validation (up to 1,000 sample matches without creating live alerts) and publication before Push Protection can be enabled',
    ),
    'seq_custom_secret_pattern_w1': (
        'Enable Push Protection before publishing the pattern → publish an untested `.*` wildcard regex org-wide → review 50,000 live developer alerts → run a dry run afterward',
        'GitHub disables the Push Protection toggle until a custom pattern passes dry-run testing and is published, and broad untested regexes flood teams with false positives',
    ),
    'seq_custom_secret_pattern_w2': (
        'Commit custom regexes into .gitignore → skip dry runs because AI regexes are deterministic → assign secret teams to delegated bypass → expect partner validity checks on custom tokens',
        '.gitignore does not configure Secret Protection, AI-generated regexes still require dry-run validation, and secret teams cannot be added to bypass lists',
    ),
    'seq_custom_secret_pattern_w3': (
        'Publish the pattern on a personal Free repo → expect Enterprise-wide enforcement automatically → edit the pattern assuming prior version alerts stay open → skip test strings',
        'Enterprise/Org custom patterns are configured in Org/Enterprise settings, and saving edits to an existing custom pattern closes alerts created by its prior version',
    ),

    # 4. Domain 3 (3.2 — even sets): Dependabot custom auto-triage rule rollout for targeted PRs
    'seq_dependabot_autotriage_ok': (
        'Enable Dependency Graph & Dependabot alerts → disable global `Dependabot security updates` where custom PR rules govern → create an org/repo auto-triage rule targeting EPSS/severity/scope → audit `resolution:auto-dismiss` & targeted PRs',
        'custom Dependabot auto-triage rules run before notifications, and repository-wide Dependabot security updates must be off when using custom rules to selectively open security PRs',
    ),
    'seq_dependabot_autotriage_w1': (
        'Disable Dependabot alerts completely → keep global Dependabot security updates enabled → create an `Open a pull request` rule for malware alerts → expect dismissed dev alerts never to reopen on runtime promotion',
        'auto-triage rules require Dependabot alerts enabled, global security updates override selective PR rules, malware alerts do not open PRs, and scope changes auto-reopen alerts',
    ),
    'seq_dependabot_autotriage_w2': (
        'Put auto-triage EPSS rules inside .github/secret_scanning.yml → expect repo rules to override enforced org rules → delete audit logs → manually email developers before rules evaluate',
        'Dependabot auto-triage rules live in Dependabot settings (where org rules override conflicting repo rules and evaluate before notifications), not secret_scanning.yml',
    ),
    'seq_dependabot_autotriage_w3': (
        'Export an SPDX SBOM → delete package-lock.json so transitive packages disappear → enable `Dismiss package malware alerts` to block zero-days → skip reachability review',
        'deleting lockfiles blinds transitive vulnerability detection, and the Dismiss package malware alerts preset suppresses false-positive internal namespace collisions rather than blocking malware',
    ),

    # 5. Domain 3 (3.4 — all sets): Pre-merge Dependency Review gate with branch ruleset enforcement
    'seq_dep_review_pr_gate_ok': (
        'Enable the Dependency Graph (`and Code Security on private repos`) → add an `on: pull_request` workflow running `actions/dependency-review-action@v4` → configure `fail-on-severity` & `deny-licenses` → mark the check required in a branch ruleset',
        'Dependency Review compares PR base-vs-head manifests/lockfiles via the Dependency Graph and blocks vulnerable or non-compliant licenses when required on protected branches',
    ),
    'seq_dep_review_pr_gate_w1': (
        'Trigger `dependency-review-action` only on weekly cron `schedule` → pass both `allow-licenses` and `deny-licenses` simultaneously → disable the Dependency Graph → leave main unprotected',
        'dependency-review-action requires pull_request base/head diffs and an active Dependency Graph, and allow-licenses / deny-licenses are mutually exclusive',
    ),
    'seq_dep_review_pr_gate_w2': (
        'Add SPDX license names to `.github/dependabot.yml` → expect Dependabot version updates to block developer PR merges → skip required status checks → disable lockfiles',
        'dependabot.yml schedules dependency update PRs rather than gating developer PRs on license compliance; pre-merge gating requires dependency-review-action plus required checks',
    ),
    'seq_dep_review_pr_gate_w3': (
        'Run `dependency-review-action` on an unlicensed private Free repo → grant `write-all` permissions to untrusted fork code → ignore `fail-on-scopes` → merge failing checks freely',
        'private repositories require GitHub Code Security / GHAS for Dependency Review, contents: read suffices, and unenforced checks do not block merges',
    ),

    # 6. Domain 4 (4.2 — all sets): External CI CodeQL CLI analysis and SARIF upload lifecycle
    'seq_codeql_cli_sarif_ok': (
        'Install the CodeQL CLI bundle on the CI agent → run `codeql database create` (`tracing compiled builds`) → run `codeql database analyze --format=sarif-latest` → run `codeql github upload-results` (`--sarif`, `--ref`, `--commit`)',
        'external CI integrations create the semantic CodeQL database, execute query suites into SARIF 2.1.0 (`<=10 MB` gzipped), and upload results with `security_events` write auth',
    ),
    'seq_codeql_cli_sarif_w1': (
        'Run `codeql github upload-results` on raw `.java` source files → run `codeql database analyze` before `codeql database create` → upload an uncompressed 45 MB XML report → omit `--ref` and `--commit`',
        'CodeQL cannot upload raw source files or XML; a database must be created before analysis, and SARIF 2.1.0 uploads must be <=10 MB gzipped with target ref and commit SHA',
    ),
    'seq_codeql_cli_sarif_w2': (
        'Enable Default Setup simultaneously for the same language/category → upload SARIF with a read-only `contents: read` token → strip `partialFingerprints` → expect >25,000 results to render without truncation',
        'Default Setup conflicts with custom/external CodeQL uploads, uploading SARIF requires security-events: write, and runs cap at 25,000 results (displaying top 5,000)',
    ),
    'seq_codeql_cli_sarif_w3': (
        'Create one shared SARIF file without `--sarif-category` across 6 monorepo services → overwrite prior language alerts on every upload → disable GitHub Code Security on private repos → view alerts in Actions cache',
        'omitting distinct SARIF categories causes subsequent uploads for the same commit to overwrite/mark prior component results stale, and private repos require Code Security',
    ),

    # 7. Domain 5 (5.1 — odd sets): Private Repository Security Advisory (GHSA) & CVE workflow
    'seq_ghsa_private_advisory_ok': (
        'Triage the report via Private Vulnerability Reporting (`draft GHSA`) → open a temporary private fork from the advisory to develop & verify the fix → request a `CVE` & prepare patched versions → merge the fix & publish the advisory',
        'repository security advisories keep vulnerability details confidential in a temporary private fork until a verified patch is ready to release alongside coordinated GHSA/CVE disclosure',
    ),
    'seq_ghsa_private_advisory_w1': (
        'Publish the unpatched exploit details in a public GitHub Issue immediately → ask developers to commit fixes on a public feature branch → request a CVE before confirming the bug → create a draft advisory last',
        'publishing zero-day exploit steps in public issues or public branches before a fix exists exposes all downstream users to active exploitation',
    ),
    'seq_ghsa_private_advisory_w2': (
        'Open a temporary private fork and run GitHub Actions workflows directly inside that advisory fork → auto-merge without review → delete the GHSA after release so downstream Dependabot alerts never fire',
        'temporary private advisory forks intentionally disable GitHub Actions to prevent side-channel leaks, and publishing the GHSA is what powers downstream Dependabot alerts',
    ),
    'seq_ghsa_private_advisory_w3': (
        'Dismiss the researcher report without reading it → rotate unrelated SSH keys → add the vulnerable source folder to `secret_scanning.yml` → expect CVEs to assign without advisory metadata',
        'secret_scanning.yml only filters secret-scanning paths and has nothing to do with patching or disclosing CWE/CVE code vulnerabilities',
    ),

    # 8. Domain 5 (5.3 — all sets): Security Campaign creation and Copilot-assisted remediation
    'seq_security_campaign_autofix_ok': (
        'Filter high-risk default-branch alerts in Security Overview → create a Security Campaign (`<=1,000` alerts) with due date & contact → trigger Copilot Autofix (`or assign <=25 alerts to @copilot`) → verify CI checks & track burndown',
        'Security Campaigns group high-risk default-branch alerts around a dedicated security contact and accelerate developer burndown with Copilot Autofix or @copilot draft PRs',
    ),
    'seq_security_campaign_autofix_w1': (
        'Create a campaign containing 50,000 unmerged fork-branch alerts with no contact owner → auto-merge Copilot suggestions bypassing CI tests → revoke developer write access → close the campaign with alerts still open',
        'code security campaigns target default-branch alerts (up to 1,000 per campaign) with a named contact, and developers need write access plus passing CI checks to merge fixes',
    ),
    'seq_security_campaign_autofix_w2': (
        'Export alerts to a static spreadsheet with no GitHub links → disable CodeQL so open counts fall to zero → bulk-dismiss every alert without comments → report 100% remediation',
        'disabling scanners or bulk-dismissing unreviewed findings hides real production vulnerabilities rather than remediating security debt',
    ),
    'seq_security_campaign_autofix_w3': (
        'Assign 500 alerts in one batch to `@copilot` without AI credits or branch protection → skip human PR review → disable Security Overview → expect secret campaigns to auto-rotate AWS IAM keys',
        'agentic @copilot campaign assignments cap at 25 alerts per batch (opening a PR for human/CI verification), and Copilot cannot rotate external cloud provider IAM credentials',
    ),

    # 9. Domain 6 (6.1 — all sets): Organization/Enterprise Security Configuration staged rollout
    'seq_security_config_rollout_ok': (
        'Verify committer license headroom (`or metered budget`) → create/select a Security Configuration → attach to tiered repos (`custom properties`) & enable `Apply to new repositories` → set `Enforced` to lock baseline controls',
        'rolling out Security Configurations verifies committer license capacity first, targets repo tiers via custom properties, covers newly created repos, and locks drift with Enforced mode',
    ),
    'seq_security_config_rollout_w1': (
        'Apply an `Enforced` configuration across 2,000 private repos with zero available committer seats → set every feature to `Not set` expecting strict locks → leave new repositories uncovered → disable audit logs',
        'exceeding volume committer licenses blocks enablement on additional/new private repos, and features left as Not set remain editable by repository admins even under Enforced configurations',
    ),
    'seq_security_config_rollout_w2': (
        'Manually toggle Settings on 2,000 repositories one by one → grant every developer Organization Owner permissions → disable Push Protection globally → rely on `.gitignore` for enterprise governance',
        'manual per-repo changes do not scale or prevent configuration drift, and granting Organization Owner violates least privilege when Security Manager / Security Configurations exist',
    ),
    'seq_security_config_rollout_w3': (
        'Enable cloud-only Copilot Autofix on an air-gapped GHES instance with metered billing → skip GitHub Connect → expect transferred external repos to inherit new-repo defaults automatically without policy checks',
        'standalone GHES uses volume/subscription licensing (not metered billing) and requires GitHub Connect for Advisory DB sync, while transferred repos must be explicitly targeted by configurations',
    ),

    # 10. Domain 6 (6.5 — even sets): Organization Ruleset enforcing CodeQL code scanning results safely
    'seq_org_ruleset_code_scan_ok': (
        'Standardize CodeQL across target repos → create an Org Branch Ruleset in `Evaluate` mode with `Require code scanning results` (`High+` security severity) → audit Evaluate insights & scope bypass actors → switch enforcement to `Active`',
        'piloting an Organization Ruleset in Evaluate mode confirms CodeQL check reporting and false-positive impact before switching Require code scanning results to Active merge blocking',
    ),
    'seq_org_ruleset_code_scan_w1': (
        'Set an Org Ruleset to `Active` requiring `CodeQL` results before enabling CodeQL on any repo → grant `All repository writers` bypass access → set thresholds to `Note` style warnings → disable PR scans',
        'requiring CodeQL results before CodeQL runs deadlocks every PR awaiting a missing scan, while granting broad writer bypass or blocking on Note hints breaks governance',
    ),
    'seq_org_ruleset_code_scan_w2': (
        'Configure branch protection individually in `.github/secret_scanning.yml` → allow Copilot Autofix comments to count as human PR approvals → skip `Evaluate` mode → delete Security Manager access',
        'secret_scanning.yml only configures secret path exclusions, and AI suggestions never replace required human pull-request approvals',
    ),
    'seq_org_ruleset_code_scan_w3': (
        'Disable `pull_request` triggers in `codeql.yml` so scans run only monthly on `main` → enforce `Require code scanning results` on feature PRs → expect instant green PR gates',
        'Require code scanning results blocks PR merges until the configured tool reports scan results for that pull request head/merge ref',
    ),
}

assert len(SEQUENCE_TERMS) == 40, f'Expected 40 sequence terms, got {len(SEQUENCE_TERMS)}'
for _k, (_lbl, _note) in SEQUENCE_TERMS.items():
    assert len(_lbl) <= 245, f'{_k} label len {len(_lbl)} > 245'
    assert len(_note) <= 200, f'{_k} note len {len(_note)} > 200'
