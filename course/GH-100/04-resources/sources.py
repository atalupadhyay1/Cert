"""Official Microsoft Learn & GitHub Enterprise Docs URLs for Exam GH-100: GitHub Enterprise Administrator (6 x 100 = 600 questions).

Aligned to the official Microsoft Learn Study Guide for Exam GH-100: GitHub Enterprise Administrator
(Skills measured as of July 2026; Last updated May 5, 2026) awarding the GitHub Administration credential.
"""

STUDY_GUIDE_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-100'
CERTIFICATION_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/github-administration/'
EXAM_EXPERIENCE_URL = 'https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience'
LEARN_PATH_PART1_URL = 'https://learn.microsoft.com/en-us/training/paths/github-administration-products/'
LEARN_PATH_PART2_URL = 'https://learn.microsoft.com/en-us/training/paths/github-admin-2/github-admin-2/'

SKILL_SOURCES = {
    # Domain 1: Manage GitHub identities and access (15-20% -> 19 items)
    '1.1': ('About Enterprise Managed Users vs personal accounts', 'https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-enterprise-managed-users'),
    '1.2': ('Enforcing SAML single sign-on and two-factor authentication', 'https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise'),
    '1.3': ('Configuring SCIM provisioning vs IdP team synchronization', 'https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/provisioning-user-accounts-with-scim/provisioning-users-and-groups-with-scim-using-the-rest-api'),
    '1.4': ('Choosing and configuring Identity Providers (Entra ID, Okta, PingFederate, CAS/LDAP)', 'https://docs.github.com/en/enterprise-cloud@latest/admin/managing-iam/understanding-iam-for-enterprises/about-identity-and-access-management'),
    '1.5': ('GitHub authentication and authorization model (SSH, PAT, OAuth, SAML, OIDC)', 'https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github'),
    '1.6': ('Configuring organization roles, custom roles, and repository roles', 'https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/about-custom-organization-roles'),
    '1.7': ('Defining and managing Enterprise teams across organizations', 'https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-fundamentals/teams-in-an-enterprise'),
    '1.8': ('Auditing repository, organization, and enterprise access permissions', 'https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/identifying-audit-log-events-performed-by-an-access-token'),
    '1.9': ('Managing enterprise member privileges, policies, repository rulesets, and bypass roles', 'https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise'),

    # Domain 2: Administer GitHub Enterprise environment (10-15% -> 14 items)
    '2.1': ('Identifying issues resolvable by Enterprise Admins vs GitHub Enterprise Support', 'https://docs.github.com/en/enterprise-cloud@latest/support/learning-about-github-support/about-github-support'),
    '2.2': ('Generating GHES support bundles, ghe-diagnostics, and ticket diagnostics', 'https://docs.github.com/en/enterprise-server@latest/support/contacting-github-support/providing-data-to-github-support'),
    '2.3': ('Recommending enterprise standards for developer collaboration and InnerSource', 'https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/enterprise-best-practices/organize-work'),
    '2.4': ('Defining standards for workflows, branching, CODEOWNERS reviews, merge queues, and releases', 'https://docs.github.com/en/enterprise-cloud@latest/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue'),
    '2.5': ('GitHub Enterprise deployment models (GHEC+EMU, GHEC Data Residency ghe.com, GHEC personal, GHES)', 'https://docs.github.com/en/enterprise-cloud@latest/admin/overview/about-github-for-enterprises'),
    '2.6': ('GitHub Enterprise licensing, metered user-based billing, and Visual Studio subscriptions', 'https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/about-per-user-pricing'),
    '2.7': ('Monitoring enterprise license consumption and GitHub Connect license sync', 'https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-license-for-github-enterprise/viewing-license-usage-for-github-enterprise'),

    # Domain 3: Implement secure software development and compliance (25-30% -> 29 items)
    '3.1': ('Defining organization and enterprise security policies and security configurations', 'https://docs.github.com/en/enterprise-cloud@latest/admin/managing-code-security/securing-your-enterprise/about-security-configurations'),
    '3.2': ('Strengthening enterprise security posture, SSH CAs, IP allow lists, and data protection', 'https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization'),
    '3.3': ('Implementing audit logging, audit log streaming, and compliance reporting', 'https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise'),
    '3.4': ('Configuring vulnerability alerts, secret scanning push protection, and CodeQL code scanning', 'https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning'),
    '3.5': ('Managing Dependabot alerts, security/version updates, private registries, and advisories', 'https://docs.github.com/en/enterprise-cloud@latest/code-security/dependabot/dependabot-security-updates/about-dependabot-security-updates'),
    '3.6': ('Defining a security response plan and purging sensitive data from Git history', 'https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository'),
    '3.7': ('Configuring fine-grained and classic Personal Access Token (PAT) enterprise policies', 'https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-personal-access-tokens-in-your-enterprise'),
    '3.8': ('Understanding REST and GraphQL API rate limits for PATs, GitHub Apps, and GITHUB_TOKEN', 'https://docs.github.com/en/enterprise-cloud@latest/rest/using-the-rest-api/rate-limits-for-the-rest-api'),
    '3.9': ('Comparing GitHub Apps, OAuth Apps, deploy keys, and machine users', 'https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/differences-between-github-apps-and-oauth-apps'),
    '3.10': ('Approving, denying, and governing OAuth Apps and GitHub App installations', 'https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-oauth-access-to-your-organizations-data/about-oauth-app-access-restrictions'),

    # Domain 4: Manage GitHub Actions (20-25% -> 24 items)
    '4.1': ('Sharing reusable workflows and actions privately across enterprise organizations', 'https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/sharing-actions-and-workflows-with-your-enterprise'),
    '4.2': ('Enforcing enterprise and organization GitHub Actions policies and SHA pinning', 'https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise'),
    '4.3': ('Managing runner groups, Larger runners, self-hosted runners, and Actions Runner Controller (ARC)', 'https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-self-hosted-runners/managing-access-to-self-hosted-runners-using-groups'),
    '4.4': ('Configuring IP allow lists, proxies, and Azure private networking (VNet) for runners', 'https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/about-networking-for-hosted-compute-products-in-your-organization'),
    '4.5': ('Monitoring and troubleshooting runner _diag logs, queues, and performance', 'https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/monitoring-and-troubleshooting-self-hosted-runners'),
    '4.6': ('Defining secret scope, hierarchy precedence, and deployment environment access controls', 'https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions'),
    '4.7': ('Configuring organization and repository encrypted secrets and variables via UI and REST API', 'https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/creating-secrets-for-an-organization'),
    '4.8': ('Integrating third-party secret vaults (HashiCorp Vault, Azure Key Vault, AWS) via OIDC', 'https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect'),

    # Domain 5: Monitor and optimize GitHub usage (10-15% -> 14 items)
    '5.1': ('Analyzing enterprise audit logs, Git events, and API Insights / REST/GraphQL metrics', 'https://docs.github.com/en/enterprise-cloud@latest/organizations/collaborating-with-your-team/apicenter/viewing-api-insights-for-your-organization'),
    '5.2': ('Distinguishing admin vs GitHub Support responsibilities and generating appliance/cloud diagnostics', 'https://docs.github.com/en/enterprise-server@latest/admin/monitoring-activity-in-your-enterprise/exploring-user-activity/activity-dashboard'),
    '5.3': ('Evaluating enterprise adoption, Copilot/Actions metrics, and dormant or underutilized features', 'https://docs.github.com/en/enterprise-cloud@latest/copilot/rolling-out-github-copilot-at-scale/analyzing-usage-over-time-with-the-copilot-metrics-api'),
    '5.4': ('Interpreting metered usage reports, spending limits, and cost centers for Actions, Packages, GHAS & Copilot', 'https://docs.github.com/en/enterprise-cloud@latest/billing/managing-your-billing/using-the-billing-platform'),
    '5.5': ('Recommending strategies for dormant seat reclamation, caching, and runner/storage cost optimization', 'https://docs.github.com/en/enterprise-server@latest/admin/managing-accounts-and-repositories/managing-users-in-your-enterprise/managing-dormant-users'),
}
