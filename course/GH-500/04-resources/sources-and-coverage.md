# Official Sources & July 2026 Blueprint Coverage — Exam GH-500

All `600` questions and explanations in this course are authored from primary Microsoft Learn and GitHub Security documentation (`verified November 2026`):

1. **Official Exam GH-500 Study Guide (*Skills measured as of July 2026 · Last updated May 14, 2026*):**
   - `https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500`
2. **Official GitHub Advanced Security Certification Page (*Last updated May 4, 2026*):**
   - `https://learn.microsoft.com/en-us/credentials/certifications/github-advanced-security/`
3. **Microsoft Certification Exam Duration & Experience (`100 min` exam / `120 min` seat, closed-book GitHub policy):**
   - `https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience`
4. **Microsoft Learn GH-500 Training Paths (*GitHub Advanced Security Part 1 & Part 2*):**
   - `https://learn.microsoft.com/en-us/training/paths/gh-500-part-1/`
   - `https://learn.microsoft.com/en-us/training/paths/gh-500-part-2/`
5. **GitHub Code Security, Secret Protection & Supply Chain Documentation (`docs.github.com/en/code-security`, `docs.github.com/en/billing` — mapped per skill `1.1`..`6.5` in `04-resources/sources.py`):**
   - Unbundled **GitHub Secret Protection** and **GitHub Code Security** SKUs (`on GitHub Team & Enterprise`), **Security Overview** (`Risk`, `Coverage`, `Campaigns`, free org risk assessment), **Push Protection** + **partner validity checks (`Active`/`Inactive`/`Unknown`)** + **Copilot AI generic secret push detection (`Secret Protection AI credits`)** + **Delegated Bypass** (`visible teams, roles, custom org role "Review and manage secret scanning bypass requests"`, zero secret teams), **`.github/secret_scanning.yml`** (`paths-ignore` `<=1,000` globs / `<=1 MB`), **custom regex patterns** (`100/repo`, `500/org-or-ent`, `Generate with AI`, `Save and dry run` `<=1,000` matches, `Publish pattern`), **`Dependency Submission API`** + **`SPDX` JSON SBOM export/attestation**, **`EPSS`** + **`Reachability`** + **Dependabot auto-triage (`resolution:auto-dismiss`)**, **`actions/dependency-review-action@v4`**, **`.github/dependabot.yml`** (`groups`, `ignore`, `registries` + `Dependabot secrets`), **`SARIF 2.1.0`** (`<=10 MB` gzipped, `<=25,000` / top `5,000`, `category`, `partialFingerprints`, `security-events: write`), **CodeQL `Default` vs `Advanced Setup`** (`build-mode: none|autobuild|manual` & **`CodeQL CLI`**), **`Copilot Autofix`** & **`@copilot` Security Campaign batches (`<=25`, `Code Security AI credits`)**, **YAML `CodeQL model packs`**, **Private Vulnerability Reporting (`GHSA`/`CVE`/`CWE`)**, **VS Code `MRVA`**, **`Security Configurations`** (`Enforced` vs `Unenforced`, `"Not set"` unlock behavior, transferred-repo nuance), **`GHEC` vs `GHES` (`GitHub Connect`)**, **90-day active-committer + AI credit hard budgets**, **`Security Manager`** + custom roles, and REST/GraphQL/Audit Log APIs.
