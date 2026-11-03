"""Official Microsoft Learn & GitHub Docs URLs for Exam GH-900: GitHub Foundations (6 x 100 = 600 questions).

Aligned to the official Microsoft Learn Study Guide for Exam GH-900: GitHub Foundations
(Skills at a glance as of January 2026; Last updated February 19, 2026).
"""

STUDY_GUIDE_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-900'
CERTIFICATION_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/github-foundations/'
EXAM_EXPERIENCE_URL = 'https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience'
LEARN_PATH_PART1_URL = 'https://learn.microsoft.com/en-us/training/paths/github-foundations/'
LEARN_PATH_PART2_URL = 'https://learn.microsoft.com/en-us/training/paths/github-foundations-2/'

SKILL_SOURCES = {
    # Domain 1: Understand Git and GitHub basics (25-30% -> 28 items)
    '1.1': ('About version control and Git', 'https://docs.github.com/en/get-started/using-git/about-git'),
    '1.2': ('Introduction to Git and GitHub (Microsoft Learn)', 'https://learn.microsoft.com/en-us/training/modules/introduction-to-github/'),
    '1.3': ('GitHub glossary: repositories, commits, and branches', 'https://docs.github.com/en/get-started/learning-about-github/github-glossary'),
    '1.4': ('Types of GitHub accounts and GitHub plans', 'https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts'),
    '1.5': ('GitHub flow collaborative branching workflow', 'https://docs.github.com/en/get-started/using-github/github-flow'),
    '1.6': ('Basic writing and formatting syntax in GitHub Flavored Markdown', 'https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax'),
    '1.7': ('GitHub Desktop and GitHub Mobile overview', 'https://docs.github.com/en/desktop/overview/about-github-desktop'),

    # Domain 2: Work with GitHub repositories (10-15% -> 14 items)
    '2.1': ('About READMEs, LICENSE, CONTRIBUTING, CODEOWNERS, and SECURITY files', 'https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes'),
    '2.2': ('Creating a repository from a template and managing branches', 'https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template'),
    '2.3': ('Creating, moving, and managing files in a GitHub repository', 'https://docs.github.com/en/repositories/working-with-files/managing-files'),
    '2.4': ('Viewing repository graphs, stars, feature preview, and dependency insights', 'https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/using-pulse-to-view-a-summary-of-repository-activity'),
    '2.5': ('Best practices for repositories and archiving repositories', 'https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories'),

    # Domain 3: Collaborate using GitHub (10-15% -> 14 items)
    '3.1': ('Communicating on GitHub with Issues, Pull Requests, and Discussions', 'https://docs.github.com/en/get-started/quickstart/communicating-on-github'),
    '3.2': ('Linking a pull request to an issue and configuring issue/PR templates', 'https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue'),
    '3.3': ('Configuring notifications and managing subscriptions on GitHub', 'https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications'),
    '3.4': ('Sharing content with Gists, Wikis, and GitHub Pages', 'https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages'),

    # Domain 4: Apply modern development practices (10-15% -> 14 items)
    '4.1': ('Understanding GitHub Actions workflows, events, jobs, and runners', 'https://docs.github.com/en/actions/about-github-actions/understanding-github-actions'),
    '4.2': ('About GitHub Copilot, Copilot coding agent, Agent Mode, and multi-model support', 'https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent'),
    '4.3': ('Plans for GitHub Copilot (Individual/Pro, Business, and Enterprise)', 'https://docs.github.com/en/copilot/get-started/plans'),
    '4.4': ('GitHub Codespaces overview and devcontainer.json configuration', 'https://docs.github.com/en/codespaces/overview'),
    '4.5': ('The github.dev web-based editor vs GitHub Codespaces', 'https://docs.github.com/en/codespaces/the-githubdev-web-based-editor'),

    # Domain 5: Manage projects with GitHub (5-10% -> 8 items)
    '5.1': ('About Projects and Table, Board, and Roadmap layout views', 'https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects'),
    '5.2': ('Managing custom fields, iterations, labels, milestones, and built-in workflows', 'https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations'),
    '5.3': ('Using saved replies and assigning issues and pull requests', 'https://docs.github.com/en/get-started/writing-on-github/working-with-saved-replies/about-saved-replies'),
    '5.4': ('Viewing insights and custom charts in GitHub Projects', 'https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project/about-insights-for-projects'),

    # Domain 6: Understand privacy, security, and administration (10-15% -> 14 items)
    '6.1': ('Configuring two-factor authentication (2FA) and passkeys on GitHub', 'https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys'),
    '6.2': ('Repository roles and organization roles for access management', 'https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization'),
    '6.3': ('About Enterprise Managed Users (EMUs) and organization Copilot policy management', 'https://docs.github.com/en/enterprise-cloud@latest/admin/concepts/identity-and-access-management/enterprise-managed-users'),
    '6.4': ('Setting repository visibility, branch protection rules, and rulesets', 'https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches'),
    '6.5': ('Organizing members into nested teams and managing organization settings', 'https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams'),

    # Domain 7: Explore the GitHub community (5-10% -> 8 items)
    '7.1': ('About GitHub Sponsors and open-source sustainability', 'https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors'),
    '7.2': ('Supporting open-source projects with community profiles and Security Lab / advisories', 'https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories'),
    '7.3': ('Following people and organizations on GitHub to track activity', 'https://docs.github.com/en/get-started/exploring-projects-on-github/following-people'),
    '7.4': ('About GitHub Marketplace for GitHub Apps and Actions', 'https://docs.github.com/en/apps/github-marketplace/github-marketplace-overview/about-github-marketplace'),
    '7.5': ('Introduction to InnerSource practices on GitHub (Microsoft Learn)', 'https://learn.microsoft.com/en-us/training/modules/manage-innersource-program-github/'),
    '7.6': ('Forking a repository vs templates and improving repository discoverability with topics', 'https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo'),
}
