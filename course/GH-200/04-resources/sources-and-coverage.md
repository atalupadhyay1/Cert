# Official Sources & January 2026 Blueprint Coverage — Exam GH-200

All `600` questions and explanations in this course are authored from primary Microsoft Learn and GitHub Actions documentation (`verified November 2026`):

1. **Official Exam GH-200 Study Guide (*Skills measured as of January 2026 · Last updated February 5, 2026*):**
   - `https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200`
2. **Official GitHub Actions Certification Page (*Last updated August 7, 2026*):**
   - `https://learn.microsoft.com/en-us/credentials/certifications/github-actions/`
3. **Microsoft Certification Exam Duration & Experience (`100 min` exam / `120 min` seat, closed-book GitHub policy):**
   - `https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience`
4. **Microsoft Learn GH-200 Training Paths (`GH-200T00` Parts 1 & 2):**
   - `https://learn.microsoft.com/en-us/training/paths/github-actions/`
   - `https://learn.microsoft.com/en-us/training/paths/github-actions-2/`
5. **GitHub Actions Documentation (`docs.github.com/en/actions` — mapped per skill `1.1`..`5.7` in `04-resources/sources.py`):**
   - Workflow syntax, events (`schedule`, `workflow_dispatch`, `repository_dispatch`, `merge_group`, `workflow_call`), single-file YAML anchors/aliases (`&`, `*`, `<<:`), `needs:` DAGs, `$GITHUB_OUTPUT` / `$GITHUB_ENV` / `$GITHUB_PATH` / `$GITHUB_STEP_SUMMARY`, service containers (`--health-cmd`), `<=256` matrices (`ubuntu-24.04`, `ubuntu-24.04-arm`, `windows-2025`, `macos-15`), `actions/cache@v4` (`10 GB`/7d) & `actions/upload-artifact@v4` (`merge-multiple: true`), GitHub Actions VS Code extension, `node20` (`@actions/core`, `@vercel/ncc`), Docker vs Composite (`shell:`, `github.action_path`), **Immutable Actions** (`GHCR` OCI packages via `pkg.actions.githubusercontent.com` & `ghcr.io`), Marketplace publishing, Dependabot `github-actions`, Ruleset Required Workflows, `ARC` (`gha-runner-scale-set`), Azure VNet Larger runners (`GitHub.Network/networkSettings`), LibSodium Secrets REST API, script-injection hardening, OIDC (`id-token: write`), SLSA Artifact Attestations (`actions/attest-build-provenance`, `gh attestation verify`), and `ubuntu-slim` FinOps.
