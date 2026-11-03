"""Official Microsoft Learn & GitHub Docs source links for Exam GH-200 (January 2026 study guide)."""

STUDY_GUIDE_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200'
CERTIFICATION_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/github-actions/'
EXAM_EXPERIENCE_URL = 'https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience'
LEARN_PATH_PART1_URL = 'https://learn.microsoft.com/en-us/training/paths/github-actions/'
LEARN_PATH_PART2_URL = 'https://learn.microsoft.com/en-us/training/paths/github-actions-2/'

SKILL_SOURCES = {
    # Domain 1: Author and manage workflows (20–25% -> 24 items/set)
    '1.1': 'https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows',
    '1.2': 'https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow',
    '1.3': 'https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#onworkflow_dispatchinputs',
    '1.4': 'https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-conditions-to-control-job-execution',
    '1.5': 'https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/using-jobs-in-a-workflow#defining-prerequisite-jobs',
    '1.6': 'https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions',
    '1.7': 'https://docs.github.com/en/actions/use-cases-and-examples/using-containerized-services/about-service-containers',
    '1.8': 'https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-workflow',
    '1.9': 'https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations#yaml-anchors-and-aliases',
    '1.10': 'https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs',
    '1.11': 'https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/evaluate-expressions-in-workflows-and-actions',
    '1.12': 'https://docs.github.com/en/actions/writing-workflows/quickstart',
    '1.13': 'https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/caching-dependencies-to-speed-up-workflows',
    '1.14': 'https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/passing-information-between-jobs',
    '1.15': 'https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions#adding-a-job-summary',

    # Domain 2: Consume and troubleshoot workflows (15–20% -> 19 items/set)
    '2.1': 'https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/using-workflow-run-logs',
    '2.2': 'https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/troubleshooting-workflows/enabling-debug-logging',
    '2.3': 'https://docs.github.com/en/actions/reference/workflows-and-actions/reusing-workflow-configurations#yaml-anchors-and-aliases',
    '2.4': 'https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/re-running-workflows-and-jobs',
    '2.5': 'https://docs.github.com/en/rest/actions/workflow-runs',
    '2.6': 'https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/downloading-workflow-artifacts',
    '2.7': 'https://docs.github.com/en/actions/sharing-automations/reusing-workflows',
    '2.8': 'https://docs.github.com/en/actions/sharing-automations/creating-workflow-templates',
    '2.9': 'https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-workflow-runs/disabling-and-enabling-a-workflow',

    # Domain 3: Author and maintain actions (15–20% -> 19 items/set)
    '3.1': 'https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-javascript-action',
    '3.2': 'https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action',
    '3.3': 'https://docs.github.com/en/actions/sharing-automations/creating-actions/about-custom-actions',
    '3.4': 'https://docs.github.com/en/actions/sharing-automations/creating-actions/metadata-syntax-for-github-actions',
    '3.5': 'https://docs.github.com/en/actions/sharing-automations/creating-actions/setting-exit-codes-for-actions',
    '3.6': 'https://docs.github.com/en/actions/sharing-automations/creating-actions/sharing-actions-and-workflows-from-your-private-repository',
    '3.7': 'https://docs.github.com/en/actions/sharing-automations/creating-actions/publishing-actions-in-github-marketplace',
    '3.8': 'https://docs.github.com/en/actions/sharing-automations/creating-actions/releasing-and-maintaining-actions',

    # Domain 4: Manage GitHub Actions for the enterprise (20–25% -> 24 items/set)
    '4.1': 'https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/reusing-workflows',
    '4.2': 'https://docs.github.com/en/enterprise-cloud@latest/actions/sharing-automations/creating-actions/sharing-actions-and-workflows- with-your-enterprise'.replace(' ', ''),
    '4.3': 'https://docs.github.com/en/enterprise-cloud@latest/admin/enforcing-policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise',
    '4.4': 'https://docs.github.com/en/enterprise-cloud@latest/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners',
    '4.5': 'https://docs.github.com/en/enterprise-cloud@latest/admin/configuring-settings/configuring-private-networking-for-hosted-compute-products/about-azure-private-networking-for-github-hosted-runners-in-your-enterprise',
    '4.6': 'https://docs.github.com/en/enterprise-cloud@latest/actions/hosting-your-own-runners/managing-access-to-self-hosted-runners-using-groups',
    '4.7': 'https://docs.github.com/en/actions/using-github-hosted-runners/customizing-github-hosted-runners',
    '4.8': 'https://docs.github.com/en/enterprise-cloud@latest/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions',
    '4.9': 'https://docs.github.com/en/enterprise-cloud@latest/rest/actions/secrets',

    # Domain 5: Secure and optimize automation (10–15% -> 14 items/set)
    '5.1': 'https://docs.github.com/en/actions/managing-workflow-runs-and-deployments/managing-deployments/managing-environments-for-deployment',
    '5.2': 'https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions#understanding-the-risk-of-script-injections',
    '5.3': 'https://docs.github.com/en/actions/security-for-github-actions/security-guides/automatic-token-authentication',
    '5.4': 'https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect',
    '5.5': 'https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds',
    '5.6': 'https://docs.github.com/en/rest/actions/permissions#get-artifact-and-log-retention-settings-for-an-organization',
    '5.7': 'https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/control-the-concurrency-of-workflows-and-jobs',
}

assert len(SKILL_SOURCES) == 48
for _k, _url in SKILL_SOURCES.items():
    assert _url.startswith(('https://docs.github.com/', 'https://learn.microsoft.com/')), _k
