"""Official July 2026 Exam GH-500 (GitHub Advanced Security) domains, 34 skills, and documentation URLs."""

STUDY_GUIDE_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500'
CERT_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/github-advanced-security/'
CERT_PAGE_URL = CERT_URL
LEARN_PATH_1_URL = 'https://learn.microsoft.com/en-us/training/paths/github-advanced-security/'
LEARN_PATH_2_URL = 'https://learn.microsoft.com/en-us/training/paths/github-advanced-security-2/'
EXAM_EXPERIENCE_URL = 'https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience'

BLUEPRINT_EFFECTIVE_DATE = 'July 2026 (Last updated May 14, 2026)'

DOMAINS = {
    '1': 'Describe GitHub Security suites, features, and ecosystem',
    '2': 'Configure and use Secret Protection (formerly secret scanning)',
    '3': 'Configure and use supply chain security (formerly Dependabot/Dependency Review)',
    '4': 'Configure and use Code Security (formerly Code Scanning with CodeQL)',
    '5': 'Security operations: best practices, prioritization, and remediation',
    '6': 'GitHub Security suites administration',
}

DOMAIN_WEIGHTS = {
    '1': ('15–20%', 18, 3),
    '2': ('15–20%', 18, 3),
    '3': ('15–20%', 18, 3),
    '4': ('10–15%', 14, 2),
    '5': ('15–20%', 18, 3),
    '6': ('10–15%', 14, 2),
}

SKILLS = {
    # Domain 1 — Describe GitHub Security suites, features, and ecosystem (18 items: 6 skills x 3)
    '1.1': (
        '1',
        'Describe GitHub Security suite structure, navigation, and contrast Code Security, Secret Protection, and Supply Chain Security',
        'https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security',
    ),
    '1.2': (
        '1',
        'Differentiate security feature availability for public repositories vs. enterprise environments and explain Security Overview',
        'https://docs.github.com/en/code-security/security-overview/about-security-overview',
    ),
    '1.3': (
        '1',
        'Explain differences and interplay between Secret Protection and Code Security across an end-to-end secure SDLC',
        'https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats',
    ),
    '1.4': (
        '1',
        'Compare prevention-first approaches vs. gate-based security strategies and explain security campaigns',
        'https://docs.github.com/en/code-security/concepts/security-at-scale/about-security-campaigns',
    ),
    '1.5': (
        '1',
        'Identify vulnerability and secret detection mechanisms, act on alerts, and govern ignoring or dismissing alerts',
        'https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/vulnerability-exposure',
    ),
    '1.6': (
        '1',
        'Describe developer, security, and admin responsibilities, alert access management, delegated bypass, and supply chain security concepts',
        'https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization',
    ),

    # Domain 2 — Configure and use Secret Protection (formerly secret scanning) (18 items: 6 skills x 3)
    '2.1': (
        '2',
        'Enable and configure GitHub Secret Protection at repository and organization levels and contrast public vs. private/enterprise behavior',
        'https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning',
    ),
    '2.2': (
        '2',
        'Prevent secret exposure using Push Protection, validity checks, and prioritized high-confidence or generic secret detection',
        'https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection',
    ),
    '2.3': (
        '2',
        'Manage the Secret Protection alert lifecycle, apply secret remediation actions, and govern alert dismissals',
        'https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning/evaluating-alerts',
    ),
    '2.4': (
        '2',
        'Configure role-based and delegated bypass policies in Secret Protection',
        'https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/delegated-bypass-for-push-protection/about-delegated-bypass-for-push-protection',
    ),
    '2.5': (
        '2',
        'Configure Secret Protection alert recipients and path exclusions (.github/secret_scanning.yml)',
        'https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/excluding-folders-and-files-from-secret-scanning',
    ),
    '2.6': (
        '2',
        'Create, dry-run, and manage custom secret patterns (including Copilot regex generation and Push Protection)',
        'https://docs.github.com/en/code-security/secret-scanning/defining-custom-patterns-for-secret-scanning',
    ),

    # Domain 3 — Configure and use supply chain security (formerly Dependabot/Dependency Review) (18 items: 6 skills x 3)
    '3.1': (
        '3',
        'Generate and interpret the dependency graph, vulnerability databases, Dependency Submission API, and SPDX SBOM exports',
        'https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository',
    ),
    '3.2': (
        '3',
        'Prioritize supply chain alerts (EPSS, CVSS, reachability) and configure Dependabot auto-triage (auto-dismiss) rules',
        'https://docs.github.com/en/code-security/dependabot/dependabot-auto-triage-rules/about-dependabot-auto-triage-rules',
    ),
    '3.3': (
        '3',
        'Remediate supply chain alerts through Dependabot security updates, version updates, and security campaigns',
        'https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates',
    ),
    '3.4': (
        '3',
        'Secure dependencies during development using pre-merge Dependency Review (dependency-review-action) for vulnerabilities and licenses',
        'https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/configuring-the-dependency-review-action',
    ),
    '3.5': (
        '3',
        'Configure advanced dependency update rules in dependabot.yml (grouping, ignore rules, update strategies, private registries)',
        'https://docs.github.com/en/code-security/dependabot/working-with-dependabot/dependabot-options-reference',
    ),
    '3.6': (
        '3',
        'Configure supply chain alert permissions, Dependabot workflows/runners, webhooks, and external production-context integrations',
        'https://docs.github.com/en/code-security/dependabot/working-with-dependabot/automating-dependabot-with-github-actions',
    ),

    # Domain 4 — Configure and use Code Security (formerly Code Scanning with CodeQL) (14 items: 3,3,3,3,2)
    '4.1': (
        '4',
        'Compare CodeQL and third-party analysis tools and manage SARIF 2.1.0 ingestion, fingerprints, and limits',
        'https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/sarif-support-for-code-scanning',
    ),
    '4.2': (
        '4',
        'Set up and configure Code Security via Default Setup, Advanced Setup workflows, matrix build-modes, and external CI (CodeQL CLI)',
        'https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/codeql-code-scanning-for-compiled-languages',
    ),
    '4.3': (
        '4',
        'Review CodeQL dataflow analysis insights and remediate alerts using Copilot Autofix and pull request workflows',
        'https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/about-autofix-for-codeql-code-scanning',
    ),
    '4.4': (
        '4',
        'Manage code scanning alert lifecycles, dismissals, severity thresholds, and analysis categories',
        'https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/assessing-code-scanning-alerts-for-your-repository',
    ),
    '4.5': (
        '4',
        'Optimize and troubleshoot Code Security operations with custom configurations, model packs, and build/performance diagnostics',
        'https://docs.github.com/en/code-security/code-scanning/creating-an-advanced-setup-for-code-scanning/customizing-your-advanced-setup-for-code-scanning',
    ),

    # Domain 5 — Security operations: best practices, prioritization, and remediation (18 items: 6 skills x 3)
    '5.1': (
        '5',
        'Understand CVE, CWE, and GitHub Security Advisory (GHSA) concepts and execute end-to-end advisory remediation workflows',
        'https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories',
    ),
    '5.2': (
        '5',
        'Define, prioritize, and enforce severity rulesets and production-context prioritization at scale',
        'https://docs.github.com/en/code-security/securing-your-organization/understanding-your-organizations-exposure-to-vulnerabilities/alerts-in-production-code',
    ),
    '5.3': (
        '5',
        'Execute campaign-based remediation strategies, bulk alert management, and audited alert dismissal documentation',
        'https://docs.github.com/en/code-security/tutorials/manage-security-alerts/best-practices-for-participating-in-a-security-campaign',
    ),
    '5.4': (
        '5',
        'Customize CodeQL query suites, multi-repository variant analysis, and risk-profile-tailored security detection',
        'https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites',
    ),
    '5.5': (
        '5',
        'Collaborate across security roles, delegated exceptions, alert ownership, and cross-suite governance rulesets',
        'https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets',
    ),
    '5.6': (
        '5',
        'Shift left and strengthen preventive security through push protection, pre-merge dependency scanning, and PR CodeQL analysis',
        'https://docs.github.com/en/code-security/tutorials/secure-your-organization/protect-against-threats',
    ),

    # Domain 6 — GitHub Security suites administration (14 items: 3,3,3,3,2)
    '6.1': (
        '6',
        'Roll out GitHub Security Suites at enterprise, organization, and repository scale and contrast GHEC vs. GHES capabilities',
        'https://docs.github.com/en/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/choosing-a-security-configuration-for-your-repositories',
    ),
    '6.2': (
        '6',
        'Configure suite defaults, Enforced vs. Unenforced inheritance, 90-day active-committer licensing, and AI credit budgets',
        'https://docs.github.com/en/enterprise-cloud@latest/billing/concepts/product-billing/github-advanced-security',
    ),
    '6.3': (
        '6',
        'Define enterprise and organization security policies, enforcement boundaries, bypass permissions, and audit log governance',
        'https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-code-security-and-analysis-for-your-enterprise',
    ),
    '6.4': (
        '6',
        'Define administrator, Security Manager, developer, and fine-grained custom roles for viewing and dismissing security alerts',
        'https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization',
    ),
    '6.5': (
        '6',
        'Enforce default or approved custom CodeQL workflows and automate large-scale security governance via REST and GraphQL APIs',
        'https://docs.github.com/en/rest/code-security/configurations',
    ),
}

SKILL_PLAN = {
    '1.1': 3, '1.2': 3, '1.3': 3, '1.4': 3, '1.5': 3, '1.6': 3,
    '2.1': 3, '2.2': 3, '2.3': 3, '2.4': 3, '2.5': 3, '2.6': 3,
    '3.1': 3, '3.2': 3, '3.3': 3, '3.4': 3, '3.5': 3, '3.6': 3,
    '4.1': 3, '4.2': 3, '4.3': 3, '4.4': 3, '4.5': 2,
    '5.1': 3, '5.2': 3, '5.3': 3, '5.4': 3, '5.5': 3, '5.6': 3,
    '6.1': 3, '6.2': 3, '6.3': 3, '6.4': 3, '6.5': 2,
}

assert len(SKILLS) == 34, f'Expected 34 skills, got {len(SKILLS)}'
assert sum(SKILL_PLAN.values()) == 100, f'Expected 100 items/set, got {sum(SKILL_PLAN.values())}'
for _d, (_rng, _quota, _ms) in DOMAIN_WEIGHTS.items():
    _actual = sum(cnt for sk, cnt in SKILL_PLAN.items() if SKILLS[sk][0] == _d)
    assert _actual == _quota, f'Domain {_d}: expected {_quota}, got {_actual}'

SKILL_SOURCES = {sk: ('GitHub Security Documentation', url) for sk, (_dom, _title, url) in SKILLS.items()}

