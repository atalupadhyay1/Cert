# Microsoft / GitHub Exam GH-300: GitHub Copilot — Full-Length Mock Exam 6

**Theme:** Enterprise Privacy, Content Exclusions, Public-Code Filtering, IP Indemnity & REST Seat Governance  
**Credential:** `GitHub Copilot` *(Intermediate · **no prerequisite** · **2-year validity** transitioning to Microsoft Learn recertification)*  
**Study guide baseline:** `August 7, 2026 (Last updated July 9, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-300 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Copilot documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Use GitHub Copilot responsibly (15–20% official weight · 18 questions)

### 1. A computational biologist at ArdentBio Therapeutics uses GitHub Copilot in R and Python to write false-discovery-rate (`Benjamini-Hochberg`) p-value adjustment logic for CRISPR off-target assays. Why must biostatisticians validate the rank-tie handling mathematically?

- **A.** Generative AI models predict statistically probable token sequences (`not proven correctness`), risking hallucinated APIs, outdated idioms, training-data bias, and subtle security bugs
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 2. In `ardentbio/crispr-pipeline`, Copilot suggests `npm install @biocore/fastq-quality-trimmer` in a TypeScript visualization portal. Before running `npm install`, how do you prevent a **slopsquatting** supply-chain incident?

- **A.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **B.** Inspect **Audit Logs** (`category:copilot`, e.g., `copilot.cfb_seat_created`, `copilot.content_exclusion_changed`) for admin changes and `GET /orgs/{org}/copilot/metrics` (`>=5 active users`) for aggregated usage
- **C.** Verify every AI-suggested package name, publisher, and version in your trusted registry (`preventing slopsquatting / hallucinated dependency attacks`) before installing
- **D.** Use **GitHub Spark** to build, iterate on, and share AI-powered full-stack micro-apps (`with natural-language prompts, live preview, managed KV persistence, and optional GitHub repository sync`)

### 3. ArdentBio's GxP validation lead observes that engineers rarely write negative test cases when Copilot generates clean-looking docstrings and type hints (`automation ____`). Which GxP practice restores verification rigor?

- **A.** Install `@github/copilot` via `npm install -g @github/copilot` (`Node.js 22+`), `winget install GitHub.Copilot`, or Homebrew, launch `copilot` in your repo, run `/login`, and confirm folder trust
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **D.** Guard against **automation bias / complacency** (`over-trusting plausible-looking AI completions`) by reviewing edge cases, error paths, and security invariants manually

### 4. ArdentBio's GxP software quality SOP explains generative AI limitations to new bioinformatics hires. Which two risks must every developer mitigate? Select two.

- **A.** Verify every AI-suggested package name, publisher, and version in your trusted registry (`preventing slopsquatting / hallucinated dependency attacks`) before installing
- **B.** Generative AI models predict statistically probable token sequences (`not proven correctness`), risking hallucinated APIs, outdated idioms, training-data bias, and subtle security bugs
- **C.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **D.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **E.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 5. ArdentBio evaluates clinical-trial cohort stratification scripts built with Copilot across ancestral populations (`EUR, AFR, EAS, SAS, AMR`) to prevent under-calling rare pharmacogenomic alleles in underrepresented groups. Complete the Responsible AI principle: `____`.

- **A.** Use `copilot -p "..."` for non-interactive runs (`-s` for clean stdout, `--output-format=json` for JSONL), `--available-tools` / `--deny-tool` for tool scoping, and `--fleet` for parallel subagents
- **B.** Apply the six Responsible AI principles—**Fairness**, **Reliability & Safety**, **Privacy & Security**, **Inclusiveness**, **Transparency**, and **Accountability**
- **C.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **D.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits

### 6. Protecting donor whole-genome FASTQ identifiers, enforcing least-privilege Content Exclusions, and preventing secret leakage in genomics pipelines operationalize which Responsible AI principle? (`____ & Security`)

- **A.** Apply the six Responsible AI principles—**Fairness**, **Reliability & Safety**, **Privacy & Security**, **Inclusiveness**, **Transparency**, and **Accountability**
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **D.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits

### 7. ArdentBio's GxP electronic change-control log records whether AI coding tools assisted a PR alongside the human author's and reviewer's cryptographic sign-offs. Which two Responsible AI principles work together here?

- **A.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **B.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **C.** Maintain **Transparency** and **Accountability** by disclosing AI assistance per team norms, honoring open-source licenses, and ensuring humans own every committed line
- **D.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)

### 8. ArdentBio's Bioethics & AI Governance Board audits software pipelines built with GitHub Copilot Enterprise. Which three pillars anchor their review? Select three.

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** Apply the six Responsible AI principles—**Fairness**, **Reliability & Safety**, **Privacy & Security**, **Inclusiveness**, **Transparency**, and **Accountability**
- **C.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **D.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **E.** Maintain **Transparency** and **Accountability** by disclosing AI assistance per team norms, honoring open-source licenses, and ensuring humans own every committed line
- **F.** Evaluate AI-generated UI copy, validation rules, and domain models for **Fairness** and **Inclusiveness** (`avoiding demographic stereotyping, exclusionary naming, or accessibility regressions`)

### 9. In a Python Nextflow wrapper script, Copilot suggests `subprocess.run(f"samtools view {sample_id}.bam", shell=True)`, risking OS command injection if `sample_id` contains `;` or backticks. Which coding rule + CI check eliminates this harm?

- **A.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **B.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **C.** Mitigate AI harms (`historical dataset bias, weak crypto/SQL defaults, PII exposure, and insecure scaffolding`) using RAI filters, `CodeQL` SAST, secret scanning, and diverse test suites
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free

### 10. An ArdentBio researcher uses VS Code Agent Mode with an MCP server fetching external preprint metadata, and a malicious abstract embeds hidden prompt text instructing the agent to append an SSH key to `~/.ssh/authorized_keys`. What stops this **indirect prompt injection**?

- **A.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **B.** `#runSubagent` merges every raw intermediate grep output directly into the main chat's token window and pauses mid-search to interview the user after every file read
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Treat untrusted external content (`issues, PR bodies, web pages, third-party MCP tool outputs`) as **indirect prompt injection** risks and require human approval on tool actions

### 11. ArdentBio handles donor genomic VCF records and AWS S3 KMS keys. Which two safeguards protect against data leakage and AI-generated vulnerabilities? Select two.

- **A.** Mitigate AI harms (`historical dataset bias, weak crypto/SQL defaults, PII exposure, and insecure scaffolding`) using RAI filters, `CodeQL` SAST, secret scanning, and diverse test suites
- **B.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **C.** Never paste live customer PII, PHI, production database dumps, or active credentials/private keys into Copilot prompts or sample fixtures
- **D.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **E.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models

### 12. An ArdentBio TypeScript/Python engineer uses Copilot to build a clinical assay QC threshold evaluator. Place the Responsible AI verification steps in exact order prior to merge.

- **A.** Set public-code filtering to `Allow` → Paste live customer PII into Chat as sample fixtures → Run unit tests locally → Self-approve your own pull request
- **B.** Merge Copilot output directly to `main` → Run `CodeQL` weekly in production → Check package names only if builds fail → Skip human review when Copilot Code Review leaves zero comments
- **C.** Approve an empty PR branch first → Disable `CodeQL` to speed up Copilot completions → Install unfamiliar suggested packages blindly from public registries → Deploy without unit tests
- **D.** Prompt Copilot with explicit security & type constraints → Review logic & verify suggested packages exist in trusted registries → Run unit/edge-case tests plus `CodeQL` & secret scanning → Complete human peer PR review before merging

### 13. In Python/NumPy, Copilot writes `np.mean(phred_scores)` ignoring `NaN` values (`producing NaN instead of calling np.nanmean` or explicitly rejecting missing base qualities). Why must scientists inspect and unit-test numerical semantics?

- **A.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **B.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **C.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **D.** Treat Copilot as a **pair-programming assistant (`not an oracle`)**: review diffs line-by-line, execute unit/integration/edge-case tests, and scan with `CodeQL` and Dependabot

### 14. Why is **pinned automated CI testing** (`pytest`, `Vitest`, `testthat`) mandatory in GxP bioinformatics repositories even when developers use reusable `.prompt.md` files?

- **A.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **B.** Because LLM sampling is **stochastic (`non-deterministic`)**, identical prompts can yield varying implementations whose runtime behavior, complexity, and thread safety must be verified
- **C.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 15. ArdentBio's IT license admin wants to list the exact GitHub `login` usernames of 19 departed interns still holding paid Copilot Enterprise seats so they can revoke them via API. Proposed solution: Query `GET /orgs/ardentbio/copilot/metrics` expecting individual `login` usernames in the JSON response. Does this meet the goal?

- **A.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements
- **B.** Inspect **Audit Logs** (`category:copilot`, e.g., `copilot.cfb_seat_created`, `copilot.content_exclusion_changed`) for admin changes and `GET /orgs/{org}/copilot/metrics` (`>=5 active users`) for aggregated usage
- **C.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **D.** No — `GET /orgs/{org}/copilot/metrics` returns **aggregated, anonymized** team/org usage (`requiring >=5 active users`), NOT per-developer `last_activity_at` usernames; query `GET /orgs/{org}/copilot/billing/seats`

### 16. ArdentBio operates **Copilot Enterprise** on GitHub Enterprise Cloud (`ardentbio-ent`) with strict IP and clinical privacy mandates. Which four controls establish a compliant baseline?

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **C.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **D.** Operate Copilot responsibly by keeping `Suggestions matching public code = Block`, configuring Content Exclusions, omitting PII/secrets from prompts, and enforcing human PR review

### 17. ArdentBio's Enterprise Owner locks `Suggestions matching public code = Block` across `ardentbio-ent`, blocks personal outside agent overrides via Enterprise `AI controls`, configures Org Content Exclusions for `- "/molecules/**"`, and enforces `CodeQL` + `2` human PR approvals. Proposed solution: Use this Enterprise governance architecture for proprietary drug-discovery repositories. Does this meet the goal?

- **A.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements
- **B.** No — GitHub's **Copilot IP Indemnity** on Business/Enterprise ceases to cover suggestions when `Suggestions matching public code` is set to **`Allow`**; set the filter to **`Block`**
- **C.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **D.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins

### 18. Under FDA 21 CFR Part 11 / GxP software validation principles, can an automated AI review comment substitute for the documented human Quality/Engineering sign-off on a release pull request?

- **A.** Require a human engineer to review, test, and approve every AI-assisted pull request—never delegating final merge accountability to an LLM
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **D.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review

---

## Domain 2 — Use GitHub Copilot features (25–30% official weight · 28 questions)

### 19. ArdentBio scientists code in **VS Code**, **JetBrains PyCharm**, and **Neovim** (`on HPC login nodes`). When Enterprise `ardentbio-ent` enforces SAML SSO (`or Enterprise Managed Users — EMU`), what must be true for IDE authentication to activate their Copilot Enterprise seat?

- **A.** Install the official GitHub Copilot extension in a supported IDE (`VS Code, Visual Studio, JetBrains, Xcode, Eclipse, or Neovim`), sign in via GitHub OAuth, and verify an active seat
- **B.** Inspect **Audit Logs** (`category:copilot`, e.g., `copilot.cfb_seat_created`, `copilot.content_exclusion_changed`) for admin changes and `GET /orgs/{org}/copilot/metrics` (`>=5 active users`) for aggregated usage
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`

### 20. Which GitHub platform hosting tier is required to purchase and deploy **GitHub Copilot Enterprise** (`$39/user/month`, including Copilot Spaces / Knowledge Bases and full Enterprise-level AI policy governance)? (**GitHub `____` Cloud**)

- **A.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **B.** Choose **Copilot Business** (`Org policies, Content Exclusions, IP Indemnity, zero model training`) or **Copilot Enterprise** (`adds GHEC Copilot Spaces/Knowledge Bases & org-wide GitHub.com grounding`)
- **C.** Choose **Copilot Free** for capped monthly completions/chats or **Copilot Pro / Pro+** for individual developers needing unlimited completions, higher premium-model quotas, and **GitHub Spark**
- **D.** No — Repository and Organization **Content Exclusions** require **Copilot Business or Copilot Enterprise**; personal Copilot Free/Pro/Pro+ plans do not support Org Content Exclusions

### 21. Inside a Python file in VS Code, a scientist selects a 14-line Pandas `groupby` aggregation and presses `Ctrl+I` (`Cmd+I` on macOS) to rewrite it in Polars right in place with an inline diff accept/discard bar. Complete the feature name: **`____` Chat**.

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** Match interaction surfaces to scope: **Inline Chat (`Ctrl+I` / `Cmd+I`)** for in-place file edits, **Chat `Ask`** for Q&A, **Copilot Edits** for multi-file working sets, and **Agent Mode / CLI** for autonomous loops
- **C.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **D.** No — Copilot Chat **`Ask` mode** only answers questions and proposes snippets in chat; autonomous multi-file workspace edits with iterative terminal test execution require **Agent Mode** (`or Copilot CLI`)

### 22. ArdentBio's developer guide contrasts four daily Copilot interaction modes in VS Code. Which two descriptions are accurate? Select two.

- **A.** No — Copilot Chat **`Ask` mode** only answers questions and proposes snippets in chat; autonomous multi-file workspace edits with iterative terminal test execution require **Agent Mode** (`or Copilot CLI`)
- **B.** Match interaction surfaces to scope: **Inline Chat (`Ctrl+I` / `Cmd+I`)** for in-place file edits, **Chat `Ask`** for Q&A, **Copilot Edits** for multi-file working sets, and **Agent Mode / CLI** for autonomous loops
- **C.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **E.** Use **Inline ghost-text completions** (`Tab` to accept, `Alt+]` / `Option+]` to cycle) and **Next Edit Suggestions (`NES`)** to predict subsequent ripple edits across nearby lines

### 23. In `ardentbio/assay-pipeline`, an admin configures Repository Content Exclusion `- "/proprietary_primers/**"` and `- "**/*.fasta.enc"`. Are those files also excluded from `@workspace` / `#codebase` chat context in VS Code for seat holders?

- **A.** No — `.gitignore` only prevents untracked files from being staged by Git; excluding tracked repository files from Copilot requires **Copilot Content Exclusions** (`Settings -> Copilot -> Content exclusion`)
- **B.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **C.** Configure Repository or Organization **Content Exclusions** (`Settings -> Copilot -> Content exclusion`) so IDEs omit matched sensitive files across completions, Chat, and code review
- **D.** Configuring Copilot Content Exclusions also blocks `git clone`, GitHub Actions runners, and `CodeQL` security scans from reading the excluded files

### 24. ArdentBio adds `- "/chem/lead_compounds.py"` to Content Exclusions, while `docking_runner.py` (`not excluded`) has `from chem.lead_compounds import COMPOUND_AZ991_SMILES` and hovers/uses its typed constants. Proposed solution: Keep importing sensitive constants from excluded modules into non-excluded files assuming Python language-server (`Pylance`) hover types can never enter `docking_runner.py`'s prompt context. Does this meet the goal?

- **A.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements
- **B.** No — while Content Exclusions block direct file reads, IDE **language-server (`LSP`) type/signature hover metadata** from symbols imported out of an excluded file can still surface in non-excluded open files
- **C.** Configuring Copilot Content Exclusions also blocks `git clone`, GitHub Actions runners, and `CodeQL` security scans from reading the excluded files
- **D.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files

### 25. ArdentBio's HPC bioinformaticians submit Slurm batch jobs from Linux SSH terminals (`no X11/GUI`). What key benefit does **GitHub Copilot CLI (`copilot`)** deliver directly in their SSH workflow?

- **A.** GitHub Copilot CLI (`copilot`) is a terminal-native AI coding agent that understands shell context, edits files, executes commands with approval prompts, and automates multi-step repo workflows
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **D.** Inspect **Audit Logs** (`category:copilot`, e.g., `copilot.cfb_seat_created`, `copilot.content_exclusion_changed`) for admin changes and `GET /orgs/{org}/copilot/metrics` (`>=5 active users`) for aggregated usage

### 26. An ArdentBio HPC engineer installs **GitHub Copilot CLI** (`via npm on Node.js 22+ or Linuxbrew`) and initializes it inside `~/pipelines/rnaseq-nf`. Place the four steps in exact order.

- **A.** Install Node.js `22+` (or WinGet/Homebrew) & `npm install -g @github/copilot` → `cd` into the project directory & launch `copilot` → Enter `/login` to complete GitHub OAuth authentication → Confirm directory trust & verify `/permissions show`
- **B.** Run `/login` in raw Bash before installing `@github/copilot` → Pass `--allow-all` on `/` root filesystem → Write plaintext passwords into `~/.copilot/config.json` → Downgrade to Node.js `14`
- **C.** Clone the repo inside `~/.copilot/logs/` → Set `Suggestions matching public code` to `Allow` → Run `gh auth logout` → Expect silent file edits without permission prompts
- **D.** Install `@github/copilot` → Delete `~/.copilot/session-store.db` before signing in → Disable the Organization Copilot CLI policy → Run `copilot -p` unauthenticated

### 27. By default, under which home-directory path does **GitHub Copilot CLI** store `settings.json`, `permissions-config.json`, `session-state/`, and `logs/` (`overridable via XDG_STATE_HOME / COPILOT_HOME where configured`)? (`~/____`)

- **A.** Install `@github/copilot` via `npm install -g @github/copilot` (`Node.js 22+`), `winget install GitHub.Copilot`, or Homebrew, launch `copilot` in your repo, run `/login`, and confirm folder trust
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **D.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`

### 28. An ArdentBio pipeline wrapper runs `copilot -p "Validate Nextflow config syntax" --available-tools=view,grep --____-tool=bash` to guarantee `bash` can never be called even if tool lists change. Complete the deny flag (`and state precedence`).

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Use `copilot -p "..."` for non-interactive runs (`-s` for clean stdout, `--output-format=json` for JSONL), `--available-tools` / `--deny-tool` for tool scoping, and `--fleet` for parallel subagents

### 29. An ArdentBio security architect audits non-interactive `copilot -p` scripts running in staging sandboxes. Which two CLI security practices are essential? Select two.

- **A.** Use `copilot -p "..."` for non-interactive runs (`-s` for clean stdout, `--output-format=json` for JSONL), `--available-tools` / `--deny-tool` for tool scoping, and `--fleet` for parallel subagents
- **B.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **C.** Scope non-interactive Copilot CLI automation with `--available-tools` / `--deny-tool`, `--secret-env-vars` redaction, and single-run `--trust-folder` rather than blanket `--allow-all`
- **D.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **E.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models

### 30. To save a completed non-interactive Copilot CLI run's full transcript to a local Markdown report `qc-audit.md` for GxP review (`without uploading anything to GitHub Gist`), complete the CLI flag: `copilot -p "Audit Dockerfile" --____=qc-audit.md`.

- **A.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **B.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **C.** Use Copilot CLI **infinite sessions** (auto-compaction under `~/.copilot/session-state/{id}/`), inspect `/session plan`, `/session checkpoints`, and `/session files`, and resume via `--resume` or `--continue`
- **D.** `#runSubagent` merges every raw intermediate grep output directly into the main chat's token window and pauses mid-search to interview the user after every file read

### 31. Midway through an interactive `copilot` CLI session, a researcher approved `"Always for this session"` on shell `write` operations and now wants to inspect active approvals and revert immediately to manual per-action prompts before touching `prod.nf`. Which two `/permissions` commands do that?

- **A.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **B.** Inside interactive Copilot CLI, use `/permissions show` or `/permissions manual` to inspect/set approval mode, `--model` to pin a model, and `~/.copilot/settings.json` for user preferences
- **C.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **D.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`

### 32. Which five repository/agent instruction filenames does **GitHub Copilot CLI** automatically recognize (`alongside $HOME/.copilot/copilot-instructions.md`) when working inside a multi-tool Git repository?

- **A.** Generate scripts and edit files safely in Copilot CLI via interactive **permission prompts** (`write`, `commands`), `--add-dir` for extra paths, `--secret-env-vars` redaction, and `--share` / `--share-gist`
- **B.** Configuring Copilot Content Exclusions also blocks `git clone`, GitHub Actions runners, and `CodeQL` security scans from reading the excluded files
- **C.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **D.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`

### 33. Inside `~/.copilot/session-state/{session-id}/`, which Markdown file stores the structured implementation plan displayed when you run `/session plan` in an interactive CLI session? (`____.md`)

- **A.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **B.** Generate scripts and edit files safely in Copilot CLI via interactive **permission prompts** (`write`, `commands`), `--add-dir` for extra paths, `--secret-env-vars` redaction, and `--share` / `--share-gist`
- **C.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **D.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke

### 34. An ArdentBio bioinformatics engineer configures a DuckDB Parquet assay **MCP** server in `.vscode/mcp.json` and uses **`#runSubagent`** to profile 28 Parquet schemas before Agent Mode generates TypeScript API handlers. Order the steps.

- **A.** Accept (`Keep`) all generated edits before running tests → Add `.vscode/mcp.json` after closing VS Code → Attach 80 unrelated files to main chat → Switch to `Ask` mode expecting autonomous test loops
- **B.** Define MCP servers inside `.git/HEAD` → Run `/clear` after every single edit so Agent Mode loses its plan → Skip working-set diff inspection → Force-push to `main`
- **C.** Register the MCP server in `.vscode/mcp.json` & verify tools → Delegate broad codebase search to isolated `#runSubagent` → Apply multi-file edits & run terminal tests in Agent Mode → Inspect working-set diffs & `Keep` verified changes
- **D.** Commit plaintext MCP API keys to `.github/copilot-instructions.md` → Expect `#runSubagent` to pause mid-run for interactive Q&A → Disable all workspace tools → Auto-push unreviewed edits to `main`

### 35. While a local VS Code **Agent Mode** session is mid-way through refactoring 6 TypeScript modules, the engineer spots a missing import constraint and types a follow-up steering note right into the **Agent Sessions** chat editor. Does Agent Sessions support mid-run steering across active sessions?

- **A.** No — Copilot Chat **`Ask` mode** only answers questions and proposes snippets in chat; autonomous multi-file workspace edits with iterative terminal test execution require **Agent Mode** (`or Copilot CLI`)
- **B.** Monitor local IDE, CLI, and cloud coding agents from the unified **Agent Sessions** view (`steering mid-run via chat editors`) and delegate noisy codebase research to **`#runSubagent`** for isolated context
- **C.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **D.** `#runSubagent` merges every raw intermediate grep output directly into the main chat's token window and pauses mid-search to interview the user after every file read

### 36. ArdentBio's AI platform team documents how **MCP**, **`#runSubagent`**, **Agent Sessions**, and the **Copilot coding agent** fit together. Which three statements are accurate? Select three.

- **A.** No — Copilot Chat **`Ask` mode** only answers questions and proposes snippets in chat; autonomous multi-file workspace edits with iterative terminal test execution require **Agent Mode** (`or Copilot CLI`)
- **B.** Assign a GitHub Issue or PR comment (`@copilot`) to the **Copilot coding agent (`cloud agent`)**, which runs in an ephemeral Actions sandbox, pushes to `copilot/*`, and opens a draft PR for human review
- **C.** Use **Agent Mode** with `.vscode/mcp.json` **Model Context Protocol (`MCP`)** servers to query external tools, edit multiple files, read compiler/terminal diagnostics, and self-heal until tests pass
- **D.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **E.** `#runSubagent` merges every raw intermediate grep output directly into the main chat's token window and pauses mid-search to interview the user after every file read
- **F.** Monitor local IDE, CLI, and cloud coding agents from the unified **Agent Sessions** view (`steering mid-run via chat editors`) and delegate noisy codebase research to **`#runSubagent`** for isolated context

### 37. When **Copilot Code Review** posts an inline suggested code fix on a pull request on GitHub.com (`inside a suggestion block`), what should the PR author verify before selecting `Commit suggestion`?

- **A.** Run **Copilot Code Review** locally on uncommitted IDE diffs or on GitHub.com PRs (`with Automatic Copilot code review, Review new pushes, and Review draft pull requests`), paired with human approval
- **B.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **C.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **D.** No — **Copilot Code Review** posts `Comment` reviews (`never Approve` reviews that satisfy required human branch-protection approver counts); a human reviewer must still approve

### 38. ArdentBio creates `.github/instructions/assay-gxpreview.instructions.md` (`applyTo: "pipelines/**/*.py"`) specifically to guide **Copilot Code Review** on pull requests (`and accidentally adds excludeAgent: "code-review"` in the YAML frontmatter). Proposed solution: Keep `excludeAgent: "code-review"` in `assay-gxpreview.instructions.md` expecting PR Copilot Code Review to enforce those rules. Does this meet the goal?

- **A.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **B.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **C.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements
- **D.** No — setting `excludeAgent: "code-review"` in `.instructions.md` frontmatter explicitly **prevents** Copilot Code Review from using that file (`use applyTo: without excluding code-review`)

### 39. When an ArdentBio repository administrator pushes new commits to `ardentbio/SOP-assay-standards` (`a repository linked inside a shared Copilot Space`), does someone have to re-upload the files manually for the **Copilot Space** to reflect the latest `main` branch?

- **A.** Curate **Copilot Spaces** on GitHub.com (`grouping specific repositories, files, PRs, issues, free-text notes, and custom instructions`) to ground team Q&A and IDE MCP queries on authoritative org context
- **B.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Use **GitHub Spark** to build, iterate on, and share AI-powered full-stack micro-apps (`with natural-language prompts, live preview, managed KV persistence, and optional GitHub repository sync`)

### 40. An ArdentBio lab manager prototypes a sample-plate barcode layout visualizer in **GitHub Spark** and now wants software engineers to add CI workflows and Playwright tests in Git. Can a **GitHub Spark** app be synced to a GitHub repository?

- **A.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **B.** Use **GitHub Spark** to build, iterate on, and share AI-powered full-stack micro-apps (`with natural-language prompts, live preview, managed KV persistence, and optional GitHub repository sync`)
- **C.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **D.** Curate **Copilot Spaces** on GitHub.com (`grouping specific repositories, files, PRs, issues, free-text notes, and custom instructions`) to ground team Q&A and IDE MCP queries on authoritative org context

### 41. ArdentBio configures custom instructions for its polyglot repository (`Python pipelines in pipelines/**/*.py, TypeScript UI in web/**/*.tsx`). Which two rules reflect documented GitHub behavior? Select two.

- **A.** Create modular `.github/instructions/*.instructions.md` files with YAML frontmatter `applyTo:` globs (`and optional excludeAgent: "code-review" | "cloud-agent"`) for path-specific standards
- **B.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **C.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **D.** No — setting `excludeAgent: "code-review"` in `.instructions.md` frontmatter explicitly **prevents** Copilot Code Review from using that file (`use applyTo: without excluding code-review`)
- **E.** Generate **Copilot Pull Request Summaries** on GitHub.com and enforce coding/review standards via `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` (`applyTo:`, `excludeAgent:`), and `AGENTS.md`

### 42. In `.github/prompts/crispr-qc-report.prompt.md`, which optional YAML frontmatter keys configure `(1)` whether it runs in `ask`, `edit`, or `agent` mode and `(2)` which allowed tools (`such as ['search/codebase', 'githubRepo']`) it can invoke?

- **A.** Inspect **Audit Logs** (`category:copilot`, e.g., `copilot.cfb_seat_created`, `copilot.content_exclusion_changed`) for admin changes and `GET /orgs/{org}/copilot/metrics` (`>=5 active users`) for aggregated usage
- **B.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **C.** Enable `"chat.promptFiles": true` and commit reusable `.github/prompts/*.prompt.md` files (`YAML frontmatter: description, agent, model, tools` + Markdown `#file:` links) invoked via `/prompt-name`
- **D.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files

### 43. ArdentBio's VS Code onboarding cheat-sheet summarizes Copilot Chat context variables and reusable prompt files. Which two items are accurate? Select two.

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Scope Copilot Chat with participants (`@workspace`, `@github`, `@vscode`, `@terminal`), slash commands (`/explain`, `/fix`, `/tests`, `/doc`, `/new`, `/clear`), `#file:`/`#codebase` variables, and thumbs feedback
- **E.** Enable `"chat.promptFiles": true` and commit reusable `.github/prompts/*.prompt.md` files (`YAML frontmatter: description, agent, model, tools` + Markdown `#file:` links) invoked via `/prompt-name`

### 44. ArdentBio's Enterprise Owner wants a single hard switch ensuring **no user** (`not even an external collaborator holding a personal Copilot Pro+ license`) can invoke the **Copilot cloud coding agent** inside any repository owned by `ardentbio-ent`. Where is that enforced?

- **A.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **B.** No — Repository and Organization **Content Exclusions** require **Copilot Business or Copilot Enterprise**; personal Copilot Free/Pro/Pro+ plans do not support Org Content Exclusions
- **C.** Use Enterprise `AI controls -> Agents` (`Block Copilot cloud agent` / `Block Copilot code review`) and `Only allow Copilot code review to be triggered by authorized users` to govern enterprise repos
- **D.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits

### 45. To retain `category:copilot` audit log events (`seat grants, policy edits, content exclusions`) for 7 years under GxP record-retention rules (`beyond GitHub's standard interactive audit-log retention window`), which GitHub Enterprise Cloud feature should ArdentBio configure? (**Audit log `____`**)

- **A.** Inspect **Audit Logs** (`category:copilot`, e.g., `copilot.cfb_seat_created`, `copilot.content_exclusion_changed`) for admin changes and `GET /orgs/{org}/copilot/metrics` (`>=5 active users`) for aggregated usage
- **B.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **C.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **D.** No — `GET /orgs/{org}/copilot/metrics` returns **aggregated, anonymized** team/org usage (`requiring >=5 active users`), NOT per-developer `last_activity_at` usernames; query `GET /orgs/{org}/copilot/billing/seats`

### 46. ArdentBio automates **Copilot Enterprise** seat provisioning via IdP-synced team `bioinformatics-eng` and reclaims seats idle `>30 days` using the GitHub REST API. Place the four REST lifecycle steps in order.

- **A.** Promote all developers to Organization Owner → Have engineers buy personal Copilot Pro plans → Configure Org Content Exclusions expecting personal Pro plans to inherit them → Skip seat audits
- **B.** Mint a `repo`-only PAT lacking `manage_billing:copilot` → POST CSV files to `/repos/{owner}/{repo}/issues` → Expect seats to provision automatically → Disable SAML SSO
- **C.** Authorize `manage_billing:copilot` & enable selected access → `POST /orgs/{org}/copilot/billing/selected_teams` to grant seats → `GET /orgs/{org}/copilot/billing/seats` for `last_activity_at` → `DELETE .../selected_users` to reclaim idle seats
- **D.** Query `GET /orgs/{org}/copilot/metrics` expecting per-user login names → Send unauthenticated `PUT /users/{u}/copilot` calls → Delete the GitHub Organization to free 3 seats → Re-invite members manually

---

## Domain 3 — Understand GitHub Copilot data and architecture (10–15% official weight · 14 questions)

### 47. ArdentBio's Data Protection Officer reviews **Copilot Enterprise** data flows for inline Python completions in VS Code. Once the LLM finishes generating ghost text (`over TLS ____+`) and post-filtering completes, what happens to the transient prompt (`FIM prefix/suffix + neighbor tabs`) in the inference tier?

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** On **Copilot Business & Enterprise**, prompts and completions travel over `TLS 1.2+`, process ephemerally in memory for inline completions, and are **never retained to train foundational models**
- **C.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **D.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits

### 48. Which two distinct telemetry categories (`user ____ telemetry` vs source-code prompts) must an architect never confuse when explaining **Copilot Business/Enterprise** privacy to an enterprise CISO?

- **A.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **B.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **C.** Distinguish **user engagement telemetry** (`acceptance/dismissal counts, latency, IDE version, encrypted at rest`) from **source-code prompts/suggestions** (`discarded after inline inference on Business/Enterprise`)
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 49. On an **Individual (`Copilot Free / Pro / Pro+`)** account on GitHub.com (`Settings -> Copilot`), which privacy setting (`Allow GitHub to use my code ____ from the code editor for product improvements`) must a freelancer uncheck if they do NOT want snippet retention?

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **C.** On Individual plans (`Copilot Free / Pro / Pro+`), disable `Allow GitHub to use my code snippets from the code editor for product improvements` in GitHub Copilot settings to opt out of model training
- **D.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)

### 50. A scientist opens `aligner_types.py` (`defining ReadPair and CigarOp`) in one VS Code tab and edits `variant_caller.py` (`also `.py``) in the active tab. How does the Copilot IDE extension select snippets from `aligner_types.py` (`via ____ similarity`) during inline completion?

- **A.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** The IDE extension constructs prompts from **Fill-in-the-Middle (`FIM`)** cursor prefix + suffix, language/filepath metadata, Jacobi/Jaccard-ranked snippets from open tabs, and custom instructions

### 51. On GitHub Enterprise Cloud (`Copilot Enterprise`), what advantage does a **remote semantic repository `____`** provide when engineers query `@github` / `@workspace` or **Copilot Spaces** across massive 10,000-file genomics monorepos?

- **A.** For `@workspace` and GitHub.com repository chat, Copilot uses **lexical and semantic (`embedding`) retrieval (`RAG`)** to inject top-ranked code chunks into the prompt rather than sending entire gigabyte repos
- **B.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically

### 52. ArdentBio's technical onboarding diagram contrasts context assembly for `(1)` inline editor ghost text and `(2)` `@workspace` / Copilot Spaces Chat. Which two architectural blocks are accurate? Select two.

- **A.** Include both code **before** the cursor (`prefix`) and code **after** the cursor (`suffix`) via Fill-in-the-Middle (`FIM`) alongside matching open-tab symbols
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **D.** For `@workspace` and GitHub.com repository chat, Copilot uses **lexical and semantic (`embedding`) retrieval (`RAG`)** to inject top-ranked code chunks into the prompt rather than sending entire gigabyte repos
- **E.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models

### 53. In `ardentbio`, an attacker crafts a repository comment trying to trick Copilot Chat into bypassing safety guardrails (`"Ignore all previous instructions..."`). Which server-side defense (`cloud proxy ____ moderation`) blocks this?

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** The Copilot **cloud proxy** validates entitlement tokens, applies inbound/outbound **RAI safety filters** (`hate speech, violence, sexual content, PII, prompt injection`), and runs the `~150-char` public-code filter
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free

### 54. When the proxy's **`~150-character` public-code duplication filter** compares a candidate completion against public GitHub code, does trivial indentation/whitespace reformatting bypass lexical matching?

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **C.** The Copilot **cloud proxy** validates entitlement tokens, applies inbound/outbound **RAI safety filters** (`hate speech, violence, sexual content, PII, prompt injection`), and runs the `~150-char` public-code filter
- **D.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins

### 55. Which two statements accurately describe the **GitHub Copilot cloud proxy**? Select two.

- **A.** Pass generated tokens through cloud-proxy Responsible AI toxicity/harm classifiers and the `~150-character` public-code duplication filter before IDE rendering
- **B.** The Copilot **cloud proxy** validates entitlement tokens, applies inbound/outbound **RAI safety filters** (`hate speech, violence, sexual content, PII, prompt injection`), and runs the `~150-char` public-code filter
- **C.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **D.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **E.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 56. Place the end-to-end **inline code suggestion lifecycle** steps in exact order when an ArdentBio researcher edits `primer_design.py` in VS Code under Copilot Enterprise.

- **A.** IDE bypasses Organization Content Exclusions → Forwards raw files to unauthenticated endpoints → Skips toxicity & prompt-injection filters → Publishes prompts to public GitHub Gists
- **B.** Public-code duplication filter runs offline with network unplugged → LLM generates code before receiving file language or cursor prefix → IDE validates seat tokens once per decade → Proxy disables TLS encryption
- **C.** IDE uploads your entire disk (`~/.ssh` & closed repos) over HTTP → Cloud GPUs execute your local unit tests → Copilot commits directly to `main` without ghost text → Copilot Business trains shared base LLMs on your prompt
- **D.** IDE gathers FIM prefix/suffix & open tabs (minus exclusions) → Client sends `TLS 1.2+` prompt to proxy & checks seat token → Proxy runs RAI filters, LLM & `~150+` char duplication check → IDE renders ghost text & Business skips model training

### 57. When VS Code caches an already-returned inline ghost-text completion locally for `primer_design.py` as you type the first three matching characters (`def`), why does ghost text remain instantaneous?

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** Suggestion lifecycle: typing debounce -> IDE FIM/tab context assembly -> `TLS` request to Copilot proxy -> RAI pre-filter & LLM generation -> post-filter & duplication check -> ghost-text render -> telemetry
- **D.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review

### 58. An ArdentBio scientist asks Copilot Chat `"Give me the exact PubMed PMID and DOI for the 2025 Nature Biotechnology paper by Dr. Rao on Cas13d RNA editing"` (`without web search or MCP`). Why must every returned PMID/DOI be verified externally?

- **A.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **B.** Account for LLM & Copilot architectural limits: **finite context windows**, **pre-training knowledge cutoffs**, **stochastic sampling**, **no runtime execution** during inline completion, and unseen unindexed external systems
- **C.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 59. Why can Copilot suggest an R Bioconductor function signature from `DESeq2 1.34` when ArdentBio's Docker container runs `DESeq2 1.44` with a deprecated argument removed?

- **A.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **B.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **C.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **D.** Account for LLM & Copilot architectural limits: **finite context windows**, **pre-training knowledge cutoffs**, **stochastic sampling**, **no runtime execution** during inline completion, and unseen unindexed external systems

### 60. Does GitHub Copilot run locally offline on an air-gapped cleanroom laptop that has zero outbound network access to GitHub Copilot cloud endpoints?

- **A.** Account for LLM & Copilot architectural limits: **finite context windows**, **pre-training knowledge cutoffs**, **stochastic sampling**, **no runtime execution** during inline completion, and unseen unindexed external systems
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins

---

## Domain 4 — Apply prompt engineering and context crafting (10–15% official weight · 13 questions)

### 61. An ArdentBio engineer writes: `"As a TypeScript 5.6 bioinformatics developer, implement parseVcfHeader(lines: string[]): VcfHeaderMeta (#file:vcf-types.ts); reject missing ##fileformat=VCFv4.3 with VcfFormatError; zero regex backtracking."` Which four structural pillars make this prompt sharp?

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **C.** Structure effective prompts with **Role/Goal**, **Grounded Context** (`#file`, `#selection`, versions), **Explicit Constraints** (`security, error handling, edge cases`), and **Output Format** (`types, signatures`)
- **D.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions

### 62. In Python 3.12, compare `def gc(s):` against `def calc_gc_fraction(dna_seq: str) -> float: """Return (G+C)/len(dna_seq) in [0.0, 1.0] for uppercase/lowercase IUPAC A/C/G/T; raise ValueError on empty or invalid bases."""`. Why does the second signature produce bug-free inline code on try one?

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** Inspect **Audit Logs** (`category:copilot`, e.g., `copilot.cfb_seat_created`, `copilot.content_exclusion_changed`) for admin changes and `GET /orgs/{org}/copilot/metrics` (`>=5 active users`) for aggregated usage
- **D.** Guide inline completions directly inside source files using **top-of-file architecture comments**, **explicit parameter/return type annotations**, and **domain-specific function/variable names**

### 63. In VS Code Copilot Chat, a researcher highlights 12 lines of a failing Nextflow stderr traceback inside the integrated terminal and wants Chat grounded on **only those highlighted terminal lines**. Complete the context variable: `#____`.

- **A.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **B.** Curate Copilot's active context: open target interface/DTO tabs (`closing unrelated files`), attach `#file:`, `#selection`, `#sym:`, or **Copilot Spaces**, and scope `.instructions.md` with `applyTo:` globs
- **C.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 64. ArdentBio configures `.github/instructions/r-bioc.instructions.md` (`applyTo: "**/*.R,**/*.Rmd"`). Does Copilot inject `r-bioc.instructions.md` when a developer runs Copilot Code Review on a pull request touching ONLY `web/src/PlateGrid.tsx`?

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** Curate Copilot's active context: open target interface/DTO tabs (`closing unrelated files`), attach `#file:`, `#selection`, `#sym:`, or **Copilot Spaces**, and scope `.instructions.md` with `applyTo:` globs
- **C.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **D.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files

### 65. Which two developer actions directly control what context GitHub Copilot selects for a Python refactoring task in VS Code? Select two.

- **A.** Curate Copilot's active context: open target interface/DTO tabs (`closing unrelated files`), attach `#file:`, `#selection`, `#sym:`, or **Copilot Spaces**, and scope `.instructions.md` with `applyTo:` globs
- **B.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **C.** Close unrelated editor tabs and open the exact target interfaces/DTOs (`or pin them via #file:`) so neighbor-tab ranking injects clean, relevant types
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **E.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files

### 66. ArdentBio's internal LIMS sample barcodes follow a bespoke structure (`"ARD-2026-PLT09-WELL_H12-REP2" -> SampleKey(year=2026, plate=9, row="H", col=12, replicate=2)`). Which prompting strategy yields exact parser + serializer symmetry?

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **C.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **D.** Use **zero-shot prompting** for standard algorithms/APIs, and **few-shot prompting** (`1–3 concrete input -> output examples`) when teaching proprietary schemas, custom DSLs, or bespoke test conventions

### 67. Why can supplying **15 redundant, verbose examples** in a few-shot prompt sometimes perform *worse* than supplying **`2–3` crisp, diverse examples**?

- **A.** Use **zero-shot prompting** for standard algorithms/APIs, and **few-shot prompting** (`1–3 concrete input -> output examples`) when teaching proprietary schemas, custom DSLs, or bespoke test conventions
- **B.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **C.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free

### 68. An ArdentBio engineer needs a full TypeScript plate-assay QC module (`CSV parser -> control-well Z'-factor math -> outlier flagger -> PDF summary DTO`). What prompt-crafting workflow gives the highest quality?

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** No — keeping dozens of unrelated tabs open and reusing one marathon chat thread across unrelated tasks causes **context pollution and token truncation**; close stale tabs and use `/clear` or `#runSubagent`
- **D.** Decompose complex epics into small, testable steps, state exact framework/SDK versions (`preventing pre-cutoff API drift`), and iterate in follow-up turns using compiler or test output

### 69. When asking Copilot to write regexes for FASTQ header validation in TypeScript or Python, which explicit security constraint prevents Regular Expression Denial of Service (`ReDoS`) on malformed 10 KB headers?

- **A.** Decompose complex epics into small, testable steps, state exact framework/SDK versions (`preventing pre-cutoff API drift`), and iterate in follow-up turns using compiler or test output
- **B.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **C.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 70. ArdentBio standardizes GxP assay validation test scaffolding in VS Code via `.github/prompts/gxp-pytest.prompt.md`. Place the four setup and usage steps in exact order.

- **A.** Set `"chat.promptFiles": true` & add `.github/prompts/api.prompt.md` → Link exemplars (`#file:`) & commit to Git → Close unrelated tabs & invoke `/api` in Chat with inputs → Run `/clear` (or open a new chat) before switching topics
- **B.** Save `prompt.txt` outside the workspace → Add `applyTo: "false"` so nothing matches → Type `@terminal` expecting inline ghost text in closed files → Commit unreviewed output
- **C.** Embed production PATs inside `.github/prompts/deploy.prompt.md` → Publish private prompts to public npm → Send one-word `'fix'` with zero file context → Skip code review
- **D.** Place prompt templates in `.github/workflows/prompt.yml` expecting `/prompt` in Chat → Keep 45 unrelated legacy files open in tabs → Reuse one 200-turn chat thread across 12 services → Omit output types and error rules

### 71. Why should ArdentBio commit durable coding rules (`Python 3.12, Polars over Pandas, ruff, pytest, no shell=True`) into `.github/copilot-instructions.md` rather than asking 90 scientists to paste a 12-line preamble manually into every Chat prompt?

- **A.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **B.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **C.** Write **positive, specific constraints** (`'use parameterized pg queries with $1 parameters'`) rather than vague negations, ground domain rules via `#file:`, and codify standards in `.prompt.md` / `.instructions.md`
- **D.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases

### 72. After finishing a 20-turn R `ggplot2` volcano-plot styling conversation in VS Code Chat, a scientist immediately types `"Write an AWS IAM Terraform policy for S3 bucket ardent-fastq"` in the same chat. Complete the command they SHOULD have run first: `/____`.

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** Copilot Chat appends prior turns from the active thread up to its **token context limit**; run `/clear` (or open a new chat) on topic switches and use `#runSubagent` to keep noisy exploration out of history
- **C.** `#runSubagent` merges every raw intermediate grep output directly into the main chat's token window and pauses mid-search to interview the user after every file read
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 73. Which two statements accurately describe how **chat history and context windows** behave in GitHub Copilot Chat and Agent Mode? Select two.

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** `#runSubagent` merges every raw intermediate grep output directly into the main chat's token window and pauses mid-search to interview the user after every file read
- **C.** No — keeping dozens of unrelated tabs open and reusing one marathon chat thread across unrelated tasks causes **context pollution and token truncation**; close stale tabs and use `/clear` or `#runSubagent`
- **D.** Run `/clear` or start a new Chat session when pivoting to an unrelated module so stale conversation turns do not consume token budget or bias new answers
- **E.** Copilot Chat appends prior turns from the active thread up to its **token context limit**; run `/clear` (or open a new chat) on topic switches and use `#runSubagent` to keep noisy exploration out of history

---

## Domain 5 — Improve developer productivity with GitHub Copilot (10–15% official weight · 14 questions)

### 74. ArdentBio's Python assay SDK needs NumPy-style docstrings (`Parameters, Returns, Raises`) and `mypy --strict` type annotations added across 16 untyped helper modules. How can Copilot complete this safely?

- **A.** Use `Inline Chat`, `Copilot Edits`, **Next Edit Suggestions**, and `/doc` to scaffold repetitive DTOs/validators, extract pure functions to reduce cyclomatic complexity, and generate JSDoc/OpenAPI/Mermaid docs
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **D.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically

### 75. A 260-line Python script mixes CLI `argparse`, CSV file reading, Z'-factor assay math, and Matplotlib plotting inside `main()`. How should you prompt Copilot to refactor it for GxP unit testing?

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **C.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **D.** Use `Inline Chat`, `Copilot Edits`, **Next Edit Suggestions**, and `/doc` to scaffold repetitive DTOs/validators, extract pure functions to reduce cyclomatic complexity, and generate JSDoc/OpenAPI/Mermaid docs

### 76. An ArdentBio engineer wants Copilot in VS Code to scaffold 4 TypeScript Zod schemas, update 3 React components, run `npm run typecheck && npm test`, read a Vitest failure, and fix the off-by-one slice automatically. Proposed solution: Submit the prompt in **`Ask` mode** without switching to **Agent Mode** (`or Copilot CLI`). Does this meet the goal?

- **A.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements
- **B.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **C.** No — Copilot Chat **`Ask` mode** only answers questions and proposes snippets in chat; autonomous multi-file workspace edits with iterative terminal test execution require **Agent Mode** (`or Copilot CLI`)
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free

### 77. A TypeScript engineer at ArdentBio needs to maintain an unfamiliar Nextflow DSL2 workflow (`channel.fromFilePairs(...).combine(...)`) and wants a clear explanation of channel cardinality without leaving VS Code. Which slash command delivers that? (`/____`)

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** Minimize context switching by running `/explain` on complex regexes/SQL/legacy modules, `@terminal` + `/fix` (`or Copilot CLI`) on shell/build errors, and `@workspace` / **Spaces** for repo onboarding
- **D.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions

### 78. How does pairing a team **Copilot Space** (`ardentbio-genomics-platform`) with local IDE `@workspace` help scientists avoid spending hours hunting across Slack and Confluence?

- **A.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **B.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **C.** Minimize context switching by running `/explain` on complex regexes/SQL/legacy modules, `@terminal` + `/fix` (`or Copilot CLI`) on shell/build errors, and `@workspace` / **Spaces** for repo onboarding
- **D.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins

### 79. ArdentBio needs 500 synthetic FASTQ read pairs (`150 bp A/C/G/T sequences, Phred+33 ASCII quality strings, synthetic @SIM_READ_0001 headers, zero human donor DNA`) for pipeline smoke tests. How should Copilot generate them?

- **A.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **B.** Generate schema-valid **synthetic test fixtures** (`zero real customer PII`) and modernize legacy code (`e.g., Java 8 -> 21, Python 2 -> 3.12, callbacks -> async/await`) incrementally behind characterization tests
- **C.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **D.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions

### 80. ArdentBio is migrating legacy Python 2.7 bioinformatics scripts (`integer division 3/2 == 1`, `str` vs `bytes`, `dict.iteritems()`) to Python 3.12. Why MUST characterization tests be captured before running Copilot Edits?

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **C.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **D.** Generate schema-valid **synthetic test fixtures** (`zero real customer PII`) and modernize legacy code (`e.g., Java 8 -> 21, Python 2 -> 3.12, callbacks -> async/await`) incrementally behind characterization tests

### 81. When migrating legacy R base-graphics scripts to typed Python `Polars` pipelines with Copilot, what intermediate artifact guarantees numerical equivalence across both languages?

- **A.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **D.** Generate schema-valid **synthetic test fixtures** (`zero real customer PII`) and modernize legacy code (`e.g., Java 8 -> 21, Python 2 -> 3.12, callbacks -> async/await`) incrementally behind characterization tests

### 82. When generating `pytest` unit tests for `BenchlingApiSync.py` (`which calls external HTTPS REST endpoints with rate-limit HTTP 429 Retry-After headers`), how should you instruct Copilot `/tests`?

- **A.** Use `/tests` (paired with testing `.instructions.md` conventions) to generate unit and integration tests with isolated I/O mocks/stubs, parameterized table cases, and deterministic teardown
- **B.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **C.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **D.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically

### 83. ArdentBio's GxP validation SOP defines rules for Copilot-generated unit and integration tests. Which two rules are required? Select two.

- **A.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **B.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **C.** Lock existing legacy behavior with characterization and boundary-value unit tests **before** refactoring idioms with Copilot Edits or Agent Mode
- **D.** Use `/tests` (paired with testing `.instructions.md` conventions) to generate unit and integration tests with isolated I/O mocks/stubs, parameterized table cases, and deterministic teardown
- **E.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review

### 84. For `calc_z_prime(pos_mean, pos_sd, neg_mean, neg_sd)` (`formula: 1 - 3*(pos_sd + neg_sd) / abs(pos_mean - neg_mean)`), which critical edge case will crash with `ZeroDivisionError` unless explicitly tested and guarded?

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **C.** Prompt explicitly for **boundary and adversarial edge cases** (`null/empty, 0/-1/MAX_INT, leap-year/DST timestamps, Unicode, timeouts, race conditions`) and assert concrete outputs/errors (`never tautologies`)
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free

### 85. Before approving an AI-assisted PR in `ardentbio/assay-qc`, reviewers verify three engineering gates. Which three gates apply? Select three.

- **A.** Use `/tests` (paired with testing `.instructions.md` conventions) to generate unit and integration tests with isolated I/O mocks/stubs, parameterized table cases, and deterministic teardown
- **B.** Validate that security fixes (`such as CodeQL Copilot Autofix`) replace string-concatenated queries/commands with parameterized APIs and pass full regression + SAST checks
- **C.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **D.** Prompt explicitly for **boundary and adversarial edge cases** (`null/empty, 0/-1/MAX_INT, leap-year/DST timestamps, Unicode, timeouts, race conditions`) and assert concrete outputs/errors (`never tautologies`)
- **E.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **F.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases

### 86. On a pull request in `ardentbio/lims-portal`, `CodeQL` flags a SQL injection alert in a raw DuckDB/Postgres query and proposes a **Copilot Autofix** diff using bound `$1` parameters. Place the governance and verification steps in order.

- **A.** Set `Suggestions matching public code = Block` in Org policy → Inspect `CodeQL` PR **Copilot Autofix** diff & explanation → Validate the patch (`parameterized SQL`) & package imports → Commit fix, pass `CodeQL` + tests & get human PR approval
- **B.** Set `Suggestions matching public code = Allow` while expecting full IP indemnity on verbatim matches → Auto-commit every Copilot Autofix directly to `main` untested → Disable `CodeQL` PR checks → Skip human review
- **C.** Delete Content Exclusions thinking they block `CodeQL` → Paste live DB passwords into PR comments to test Autofix → Merge with red integration tests → Rotate credentials next quarter
- **D.** Paste GPL-3.0 source into `.github/copilot-instructions.md` → Treat Copilot Chat as binding legal license sign-off → Dismiss `CodeQL` SQLi alerts without patching → Deploy to production

### 87. A Python script checks `if read_id in blacklisted_ids:` inside a 10-million-read loop where `blacklisted_ids` is a `50,000`-item Python `list` (`O(N * M)` = `500 billion` comparisons!). Which 1-word data-structure change should Copilot suggest?

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** Use Copilot Chat and **CodeQL Copilot Autofix** to remediate vulnerabilities (`SQLi -> parameterized queries, XSS -> encoding, path traversal, SSRF`) and eliminate `O(n^2)` loops or `N+1` ORM queries
- **C.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

---

## Domain 6 — Configure privacy, content exclusions, and safeguards (10–15% official weight · 13 questions)

### 88. ArdentBio's security team configures Organization **Content Exclusions** (`- "/molecules/**"`, `- "**/*.mol2"`) across `ardentbio` and verifies enforcement and auditability. Place the four steps in exact order.

- **A.** Put exclusion rules in `package.json` → Wait 14 days for policy propagation → Have a Repo Admin delete Organization-level Content Exclusions → Disable Enterprise Audit Logs
- **B.** Add `fnmatch` globs (`- "/secrets/**"`) in `Content exclusion` → Allow `<=30 min` (or reload IDE) for policy sync → Verify crossed-out icon & `copilot.content_exclusion_changed` log → Avoid cross-file imports where IDE LSP hover types surface
- **C.** List tracked `secrets.yaml` in `.gitignore` expecting Copilot to exclude it → Set `Suggestions matching public code = Allow` → Disable IDE TLS verification → Share one seat login across 10 engineers
- **D.** Configure Content Exclusions on a personal Copilot Free plan → Write PCRE lookbehind regexes instead of `fnmatch` globs → Expect exclusions to block `git clone` and Actions runs → Ignore IDE status icons

### 89. In Organization `Settings -> Copilot -> Content exclusion`, ArdentBio wants to exclude `.env` and `.env.*` files across **every repository** in the `ardentbio` organization using a single YAML top-level key. Complete that YAML top-level repository key: `"____":`.

- **A.** No — Repository and Organization **Content Exclusions** require **Copilot Business or Copilot Enterprise**; personal Copilot Free/Pro/Pro+ plans do not support Org Content Exclusions
- **B.** Configure **Content Exclusions** (`Copilot Business & Enterprise`) in Repo/Org settings with YAML `fnmatch` globs (`- "/secrets/**"`); rules combine additively (`Repo cannot weaken Org`) and sync in `<=30 min`
- **C.** Configuring Copilot Content Exclusions also blocks `git clone`, GitHub Actions runners, and `CodeQL` security scans from reading the excluded files
- **D.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files

### 90. An ArdentBio scientist runs a third-party non-GitHub CLI tool (`or pastes an excluded file's contents manually into an external browser chatbot`). Do GitHub Copilot **Content Exclusions** stop non-Copilot tools or manual copy-pasting outside Copilot?

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** Excluded files are omitted from inline completions, IDE Chat, and Copilot Code Review, **but** IDE language-server (`LSP`) hover types from imported symbols can still surface, and `git`/`CodeQL`/Actions are unaffected
- **C.** Configuring Copilot Content Exclusions also blocks `git clone`, GitHub Actions runners, and `CodeQL` security scans from reading the excluded files
- **D.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files

### 91. Organization `ardentbio` excludes `"*": ["- /molecules/**"]`. A repo admin on `ardentbio/sandbox-docking` wants Copilot completions inside `/molecules/test.sdf`. Proposed solution: Leave Repository Content Exclusions empty (`or add a comment`) on `ardentbio/sandbox-docking` expecting that to override and re-enable `/molecules/test.sdf`. Does this meet the goal?

- **A.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **B.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **C.** No — Repository administrators **cannot delete or override** Organization-level Content Exclusions (`Repo and Org exclusions combine additively, and the most restrictive policy wins`)
- **D.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements

### 92. ArdentBio's patent counsel asks whether code authored with **GitHub Copilot Enterprise** (`with Suggestions matching public code = Block`) belongs to ArdentBio for patent/proprietary filing purposes and carries Microsoft/GitHub IP Indemnity. What is accurate?

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **C.** No — Repository and Organization **Content Exclusions** require **Copilot Business or Copilot Enterprise**; personal Copilot Free/Pro/Pro+ plans do not support Org Content Exclusions
- **D.** Customers retain ownership of their code (`GitHub claims no copyright over suggestions`), and **Copilot Business / Enterprise** provide **IP Indemnity** when `Suggestions matching public code` is set to **`Block`**

### 93. A bioinformatics contractor uses a personal **GitHub Copilot Pro** subscription (`with Suggestions matching public code = Block`) on a personal laptop outside ArdentBio's Enterprise. Proposed solution: Rely on GitHub's corporate **Copilot IP Indemnity** under that personal Copilot Pro plan. Does this meet the goal?

- **A.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **B.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements
- **C.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **D.** No — GitHub's **Copilot IP Indemnity** on Business/Enterprise ceases to cover suggestions when `Suggestions matching public code` is set to **`Allow`**; set the filter to **`Block`**

### 94. Why does GitHub require customers claiming **Copilot IP Indemnity** to keep Copilot's duplication filter (`Block`) and Responsible AI filtering active rather than tampering with or disabling them?

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **D.** Customers retain ownership of their code (`GitHub claims no copyright over suggestions`), and **Copilot Business / Enterprise** provide **IP Indemnity** when `Suggestions matching public code` is set to **`Block`**

### 95. In VS Code (`when an academic lab org sets Suggestions matching public code = Allow`), where can a developer inspect **GitHub Code Referencing** logs (`matched public repository URL, commit SHA, and license type`) when a completion matches public GitHub code?

- **A.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **D.** Set **`Suggestions matching public code = Block`** to suppress `~150+` char matches against public GitHub repos; when set to **`Allow`**, **Code Referencing** logs matched repo URLs and licenses in the IDE

### 96. If **GitHub Code Referencing** (`under Allow`) reports that a 180-character helper matched a public GitHub repository licensed under **`GPL-3.0-only`**, why is that license metadata critical before pasting into a closed-source commercial therapeutic platform?

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** Set **`Suggestions matching public code = Block`** to suppress `~150+` char matches against public GitHub repos; when set to **`Allow`**, **Code Referencing** logs matched repo URLs and licenses in the IDE
- **C.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 97. ArdentBio's legal & engineering policy summarizes **`Suggestions matching public code`** (`Block` vs `Allow`) on Copilot Enterprise. Which two statements belong in that policy? Select two.

- **A.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **B.** Set **`Suggestions matching public code = Block`** to suppress `~150+` char matches against public GitHub repos; when set to **`Allow`**, **Code Referencing** logs matched repo URLs and licenses in the IDE
- **C.** Customers retain ownership of their code (`GitHub claims no copyright over suggestions`), and **Copilot Business / Enterprise** provide **IP Indemnity** when `Suggestions matching public code` is set to **`Block`**
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **E.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits

### 98. An ArdentBio developer updates Organization Content Exclusions at `10:00 AM` and tests a file in PyCharm at `10:02 AM`, seeing ghost text still appear. Before filing a bug, what documented behavior and quick action should they take?

- **A.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **B.** Diagnose missing completions or unexpected exclusions via **Copilot Diagnostics / Output logs**: verify seat assignment, filetype toggle, active exclusion icon (`most restrictive org wins`), and TLS proxy allowlists (`*.githubcopilot.com`)
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins

### 99. An academic collaborator (`holding only a personal Copilot Pro seat, not a Copilot Business/Enterprise seat`) asks to configure Repository **Content Exclusions** on their personal `github.com/dr-lin/rna-notes` user-namespace repository. Proposed solution: Open `Settings -> Copilot -> Content exclusion` on the personal user-owned repository under Copilot Pro. Does this meet the goal?

- **A.** No — Repository and Organization **Content Exclusions** require **Copilot Business or Copilot Enterprise**; personal Copilot Free/Pro/Pro+ plans do not support Org Content Exclusions
- **B.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **C.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements
- **D.** Choose **Copilot Free** for capped monthly completions/chats or **Copilot Pro / Pro+** for individual developers needing unlimited completions, higher premium-model quotas, and **GitHub Spark**

### 100. ArdentBio's IT helpdesk troubleshoots two recurring developer questions: `(1)` `"Why is Copilot Chat disabled for me when ArdentBio enabled it?"` (`the user also belongs to an external clinical-consortium org that disabled Chat`) and `(2)` `"Why did Copilot stop connecting on our new lab VLAN?"`. Which two answers are accurate? Select two.

- **A.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **B.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **C.** When a user receives Copilot policies from multiple Organizations (or Enterprise + Org), GitHub enforces the **most restrictive** policy (`Block overrides Allow; Disabled overrides Enabled`)
- **D.** Diagnose missing completions or unexpected exclusions via **Copilot Diagnostics / Output logs**: verify seat assignment, filetype toggle, active exclusion icon (`most restrictive org wins`), and TLS proxy allowlists (`*.githubcopilot.com`)
- **E.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

---

## Answer Key and Explanations

### Question 1 — `A` (Use GitHub Copilot responsibly)

Correct answer: A (is correct). LLMs emit statistically likely code tokens rather than proving statistical theorems; subtle rank-tie or step-up vs step-down monotonicity bugs can distort assay significance thresholds while passing syntax checks. [Skill 1.1: Describe risks and limitations of Generative AI tools | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/responsible-ai-with-github-copilot/)]

- **A:** Correct. Generative AI risks and limitations (`1.1`) address probabilistic next-token prediction, hallucinations, outdated APIs, and bias—not IDE installation or REST seat billing.
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 2 — `C` (Use GitHub Copilot responsibly)

Correct answer: C (is correct). Verify `@biocore/fastq-quality-trimmer` exists in ArdentBio's Artifactory/npm registry with authentic maintainer provenance (`since attackers register AI-hallucinated package scopes with postinstall malware`). [Skill 1.1: Describe risks and limitations of Generative AI tools | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/responsible-ai-with-github-copilot/)]

- **A:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **B:** Incorrect. Copilot Audit Logs and Metrics API (`2.14`) separate security/compliance event logs from anonymized (`>=5`-user) adoption telemetry.
- **C:** Correct. Package hallucination / slopsquatting verification (`1.1`, `1.4`) protects dependency supply chains—not Markdown PR summaries or status badges.
- **D:** Incorrect. GitHub Spark (`2.11`) accelerates full-stack micro-app prototyping and deployment directly from natural language and visual controls.

### Question 3 — `D` (Use GitHub Copilot responsibly)

Correct answer: D (is correct). Counter **automation complacency (`automation bias`)** by requiring traceable requirement-to-test boundary assertions and independent human code review before GxP branch merges. [Skill 1.1: Describe risks and limitations of Generative AI tools | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/responsible-ai-with-github-copilot/)]

- **A:** Incorrect. Installing GitHub Copilot CLI (`2.5`) uses `@github/copilot` (`Node 22+`), WinGet, or Homebrew, followed by `/login` OAuth and directory trust confirmation.
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **D:** Correct. Automation bias (`1.1`, `1.4`) occurs when developers accept syntactically clean completions without verifying business logic or security invariants.

### Question 4 — `A, B` (Use GitHub Copilot responsibly)

Correct answers: A and B (are correct). LLMs can hallucinate plausible-sounding PyPI/CRAN/npm packages (`slopsquatting`) and generate syntactically valid code with subtle scientific or security flaws. [Skill 1.1: Describe risks and limitations of Generative AI tools | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/responsible-ai-with-github-copilot/)]

- **A:** Correct. Package hallucination / slopsquatting verification (`1.1`, `1.4`) protects dependency supply chains—not Markdown PR summaries or status badges.
- **B:** Correct. Generative AI risks and limitations (`1.1`) address probabilistic next-token prediction, hallucinations, outdated APIs, and bias—not IDE installation or REST seat billing.
- **C:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **D:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **E:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 5 — `B` (Use GitHub Copilot responsibly)

Correct answer: B (is correct). **Fairness** mandates testing and mitigating demographic or ancestral performance disparities in AI-assisted software and pipelines. [Skill 1.2: Describe ethical and responsible AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-code-completion)]

- **A:** Incorrect. Copilot CLI programmatic flags (`2.6`) control non-interactive scripting (`-p`, `-s`, `--output-format=json`), tool permissions, and `--fleet` parallelism.
- **B:** Correct. Microsoft/GitHub Responsible AI (`1.2`) centers on Fairness, Reliability & Safety, Privacy & Security, Inclusiveness, Transparency, and human Accountability.
- **C:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **D:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).

### Question 6 — `A` (Use GitHub Copilot responsibly)

Correct answer: A (is correct). **Privacy & Security** governs safeguarding sensitive genomic/personal data, secrets, and system boundaries throughout AI-assisted development. [Skill 1.2: Describe ethical and responsible AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-code-completion)]

- **A:** Correct. Microsoft/GitHub Responsible AI (`1.2`) centers on Fairness, Reliability & Safety, Privacy & Security, Inclusiveness, Transparency, and human Accountability.
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **D:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).

### Question 7 — `C` (Use GitHub Copilot responsibly)

Correct answer: C (is correct). **Transparency** (`documenting AI assistance openly`) and **Accountability** (`recording explicit human verification and sign-off`). [Skill 1.2: Describe ethical and responsible AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-code-completion)]

- **A:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **B:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **C:** Correct. Ethical AI governance (`1.2`) requires human ownership, license respect, and transparent review—never treating Copilot as an autonomous merge authority.
- **D:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.

### Question 8 — `B, E, F` (Use GitHub Copilot responsibly)

Correct answers: B, E, and F (are correct). Compliance with all six Responsible AI principles, ancestral/accessibility equity (`Fairness & Inclusiveness`), and transparent disclosure paired with human accountability and license compliance. [Skill 1.2: Describe ethical and responsible AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-code-completion)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Correct. Microsoft/GitHub Responsible AI (`1.2`) centers on Fairness, Reliability & Safety, Privacy & Security, Inclusiveness, Transparency, and human Accountability.
- **C:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **D:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **E:** Correct. Ethical AI governance (`1.2`) requires human ownership, license respect, and transparent review—never treating Copilot as an autonomous merge authority.
- **F:** Correct. Fairness and Inclusiveness (`1.2`, `1.3`) ensure AI-assisted software serves diverse users equitably and meets accessibility standards.

### Question 9 — `C` (Use GitHub Copilot responsibly)

Correct answer: C (is correct). Mandate `shell=False` argument lists (`["samtools", "view", f"{validated_id}.bam"]`) in `.instructions.md` and enforce **`CodeQL` (`py/command-line-injection`) / Bandit** in CI. [Skill 1.3: Identify potential harms and mitigation strategies of AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/overview)]

- **A:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **B:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **C:** Correct. Harm mitigation (`1.3`) combines RAI safety filters, bias testing, SAST scanning, and privacy controls—not disabling code review.
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).

### Question 10 — `D` (Use GitHub Copilot responsibly)

Correct answer: D (is correct). Workspace path containment (`blocking writes outside the repo`), manual human approval gates on filesystem/shell tools, and diff review before accepting any action. [Skill 1.3: Identify potential harms and mitigation strategies of AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/overview)]

- **A:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **B:** Incorrect. False: `#runSubagent` runs autonomously in its **own isolated context window** without pausing for user feedback, returning only the distilled result (`2.9`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Correct. Indirect prompt-injection defense (`1.3`, `1.5`) guards Agent Mode and MCP tool invocations against malicious instructions hidden in external data.

### Question 11 — `A, C` (Use GitHub Copilot responsibly)

Correct answers: A and C (are correct). Never paste donor genomic PII or live AWS credentials into Copilot prompts (`use synthetic reference genomes + Content Exclusions`), and enforce **`CodeQL` + Secret Scanning Push Protection** on every repository. [Skill 1.3: Identify potential harms and mitigation strategies of AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/overview)]

- **A:** Correct. Harm mitigation (`1.3`) combines RAI safety filters, bias testing, SAST scanning, and privacy controls—not disabling code review.
- **B:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **C:** Correct. Data minimization in prompts (`1.3`, `1.5`) prevents accidental exposure of regulated personal data or live secrets.
- **D:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **E:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).

### Question 12 — `D` (Use GitHub Copilot responsibly)

Correct answer: D (is correct). Prompting with explicit security/type constraints -> inspecting QC logic & verifying internal Artifactory packages -> running pytest/Vitest edge-case suites + `CodeQL` -> completing human GxP PR review. [Skill 1.4: Explain the need to validate AI output | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)]

- **A:** Incorrect. Incorrect: pasting real PII into prompts and bypassing human review violates privacy and Responsible AI governance.
- **B:** Incorrect. Incorrect: merging unverified LLM output or replacing human peer review with Copilot Code Review violates Responsible AI accountability.
- **C:** Incorrect. Incorrect: blindly installing hallucinated package names exposes builds to dependency confusion and slopsquatting.
- **D:** Correct. Correct order: constrained prompt -> manual logic & dependency check (`blocking slopsquatting`) -> automated tests/SAST -> human PR review.

### Question 13 — `D` (Use GitHub Copilot responsibly)

Correct answer: D (is correct). Syntactically clean array calls silently propagate `NaN` or floating-point underflow unless validated against explicit domain contracts and edge-case unit tests. [Skill 1.4: Explain the need to validate AI output | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)]

- **A:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **B:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **C:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **D:** Correct. Validating AI output (`1.4`) requires human code review, automated tests, and security scanning before merge.

### Question 14 — `B` (Use GitHub Copilot responsibly)

Correct answer: B (is correct). Because LLM output remains **non-deterministic** across model updates and context shifts; deterministic automated test suites are the only repeatable proof of functional correctness. [Skill 1.4: Explain the need to validate AI output | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)]

- **A:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **B:** Correct. Non-determinism (`1.4`, `3.5`) means syntactic plausibility never guarantees functional equivalence across repeated prompts.
- **C:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 15 — `D` (Use GitHub Copilot responsibly)

Correct answer: D (is correct). No — `GET /orgs/{org}/copilot/metrics` provides anonymized aggregate adoption telemetry (`>= 5` active users) without usernames; call `GET /orgs/{org}/copilot/billing/seats` to inspect per-user `assignee.login` and `last_activity_at`. [Skill 1.4: Explain the need to validate AI output | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)]

- **A:** Incorrect. The proposed GitHub Copilot configuration or workflow violates at least one stated governance, privacy, or technical requirement. No — `GET /orgs/{org}/copilot/metrics` provides anonymized aggregate adoption telemetry (`>= 5` active users) without usernames; call `GET /orgs/{org}/copilot/billing/seats` to inspect per-user `assignee.login` and `last_activity_at`.
- **B:** Incorrect. Copilot Audit Logs and Metrics API (`2.14`) separate security/compliance event logs from anonymized (`>=5`-user) adoption telemetry.
- **C:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **D:** Correct. Per-seat dormancy audits (`2.14`, `2.15`) require `/copilot/billing/seats`, whereas `/copilot/metrics` aggregates anonymized adoption stats.

### Question 16 — `D` (Use GitHub Copilot responsibly)

Correct answer: D (is correct). Lock `Suggestions matching public code = Block` at Enterprise level, enforce Content Exclusions on proprietary molecule structures/donor configs, prohibit real donor data in prompts, and require green CI + human PR approval. [Skill 1.5: Identify how to operate GitHub Copilot responsibly | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **C:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **D:** Correct. Responsible Copilot operation (`1.5`) pairs duplication filtering, Content Exclusions, zero-PII prompting, and mandatory human PR review.

### Question 17 — `A` (Use GitHub Copilot responsibly)

Correct answer: A (is correct). Yes — locking `Block` at Enterprise scope preserves IP Indemnity across all child orgs while Content Exclusions, Enterprise AI controls, `CodeQL`, and `2` human approvals enforce defense in depth. [Skill 1.5: Identify how to operate GitHub Copilot responsibly | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use)]

- **A:** Correct. Evaluate whether every stated plan tier, CLI/IDE mechanism, context scope, and Enterprise/Org policy requirement is genuinely met.
- **B:** Incorrect. Enabling `Block` on public-code duplication (`6.2`, `6.3`) is a mandatory condition for GitHub Copilot IP Indemnity protection.
- **C:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **D:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).

### Question 18 — `A` (Use GitHub Copilot responsibly)

Correct answer: A (is correct). No — automated AI review is an assistive check only; validated human reviewers retain sole regulatory and engineering accountability for release approval. [Skill 1.5: Identify how to operate GitHub Copilot responsibly | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use)]

- **A:** Correct. Human-in-the-loop accountability (`1.2`, `1.4`) ensures engineers remain responsible for correctness, security, and license compliance.
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **D:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).

### Question 19 — `A` (Use GitHub Copilot features)

Correct answer: A (is correct). They must sign in with their SSO-authorized corporate GitHub identity (`or EMU account` such as `priya_ardentbio`) to which an active Copilot seat has been assigned. [Skill 2.1: Enable Copilot in the IDE | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/quickstart)]

- **A:** Correct. Enabling Copilot in the IDE (`2.1`) requires installing the IDE extension, authenticating with GitHub, and holding an active Copilot plan.
- **B:** Incorrect. Copilot Audit Logs and Metrics API (`2.14`) separate security/compliance event logs from anonymized (`>=5`-user) adoption telemetry.
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).

### Question 20 — `B` (Use GitHub Copilot features)

Correct answer: B (is correct). **GitHub Copilot Enterprise** requires **GitHub Enterprise Cloud (`GHEC`)** (`whereas Copilot Business is available to organizations on GitHub Team or GitHub Enterprise Cloud`). [Skill 2.1: Enable Copilot in the IDE | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/quickstart)]

- **A:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **B:** Correct. Organization/Enterprise Copilot tiers (`2.1`, `2.15`, `6.2`) add centralized governance, Content Exclusions, audit logs, and IP Indemnity.
- **C:** Incorrect. Individual Copilot tiers (`2.1`, `2.15`) serve single accounts without Organization policy management or Org Content Exclusions.
- **D:** Incorrect. Content Exclusions (`2.3`, `6.1`) are only enforced for seats governed under Copilot Business or Copilot Enterprise.

### Question 21 — `B` (Use GitHub Copilot features)

Correct answer: B (is correct). **Inline Chat** (`Ctrl+I` / `Cmd+I`) opens a scoped prompt overlay directly at the editor selection with an in-place side-by-side/inline diff preview. [Skill 2.2: Trigger Copilot through inline suggestions, chat, CLI, and agent mode | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Correct. Triggering Copilot across surfaces (`2.2`) matches Inline Chat, `Ask`, `Edit`, Agent Mode, and Copilot CLI to task complexity.
- **C:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **D:** Incorrect. Only **Agent Mode** (or **Copilot CLI**, `2.2`, `2.9`) autonomously edits multiple files and runs terminal verification loops.

### Question 22 — `B, E` (Use GitHub Copilot features)

Correct answers: B and E (are correct). **Ghost-text completions + Next Edit Suggestions (`NES`)** stream inline `Tab`-accepted predictions as you type/edit, while **Agent Mode** autonomously plans multi-file edits, calls MCP tools, and runs terminal tests. [Skill 2.2: Trigger Copilot through inline suggestions, chat, CLI, and agent mode | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot)]

- **A:** Incorrect. Only **Agent Mode** (or **Copilot CLI**, `2.2`, `2.9`) autonomously edits multiple files and runs terminal verification loops.
- **B:** Correct. Triggering Copilot across surfaces (`2.2`) matches Inline Chat, `Ask`, `Edit`, Agent Mode, and Copilot CLI to task complexity.
- **C:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **E:** Correct. Inline completions and Next Edit Suggestions (`2.2`, `5.1`) accelerate localized cursor-level coding and follow-on edits.

### Question 23 — `C` (Use GitHub Copilot features)

Correct answer: C (is correct). Yes — files matched by Repository or Organization **Content Exclusions** are excluded from IDE inline completions, IDE Copilot Chat (`including @workspace`), and GitHub.com PR Copilot Code Review. [Skill 2.3: Configure content exclusions for specific files or repositories (app knowledge) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion)]

- **A:** Incorrect. Adding a tracked path to `.gitignore` (`6.1`) does NOT stop Copilot from reading that file in the IDE or on GitHub.com.
- **B:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **C:** Correct. IDE/repo content exclusion awareness (`2.3`) prevents specified paths from being read into Copilot prompts on Business and Enterprise plans.
- **D:** Incorrect. False: Copilot Content Exclusions apply strictly to **GitHub Copilot** features—they never restrict Git repository ACLs, Actions workflows, or `CodeQL` (`6.1`).

### Question 24 — `B` (Use GitHub Copilot features)

Correct answer: B (is correct). No — while `lead_compounds.py` is never read directly by Copilot, IDE language-server (`LSP`) hover/type metadata exposed on symbols imported into non-excluded `docking_runner.py` can still appear in local prompt context (`load secrets/sensitive payloads at runtime from vaults instead`). [Skill 2.3: Configure content exclusions for specific files or repositories (app knowledge) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion)]

- **A:** Incorrect. The proposed GitHub Copilot configuration or workflow violates at least one stated governance, privacy, or technical requirement. No — while `lead_compounds.py` is never read directly by Copilot, IDE language-server (`LSP`) hover/type metadata exposed on symbols imported into non-excluded `docking_runner.py` can still appear in local prompt context (`load secrets/sensitive payloads at runtime from vaults instead`).
- **B:** Correct. GitHub documents that IDE semantic/LSP hover information (`6.1`) is outside direct Content Exclusion file-read blocking when symbols are imported.
- **C:** Incorrect. False: Copilot Content Exclusions apply strictly to **GitHub Copilot** features—they never restrict Git repository ACLs, Actions workflows, or `CodeQL` (`6.1`).
- **D:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).

### Question 25 — `A` (Use GitHub Copilot features)

Correct answer: A (is correct). It provides an **agentic terminal assistant** that reads Nextflow/Slurm scripts, diagnoses job error logs, edits pipeline configs, and runs approved shell validation commands without leaving SSH. [Skill 2.4: Define GitHub Copilot CLI and how it benefits developers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-cli)]

- **A:** Correct. GitHub Copilot CLI (`2.4`) brings agentic file editing, command execution, and GitHub workflow integration directly to the terminal.
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **D:** Incorrect. Copilot Audit Logs and Metrics API (`2.14`) separate security/compliance event logs from anonymized (`>=5`-user) adoption telemetry.

### Question 26 — `A` (Use GitHub Copilot features)

Correct answer: A (is correct). Installing `@github/copilot` (`Node 22+` or Brew/WinGet) -> `cd`ing to `~/pipelines/rnaseq-nf` & running `copilot` -> authenticating via `/login` -> confirming directory trust & reviewing `/permissions show`. [Skill 2.5: Identify the steps for installing GitHub Copilot CLI | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/get-started/cli-quickstart)]

- **A:** Correct. Correct order: install `@github/copilot` -> `cd` to project & start `copilot` -> authenticate via `/login` -> confirm folder trust & inspect tool permissions.
- **B:** Incorrect. Incorrect: `/login` runs inside interactive `copilot`, npm installs require Node.js `22+`, and `config.json` never stores plaintext passwords.
- **C:** Incorrect. Incorrect: `~/.copilot/logs/` stores session logs, and Copilot CLI requires approval before modifying files in default mode.
- **D:** Incorrect. Incorrect: disabling the org Copilot CLI policy blocks access, and authentication must precede non-interactive execution.

### Question 27 — `A` (Use GitHub Copilot features)

Correct answer: A (is correct). By default, GitHub Copilot CLI stores its configuration, permissions, logs, and local session state under **`~/.copilot/`**. [Skill 2.5: Identify the steps for installing GitHub Copilot CLI | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/get-started/cli-quickstart)]

- **A:** Correct. Installing GitHub Copilot CLI (`2.5`) uses `@github/copilot` (`Node 22+`), WinGet, or Homebrew, followed by `/login` OAuth and directory trust confirmation.
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **D:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).

### Question 28 — `D` (Use GitHub Copilot features)

Correct answer: D (is correct). Passing `--deny-tool=bash` explicitly blocks the `bash` tool, and **`--deny-tool` always takes precedence over `--available-tools` / `--allow-tool`**. [Skill 2.6: Describe key GitHub Copilot CLI features and commands | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/copilot-cli-reference/cli-programmatic-reference)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Correct. Copilot CLI programmatic flags (`2.6`) control non-interactive scripting (`-p`, `-s`, `--output-format=json`), tool permissions, and `--fleet` parallelism.

### Question 29 — `A, C` (Use GitHub Copilot features)

Correct answers: A and C (are correct). Avoid `--allow-all` (`--yolo`) on non-disposable hosts in favor of granular `--available-tools` / `--deny-tool` + `--allow-url` / `--deny-url`, and redact custom tokens via `--secret-env-vars=VAR1,VAR2`. [Skill 2.6: Describe key GitHub Copilot CLI features and commands | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/copilot-cli-reference/cli-programmatic-reference)]

- **A:** Correct. Copilot CLI programmatic flags (`2.6`) control non-interactive scripting (`-p`, `-s`, `--output-format=json`), tool permissions, and `--fleet` parallelism.
- **B:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **C:** Correct. Least-privilege Copilot CLI flags (`2.6`, `2.8`) restrict tool execution, path writes, and secret exposure in automated scripts.
- **D:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **E:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).

### Question 30 — `C` (Use GitHub Copilot features)

Correct answer: C (is correct). Passing `--share=qc-audit.md` (`default ./copilot-session-<ID>.md` if path omitted) writes the session transcript to a local Markdown file (`unlike --share-gist, which creates a secret GitHub Gist`). [Skill 2.7: Use GitHub Copilot CLI interactively and in sessions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-cli/cli-best-practices)]

- **A:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **B:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **C:** Correct. Interactive Copilot CLI sessions (`2.7`) persist plans, compaction checkpoints, and artifacts in `~/.copilot/session-state/` for `--resume`.
- **D:** Incorrect. False: `#runSubagent` runs autonomously in its **own isolated context window** without pausing for user feedback, returning only the distilled result (`2.9`).

### Question 31 — `B` (Use GitHub Copilot features)

Correct answer: B (is correct). Run `/permissions show` to inspect currently active session approvals, then run `/permissions manual` to clear session auto-approvals and require manual confirmation again. [Skill 2.7: Use GitHub Copilot CLI interactively and in sessions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-cli/cli-best-practices)]

- **A:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **B:** Correct. Copilot CLI interactive slash commands and `~/.copilot/settings.json` (`2.6`, `2.8`) govern tool approvals and model selection (`config.json` is internal runtime state).
- **C:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **D:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).

### Question 32 — `A` (Use GitHub Copilot features)

Correct answer: A (is correct). `.github/copilot-instructions.md`, `.github/instructions/**/*.instructions.md`, `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` (`plus directories listed in COPILOT_CUSTOM_INSTRUCTIONS_DIRS`). [Skill 2.8: Generate scripts and manage files with GitHub Copilot CLI | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/copilot-cli-reference/cli-config-dir-reference)]

- **A:** Correct. Copilot CLI file and script management (`2.8`) enforces explicit write/command approval, `--add-dir` path boundaries, and secret redaction (`GITHUB_TOKEN` redacted by default).
- **B:** Incorrect. False: Copilot Content Exclusions apply strictly to **GitHub Copilot** features—they never restrict Git repository ACLs, Actions workflows, or `CodeQL` (`6.1`).
- **C:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **D:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).

### Question 33 — `B` (Use GitHub Copilot features)

Correct answer: B (is correct). Copilot CLI stores the session's structured implementation plan at `~/.copilot/session-state/{session-id}/plan.md` (`alongside events.jsonl, checkpoints/, and files/`). [Skill 2.8: Generate scripts and manage files with GitHub Copilot CLI | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/copilot-cli-reference/cli-config-dir-reference)]

- **A:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **B:** Correct. Copilot CLI file and script management (`2.8`) enforces explicit write/command approval, `--add-dir` path boundaries, and secret redaction (`GITHUB_TOKEN` redacted by default).
- **C:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **D:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).

### Question 34 — `C` (Use GitHub Copilot features)

Correct answer: C (is correct). Registering `.vscode/mcp.json` & verifying tools -> delegating 28-schema profiling to `#runSubagent` -> applying multi-file edits + `npm test` in Agent Mode -> inspecting working-set diffs & `Keep`ing verified changes. [Skill 2.9: Use Agent Mode, Copilot Edits, and MCP for enhanced development and workflows; manage Agent Sessions and delegate tasks to Sub-Agents for optimized context usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp)]

- **A:** Incorrect. Incorrect: `Ask` mode cannot autonomously edit files or execute terminal loops, and `Keep` should follow diff & test verification.
- **B:** Incorrect. Incorrect: `.git/HEAD` is Git metadata (not `.vscode/mcp.json`), and diffs must be reviewed before commit.
- **C:** Correct. Correct order: register `.vscode/mcp.json` tools -> isolate noisy research via `#runSubagent` -> iterate edits/tests in Agent Mode -> inspect & `Keep` verified diffs.
- **D:** Incorrect. Incorrect: never commit secrets to `.github/copilot-instructions.md`, and `#runSubagent` runs autonomously in isolated context without pausing for user input.

### Question 35 — `B` (Use GitHub Copilot features)

Correct answer: B (is correct). Yes — the **Agent Sessions** view lets you monitor progress, send mid-run steering corrections, review tool-approval prompts, and switch cleanly across local, background CLI, and cloud coding agent sessions. [Skill 2.9: Use Agent Mode, Copilot Edits, and MCP for enhanced development and workflows; manage Agent Sessions and delegate tasks to Sub-Agents for optimized context usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp)]

- **A:** Incorrect. Only **Agent Mode** (or **Copilot CLI**, `2.2`, `2.9`) autonomously edits multiple files and runs terminal verification loops.
- **B:** Correct. Agent Sessions and `#runSubagent` (`2.9`) provide unified multi-agent orchestration and isolated sub-agent context windows.
- **C:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **D:** Incorrect. False: `#runSubagent` runs autonomously in its **own isolated context window** without pausing for user feedback, returning only the distilled result (`2.9`).

### Question 36 — `B, C, F` (Use GitHub Copilot features)

Correct answers: B, C, and F (are correct). `.vscode/mcp.json` exposes external schemas/tools to Agent Mode, `#runSubagent` executes research in an isolated context window, and `Agent Sessions` tracks both local agents and cloud coding agent draft-PR runs. [Skill 2.9: Use Agent Mode, Copilot Edits, and MCP for enhanced development and workflows; manage Agent Sessions and delegate tasks to Sub-Agents for optimized context usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp)]

- **A:** Incorrect. Only **Agent Mode** (or **Copilot CLI**, `2.2`, `2.9`) autonomously edits multiple files and runs terminal verification loops.
- **B:** Correct. Copilot coding agent (`2.9`) executes asynchronous repository tasks in an isolated cloud sandbox and opens a draft PR without merging autonomously.
- **C:** Correct. Agent Mode + MCP (`2.9`) connects Copilot to external tools/APIs via `.vscode/mcp.json` and iterates across edits and terminal runs autonomously.
- **D:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **E:** Incorrect. False: `#runSubagent` runs autonomously in its **own isolated context window** without pausing for user feedback, returning only the distilled result (`2.9`).
- **F:** Correct. Agent Sessions and `#runSubagent` (`2.9`) provide unified multi-agent orchestration and isolated sub-agent context windows.

### Question 37 — `A` (Use GitHub Copilot features)

Correct answer: A (is correct). Inspect the suggested diff for semantic accuracy, edge cases, and imports, commit it to the PR branch so **CI tests and `CodeQL`** execute against it, and still obtain required human reviewer approval. [Skill 2.10: Use Copilot for code review and coding assistance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/configure-code-review)]

- **A:** Correct. Copilot Code Review (`2.10`) posts `Comment` reviews with `suggestion` blocks—never counting toward required human merge approvals.
- **B:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **C:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **D:** Incorrect. Copilot Code Review (`1.4`, `2.10`) supplements—never replaces—required human pull-request approvals.

### Question 38 — `D` (Use GitHub Copilot features)

Correct answer: D (is correct). No — `excludeAgent: "code-review"` explicitly instructs **Copilot Code Review** to ignore that file (`remove excludeAgent or set excludeAgent: "cloud-agent"` if you want only Code Review to read it). [Skill 2.10: Use Copilot for code review and coding assistance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/configure-code-review)]

- **A:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **B:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **C:** Incorrect. The proposed GitHub Copilot configuration or workflow violates at least one stated governance, privacy, or technical requirement. No — `excludeAgent: "code-review"` explicitly instructs **Copilot Code Review** to ignore that file (`remove excludeAgent or set excludeAgent: "cloud-agent"` if you want only Code Review to read it).
- **D:** Correct. `excludeAgent: "code-review"` (`2.11`) tells GitHub.com to omit that instruction file during Copilot Code Review.

### Question 39 — `A` (Use GitHub Copilot features)

Correct answer: A (is correct). No — GitHub repositories and files linked into a **Copilot Space** stay dynamically synchronized with repository updates (`respecting each viewer's GitHub repository read permissions`). [Skill 2.11: Utilize Spaces, Spark, Pull Request summaries, and customizable review standards via instructions files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)]

- **A:** Correct. Copilot Spaces (`2.11`) organize shareable, always-synced multi-repo project context so responses stay grounded in team architecture.
- **B:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. GitHub Spark (`2.11`) accelerates full-stack micro-app prototyping and deployment directly from natural language and visual controls.

### Question 40 — `B` (Use GitHub Copilot features)

Correct answer: B (is correct). Yes — **GitHub Spark** micro-apps support two-way/repository creation sync to a GitHub repository (`and Codespaces / VS Code editing`) when a prototype graduates to full engineering maintenance. [Skill 2.11: Utilize Spaces, Spark, Pull Request summaries, and customizable review standards via instructions files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)]

- **A:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **B:** Correct. GitHub Spark (`2.11`) accelerates full-stack micro-app prototyping and deployment directly from natural language and visual controls.
- **C:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **D:** Incorrect. Copilot Spaces (`2.11`) organize shareable, always-synced multi-repo project context so responses stay grounded in team architecture.

### Question 41 — `A, E` (Use GitHub Copilot features)

Correct answers: A and E (are correct). Put shared cross-stack rules in `.github/copilot-instructions.md` and stack-specific rules in `.github/instructions/*.instructions.md` with `applyTo:` globs (`omitting excludeAgent when both cloud agent and Code Review should use them`). [Skill 2.11: Utilize Spaces, Spark, Pull Request summaries, and customizable review standards via instructions files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)]

- **A:** Correct. Path-scoped `.instructions.md` files (`2.11`) automatically inject targeted coding and review rules only when matching files are touched.
- **B:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **C:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **D:** Incorrect. `excludeAgent: "code-review"` (`2.11`) tells GitHub.com to omit that instruction file during Copilot Code Review.
- **E:** Correct. PR Summaries and custom instruction files (`2.11`) automate reviewer context and tailor Copilot code generation/review (`without affecting raw inline ghost text where unsupported`).

### Question 42 — `C` (Use GitHub Copilot features)

Correct answer: C (is correct). YAML frontmatter supports `agent:` (`'ask'`, `'edit'`, `'agent'`, or custom agent name), `model:`, `tools:` (`array of permitted built-in/MCP tools`), and `description:`. [Skill 2.12: Understand the limits, options, feedback, and commands of GitHub Copilot Chat; include prompt file reuse for consistent responses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/configure-custom-instructions-in-your-ide/add-repository-instructions-in-your-ide)]

- **A:** Incorrect. Copilot Audit Logs and Metrics API (`2.14`) separate security/compliance event logs from anonymized (`>=5`-user) adoption telemetry.
- **B:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **C:** Correct. Workspace `.prompt.md` prompt files (`2.12`) standardize repeatable task prompts across VS Code and JetBrains teams.
- **D:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).

### Question 43 — `D, E` (Use GitHub Copilot features)

Correct answers: D and E (are correct). `#file:`, `#selection`, `#sym:`, `#codebase`, and `#terminalSelection` ground Chat prompts on exact workspace artifacts, while `.github/prompts/*.prompt.md` (`with "chat.promptFiles": true`) exposes reusable `/slash` prompts. [Skill 2.12: Understand the limits, options, feedback, and commands of GitHub Copilot Chat; include prompt file reuse for consistent responses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/configure-custom-instructions-in-your-ide/add-repository-instructions-in-your-ide)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Correct. Copilot Chat participants, slash commands, `#` context variables, and feedback ratings (`2.12`) focus intent and report quality signals.
- **E:** Correct. Workspace `.prompt.md` prompt files (`2.12`) standardize repeatable task prompts across VS Code and JetBrains teams.

### Question 44 — `C` (Use GitHub Copilot features)

Correct answer: C (is correct). In Enterprise **`AI controls -> Agents`**, enable **`Block Copilot cloud agent in all repositories owned by ardentbio-ent`**. [Skill 2.13: Configure organization-wide policy management; enable Copilot Code Review policies and manage feature availability across IDEs and github.com | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/block-agentic-features)]

- **A:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **B:** Incorrect. Content Exclusions (`2.3`, `6.1`) are only enforced for seats governed under Copilot Business or Copilot Enterprise.
- **C:** Correct. Enterprise repository-level agent blocks (`2.13`) protect enterprise repos even when a contributor holds an external personal Copilot plan.
- **D:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).

### Question 45 — `A` (Use GitHub Copilot features)

Correct answer: A (is correct). Configure **GitHub Enterprise Audit Log Streaming** (`to immutable S3, Azure Blob Storage, Splunk, or Datadog`) so `copilot.*` events are archived continuously for multi-year compliance. [Skill 2.14: Utilize audit log events | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-audit-logs-for-copilot-business)]

- **A:** Correct. Copilot Audit Logs and Metrics API (`2.14`) separate security/compliance event logs from anonymized (`>=5`-user) adoption telemetry.
- **B:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **C:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **D:** Incorrect. Per-seat dormancy audits (`2.14`, `2.15`) require `/copilot/billing/seats`, whereas `/copilot/metrics` aggregates anonymized adoption stats.

### Question 46 — `C` (Use GitHub Copilot features)

Correct answer: C (is correct). Authorizing `manage_billing:copilot` for `ardentbio`, assigning `bioinformatics-eng` via `POST /orgs/{org}/copilot/billing/selected_teams`, polling `GET .../billing/seats` (`last_activity_at`), and revoking idle seats via `DELETE .../selected_users` automates GxP seat hygiene. [Skill 2.15: Manage subscriptions using the REST API | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/rest/copilot/copilot-user-management)]

- **A:** Incorrect. Incorrect: personal Copilot Free/Pro/Pro+ plans do NOT inherit Organization Content Exclusions.
- **B:** Incorrect. Incorrect: Copilot seat REST endpoints live under `/orgs/{org}/copilot/billing/...` and require `manage_billing:copilot` billing authorization.
- **C:** Correct. Correct order: authorize `manage_billing:copilot` -> assign via `POST .../selected_teams` (or `selected_users`) -> audit `/seats` -> `DELETE` dormant assignments.
- **D:** Incorrect. Incorrect: `/copilot/metrics` returns aggregated anonymized stats (`>=5` active users), whereas `/copilot/billing/seats` exposes per-user `last_activity_at`.

### Question 47 — `B` (Understand GitHub Copilot data and architecture)

Correct answer: B (is correct). The transient inline prompt and raw code context (`sent over TLS 1.2+`) are **discarded from memory** after serving the response and are **never retained to train foundation models**. [Skill 3.1: Explain data usage, flow, and sharing | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-copilot-policies-as-an-individual-subscriber)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Correct. Copilot Business/Enterprise data handling (`3.1`) guarantees `TLS 1.2+` encryption and zero foundational-model training on customer code (`Free/Pro provide a training opt-out toggle`).
- **C:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **D:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).

### Question 48 — `C` (Understand GitHub Copilot data and architecture)

Correct answer: C (is correct). **User engagement telemetry** (`accepted/shown counts, language, IDE, latency` — stored encrypted for Metrics API) versus **customer source-code prompts/completions** (`never stored for foundation-model training on Business/Enterprise`). [Skill 3.1: Explain data usage, flow, and sharing | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-copilot-policies-as-an-individual-subscriber)]

- **A:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **B:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **C:** Correct. Data flow architecture (`3.1`) separates operational/metrics telemetry from ephemeral prompt/completion payloads.
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 49 — `C` (Understand GitHub Copilot data and architecture)

Correct answer: C (is correct). Uncheck **`Allow GitHub to use my code snippets from the code editor for product improvements`** (`whereas Copilot Business and Enterprise enforce zero snippet-training retention automatically`). [Skill 3.1: Explain data usage, flow, and sharing | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-copilot-policies-as-an-individual-subscriber)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **C:** Correct. Individual privacy settings (`3.1`, `6.1`) govern optional snippet training on personal plans (`whereas Business/Enterprise disable code-snippet training by default`).
- **D:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.

### Question 50 — `D` (Understand GitHub Copilot data and architecture)

Correct answer: D (is correct). It compares same-language open editor tabs using **token-similarity scoring (`Jaccard/Jacobi similarity`)** around the cursor window and injects the highest-scoring neighbor snippets into the prompt. [Skill 3.2: Describe input processing and prompt building | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot)]

- **A:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Correct. Input processing and prompt building (`3.2`) combines cursor prefix + suffix (`FIM`), relevant open-tab snippets, and repository instructions.

### Question 51 — `A` (Understand GitHub Copilot data and architecture)

Correct answer: A (is correct). Pre-built **server-side semantic + lexical indexes** retrieve accurate cross-file chunks in milliseconds without waiting for every laptop to embed 10,000 files locally (`while strictly honoring repo permissions and Content Exclusions`). [Skill 3.2: Describe input processing and prompt building | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot)]

- **A:** Correct. Retrieval-augmented generation (`RAG`, `3.2`) selects the highest-relevance code slices that fit within the model's context token budget.
- **B:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).

### Question 52 — `A, D` (Understand GitHub Copilot data and architecture)

Correct answers: A and D (are correct). Inline completions combine **FIM (`prefix + suffix`)** + open-tab similarity (`minus Content Exclusions`), while `@workspace` and Spaces execute **RAG (`semantic + lexical chunk retrieval`)**. [Skill 3.2: Describe input processing and prompt building | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot)]

- **A:** Correct. Fill-in-the-Middle (`FIM`, `3.2`) enables inline completions to align return types and variable names with surrounding downstream lines.
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **D:** Correct. Retrieval-augmented generation (`RAG`, `3.2`) selects the highest-relevance code slices that fit within the model's context token budget.
- **E:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).

### Question 53 — `C` (Understand GitHub Copilot data and architecture)

Correct answer: C (is correct). The **GitHub Copilot cloud proxy's Responsible AI (`RAI`) safety & prompt-injection classifiers** block biosecurity/harmful requests and unsafe outputs regardless of jailbreak phrasing. [Skill 3.3: Explain proxy filtering and post-processing | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-chat-in-your-ide)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Correct. Proxy filtering and post-processing (`3.3`) enforces auth, RAI moderation, public-code duplication checks, and stop-token trimming.
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).

### Question 54 — `C` (Understand GitHub Copilot data and architecture)

Correct answer: C (is correct). No — duplication matching normalizes surrounding whitespace/formatting over **`~150+` character** spans so re-indented verbatim blocks of public GitHub code are still caught. [Skill 3.3: Explain proxy filtering and post-processing | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-chat-in-your-ide)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **C:** Correct. Proxy filtering and post-processing (`3.3`) enforces auth, RAI moderation, public-code duplication checks, and stop-token trimming.
- **D:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).

### Question 55 — `A, B` (Understand GitHub Copilot data and architecture)

Correct answers: A and B (are correct). It validates OAuth/seat entitlement over **`TLS 1.2+`** before running inbound/outbound **RAI moderation**, and it enforces **`~150-character` public-code duplication filtering** (`Block` vs `Allow` Code Referencing). [Skill 3.3: Explain proxy filtering and post-processing | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-chat-in-your-ide)]

- **A:** Correct. Cloud-proxy post-processing (`3.3`, `3.4`) enforces both RAI content safety and public-code matching policies prior to displaying ghost text.
- **B:** Correct. Proxy filtering and post-processing (`3.3`) enforces auth, RAI moderation, public-code duplication checks, and stop-token trimming.
- **C:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **D:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **E:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 56 — `D` (Understand GitHub Copilot data and architecture)

Correct answer: D (is correct). VS Code collects `primer_design.py` FIM prefix/suffix & neighbor `.py` tabs (`honoring Content Exclusions`), authenticates over `TLS 1.2+` at the proxy, runs RAI + `~150+` char duplication post-filters, and renders ghost text with zero model-training storage. [Skill 3.4: Visualize code suggestion lifecycle | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/paths/copilot/)]

- **A:** Incorrect. Incorrect: Content Exclusions block excluded paths from entering prompts, and prompts are never published to Gists.
- **B:** Incorrect. Incorrect: Copilot LLM inference and public-code duplication checks execute in the cloud proxy over authenticated TLS.
- **C:** Incorrect. Incorrect: inline completion sends scoped editor context over TLS, never runs tests on inference GPUs, and Business/Enterprise never trains base models on customer prompts.
- **D:** Correct. Correct order: IDE FIM/tab assembly (respecting exclusions) -> TLS proxy auth -> RAI + LLM + public-code filter -> ghost-text render & zero training retention.

### Question 57 — `C` (Understand GitHub Copilot data and architecture)

Correct answer: C (is correct). Client-side **prefix-match suggestion caching** reuses the valid filtered completion as long as your typed characters match its prefix, avoiding redundant network round-trips. [Skill 3.4: Visualize code suggestion lifecycle | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/paths/copilot/)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Correct. Code suggestion lifecycle (`3.4`) traces a completion from keystroke pause through IDE context assembly, cloud proxy inference/filtering, and ghost-text display.
- **D:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).

### Question 58 — `B` (Understand GitHub Copilot data and architecture)

Correct answer: B (is correct). LLMs frequently **hallucinate plausible-looking numeric PMIDs and DOIs** by recombining real author names, journals, and number formats from pre-training. [Skill 3.5: Describe limitations of LLMs and Copilot | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-coding-agent)]

- **A:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **B:** Correct. LLM and Copilot limitations (`3.5`) explain why models hallucinate post-cutoff APIs, vary across runs, truncate overflow tokens, and need tests/MCP.
- **C:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 59 — `D` (Understand GitHub Copilot data and architecture)

Correct answer: D (is correct). Base LLM weights blend multiple historical package versions (`knowledge-cutoff and frequency bias`); attach the active `DESCRIPTION` / `renv.lock` (`or inspect function signatures via Agent Mode / R help`) to ground exact versions. [Skill 3.5: Describe limitations of LLMs and Copilot | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-coding-agent)]

- **A:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **B:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **C:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **D:** Correct. LLM and Copilot limitations (`3.5`) explain why models hallucinate post-cutoff APIs, vary across runs, truncate overflow tokens, and need tests/MCP.

### Question 60 — `A` (Understand GitHub Copilot data and architecture)

Correct answer: A (is correct). No — GitHub Copilot is a **cloud-backed AI service** requiring authenticated `HTTPS` connectivity to GitHub's cloud proxy and model endpoints (`offline laptops cannot generate Copilot completions`). [Skill 3.5: Describe limitations of LLMs and Copilot | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-coding-agent)]

- **A:** Correct. LLM and Copilot limitations (`3.5`) explain why models hallucinate post-cutoff APIs, vary across runs, truncate overflow tokens, and need tests/MCP.
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).

### Question 61 — `C` (Apply prompt engineering and context crafting)

Correct answer: C (is correct). **Persona (`TypeScript 5.6 bioinformatics`)**, **Context (`#file:vcf-types.ts`)**, **Explicit Constraints (`VCFv4.3 check, zero catastrophic regex backtracking`)**, and **Typed Output (`VcfHeaderMeta`)**. [Skill 4.1: Describe prompt structure and context | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **C:** Correct. Prompt structure (`4.1`) combines clear intent, grounded workspace context, explicit constraints, and expected output format.
- **D:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).

### Question 62 — `D` (Apply prompt engineering and context crafting)

Correct answer: D (is correct). Descriptive identifier naming, Python type annotations, and a contract docstring specify domain (`DNA GC content`), case normalization, `[0.0, 1.0]` range, and invalid-base `ValueError` handling right in the FIM prefix. [Skill 4.1: Describe prompt structure and context | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Incorrect. Copilot Audit Logs and Metrics API (`2.14`) separate security/compliance event logs from anonymized (`>=5`-user) adoption telemetry.
- **D:** Correct. In-editor context signals (`4.1`, `4.4`) anchor Fill-in-the-Middle inline completions without leaving the code buffer.

### Question 63 — `B` (Apply prompt engineering and context crafting)

Correct answer: B (is correct). `#terminalSelection` injects the currently highlighted text from the VS Code integrated terminal (`whereas #terminalLastCommand attaches the most recent terminal command and its output`). [Skill 4.2: Understand how context is determined | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)]

- **A:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **B:** Correct. Context determination (`4.2`) controls which open tabs, `#` chat variables, workspace indexes, and path-matched instructions enter the prompt.
- **C:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 64 — `B` (Apply prompt engineering and context crafting)

Correct answer: B (is correct). No — `applyTo: "**/*.R,**/*.Rmd"` does not match `web/src/PlateGrid.tsx`, so `r-bioc.instructions.md` is skipped (`preventing R rules from polluting TypeScript PR reviews`). [Skill 4.2: Understand how context is determined | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Correct. Context determination (`4.2`) controls which open tabs, `#` chat variables, workspace indexes, and path-matched instructions enter the prompt.
- **C:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **D:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).

### Question 65 — `A, C` (Apply prompt engineering and context crafting)

Correct answers: A and C (are correct). Keep only relevant `.py` domain/interface tabs open (`closing unrelated R/YAML/notebook tabs`), and pin exact `#file:` / `#selection` references (`backed by path-scoped .instructions.md`). [Skill 4.2: Understand how context is determined | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)]

- **A:** Correct. Context determination (`4.2`) controls which open tabs, `#` chat variables, workspace indexes, and path-matched instructions enter the prompt.
- **B:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **C:** Correct. Curating open tabs and `#file:` attachments (`4.2`, `4.4`) directly improves prompt signal-to-noise ratio.
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **E:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).

### Question 66 — `D` (Apply prompt engineering and context crafting)

Correct answer: D (is correct). Use **few-shot prompting** with `2–3` canonical barcode <-> `SampleKey` pairs (`including single-digit wells like A01 and control wells`) using synthetic barcodes. [Skill 4.3: Use zero-shot and few-shot prompting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **C:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **D:** Correct. Zero-shot vs few-shot prompting (`4.3`) reserves token-heavier exemplars for custom team patterns that general pretraining cannot infer.

### Question 67 — `A` (Apply prompt engineering and context crafting)

Correct answer: A (is correct). Excessive repetitive examples consume valuable context-window tokens (`crowding out actual #file: source code`) and can overfit the model to incidental details shared by the examples. [Skill 4.3: Use zero-shot and few-shot prompting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat)]

- **A:** Correct. Zero-shot vs few-shot prompting (`4.3`) reserves token-heavier exemplars for custom team patterns that general pretraining cannot infer.
- **B:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **C:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).

### Question 68 — `D` (Apply prompt engineering and context crafting)

Correct answer: D (is correct). Decompose into sequential, verifiable steps (`CSV schema + parser tests -> Z'-factor pure math + boundary tests -> outlier rules -> DTO`), verifying unit tests after each step. [Skill 4.4: Apply best practices for prompt crafting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Incorrect. Clean editor tabs, `/clear` between topics, and `#runSubagent` isolation (`4.2`, `4.6`) prevent context confusion.
- **D:** Correct. Prompt-crafting best practices (`4.4`) favor incremental decomposition, version pinning, and feedback-driven iteration.

### Question 69 — `A` (Apply prompt engineering and context crafting)

Correct answer: A (is correct). Explicitly constrain input length (`<= 512 chars`) and require **linear-time non-backtracking / anchored character classes** (`forbidding nested quantifiers like (a+)+`), plus test with long adversarial strings. [Skill 4.4: Apply best practices for prompt crafting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)]

- **A:** Correct. Prompt-crafting best practices (`4.4`) favor incremental decomposition, version pinning, and feedback-driven iteration.
- **B:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **C:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 70 — `A` (Apply prompt engineering and context crafting)

Correct answer: A (is correct). Setting `"chat.promptFiles": true` + creating `.github/prompts/gxp-pytest.prompt.md` -> linking `#file:` exemplars in Git -> invoking `/gxp-pytest` with clean tabs -> running `/clear` before switching topics. [Skill 4.5: Explain prompt engineering principles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/paths/gh-copilot-2/)]

- **A:** Correct. Correct order: create `.github/prompts/*.prompt.md` -> link few-shot exemplars -> invoke `/api` with clean tab context -> reset chat on topic switch.
- **B:** Incorrect. Incorrect: reusable prompt files end in `.prompt.md` under `.github/prompts/` (`whereas applyTo: belongs to *.instructions.md`).
- **C:** Incorrect. Incorrect: never embed secrets in repository prompt files, and one-word prompts lack actionable context.
- **D:** Incorrect. Incorrect: `.github/workflows/*.yml` defines Actions workflows (not `.github/prompts/*.prompt.md`), and stale tabs + long threads cause context drift.

### Question 71 — `C` (Apply prompt engineering and context crafting)

Correct answer: C (is correct). Repository custom instructions inject consistent governance **automatically** across IDE Chat, Agent Mode, CLI, and PR Code Review without manual copy-paste drift. [Skill 4.5: Explain prompt engineering principles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/paths/gh-copilot-2/)]

- **A:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **B:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **C:** Correct. Prompt engineering principles (`4.5`) emphasize specificity, positive constraints, authoritative grounding, and reusable templates.
- **D:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).

### Question 72 — `B` (Apply prompt engineering and context crafting)

Correct answer: B (is correct). Running `/clear` (`or opening a New Chat`) resets conversational history so unrelated R plotting turns don't consume context tokens or bias the Terraform policy prompt. [Skill 4.6: Describe prompt process flow and chat history usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Correct. Prompt process flow and chat history management (`4.6`) prevent context drift and token-window eviction across unrelated tasks.
- **C:** Incorrect. False: `#runSubagent` runs autonomously in its **own isolated context window** without pausing for user feedback, returning only the distilled result (`2.9`).
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 73 — `D, E` (Apply prompt engineering and context crafting)

Correct answers: D and E (are correct). Prior turns in the active thread are re-sent within the finite context window (`so /clear prevents topic cross-contamination`), and `#runSubagent` keeps noisy multi-file research out of main chat history. [Skill 4.6: Describe prompt process flow and chat history usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Incorrect. False: `#runSubagent` runs autonomously in its **own isolated context window** without pausing for user feedback, returning only the distilled result (`2.9`).
- **C:** Incorrect. Clean editor tabs, `/clear` between topics, and `#runSubagent` isolation (`4.2`, `4.6`) prevent context confusion.
- **D:** Correct. Resetting chat history on task switches (`4.6`) avoids context confusion and token-window truncation.
- **E:** Correct. Prompt process flow and chat history management (`4.6`) prevent context drift and token-window eviction across unrelated tasks.

### Question 74 — `A` (Improve developer productivity with GitHub Copilot)

Correct answer: A (is correct). Run Copilot Edits / Agent Mode module-by-module to add strict type hints and `/doc` NumPy docstrings while executing `mypy --strict` and `pytest` to verify zero runtime behavior regressions. [Skill 5.1: Use Copilot for code generation, refactoring, and documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/developer-use-cases-for-ai-with-github-copilot/)]

- **A:** Correct. Code generation, refactoring, and documentation (`5.1`) accelerates boilerplate, structural cleanup, and API docs while preserving behavior.
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **D:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).

### Question 75 — `D` (Improve developer productivity with GitHub Copilot)

Correct answer: D (is correct). Extract pure, side-effect-free `calculate_z_prime(pos_controls, neg_controls)` domain functions (`testable directly with float arrays`) separate from CLI I/O and plotting adapters. [Skill 5.1: Use Copilot for code generation, refactoring, and documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/developer-use-cases-for-ai-with-github-copilot/)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **C:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **D:** Correct. Code generation, refactoring, and documentation (`5.1`) accelerates boilerplate, structural cleanup, and API docs while preserving behavior.

### Question 76 — `C` (Improve developer productivity with GitHub Copilot)

Correct answer: C (is correct). No — `Ask` mode cannot autonomously edit workspace files or iterate on `npm test` terminal failures; use **Agent Mode** (`or Copilot CLI`). [Skill 5.1: Use Copilot for code generation, refactoring, and documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/developer-use-cases-for-ai-with-github-copilot/)]

- **A:** Incorrect. The proposed GitHub Copilot configuration or workflow violates at least one stated governance, privacy, or technical requirement. No — `Ask` mode cannot autonomously edit workspace files or iterate on `npm test` terminal failures; use **Agent Mode** (`or Copilot CLI`).
- **B:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **C:** Correct. Only **Agent Mode** (or **Copilot CLI**, `2.2`, `2.9`) autonomously edits multiple files and runs terminal verification loops.
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).

### Question 77 — `C` (Improve developer productivity with GitHub Copilot)

Correct answer: C (is correct). Selecting the Nextflow DSL2 block and running `/explain` explains channel operators, tuple cardinality, and process inputs inline inside the IDE. [Skill 5.2: Accelerate learning and reduce context switching | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/copilot-chat-cookbook)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Correct. Accelerating learning and reducing context switching (`5.2`) keeps developers productive inside the IDE and terminal.
- **D:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).

### Question 78 — `C` (Improve developer productivity with GitHub Copilot)

Correct answer: C (is correct). The **Copilot Space** answers cross-repo SOP and schema questions grounded in authoritative org repositories/docs, while `@workspace` jumps straight to local code symbols and tests. [Skill 5.2: Accelerate learning and reduce context switching | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/copilot-chat-cookbook)]

- **A:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **B:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **C:** Correct. Accelerating learning and reducing context switching (`5.2`) keeps developers productive inside the IDE and terminal.
- **D:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).

### Question 79 — `B` (Improve developer productivity with GitHub Copilot)

Correct answer: B (is correct). Prompt Copilot (`attaching only the FASTQ format specification, zero donor files`) to generate a seeded Python script emitting deterministic synthetic 150-bp reads and Phred+33 quality lines. [Skill 5.3: Generate sample data and modernize legacy code | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/tutorials/modernize-legacy-code)]

- **A:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **B:** Correct. Sample data generation and legacy modernization (`5.3`) combine synthetic non-PII fixtures with test-backed incremental upgrades.
- **C:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **D:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).

### Question 80 — `D` (Improve developer productivity with GitHub Copilot)

Correct answer: D (is correct). In Python 2.7, `3 / 2` returned integer `1` whereas Python 3 `3 / 2` returns `1.5` (`use // when integer division was intended`); characterization tests catch silent scientific-result shifts immediately. [Skill 5.3: Generate sample data and modernize legacy code | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/tutorials/modernize-legacy-code)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **C:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **D:** Correct. Sample data generation and legacy modernization (`5.3`) combine synthetic non-PII fixtures with test-backed incremental upgrades.

### Question 81 — `D` (Improve developer productivity with GitHub Copilot)

Correct answer: D (is correct). Run the legacy R script on a seeded synthetic dataset to export golden reference CSV/Parquet outputs, then assert `polars.testing.assert_frame_equal(..., rtol=1e-9)` in `pytest`. [Skill 5.3: Generate sample data and modernize legacy code | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/tutorials/modernize-legacy-code)]

- **A:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **D:** Correct. Sample data generation and legacy modernization (`5.3`) combine synthetic non-PII fixtures with test-backed incremental upgrades.

### Question 82 — `A` (Improve developer productivity with GitHub Copilot)

Correct answer: A (is correct). Mock the HTTP transport (`respx` / `pytest-httpx`) to simulate `200 OK`, `429 Retry-After` backoff, `500` retries, and schema validation errors deterministically without calling live Benchling servers. [Skill 5.4: Generate unit and integration tests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/develop-unit-tests-using-github-copilot-tools/)]

- **A:** Correct. Generating unit and integration tests (`5.4`) automates test scaffolding, dependency isolation, and parameterized coverage.
- **B:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **C:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **D:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).

### Question 83 — `C, D` (Improve developer productivity with GitHub Copilot)

Correct answers: C and D (are correct). Capture characterization golden tests before modernizing legacy scientific code, and combine isolated HTTP/S3 unit mocks (`moto`/`respx`) with real containerized DB integration tests (`Testcontainers`). [Skill 5.4: Generate unit and integration tests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/develop-unit-tests-using-github-copilot-tools/)]

- **A:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **B:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **C:** Correct. Characterization testing (`5.3`, `5.4`) guarantees legacy modernization preserves subtle business edge cases.
- **D:** Correct. Generating unit and integration tests (`5.4`) automates test scaffolding, dependency isolation, and parameterized coverage.
- **E:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).

### Question 84 — `C` (Improve developer productivity with GitHub Copilot)

Correct answer: C (is correct). When `pos_mean == neg_mean` (`zero dynamic range between positive and negative controls`), plus `NaN`/`Inf`, negative standard deviations, or empty control arrays! [Skill 5.5: Identify edge cases and write assertions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/copilot-chat-cookbook)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **C:** Correct. Edge-case identification and assertion quality (`5.5`) ensures tests catch real boundary defects rather than inflating superficial coverage.
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).

### Question 85 — `A, B, D` (Improve developer productivity with GitHub Copilot)

Correct answers: A, B, and D (are correct). Assert exact numerical tolerances (`pytest.approx`) and zero-division/`NaN`/empty edge cases (`never tautological mocks`), isolate external I/O cleanly, and verify `CodeQL` Autofix patches pass SAST and unit suites. [Skill 5.5: Identify edge cases and write assertions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/copilot-chat-cookbook)]

- **A:** Correct. Generating unit and integration tests (`5.4`) automates test scaffolding, dependency isolation, and parameterized coverage.
- **B:** Correct. Verified security remediation (`5.6`) confirms Autofix patches eliminate root-cause injection sinks without breaking callers.
- **C:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **D:** Correct. Edge-case identification and assertion quality (`5.5`) ensures tests catch real boundary defects rather than inflating superficial coverage.
- **E:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **F:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).

### Question 86 — `A` (Improve developer productivity with GitHub Copilot)

Correct answer: A (is correct). Keeping `Suggestions matching public code = Block` -> inspecting the `CodeQL` Copilot Autofix diff & explanation -> validating parameter bindings & imports -> committing the fix, passing `CodeQL` + `pytest`, and getting human PR approval. [Skill 5.6: Suggest security improvements and performance optimizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/responsible-use-autofix-code-scanning)]

- **A:** Correct. Correct order: enforce public-code `Block` policy -> inspect CodeQL Copilot Autofix -> validate logic & dependencies -> pass CI + human PR approval.
- **B:** Incorrect. Incorrect: GitHub IP indemnity requires keeping the public-code duplication filter enabled (`Block`), and Autofix patches require testing and review.
- **C:** Incorrect. Incorrect: Content Exclusions do not block `CodeQL`, and secrets must never be pasted into PR comments.
- **D:** Incorrect. Incorrect: Copilot does not provide legal license sign-off, and dismissing real vulnerabilities leaves exploits open.

### Question 87 — `B` (Improve developer productivity with GitHub Copilot)

Correct answer: B (is correct). Convert `blacklisted_ids` from a `list` to a Python `set` (`frozenset`) once before the loop, reducing membership lookup from `O(M)` linear scan to **`O(1)` average hash lookup**. [Skill 5.6: Suggest security improvements and performance optimizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/responsible-use-autofix-code-scanning)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Correct. Security and performance optimization (`5.6`) pairs Copilot/Autofix patches with profiler benchmarks and SAST re-scans.
- **C:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 88 — `B` (Configure privacy, content exclusions, and safeguards)

Correct answer: B (is correct). Defining `/molecules/**` & `**/*.mol2` `fnmatch` globs in `Content exclusion`, allowing `<=30 min` (`or reloading VS Code`) for sync, confirming the crossed-out Copilot status icon + `copilot.content_exclusion_changed` audit log, and avoiding cross-file LSP leaks secures lead compounds. [Skill 6.1: Configure content exclusions and editor settings | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion)]

- **A:** Incorrect. Incorrect: Repository admins CANNOT override or remove Organization-level Content Exclusions (`rules combine additively`), and sync takes `<=30 minutes`.
- **B:** Correct. Correct order: configure YAML `fnmatch` globs -> allow `<=30 min` IDE sync -> verify crossed-out icon & audit log -> mind IDE LSP type-hover nuance.
- **C:** Incorrect. Incorrect: `.gitignore` does not exclude already-tracked repository files from Copilot context.
- **D:** Incorrect. Incorrect: Content Exclusions require **Copilot Business or Enterprise**, use `fnmatch` globs, and govern Copilot context—not Git ACLs or Actions.

### Question 89 — `B` (Configure privacy, content exclusions, and safeguards)

Correct answer: B (is correct). Using `"*":` (`wildcard repository key`, e.g., `"*": ["**/.env", "**/.env.*"]`) applies those Content Exclusion globs across **all repositories** in the organization. [Skill 6.1: Configure content exclusions and editor settings | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion)]

- **A:** Incorrect. Content Exclusions (`2.3`, `6.1`) are only enforced for seats governed under Copilot Business or Copilot Enterprise.
- **B:** Correct. Content Exclusion configuration (`6.1`) enforces additive Org + Repo `fnmatch` path exclusions across Business and Enterprise seats.
- **C:** Incorrect. False: Copilot Content Exclusions apply strictly to **GitHub Copilot** features—they never restrict Git repository ACLs, Actions workflows, or `CodeQL` (`6.1`).
- **D:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).

### Question 90 — `B` (Configure privacy, content exclusions, and safeguards)

Correct answer: B (is correct). No — GitHub Copilot Content Exclusions govern **GitHub Copilot clients/services**; preventing external paste/exfiltration requires workstation DLP, secret scanning, and least-privilege Git repository access. [Skill 6.1: Configure content exclusions and editor settings | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Correct. Content Exclusion scope limits (`2.3`, `6.1`) distinguish Copilot prompt blocking from IDE LSP type inference, Git ACLs, and CI scanners.
- **C:** Incorrect. False: Copilot Content Exclusions apply strictly to **GitHub Copilot** features—they never restrict Git repository ACLs, Actions workflows, or `CodeQL` (`6.1`).
- **D:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).

### Question 91 — `C` (Configure privacy, content exclusions, and safeguards)

Correct answer: C (is correct). No — Repository Content Exclusions are strictly **additive** and can **never** weaken or remove Organization-level Content Exclusions (`only an Organization Owner / Copilot manager can modify the org rule`). [Skill 6.1: Configure content exclusions and editor settings | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion)]

- **A:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **B:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **C:** Correct. Organization Content Exclusions (`6.1`, `6.4`) establish a floor that repository settings can only expand, never weaken.
- **D:** Incorrect. The proposed GitHub Copilot configuration or workflow violates at least one stated governance, privacy, or technical requirement. No — Repository Content Exclusions are strictly **additive** and can **never** weaken or remove Organization-level Content Exclusions (`only an Organization Owner / Copilot manager can modify the org rule`).

### Question 92 — `D` (Configure privacy, content exclusions, and safeguards)

Correct answer: D (is correct). GitHub claims **zero ownership** over customer-generated code (`ArdentBio retains full rights to its outputs`), and unmodified eligible suggestions under Copilot Business/Enterprise with `Block` enabled are covered by **IP Indemnity**. [Skill 6.2: Describe ownership and limitations of outputs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/about-github-copilot/plans-for-github-copilot)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **C:** Incorrect. Content Exclusions (`2.3`, `6.1`) are only enforced for seats governed under Copilot Business or Copilot Enterprise.
- **D:** Correct. Output ownership and IP Indemnity (`6.2`) require Business/Enterprise licensing with the public-code duplication filter enabled (`Block`).

### Question 93 — `D` (Configure privacy, content exclusions, and safeguards)

Correct answer: D (is correct). No — **GitHub Copilot IP Indemnity** applies strictly to **Copilot Business and Copilot Enterprise** subscriptions (`with Block enabled`), NOT to Individual Free, Pro, or Pro+ plans. [Skill 6.2: Describe ownership and limitations of outputs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/about-github-copilot/plans-for-github-copilot)]

- **A:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **B:** Incorrect. The proposed GitHub Copilot configuration or workflow violates at least one stated governance, privacy, or technical requirement. No — **GitHub Copilot IP Indemnity** applies strictly to **Copilot Business and Copilot Enterprise** subscriptions (`with Block enabled`), NOT to Individual Free, Pro, or Pro+ plans.
- **C:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **D:** Correct. Enabling `Block` on public-code duplication (`6.2`, `6.3`) is a mandatory condition for GitHub Copilot IP Indemnity protection.

### Question 94 — `D` (Configure privacy, content exclusions, and safeguards)

Correct answer: D (is correct). Because the duplication filter (`suppressing ~150+ char public matches`) is the technical preventive control minimizing verbatim public-code reproduction; disabling filtering voids indemnification eligibility. [Skill 6.2: Describe ownership and limitations of outputs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/about-github-copilot/plans-for-github-copilot)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **D:** Correct. Output ownership and IP Indemnity (`6.2`) require Business/Enterprise licensing with the public-code duplication filter enabled (`Block`).

### Question 95 — `D` (Configure privacy, content exclusions, and safeguards)

Correct answer: D (is correct). In the **GitHub Copilot Log (`Code References` / Output channel & inline notification link)** inside the IDE (`as well as Chat code-reference annotations`). [Skill 6.3: Enable suggestions matching public code filtering | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/finding-public-code-that-matches-github-copilot-suggestions)]

- **A:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **D:** Correct. Public-code duplication filtering and Code Referencing (`6.3`) either block `~150+` char verbatim public matches or surface repo/license provenance.

### Question 96 — `B` (Configure privacy, content exclusions, and safeguards)

Correct answer: B (is correct). Copyleft licenses like **`GPL-3.0-only`** impose reciprocal source-disclosure/relicensing obligations on derivative distributions (`which is why commercial enterprises enforce Block instead`). [Skill 6.3: Enable suggestions matching public code filtering | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/finding-public-code-that-matches-github-copilot-suggestions)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Correct. Public-code duplication filtering and Code Referencing (`6.3`) either block `~150+` char verbatim public matches or surface repo/license provenance.
- **C:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 97 — `B, C` (Configure privacy, content exclusions, and safeguards)

Correct answers: B and C (are correct). Enforcing **`Block`** suppresses `~150+` character matches against public GitHub code and preserves **IP Indemnity**, whereas **`Allow`** surfaces repo/license matches via **Code Referencing** without IP Indemnity. [Skill 6.3: Enable suggestions matching public code filtering | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/finding-public-code-that-matches-github-copilot-suggestions)]

- **A:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **B:** Correct. Public-code duplication filtering and Code Referencing (`6.3`) either block `~150+` char verbatim public matches or surface repo/license provenance.
- **C:** Correct. Output ownership and IP Indemnity (`6.2`) require Business/Enterprise licensing with the public-code duplication filter enabled (`Block`).
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **E:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).

### Question 98 — `B` (Configure privacy, content exclusions, and safeguards)

Correct answer: B (is correct). Content Exclusion propagation to active IDE clients takes **up to 30 minutes**; reload the IDE window / restart the Copilot extension (`and confirm the local repo's git remote -v matches the org repository`) to force immediate policy refresh. [Skill 6.4: Resolve issues with suggestions and content exclusions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot)]

- **A:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **B:** Correct. Troubleshooting Copilot (`6.4`) checks multi-org policy precedence (`most restrictive wins`), Content Exclusion icons, filetype settings, and proxy/TLS trust.
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).

### Question 99 — `A` (Configure privacy, content exclusions, and safeguards)

Correct answer: A (is correct). No — **Content Exclusions** are exclusively a **Copilot Business and Copilot Enterprise** governance feature (`not available on personal Free/Pro/Pro+ user accounts`). [Skill 6.4: Resolve issues with suggestions and content exclusions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot)]

- **A:** Correct. Content Exclusions (`2.3`, `6.1`) are only enforced for seats governed under Copilot Business or Copilot Enterprise.
- **B:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **C:** Incorrect. The proposed GitHub Copilot configuration or workflow violates at least one stated governance, privacy, or technical requirement. No — **Content Exclusions** are exclusively a **Copilot Business and Copilot Enterprise** governance feature (`not available on personal Free/Pro/Pro+ user accounts`).
- **D:** Incorrect. Individual Copilot tiers (`2.1`, `2.15`) serve single accounts without Organization policy management or Org Content Exclusions.

### Question 100 — `C, D` (Configure privacy, content exclusions, and safeguards)

Correct answers: C and D (are correct). When a user holds seats in multiple organizations, the **most restrictive** active policy (`Chat = Disabled`) applies across their IDE, and lab VLANs must allowlist `HTTPS 443` + trust SSL-inspection root CAs (`checked via Copilot Diagnostics`). [Skill 6.4: Resolve issues with suggestions and content exclusions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot)]

- **A:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **B:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **C:** Correct. Multi-organization policy resolution (`2.13`, `6.4`) always applies the strictest safeguard across a user's active memberships.
- **D:** Correct. Troubleshooting Copilot (`6.4`) checks multi-org policy precedence (`most restrictive wins`), Content Exclusion icons, filetype settings, and proxy/TLS trust.
- **E:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
