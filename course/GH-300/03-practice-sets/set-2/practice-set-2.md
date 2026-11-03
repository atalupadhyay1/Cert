# Microsoft / GitHub Exam GH-300: GitHub Copilot — Full-Length Mock Exam 2

**Theme:** GitHub Copilot CLI, Agent Mode, Sub-Agents, MCP Servers & Agent Sessions  
**Credential:** `GitHub Copilot` *(Intermediate · **no prerequisite** · **2-year validity** transitioning to Microsoft Learn recertification)*  
**Study guide baseline:** `August 7, 2026 (Last updated July 9, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-300 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Copilot documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Use GitHub Copilot responsibly (15–20% official weight · 18 questions)

### 1. An avionics telemetry engineer at StratosFlight uses GitHub Copilot to draft a C++20 Kalman filter matrix inversion and notices no compiler warnings. Why could the generated routine still fail catastrophically on edge flight-envelope inputs?

- **A.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Generative AI models predict statistically probable token sequences (`not proven correctness`), risking hallucinated APIs, outdated idioms, training-data bias, and subtle security bugs

### 2. In `stratosflight/rust-canbus`, Copilot suggests adding `serde-canbus-fast = "0.9"` to `Cargo.toml`. Before running `cargo build` on a developer laptop, what supply-chain check is mandatory?

- **A.** Inspect **Audit Logs** (`category:copilot`, e.g., `copilot.cfb_seat_created`, `copilot.content_exclusion_changed`) for admin changes and `GET /orgs/{org}/copilot/metrics` (`>=5 active users`) for aggregated usage
- **B.** Verify every AI-suggested package name, publisher, and version in your trusted registry (`preventing slopsquatting / hallucinated dependency attacks`) before installing
- **C.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **D.** Use **GitHub Spark** to build, iterate on, and share AI-powered full-stack micro-apps (`with natural-language prompts, live preview, managed KV persistence, and optional GitHub repository sync`)

### 3. StratosFlight's safety lead observes experienced engineers accepting 40-line AI-generated C++ pointer arithmetic blocks in under two seconds because previous suggestions worked well. How should the team counter this **automation complacency**?

- **A.** Install `@github/copilot` via `npm install -g @github/copilot` (`Node.js 22+`), `winget install GitHub.Copilot`, or Homebrew, launch `copilot` in your repo, run `/login`, and confirm folder trust
- **B.** Guard against **automation bias / complacency** (`over-trusting plausible-looking AI completions`) by reviewing edge cases, error paths, and security invariants manually
- **C.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 4. StratosFlight's DO-178C tool-qualification committee documents why GitHub Copilot is classified as an **untrusted developer productivity aid** whose outputs must pass full verification. Which two AI risks justify that classification? Select two.

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** Guard against **automation bias / complacency** (`over-trusting plausible-looking AI completions`) by reviewing edge cases, error paths, and security invariants manually
- **C.** Generative AI models predict statistically probable token sequences (`not proven correctness`), risking hallucinated APIs, outdated idioms, training-data bias, and subtle security bugs
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **E.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review

### 5. StratosFlight's flight-deck Ground Support web app uses Copilot to generate alert banners, and QA checks screen-reader `aria-live` support plus colorblind-safe contrast so color-vision-deficient technicians are not excluded. Complete the Responsible AI principle: `____`.

- **A.** Apply the six Responsible AI principles—**Fairness**, **Reliability & Safety**, **Privacy & Security**, **Inclusiveness**, **Transparency**, and **Accountability**
- **B.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **C.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **D.** Use `copilot -p "..."` for non-interactive runs (`-s` for clean stdout, `--output-format=json` for JSONL), `--available-tools` / `--deny-tool` for tool scoping, and `--fleet` for parallel subagents

### 6. When an engineer uses Copilot to draft an internal safety-review summary on a pull request in `stratosflight/autopilot-sim`, what ethical obligation applies before publishing the PR?

- **A.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **D.** Maintain **Transparency** and **Accountability** by disclosing AI assistance per team norms, honoring open-source licenses, and ensuring humans own every committed line

### 7. StratosFlight builds a speech-command parser test dataset for ground-crew headsets using Copilot. If all generated test transcripts reflect a single regional accent and idiom set, which Responsible AI principle is at risk?

- **A.** Evaluate AI-generated UI copy, validation rules, and domain models for **Fairness** and **Inclusiveness** (`avoiding demographic stereotyping, exclusionary naming, or accessibility regressions`)
- **B.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **C.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **D.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)

### 8. StratosFlight's VP of Engineering publishes a Responsible AI scorecard for internal tools built with GitHub Copilot. Which three checks belong on that scorecard? Select three.

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **D.** Evaluate AI-generated UI copy, validation rules, and domain models for **Fairness** and **Inclusiveness** (`avoiding demographic stereotyping, exclusionary naming, or accessibility regressions`)
- **E.** Apply the six Responsible AI principles—**Fairness**, **Reliability & Safety**, **Privacy & Security**, **Inclusiveness**, **Transparency**, and **Accountability**
- **F.** Require a human engineer to review, test, and approve every AI-assisted pull request—never delegating final merge accountability to an LLM

### 9. While scaffolding a C++20 UDP telemetry receiver, Copilot suggests `strcpy(buf, packet.payload)` without bounds checking. Why can LLMs suggest unsafe C functions, and which automated safeguard catches them on PRs?

- **A.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **B.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **C.** Mitigate AI harms (`historical dataset bias, weak crypto/SQL defaults, PII exposure, and insecure scaffolding`) using RAI filters, `CodeQL` SAST, secret scanning, and diverse test suites
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free

### 10. StratosFlight connects an external vendor telemetry log server to VS Code via MCP. An untrusted vendor log line contains prompt text instructing the agent to modify `.github/workflows/release.yml`. Why must MCP tool outputs from external data sources be treated cautiously?

- **A.** Treat untrusted external content (`issues, PR bodies, web pages, third-party MCP tool outputs`) as **indirect prompt injection** risks and require human approval on tool actions
- **B.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** `#runSubagent` merges every raw intermediate grep output directly into the main chat's token window and pauses mid-search to interview the user after every file read

### 11. StratosFlight's AppSec team catalogs AI-specific threat vectors for teams adopting Copilot Agent Mode and MCP servers. Which two risks and mitigations are accurate? Select two.

- **A.** Mitigate AI harms (`historical dataset bias, weak crypto/SQL defaults, PII exposure, and insecure scaffolding`) using RAI filters, `CodeQL` SAST, secret scanning, and diverse test suites
- **B.** Treat untrusted external content (`issues, PR bodies, web pages, third-party MCP tool outputs`) as **indirect prompt injection** risks and require human approval on tool actions
- **C.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **D.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **E.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions

### 12. An embedded Rust developer at StratosFlight uses Copilot to generate a CRC-32C frame verifier in `stratosflight/link-layer`. Order the mandatory validation workflow from initial prompt through merge.

- **A.** Merge Copilot output directly to `main` → Run `CodeQL` weekly in production → Check package names only if builds fail → Skip human review when Copilot Code Review leaves zero comments
- **B.** Approve an empty PR branch first → Disable `CodeQL` to speed up Copilot completions → Install unfamiliar suggested packages blindly from public registries → Deploy without unit tests
- **C.** Prompt Copilot with explicit security & type constraints → Review logic & verify suggested packages exist in trusted registries → Run unit/edge-case tests plus `CodeQL` & secret scanning → Complete human peer PR review before merging
- **D.** Set public-code filtering to `Allow` → Paste live customer PII into Chat as sample fixtures → Run unit tests locally → Self-approve your own pull request

### 13. Copilot generates a C++ mutex wrapper that looks clean at first glance, yet forgets to unlock an early-return error path when written manually without RAII `std::scoped_lock`. What lesson does this illustrate?

- **A.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **B.** Treat Copilot as a **pair-programming assistant (`not an oracle`)**: review diffs line-by-line, execute unit/integration/edge-case tests, and scan with `CodeQL` and Dependabot
- **C.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **D.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review

### 14. A StratosFlight test script calls Copilot CLI twice with the same prompt `"Write a Python script to parse ARINC-429 hex words"` and receives `struct.unpack` on run 1 and bitwise shifts on run 2. Why?

- **A.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** Because LLM sampling is **stochastic (`non-deterministic`)**, identical prompts can yield varying implementations whose runtime behavior, complexity, and thread safety must be verified
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free

### 15. StratosFlight's engineering manager wants an automated weekly script to identify specific individual usernames with `last_activity_at == null` over 60 days so unused seats can be reassigned. Proposed solution: Query `GET /orgs/stratosflight/copilot/metrics` (`instead of /copilot/billing/seats`) to extract each inactive developer's GitHub username. Does this meet the goal?

- **A.** Inspect **Audit Logs** (`category:copilot`, e.g., `copilot.cfb_seat_created`, `copilot.content_exclusion_changed`) for admin changes and `GET /orgs/{org}/copilot/metrics` (`>=5 active users`) for aggregated usage
- **B.** No — `GET /orgs/{org}/copilot/metrics` returns **aggregated, anonymized** team/org usage (`requiring >=5 active users`), NOT per-developer `last_activity_at` usernames; query `GET /orgs/{org}/copilot/billing/seats`
- **C.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **D.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements

### 16. StratosFlight handles export-controlled ITAR propulsion tables stored under `propulsion/itar-tables/**`. How should administrators and developers operate Copilot Business responsibly in that repository?

- **A.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **B.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **C.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **D.** Operate Copilot responsibly by keeping `Suggestions matching public code = Block`, configuring Content Exclusions, omitting PII/secrets from prompts, and enforcing human PR review

### 17. StratosFlight wants terminal-first Rust developers to use **GitHub Copilot CLI** safely on flight-simulator repositories without allowing silent destructive commands or secret leakage in logs. Proposed solution: Keep Copilot CLI in manual permission-approval mode (`/permissions manual`), pass `--secret-env-vars` for custom tokens (`in addition to auto-redacted GITHUB_TOKEN`), and review every proposed file diff before committing. Does this meet the goal?

- **A.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **B.** No — Copilot Chat **`Ask` mode** only answers questions and proposes snippets in chat; autonomous multi-file workspace edits with iterative terminal test execution require **Agent Mode** (`or Copilot CLI`)
- **C.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **D.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements

### 18. A developer debugging an authentication failure is tempted to paste a live `ghp_...` classic PAT and customer flight-recorder credentials into Copilot Chat to ask why a `curl` header failed. What should they do instead?

- **A.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **B.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **C.** Never paste live customer PII, PHI, production database dumps, or active credentials/private keys into Copilot prompts or sample fixtures
- **D.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models

---

## Domain 2 — Use GitHub Copilot features (25–30% official weight · 28 questions)

### 19. StratosFlight engineers use **CLion (`JetBrains`)**, **Visual Studio 2022**, **VS Code**, and **Neovim** across teams. Can one assigned **Copilot Business** seat be used by the same authenticated developer across multiple supported IDEs?

- **A.** Install the official GitHub Copilot extension in a supported IDE (`VS Code, Visual Studio, JetBrains, Xcode, Eclipse, or Neovim`), sign in via GitHub OAuth, and verify an active seat
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** Inspect **Audit Logs** (`category:copilot`, e.g., `copilot.cfb_seat_created`, `copilot.content_exclusion_changed`) for admin changes and `GET /orgs/{org}/copilot/metrics` (`>=5 active users`) for aggregated usage
- **D.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`

### 20. StratosFlight operates on a GitHub Team (`organization`) plan without GitHub Enterprise Cloud (`GHEC`), yet needs Organization-wide policy controls, Content Exclusions, zero model training, and IP Indemnity. Complete the Copilot plan name they can purchase directly on a GitHub Organization: `Copilot ____`.

- **A.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **B.** Choose **Copilot Free** for capped monthly completions/chats or **Copilot Pro / Pro+** for individual developers needing unlimited completions, higher premium-model quotas, and **GitHub Spark**
- **C.** Choose **Copilot Business** (`Org policies, Content Exclusions, IP Indemnity, zero model training`) or **Copilot Enterprise** (`adds GHEC Copilot Spaces/Knowledge Bases & org-wide GitHub.com grounding`)
- **D.** No — Repository and Organization **Content Exclusions** require **Copilot Business or Copilot Enterprise**; personal Copilot Free/Pro/Pro+ plans do not support Org Content Exclusions

### 21. Inside VS Code, a StratosFlight developer wants to press a single shortcut right inside `kalman.cpp` to rewrite a selected 12-line loop into `std::ranges` with an inline side-by-side diff (`without switching focus to the Chat sidebar`). Complete the Windows/Linux shortcut: `Ctrl+____` (`Cmd+I` on macOS).

- **A.** No — Copilot Chat **`Ask` mode** only answers questions and proposes snippets in chat; autonomous multi-file workspace edits with iterative terminal test execution require **Agent Mode** (`or Copilot CLI`)
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** Match interaction surfaces to scope: **Inline Chat (`Ctrl+I` / `Cmd+I`)** for in-place file edits, **Chat `Ask`** for Q&A, **Copilot Edits** for multi-file working sets, and **Agent Mode / CLI** for autonomous loops
- **D.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke

### 22. A StratosFlight C++ developer wants to cycle through alternative inline ghost-text completions in VS Code and also apply coordinated multi-file edits across a defined 4-file working set (`header + impl + CMakeLists.txt + test`). Which two Copilot features fit? Select two.

- **A.** Match interaction surfaces to scope: **Inline Chat (`Ctrl+I` / `Cmd+I`)** for in-place file edits, **Chat `Ask`** for Q&A, **Copilot Edits** for multi-file working sets, and **Agent Mode / CLI** for autonomous loops
- **B.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **E.** Use **Inline ghost-text completions** (`Tab` to accept, `Alt+]` / `Option+]` to cycle) and **Next Edit Suggestions (`NES`)** to predict subsequent ripple edits across nearby lines

### 23. In `stratosflight/radar-dsp`, a repository administrator adds `- "**/*.key"` and `- "/calibration/classified/**"` under `Settings -> Copilot -> Content exclusion`. Which Copilot surfaces honor those exclusions once synced?

- **A.** Configuring Copilot Content Exclusions also blocks `git clone`, GitHub Actions runners, and `CodeQL` security scans from reading the excluded files
- **B.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **C.** Configure Repository or Organization **Content Exclusions** (`Settings -> Copilot -> Content exclusion`) so IDEs omit matched sensitive files across completions, Chat, and code review
- **D.** No — `.gitignore` only prevents untracked files from being staged by Git; excluding tracked repository files from Copilot requires **Copilot Content Exclusions** (`Settings -> Copilot -> Content exclusion`)

### 24. StratosFlight excludes `/include/CryptoTypes.hpp` via Copilot Content Exclusions, while `TelemetrySender.cpp` (`not excluded`) includes `CryptoTypes.hpp` and calls `signPacket(...)`. Proposed solution: Keep both files in the same C++ compilation target while assuming VS Code's `clangd` C++ language server will NEVER expose `signPacket`'s parameter types to Copilot inside `TelemetrySender.cpp`. Does this meet the goal?

- **A.** Configuring Copilot Content Exclusions also blocks `git clone`, GitHub Actions runners, and `CodeQL` security scans from reading the excluded files
- **B.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **C.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements
- **D.** No — while Content Exclusions block direct file reads, IDE **language-server (`LSP`) type/signature hover metadata** from symbols imported out of an excluded file can still surface in non-excluded open files

### 25. How does the modern **GitHub Copilot CLI (`copilot`)** benefit embedded Linux engineers at StratosFlight who debug `cmake`, `gdb`, and `journalctl` pipelines over headless SSH sessions?

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** GitHub Copilot CLI (`copilot`) is a terminal-native AI coding agent that understands shell context, edits files, executes commands with approval prompts, and automates multi-step repo workflows
- **C.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **D.** Inspect **Audit Logs** (`category:copilot`, e.g., `copilot.cfb_seat_created`, `copilot.content_exclusion_changed`) for admin changes and `GET /orgs/{org}/copilot/metrics` (`>=5 active users`) for aggregated usage

### 26. A Windows flight-sim developer at StratosFlight installs **GitHub Copilot CLI** (`via WinGet or npm on Node 22+`) and starts using it in `C:\src\flight-sim`. Order the installation, launch, `/login`, and trust/permission steps.

- **A.** Run `/login` in raw Bash before installing `@github/copilot` → Pass `--allow-all` on `/` root filesystem → Write plaintext passwords into `~/.copilot/config.json` → Downgrade to Node.js `14`
- **B.** Clone the repo inside `~/.copilot/logs/` → Set `Suggestions matching public code` to `Allow` → Run `gh auth logout` → Expect silent file edits without permission prompts
- **C.** Install Node.js `22+` (or WinGet/Homebrew) & `npm install -g @github/copilot` → `cd` into the project directory & launch `copilot` → Enter `/login` to complete GitHub OAuth authentication → Confirm directory trust & verify `/permissions show`
- **D.** Install `@github/copilot` → Delete `~/.copilot/session-store.db` before signing in → Disable the Organization Copilot CLI policy → Run `copilot -p` unauthenticated

### 27. A developer in organization `stratosflight` installs `@github/copilot`, runs `/login` successfully with their corporate account, yet sees an organization policy block error. Which Organization setting must an admin enable?

- **A.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **B.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **C.** Install `@github/copilot` via `npm install -g @github/copilot` (`Node.js 22+`), `winget install GitHub.Copilot`, or Homebrew, launch `copilot` in your repo, run `/login`, and confirm folder trust
- **D.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke

### 28. A StratosFlight developer wants Copilot CLI to parallelize a large multi-crate Rust migration across concurrent subagents (`either via CLI flag or interactive slash command`). Complete the flag/command name: `copilot --____ -p "..."` (`or /fleet`).

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** `#runSubagent` merges every raw intermediate grep output directly into the main chat's token window and pauses mid-search to interview the user after every file read
- **C.** Use `copilot -p "..."` for non-interactive runs (`-s` for clean stdout, `--output-format=json` for JSONL), `--available-tools` / `--deny-tool` for tool scoping, and `--fleet` for parallel subagents
- **D.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`

### 29. StratosFlight automates nightly documentation lint checks with `copilot -p` and wants `(1)` machine-parseable JSON Lines (`JSONL`) output for downstream Python scripts and `(2)` a pinned model (`--model`) plus user-editable CLI settings in the right `~/.copilot/` file. Which two facts are accurate? Select two.

- **A.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **B.** Inside interactive Copilot CLI, use `/permissions show` or `/permissions manual` to inspect/set approval mode, `--model` to pin a model, and `~/.copilot/settings.json` for user preferences
- **C.** Use `copilot -p "..."` for non-interactive runs (`-s` for clean stdout, `--output-format=json` for JSONL), `--available-tools` / `--deny-tool` for tool scoping, and `--fleet` for parallel subagents
- **D.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **E.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke

### 30. A StratosFlight engineer accidentally closes their SSH terminal mid-way through an interactive `copilot` CLI debugging session and reconnects 10 minutes later. Which CLI flags reopen that exact prior session? (`copilot --____` or `--continue`)

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **C.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **D.** Use Copilot CLI **infinite sessions** (auto-compaction under `~/.copilot/session-state/{id}/`), inspect `/session plan`, `/session checkpoints`, and `/session files`, and resume via `--resume` or `--continue`

### 31. Inside an interactive `copilot` CLI session, `~/.copilot/session-store.db` (`the SQLite cross-session checkpoint index`) was accidentally deleted during disk cleanup. Complete the slash command that rebuilds the index and syncs session history: `/____ reindex`.

- **A.** Use Copilot CLI **infinite sessions** (auto-compaction under `~/.copilot/session-state/{id}/`), inspect `/session plan`, `/session checkpoints`, and `/session files`, and resume via `--resume` or `--continue`
- **B.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **C.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **D.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)

### 32. In non-interactive CI helper scripts (`copilot -p "..."`), StratosFlight wants to trust the current repository's `.vscode/mcp.json` and hooks **only for that single invocation** without saving the directory permanently to `trustedFolders` or granting `--allow-all`. Complete the flag: `--____-folder`.

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **C.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **D.** Generate scripts and edit files safely in Copilot CLI via interactive **permission prompts** (`write`, `commands`), `--add-dir` for extra paths, `--secret-env-vars` redaction, and `--share` / `--share-gist`

### 33. In `~/.copilot/permissions-config.json`, StratosFlight's developer workstation template pre-approves one specific read-only MCP tool `telemetry_query` on MCP server `flight-db` (`without approving destructive tools`). Which `"kind"` entry governs MCP tool approvals? (`"kind": "____"`)

- **A.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **B.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Generate scripts and edit files safely in Copilot CLI via interactive **permission prompts** (`write`, `commands`), `--add-dir` for extra paths, `--secret-env-vars` redaction, and `--share` / `--share-gist`

### 34. A StratosFlight systems engineer wires a CAN-bus DBC schema **MCP** server into VS Code **Agent Mode** and delegates 50-file message-ID lookup to **`#runSubagent`** before generating Rust decoders. Order the workflow.

- **A.** Define MCP servers inside `.git/HEAD` → Run `/clear` after every single edit so Agent Mode loses its plan → Skip working-set diff inspection → Force-push to `main`
- **B.** Accept (`Keep`) all generated edits before running tests → Add `.vscode/mcp.json` after closing VS Code → Attach 80 unrelated files to main chat → Switch to `Ask` mode expecting autonomous test loops
- **C.** Commit plaintext MCP API keys to `.github/copilot-instructions.md` → Expect `#runSubagent` to pause mid-run for interactive Q&A → Disable all workspace tools → Auto-push unreviewed edits to `main`
- **D.** Register the MCP server in `.vscode/mcp.json` & verify tools → Delegate broad codebase search to isolated `#runSubagent` → Apply multi-file edits & run terminal tests in Agent Mode → Inspect working-set diffs & `Keep` verified changes

### 35. While working in VS Code, a StratosFlight lead has two local Agent Mode refactors, one background Copilot CLI task, and two cloud **Copilot coding agent** PR sessions running concurrently. Which VS Code sidebar view lets them monitor status and steer any of those agents mid-run in a chat editor? (`____ ____`)

- **A.** Monitor local IDE, CLI, and cloud coding agents from the unified **Agent Sessions** view (`steering mid-run via chat editors`) and delegate noisy codebase research to **`#runSubagent`** for isolated context
- **B.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **C.** `#runSubagent` merges every raw intermediate grep output directly into the main chat's token window and pauses mid-search to interview the user after every file read
- **D.** No — Copilot Chat **`Ask` mode** only answers questions and proposes snippets in chat; autonomous multi-file workspace edits with iterative terminal test execution require **Agent Mode** (`or Copilot CLI`)

### 36. StratosFlight compares three agentic capabilities: `(A)` VS Code `#runSubagent`, `(B)` `.vscode/mcp.json` MCP servers in Agent Mode, and `(C)` GitHub.com **Copilot coding agent**. Which three statements are true? Select three.

- **A.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **B.** Assign a GitHub Issue or PR comment (`@copilot`) to the **Copilot coding agent (`cloud agent`)**, which runs in an ephemeral Actions sandbox, pushes to `copilot/*`, and opens a draft PR for human review
- **C.** Use **Agent Mode** with `.vscode/mcp.json` **Model Context Protocol (`MCP`)** servers to query external tools, edit multiple files, read compiler/terminal diagnostics, and self-heal until tests pass
- **D.** No — Copilot Chat **`Ask` mode** only answers questions and proposes snippets in chat; autonomous multi-file workspace edits with iterative terminal test execution require **Agent Mode** (`or Copilot CLI`)
- **E.** Invoke `#runSubagent` in VS Code Agent Mode so multi-file exploration runs in an isolated context window and returns only a concise summary to main chat
- **F.** `#runSubagent` merges every raw intermediate grep output directly into the main chat's token window and pauses mid-search to interview the user after every file read

### 37. When **Copilot Code Review** spots an off-by-one array index on a GitHub.com pull request in `stratosflight/fms-core`, how does it present an actionable fix that the PR author can apply with one button?

- **A.** Run **Copilot Code Review** locally on uncommitted IDE diffs or on GitHub.com PRs (`with Automatic Copilot code review, Review new pushes, and Review draft pull requests`), paired with human approval
- **B.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **C.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **D.** No — **Copilot Code Review** posts `Comment` reviews (`never Approve` reviews that satisfy required human branch-protection approver counts); a human reviewer must still approve

### 38. StratosFlight wants **Copilot Code Review** (`and NOT just the cloud coding agent`) on GitHub.com to enforce MISRA-C++ pointer rules defined in `.github/instructions/misra.instructions.md`. Proposed solution: Add YAML frontmatter `applyTo: "**/*.cpp"` AND `excludeAgent: "code-review"` to `misra.instructions.md`. Does this meet the goal?

- **A.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements
- **B.** No — setting `excludeAgent: "code-review"` in `.instructions.md` frontmatter explicitly **prevents** Copilot Code Review from using that file (`use applyTo: without excluding code-review`)
- **C.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **D.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files

### 39. StratosFlight maintains cross-agent repository build/test instructions in a vendor-neutral root file (`supported by GitHub Copilot CLI, coding agent, and VS Code alongside .github/copilot-instructions.md`). Complete that standard filename: `____.md`.

- **A.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **B.** Generate **Copilot Pull Request Summaries** on GitHub.com and enforce coding/review standards via `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` (`applyTo:`, `excludeAgent:`), and `AGENTS.md`
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke

### 40. When files inside a repository linked to a **Copilot Space** are updated on `main` in `stratosflight/avionics-icd`, must maintainers manually re-upload snapshots to keep the Space current?

- **A.** Use **GitHub Spark** to build, iterate on, and share AI-powered full-stack micro-apps (`with natural-language prompts, live preview, managed KV persistence, and optional GitHub repository sync`)
- **B.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **C.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **D.** Curate **Copilot Spaces** on GitHub.com (`grouping specific repositories, files, PRs, issues, free-text notes, and custom instructions`) to ground team Q&A and IDE MCP queries on authoritative org context

### 41. StratosFlight wants `(1)` GitHub.com pull-request authors to generate concise file-walkthrough descriptions automatically when opening PRs and `(2)` Rust `unsafe` block rules applied ONLY when Copilot edits or reviews `crates/hal/**/*.rs`. Which two features achieve this? Select two.

- **A.** Generate **Copilot Pull Request Summaries** on GitHub.com and enforce coding/review standards via `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` (`applyTo:`, `excludeAgent:`), and `AGENTS.md`
- **B.** No — setting `excludeAgent: "code-review"` in `.instructions.md` frontmatter explicitly **prevents** Copilot Code Review from using that file (`use applyTo: without excluding code-review`)
- **C.** Create modular `.github/instructions/*.instructions.md` files with YAML frontmatter `applyTo:` globs (`and optional excludeAgent: "code-review" | "cloud-agent"`) for path-specific standards
- **D.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **E.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke

### 42. A StratosFlight engineer wants to ask Copilot Chat inside VS Code how to configure VS Code's own `tasks.json` problem matcher and keyboard shortcuts (`rather than querying repository source code`). Complete the Chat participant: `@____`.

- **A.** Scope Copilot Chat with participants (`@workspace`, `@github`, `@vscode`, `@terminal`), slash commands (`/explain`, `/fix`, `/tests`, `/doc`, `/new`, `/clear`), `#file:`/`#codebase` variables, and thumbs feedback
- **B.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **C.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 43. StratosFlight standardizes an incident postmortem helper `.github/prompts/triage-crash.prompt.md` and trains developers on Copilot Chat feedback loops. Which two statements accurately describe `.prompt.md` files and Chat feedback? Select two.

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **C.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **D.** Enable `"chat.promptFiles": true` and commit reusable `.github/prompts/*.prompt.md` files (`YAML frontmatter: description, agent, model, tools` + Markdown `#file:` links) invoked via `/prompt-name`
- **E.** Scope Copilot Chat with participants (`@workspace`, `@github`, `@vscode`, `@terminal`), slash commands (`/explain`, `/fix`, `/tests`, `/doc`, `/new`, `/clear`), `#file:`/`#codebase` variables, and thumbs feedback

### 44. In Organization `stratosflight`, an admin configures an Organization Branch Ruleset targeting `*` repositories (`excluding sandbox-*`) with **`Automatically request Copilot code review`**. What extra organization setting stops external contributors from burning their own personal Copilot licenses to run unauthorized Copilot reviews on `stratosflight` repos?

- **A.** No — Repository and Organization **Content Exclusions** require **Copilot Business or Copilot Enterprise**; personal Copilot Free/Pro/Pro+ plans do not support Org Content Exclusions
- **B.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **C.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **D.** Enforce Enterprise/Org Copilot policies (`Enabled`, `Disabled`, `No policy`), Branch Ruleset automatic Copilot Code Review (`authorized users only`), and Enterprise `AI controls -> Agents` repo-wide blocks

### 45. A smaller 3-person R&D org `stratosflight-proto` calls `GET /orgs/stratosflight-proto/copilot/metrics` and sees empty breakdown metrics for yesterday even though 3 engineers used Copilot. What built-in privacy threshold caused this? (`at least ____ active users`)

- **A.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **B.** No — `GET /orgs/{org}/copilot/metrics` returns **aggregated, anonymized** team/org usage (`requiring >=5 active users`), NOT per-developer `last_activity_at` usernames; query `GET /orgs/{org}/copilot/billing/seats`
- **C.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **D.** Inspect **Audit Logs** (`category:copilot`, e.g., `copilot.cfb_seat_created`, `copilot.content_exclusion_changed`) for admin changes and `GET /orgs/{org}/copilot/metrics` (`>=5 active users`) for aggregated usage

### 46. StratosFlight's IAM service automates **Copilot Business** seat provisioning for Entra-synced GitHub teams and reclaims seats idle for `>45 days` via the GitHub REST API. Place the API workflow steps in order.

- **A.** Promote all developers to Organization Owner → Have engineers buy personal Copilot Pro plans → Configure Org Content Exclusions expecting personal Pro plans to inherit them → Skip seat audits
- **B.** Query `GET /orgs/{org}/copilot/metrics` expecting per-user login names → Send unauthenticated `PUT /users/{u}/copilot` calls → Delete the GitHub Organization to free 3 seats → Re-invite members manually
- **C.** Authorize `manage_billing:copilot` & enable selected access → `POST /orgs/{org}/copilot/billing/selected_teams` to grant seats → `GET /orgs/{org}/copilot/billing/seats` for `last_activity_at` → `DELETE .../selected_users` to reclaim idle seats
- **D.** Mint a `repo`-only PAT lacking `manage_billing:copilot` → POST CSV files to `/repos/{owner}/{repo}/issues` → Expect seats to provision automatically → Disable SAML SSO

---

## Domain 3 — Understand GitHub Copilot data and architecture (10–15% official weight · 14 questions)

### 47. How does GitHub Copilot protect prompts and code suggestions **in transit** between a StratosFlight developer's IDE (`or Copilot CLI`) and the GitHub Copilot cloud proxy (`minimum protocol `TLS ____+``)?

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** On **Copilot Business & Enterprise**, prompts and completions travel over `TLS 1.2+`, process ephemerally in memory for inline completions, and are **never retained to train foundational models**
- **C.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 48. Contrast **inline editor completions** (`processed ____ in memory`) with **GitHub.com Copilot Chat threads** under Copilot Enterprise regarding persistence: why can a developer reopen yesterday's GitHub.com Chat thread even though neither surface trains foundational models?

- **A.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **B.** On **Copilot Business & Enterprise**, prompts and completions travel over `TLS 1.2+`, process ephemerally in memory for inline completions, and are **never retained to train foundational models**
- **C.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **D.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models

### 49. When a StratosFlight developer presses `____` to accept a 6-line Rust completion on **Copilot Business**, what is recorded for organization analytics (`Metrics API`) versus discarded?

- **A.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **B.** Distinguish **user engagement telemetry** (`acceptance/dismissal counts, latency, IDE version, encrypted at rest`) from **source-code prompts/suggestions** (`discarded after inline inference on Business/Enterprise`)
- **C.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 50. When assembling an inline completion prompt in CLion for `AltitudeController.cpp`, which neighbor files does the Copilot extension prioritize scanning for matching function/struct context?

- **A.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **B.** The IDE extension constructs prompts from **Fill-in-the-Middle (`FIM`)** cursor prefix + suffix, language/filepath metadata, Jacobi/Jaccard-ranked snippets from open tabs, and custom instructions
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free

### 51. Do `.github/copilot-instructions.md` and `.instructions.md` files primarily steer **Copilot Chat, Agent Mode, and Copilot Code Review**, or do `.prompt.md` files automatically run on every raw single-keystroke ghost-text completion?

- **A.** The IDE extension constructs prompts from **Fill-in-the-Middle (`FIM`)** cursor prefix + suffix, language/filepath metadata, Jacobi/Jaccard-ranked snippets from open tabs, and custom instructions
- **B.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **C.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 52. StratosFlight's internal Copilot guide explains what signals the IDE extension packages into an inline completion request. Which two inputs are included (`assuming no Content Exclusion applies`)? Select two.

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** The IDE extension constructs prompts from **Fill-in-the-Middle (`FIM`)** cursor prefix + suffix, language/filepath metadata, Jacobi/Jaccard-ranked snippets from open tabs, and custom instructions
- **C.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **D.** Configuring Copilot Content Exclusions also blocks `git clone`, GitHub Actions runners, and `CodeQL` security scans from reading the excluded files
- **E.** Include both code **before** the cursor (`prefix`) and code **after** the cursor (`suffix`) via Fill-in-the-Middle (`FIM`) alongside matching open-tab symbols

### 53. Before a prompt ever reaches the LLM (`inbound`) and again before tokens return to the IDE (`outbound`), what class of classifiers runs in the GitHub Copilot proxy to block hate speech, self-harm, violence, sexual content, and jailbreak attempts?

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** The Copilot **cloud proxy** validates entitlement tokens, applies inbound/outbound **RAI safety filters** (`hate speech, violence, sexual content, PII, prompt injection`), and runs the `~150-char` public-code filter
- **C.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free

### 54. During post-processing in the Copilot proxy, why does the completion engine stop generating tokens at syntactic boundaries (`such as a closing } brace or newline stop sequence`) on single-line/block completions?

- **A.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **B.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **C.** The Copilot **cloud proxy** validates entitlement tokens, applies inbound/outbound **RAI safety filters** (`hate speech, violence, sexual content, PII, prompt injection`), and runs the `~150-char` public-code filter
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 55. A StratosFlight security review asks why a developer occasionally sees zero ghost text when typing a verbatim header from a famous GPLv3 public C library (`with Public code = Block`) or an adversarial jailbreak prompt. Which two proxy mechanisms suppressed those responses? Select two.

- **A.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **B.** Pass generated tokens through cloud-proxy Responsible AI toxicity/harm classifiers and the `~150-character` public-code duplication filter before IDE rendering
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **E.** The Copilot **cloud proxy** validates entitlement tokens, applies inbound/outbound **RAI safety filters** (`hate speech, violence, sexual content, PII, prompt injection`), and runs the `~150-char` public-code filter

### 56. Order the four stages of GitHub Copilot's **code suggestion lifecycle** for an embedded C++ engineer working in VS Code under StratosFlight's Copilot Business plan.

- **A.** Public-code duplication filter runs offline with network unplugged → LLM generates code before receiving file language or cursor prefix → IDE validates seat tokens once per decade → Proxy disables TLS encryption
- **B.** IDE gathers FIM prefix/suffix & open tabs (minus exclusions) → Client sends `TLS 1.2+` prompt to proxy & checks seat token → Proxy runs RAI filters, LLM & `~150+` char duplication check → IDE renders ghost text & Business skips model training
- **C.** IDE bypasses Organization Content Exclusions → Forwards raw files to unauthenticated endpoints → Skips toxicity & prompt-injection filters → Publishes prompts to public GitHub Gists
- **D.** IDE uploads your entire disk (`~/.ssh` & closed repos) over HTTP → Cloud GPUs execute your local unit tests → Copilot commits directly to `main` without ghost text → Copilot Business trains shared base LLMs on your prompt

### 57. If a developer types rapidly while a previous ghost-text HTTP request is still in flight (`before tokens render`) and changes the current line completely, what does the Copilot IDE extension do with the stale in-flight request?

- **A.** Suggestion lifecycle: typing debounce -> IDE FIM/tab context assembly -> `TLS` request to Copilot proxy -> RAI pre-filter & LLM generation -> post-filter & duplication check -> ghost-text render -> telemetry
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **D.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review

### 58. A StratosFlight developer asks Copilot Chat (`with no MCP server or attachments`) `"What is the current CPU load on staging pod telemetry-7b9d?"` Why can Copilot not answer accurately?

- **A.** Account for LLM & Copilot architectural limits: **finite context windows**, **pre-training knowledge cutoffs**, **stochastic sampling**, **no runtime execution** during inline completion, and unseen unindexed external systems
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)

### 59. When refactoring intricate bit-field endianness shifts (`big-endian network order to little-endian ARM`) in C++20, why do LLMs occasionally invert bit masks despite confident comments?

- **A.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **B.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **C.** Account for LLM & Copilot architectural limits: **finite context windows**, **pre-training knowledge cutoffs**, **stochastic sampling**, **no runtime execution** during inline completion, and unseen unindexed external systems
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free

### 60. Why can `@workspace` occasionally miss a dynamically constructed symbol call (`e.g., getattr(handler, "on_" + msg_type)`) compared to a static IDE language-server call hierarchy?

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** For `@workspace` and GitHub.com repository chat, Copilot uses **lexical and semantic (`embedding`) retrieval (`RAG`)** to inject top-ranked code chunks into the prompt rather than sending entire gigabyte repos
- **C.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **D.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically

---

## Domain 4 — Apply prompt engineering and context crafting (10–15% official weight · 13 questions)

### 61. A StratosFlight Rust engineer prompts Copilot Chat: `"Using #file:frame.rs (no_std, zero heap alloc), implement TryFrom<&[u8]> for TelemetryFrame returning Result<Self, FrameError::ShortBuffer | BadCrc>."` Which prompt element prevents Copilot from emitting `Vec<u8>` or `unwrap()` panics?

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **C.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **D.** Structure effective prompts with **Role/Goal**, **Grounded Context** (`#file`, `#selection`, versions), **Explicit Constraints** (`security, error handling, edge cases`), and **Output Format** (`types, signatures`)

### 62. In `attitude_ekf.hpp`, a developer writes `[[nodiscard]] std::expected<Quaterniond, EkfError> fuseImuSample(const ImuReading& r, std::chrono::nanoseconds dt) noexcept;` before pressing `Enter` to generate the body. Why does this signature dramatically improve the completion?

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** Inspect **Audit Logs** (`category:copilot`, e.g., `copilot.cfb_seat_created`, `copilot.content_exclusion_changed`) for admin changes and `GET /orgs/{org}/copilot/metrics` (`>=5 active users`) for aggregated usage
- **C.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **D.** Guide inline completions directly inside source files using **top-of-file architecture comments**, **explicit parameter/return type annotations**, and **domain-specific function/variable names**

### 63. In VS Code Copilot Chat, a developer wants to ask how function `computeMachNumber` is defined and referenced without manually locating its file first. Complete the `#` variable that attaches a specific workspace code symbol: `#____:computeMachNumber`.

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** Curate Copilot's active context: open target interface/DTO tabs (`closing unrelated files`), attach `#file:`, `#selection`, `#sym:`, or **Copilot Spaces**, and scope `.instructions.md` with `applyTo:` globs
- **C.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **D.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically

### 64. After submitting a prompt in VS Code Copilot Chat, how can a StratosFlight engineer verify whether `.github/copilot-instructions.md` and `crates/hal.instructions.md` were actually included in the prompt context?

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **C.** Curate Copilot's active context: open target interface/DTO tabs (`closing unrelated files`), attach `#file:`, `#selection`, `#sym:`, or **Copilot Spaces**, and scope `.instructions.md` with `applyTo:` globs
- **D.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke

### 65. A StratosFlight developer notices `.github/instructions/embedded-c.instructions.md` was NOT listed under `References` when editing `firmware/nav/imu.c`. Which two checks explain and fix context determination here? Select two.

- **A.** Close unrelated editor tabs and open the exact target interfaces/DTOs (`or pin them via #file:`) so neighbor-tab ranking injects clean, relevant types
- **B.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **C.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **D.** Curate Copilot's active context: open target interface/DTO tabs (`closing unrelated files`), attach `#file:`, `#selection`, `#sym:`, or **Copilot Spaces**, and scope `.instructions.md` with `applyTo:` globs
- **E.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically

### 66. StratosFlight converts binary ICD tables into custom C++ `STATIC_ICD_FIELD(name, start_bit, bit_len, scale)` macros. Providing `2` completed macro rows in the prompt before asking Copilot to convert 12 more rows is an example of `____-shot prompting`.

- **A.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **B.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **C.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **D.** Use **zero-shot prompting** for standard algorithms/APIs, and **few-shot prompting** (`1–3 concrete input -> output examples`) when teaching proprietary schemas, custom DSLs, or bespoke test conventions

### 67. When is **few-shot prompting** counterproductive compared to **zero-shot prompting** in Copilot Chat?

- **A.** Use **zero-shot prompting** for standard algorithms/APIs, and **few-shot prompting** (`1–3 concrete input -> output examples`) when teaching proprietary schemas, custom DSLs, or bespoke test conventions
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **D.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically

### 68. A developer asks Copilot to generate a C++20 ring buffer, runs `ctest`, and gets a thread-sanitizer (`TSan`) race warning on `head_`. What is the most effective iterative follow-up prompt?

- **A.** Decompose complex epics into small, testable steps, state exact framework/SDK versions (`preventing pre-cutoff API drift`), and iterate in follow-up turns using compiler or test output
- **B.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **C.** No — keeping dozens of unrelated tabs open and reusing one marathon chat thread across unrelated tasks causes **context pollution and token truncation**; close stale tabs and use `/clear` or `#runSubagent`
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free

### 69. Why does naming a helper `parseArinc429LabelOctal(uint32_t word)` instead of `proc(uint32_t x)` produce markedly higher-accuracy inline completions?

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **C.** Decompose complex epics into small, testable steps, state exact framework/SDK versions (`preventing pre-cutoff API drift`), and iterate in follow-up turns using compiler or test output
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 70. StratosFlight's avionics team creates a reusable `.github/prompts/icd-decoder.prompt.md` slash template in VS Code so every engineer scaffolds Rust packet decoders consistently. Order the steps.

- **A.** Set `"chat.promptFiles": true` & add `.github/prompts/api.prompt.md` → Link exemplars (`#file:`) & commit to Git → Close unrelated tabs & invoke `/api` in Chat with inputs → Run `/clear` (or open a new chat) before switching topics
- **B.** Save `prompt.txt` outside the workspace → Add `applyTo: "false"` so nothing matches → Type `@terminal` expecting inline ghost text in closed files → Commit unreviewed output
- **C.** Embed production PATs inside `.github/prompts/deploy.prompt.md` → Publish private prompts to public npm → Send one-word `'fix'` with zero file context → Skip code review
- **D.** Place prompt templates in `.github/workflows/prompt.yml` expecting `/prompt` in Chat → Keep 45 unrelated legacy files open in tabs → Reuse one 200-turn chat thread across 12 services → Omit output types and error rules

### 71. Instead of pasting the same 18 lines of `"Use Rust 2024 edition, thiserror v2, and cargo clippy -D warnings"` into every single Chat prompt, where should StratosFlight codify repository-wide always-on coding standards? (`.github/____-instructions.md`)

- **A.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **B.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **C.** Write **positive, specific constraints** (`'use parameterized pg queries with $1 parameters'`) rather than vague negations, ground domain rules via `#file:`, and codify standards in `.prompt.md` / `.instructions.md`
- **D.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically

### 72. Why does delegating `"Find all 28 callers of LegacyBus::send() across the monorepo and summarize their error types"` to **`#runSubagent`** outperform running those 28 file reads directly inside the main Agent Mode chat thread?

- **A.** Copilot Chat appends prior turns from the active thread up to its **token context limit**; run `/clear` (or open a new chat) on topic switches and use `#runSubagent` to keep noisy exploration out of history
- **B.** `#runSubagent` merges every raw intermediate grep output directly into the main chat's token window and pauses mid-search to interview the user after every file read
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically

### 73. A StratosFlight engineer notices Agent Mode slowing down and confusing struct names after 60 turns across three different crates. Which two actions restore sharp prompt performance? Select two.

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** Run `/clear` or start a new Chat session when pivoting to an unrelated module so stale conversation turns do not consume token budget or bias new answers
- **C.** No — keeping dozens of unrelated tabs open and reusing one marathon chat thread across unrelated tasks causes **context pollution and token truncation**; close stale tabs and use `/clear` or `#runSubagent`
- **D.** `#runSubagent` merges every raw intermediate grep output directly into the main chat's token window and pauses mid-search to interview the user after every file read
- **E.** Copilot Chat appends prior turns from the active thread up to its **token context limit**; run `/clear` (or open a new chat) on topic switches and use `#runSubagent` to keep noisy exploration out of history

---

## Domain 5 — Improve developer productivity with GitHub Copilot (10–15% official weight · 14 questions)

### 74. A StratosFlight team maintains 35 repetitive C++ telemetry structs that each need `fmt::formatter` specializations and JSON serializers. Which Copilot workflow eliminates manual boilerplate fastest across all 8 header files?

- **A.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **B.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **C.** Use `Inline Chat`, `Copilot Edits`, **Next Edit Suggestions**, and `/doc` to scaffold repetitive DTOs/validators, extract pure functions to reduce cyclomatic complexity, and generate JSDoc/OpenAPI/Mermaid docs
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free

### 75. To help new systems engineers visualize state transitions inside `FlightModeStateMachine.rs`, which text-based diagram syntax can Copilot generate directly inside `README.md` or PR descriptions that GitHub.com renders natively? (`____` diagrams)

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** Use `Inline Chat`, `Copilot Edits`, **Next Edit Suggestions**, and `/doc` to scaffold repetitive DTOs/validators, extract pure functions to reduce cyclomatic complexity, and generate JSDoc/OpenAPI/Mermaid docs
- **C.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **D.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)

### 76. After adding a new `timestamp_ns: u64` parameter to `Packet::new(...)` on line 18 of `packet.rs`, VS Code immediately highlights three call sites further down the file and offers `Tab` jump-and-apply suggestions. Which productivity feature is assisting here?

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **C.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **D.** Use **Inline ghost-text completions** (`Tab` to accept, `Alt+]` / `Option+]` to cycle) and **Next Edit Suggestions (`NES`)** to predict subsequent ripple edits across nearby lines

### 77. A Rust developer at StratosFlight hits a complex borrow-checker lifetime error (`error[E0597]: borrowed value does not live long enough`) in the integrated terminal. Which in-IDE Copilot Chat command explains the lifetime conflict and proposes a borrow-safe patch without opening a web browser? (`@terminal /____`)

- **A.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** Minimize context switching by running `/explain` on complex regexes/SQL/legacy modules, `@terminal` + `/fix` (`or Copilot CLI`) on shell/build errors, and `@workspace` / **Spaces** for repo onboarding
- **D.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically

### 78. An engineer unfamiliar with legacy `awk` and `sed` build scripts in `stratosflight/yocto-bsp` needs to understand subtle field-splitting flags before modifying a recipe. How does Copilot accelerate safe comprehension?

- **A.** Minimize context switching by running `/explain` on complex regexes/SQL/legacy modules, `@terminal` + `/fix` (`or Copilot CLI`) on shell/build errors, and `@workspace` / **Spaces** for repo onboarding
- **B.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **C.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **D.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins

### 79. StratosFlight needs 1,000 realistic synthetic ADS-B aircraft position frames (`ICAO hex, latitude, longitude, barometric altitude, squawk`) to load-test its ground receiver without using restricted customer flight tracks. How should Copilot be used?

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** Generate schema-valid **synthetic test fixtures** (`zero real customer PII`) and modernize legacy code (`e.g., Java 8 -> 21, Python 2 -> 3.12, callbacks -> async/await`) incrementally behind characterization tests
- **C.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **D.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases

### 80. StratosFlight is migrating a 15-year-old C++98 sensor library (`raw new/delete, manual pthread_mutex_t, NULL macros`) to C++20 (`std::unique_ptr, std::jthread, std::span, nullptr`). Why must the migration proceed module-by-module behind characterization tests?

- **A.** Generate schema-valid **synthetic test fixtures** (`zero real customer PII`) and modernize legacy code (`e.g., Java 8 -> 21, Python 2 -> 3.12, callbacks -> async/await`) incrementally behind characterization tests
- **B.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **C.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **D.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions

### 81. StratosFlight's Python ground-station team migrates legacy untyped Python 3.7 scripts to typed Python 3.12 (`pydantic v2`, `pytest`). Proposed solution: First generate `pytest` characterization tests covering current CSV inputs/outputs, configure `.github/instructions/python312.instructions.md` (`applyTo: "**/*.py"`), refactor one module at a time in Agent Mode running `pytest` + `mypy --strict`, and review diffs. Does this meet the goal?

- **A.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements
- **B.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **C.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **D.** No — Copilot Chat **`Ask` mode** only answers questions and proposes snippets in chat; autonomous multi-file workspace edits with iterative terminal test execution require **Agent Mode** (`or Copilot CLI`)

### 82. When generating unit tests for `AltimeterService` (`which reads hardware I2C registers via trait I2cBus`), how should you prompt `/tests` so CI runs deterministically on Linux runners without physical I2C hardware?

- **A.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **B.** Use `/tests` (paired with testing `.instructions.md` conventions) to generate unit and integration tests with isolated I/O mocks/stubs, parameterized table cases, and deterministic teardown
- **C.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **D.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically

### 83. StratosFlight's Rust testing standard (`rust-tests.instructions.md`) governs AI-generated tests across crates. Which two rules ensure high defect-detection value? Select two.

- **A.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **B.** Lock existing legacy behavior with characterization and boundary-value unit tests **before** refactoring idioms with Copilot Edits or Agent Mode
- **C.** Use `/tests` (paired with testing `.instructions.md` conventions) to generate unit and integration tests with isolated I/O mocks/stubs, parameterized table cases, and deterministic teardown
- **D.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **E.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases

### 84. A Copilot-generated test for `normalizeHeadingDeg(double deg)` checks `90.0 -> 90.0` and `450.0 -> 90.0`. Which critical floating-point and boundary edge cases should the engineer ask Copilot to add assertions for?

- **A.** Prompt explicitly for **boundary and adversarial edge cases** (`null/empty, 0/-1/MAX_INT, leap-year/DST timestamps, Unicode, timeouts, race conditions`) and assert concrete outputs/errors (`never tautologies`)
- **B.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **C.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free

### 85. StratosFlight audits AI-generated test suites and security patches in `stratosflight/ground-api`. Which three engineering checks separate production-grade test & security engineering from superficial coverage? Select three.

- **A.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **B.** Validate that security fixes (`such as CodeQL Copilot Autofix`) replace string-concatenated queries/commands with parameterized APIs and pass full regression + SAST checks
- **C.** Use `/tests` (paired with testing `.instructions.md` conventions) to generate unit and integration tests with isolated I/O mocks/stubs, parameterized table cases, and deterministic teardown
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **E.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **F.** Prompt explicitly for **boundary and adversarial edge cases** (`null/empty, 0/-1/MAX_INT, leap-year/DST timestamps, Unicode, timeouts, race conditions`) and assert concrete outputs/errors (`never tautologies`)

### 86. In `stratosflight/ground-portal`, `CodeQL` detects a path-traversal vulnerability (`os.path.join(base_dir, user_filename)`) on a pull request and generates a **Copilot Autofix** patch (`os.path.realpath` prefix validation). Order the governance and remediation steps.

- **A.** Delete Content Exclusions thinking they block `CodeQL` → Paste live DB passwords into PR comments to test Autofix → Merge with red integration tests → Rotate credentials next quarter
- **B.** Set `Suggestions matching public code = Block` in Org policy → Inspect `CodeQL` PR **Copilot Autofix** diff & explanation → Validate the patch (`parameterized SQL`) & package imports → Commit fix, pass `CodeQL` + tests & get human PR approval
- **C.** Set `Suggestions matching public code = Allow` while expecting full IP indemnity on verbatim matches → Auto-commit every Copilot Autofix directly to `main` untested → Disable `CodeQL` PR checks → Skip human review
- **D.** Paste GPL-3.0 source into `.github/copilot-instructions.md` → Treat Copilot Chat as binding legal license sign-off → Dismiss `CodeQL` SQLi alerts without patching → Deploy to production

### 87. A C++ telemetry parser allocates `std::string` copies inside a 100-kHz inner loop and concatenates shell arguments via `std::system(("tar -xf " + archive).c_str())`. Which two improvements should the engineer prompt Copilot to apply?

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **C.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **D.** Use Copilot Chat and **CodeQL Copilot Autofix** to remediate vulnerabilities (`SQLi -> parameterized queries, XSS -> encoding, path traversal, SSRF`) and eliminate `O(n^2)` loops or `N+1` ORM queries

---

## Domain 6 — Configure privacy, content exclusions, and safeguards (10–15% official weight · 13 questions)

### 88. StratosFlight's security administrator configures Organization **Content Exclusions** for `- "/itar/**"` across all repositories in `stratosflight` and validates client enforcement. Place the steps in order.

- **A.** Add `fnmatch` globs (`- "/secrets/**"`) in `Content exclusion` → Allow `<=30 min` (or reload IDE) for policy sync → Verify crossed-out icon & `copilot.content_exclusion_changed` log → Avoid cross-file imports where IDE LSP hover types surface
- **B.** Put exclusion rules in `package.json` → Wait 14 days for policy propagation → Have a Repo Admin delete Organization-level Content Exclusions → Disable Enterprise Audit Logs
- **C.** Configure Content Exclusions on a personal Copilot Free plan → Write PCRE lookbehind regexes instead of `fnmatch` globs → Expect exclusions to block `git clone` and Actions runs → Ignore IDE status icons
- **D.** List tracked `secrets.yaml` in `.gitignore` expecting Copilot to exclude it → Set `Suggestions matching public code = Allow` → Disable IDE TLS verification → Share one seat login across 10 engineers

### 89. After saving a new Organization Content Exclusion rule in GitHub.com Settings, up to how many minutes may connected VS Code or JetBrains clients take to fetch the updated policy automatically (`if the developer does not reload the IDE`)? (`up to ____ minutes`)

- **A.** Configuring Copilot Content Exclusions also blocks `git clone`, GitHub Actions runners, and `CodeQL` security scans from reading the excluded files
- **B.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **C.** Configure **Content Exclusions** (`Copilot Business & Enterprise`) in Repo/Org settings with YAML `fnmatch` globs (`- "/secrets/**"`); rules combine additively (`Repo cannot weaken Org`) and sync in `<=30 min`
- **D.** No — Repository and Organization **Content Exclusions** require **Copilot Business or Copilot Enterprise**; personal Copilot Free/Pro/Pro+ plans do not support Org Content Exclusions

### 90. A StratosFlight DevOps engineer worries that adding `- "/infra/prod-vars.tfvars"` to Copilot Content Exclusions will break their nightly GitHub Actions `terraform plan` workflow and `CodeQL` IaC scans. Will Content Exclusions block Actions or `CodeQL`?

- **A.** Configuring Copilot Content Exclusions also blocks `git clone`, GitHub Actions runners, and `CodeQL` security scans from reading the excluded files
- **B.** Excluded files are omitted from inline completions, IDE Chat, and Copilot Code Review, **but** IDE language-server (`LSP`) hover types from imported symbols can still surface, and `git`/`CodeQL`/Actions are unaffected
- **C.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 91. Organization `stratosflight` defines an Organization Content Exclusion `*` -> `- "/classified/**"`. A team lead with Admin role on `stratosflight/sim-sandbox` wants Copilot enabled inside `/classified/mock.yaml`. Proposed solution: Edit Repository `Settings -> Copilot -> Content exclusion` in `sim-sandbox` to remove `/classified/**` without changing the Organization rule. Does this meet the goal?

- **A.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **B.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements
- **C.** No — Repository administrators **cannot delete or override** Organization-level Content Exclusions (`Repo and Org exclusions combine additively, and the most restrictive policy wins`)
- **D.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins

### 92. Does GitHub's **Copilot IP Indemnity** cover a developer on Copilot Business who deliberately pastes half of a copyrighted third-party commercial library into a file to force Copilot to reconstruct the rest verbatim?

- **A.** No — Repository and Organization **Content Exclusions** require **Copilot Business or Copilot Enterprise**; personal Copilot Free/Pro/Pro+ plans do not support Org Content Exclusions
- **B.** Customers retain ownership of their code (`GitHub claims no copyright over suggestions`), and **Copilot Business / Enterprise** provide **IP Indemnity** when `Suggestions matching public code` is set to **`Block`**
- **C.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **D.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models

### 93. A StratosFlight procurement lawyer asks whether Individual plans (`Copilot Free, Pro, or Pro+`) include enterprise third-party intellectual-property legal defense (**IP Indemnity**). Which plans include IP Indemnity?

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **C.** Customers retain ownership of their code (`GitHub claims no copyright over suggestions`), and **Copilot Business / Enterprise** provide **IP Indemnity** when `Suggestions matching public code` is set to **`Block`**
- **D.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models

### 94. On **Copilot Business and Copilot Enterprise**, is there a per-user checkbox allowing an individual developer to opt corporate repository code **into** GitHub foundational model training?

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **C.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **D.** On Individual plans (`Copilot Free / Pro / Pro+`), disable `Allow GitHub to use my code snippets from the code editor for product improvements` in GitHub Copilot settings to opt out of model training

### 95. StratosFlight's Enterprise policy sets `Suggestions matching public code = No policy`, and Organization `stratosflight` sets `Suggestions matching public code = Block`. What effective duplication filter applies to `stratosflight` seat holders?

- **A.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **B.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Set **`Suggestions matching public code = Block`** to suppress `~150+` char matches against public GitHub repos; when set to **`Allow`**, **Code Referencing** logs matched repo URLs and licenses in the IDE

### 96. An engineering lead wants **GitHub Code Referencing** license links in VS Code while simultaneously retaining **GitHub Copilot IP Indemnity** on the same organization. Proposed solution: Set `Suggestions matching public code` to `Allow` on `stratosflight` and rely on IP Indemnity if any AGPL-3.0 match slips into a product release. Does this meet the goal?

- **A.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **B.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **C.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements
- **D.** No — GitHub's **Copilot IP Indemnity** on Business/Enterprise ceases to cover suggestions when `Suggestions matching public code` is set to **`Allow`**; set the filter to **`Block`**

### 97. A StratosFlight architect briefs legal counsel on how GitHub Copilot handles open-source code similarity. Which two technical facts should they present? Select two.

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Set **`Suggestions matching public code = Block`** to suppress `~150+` char matches against public GitHub repos; when set to **`Allow`**, **Code Referencing** logs matched repo URLs and licenses in the IDE
- **E.** Customers retain ownership of their code (`GitHub claims no copyright over suggestions`), and **Copilot Business / Enterprise** provide **IP Indemnity** when `Suggestions matching public code` is set to **`Block`**

### 98. A StratosFlight developer opens `config.yaml` in VS Code and sees a **crossed-out Copilot eye/logo icon** in the bottom status bar (`hover tooltip: Copilot is disabled for this file by organization policy`), while `main.rs` in the same repo gets completions normally. What is the cause?

- **A.** Diagnose missing completions or unexpected exclusions via **Copilot Diagnostics / Output logs**: verify seat assignment, filetype toggle, active exclusion icon (`most restrictive org wins`), and TLS proxy allowlists (`*.githubcopilot.com`)
- **B.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files

### 99. A developer gets inline completions in `.rs` and `.cpp` files, yet receives zero inline ghost text in `.md` Markdown files even though no Content Exclusion exists. Which local VS Code setting is disabled by default or customized per language? (`github.copilot.____`)

- **A.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **B.** Configuring Copilot Content Exclusions also blocks `git clone`, GitHub Actions runners, and `CodeQL` security scans from reading the excluded files
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Diagnose missing completions or unexpected exclusions via **Copilot Diagnostics / Output logs**: verify seat assignment, filetype toggle, active exclusion icon (`most restrictive org wins`), and TLS proxy allowlists (`*.githubcopilot.com`)

### 100. Two StratosFlight engineers troubleshoot Copilot issues: Engineer A sees `Copilot Chat disabled by organization` despite `stratosflight` enabling Chat (`Engineer A also belongs to contractor org acme-defense`), and Engineer B sees HTTP `407 Proxy Authentication Required`. Which two root causes apply? Select two.

- **A.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **B.** When a user receives Copilot policies from multiple Organizations (or Enterprise + Org), GitHub enforces the **most restrictive** policy (`Block overrides Allow; Disabled overrides Enabled`)
- **C.** Diagnose missing completions or unexpected exclusions via **Copilot Diagnostics / Output logs**: verify seat assignment, filetype toggle, active exclusion icon (`most restrictive org wins`), and TLS proxy allowlists (`*.githubcopilot.com`)
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **E.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins

---

## Answer Key and Explanations

### Question 1 — `D` (Use GitHub Copilot responsibly)

Correct answer: D (is correct). Generative AI models optimize next-token likelihood rather than numerical stability or domain physics, so singular-matrix divide-by-zero or floating-point overflow edge cases require rigorous engineering verification. [Skill 1.1: Describe risks and limitations of Generative AI tools | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/responsible-ai-with-github-copilot/)]

- **A:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Correct. Generative AI risks and limitations (`1.1`) address probabilistic next-token prediction, hallucinations, outdated APIs, and bias—not IDE installation or REST seat billing.

### Question 2 — `B` (Use GitHub Copilot responsibly)

Correct answer: B (is correct). Confirm on `crates.io` (`or StratosFlight's internal Artifactory mirror`) that the crate genuinely exists, comes from a trusted maintainer, and is not an AI-hallucinated **slopsquatting** trap. [Skill 1.1: Describe risks and limitations of Generative AI tools | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/responsible-ai-with-github-copilot/)]

- **A:** Incorrect. Copilot Audit Logs and Metrics API (`2.14`) separate security/compliance event logs from anonymized (`>=5`-user) adoption telemetry.
- **B:** Correct. Package hallucination / slopsquatting verification (`1.1`, `1.4`) protects dependency supply chains—not Markdown PR summaries or status badges.
- **C:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **D:** Incorrect. GitHub Spark (`2.11`) accelerates full-stack micro-app prototyping and deployment directly from natural language and visual controls.

### Question 3 — `B` (Use GitHub Copilot responsibly)

Correct answer: B (is correct). Require deliberate line-by-line review (`supported by clang-tidy, AddressSanitizer/UBSan, unit tests, and independent human PR sign-off`) on every AI-assisted change. [Skill 1.1: Describe risks and limitations of Generative AI tools | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/responsible-ai-with-github-copilot/)]

- **A:** Incorrect. Installing GitHub Copilot CLI (`2.5`) uses `@github/copilot` (`Node 22+`), WinGet, or Homebrew, followed by `/login` OAuth and directory trust confirmation.
- **B:** Correct. Automation bias (`1.1`, `1.4`) occurs when developers accept syntactically clean completions without verifying business logic or security invariants.
- **C:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 4 — `B, C` (Use GitHub Copilot responsibly)

Correct answers: B and C (are correct). LLMs generate probabilistic (`non-guaranteed`) token sequences prone to subtle hallucinations/edge-case bugs, and developers face automation complacency if they treat clean syntax as proof of correctness. [Skill 1.1: Describe risks and limitations of Generative AI tools | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/responsible-ai-with-github-copilot/)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Correct. Automation bias (`1.1`, `1.4`) occurs when developers accept syntactically clean completions without verifying business logic or security invariants.
- **C:** Correct. Generative AI risks and limitations (`1.1`) address probabilistic next-token prediction, hallucinations, outdated APIs, and bias—not IDE installation or REST seat billing.
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **E:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).

### Question 5 — `A` (Use GitHub Copilot responsibly)

Correct answer: A (is correct). **Inclusiveness** ensures AI-assisted interfaces and workflows empower users across diverse physical, visual, auditory, and cognitive abilities. [Skill 1.2: Describe ethical and responsible AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-code-completion)]

- **A:** Correct. Microsoft/GitHub Responsible AI (`1.2`) centers on Fairness, Reliability & Safety, Privacy & Security, Inclusiveness, Transparency, and human Accountability.
- **B:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **C:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **D:** Incorrect. Copilot CLI programmatic flags (`2.6`) control non-interactive scripting (`-p`, `-s`, `--output-format=json`), tool permissions, and `--fleet` parallelism.

### Question 6 — `D` (Use GitHub Copilot responsibly)

Correct answer: D (is correct). The human author must verify every factual claim in the AI-generated PR summary against the actual code diff (`Transparency & Accountability`) so reviewers are never misled by inaccurate descriptions. [Skill 1.2: Describe ethical and responsible AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-code-completion)]

- **A:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **D:** Correct. Ethical AI governance (`1.2`) requires human ownership, license respect, and transparent review—never treating Copilot as an autonomous merge authority.

### Question 7 — `A` (Use GitHub Copilot responsibly)

Correct answer: A (is correct). **Fairness** (`and Inclusiveness`) is compromised when unrepresentative datasets cause uneven error rates across different demographic or linguistic user groups. [Skill 1.2: Describe ethical and responsible AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-code-completion)]

- **A:** Correct. Fairness and Inclusiveness (`1.2`, `1.3`) ensure AI-assisted software serves diverse users equitably and meets accessibility standards.
- **B:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **C:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **D:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.

### Question 8 — `D, E, F` (Use GitHub Copilot responsibly)

Correct answers: D, E, and F (are correct). Evaluate systems against all six Responsible AI principles, test UI/data flows for Fairness and Inclusiveness (`accessibility & representative inputs`), and enforce human-in-the-loop merge accountability. [Skill 1.2: Describe ethical and responsible AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-code-completion)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **D:** Correct. Fairness and Inclusiveness (`1.2`, `1.3`) ensure AI-assisted software serves diverse users equitably and meets accessibility standards.
- **E:** Correct. Microsoft/GitHub Responsible AI (`1.2`) centers on Fairness, Reliability & Safety, Privacy & Security, Inclusiveness, Transparency, and human Accountability.
- **F:** Correct. Human-in-the-loop accountability (`1.2`, `1.4`) ensures engineers remain responsible for correctness, security, and license compliance.

### Question 9 — `C` (Use GitHub Copilot responsibly)

Correct answer: C (is correct). Public training corpora contain decades of legacy unsafe C/C++ code (`historical code bias`); pairing explicit safe-API instructions (`std::span` / bounds checks) with **`CodeQL` SAST** (`and ASan`) blocks buffer-overflow sinks. [Skill 1.3: Identify potential harms and mitigation strategies of AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/overview)]

- **A:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **B:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **C:** Correct. Harm mitigation (`1.3`) combines RAI safety filters, bias testing, SAST scanning, and privacy controls—not disabling code review.
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).

### Question 10 — `A` (Use GitHub Copilot responsibly)

Correct answer: A (is correct). External logs/issues/docs can carry **indirect prompt injection** payloads designed to hijack agent tool calls, so write/shell actions must remain gated by human review and least-privilege tool scopes. [Skill 1.3: Identify potential harms and mitigation strategies of AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/overview)]

- **A:** Correct. Indirect prompt-injection defense (`1.3`, `1.5`) guards Agent Mode and MCP tool invocations against malicious instructions hidden in external data.
- **B:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. False: `#runSubagent` runs autonomously in its **own isolated context window** without pausing for user feedback, returning only the distilled result (`2.9`).

### Question 11 — `A, B` (Use GitHub Copilot responsibly)

Correct answers: A and B (are correct). Mitigate insecure legacy code patterns via `CodeQL` + secure `.instructions.md` rules, and defend against **indirect prompt injection** from untrusted external inputs via human tool-call approvals. [Skill 1.3: Identify potential harms and mitigation strategies of AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/overview)]

- **A:** Correct. Harm mitigation (`1.3`) combines RAI safety filters, bias testing, SAST scanning, and privacy controls—not disabling code review.
- **B:** Correct. Indirect prompt-injection defense (`1.3`, `1.5`) guards Agent Mode and MCP tool invocations against malicious instructions hidden in external data.
- **C:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **D:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **E:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).

### Question 12 — `C` (Use GitHub Copilot responsibly)

Correct answer: C (is correct). Constrain the prompt -> inspect logic & verify crates exist in trusted registries -> run unit/property tests plus `CodeQL` & secret scanning -> complete human peer PR review. [Skill 1.4: Explain the need to validate AI output | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)]

- **A:** Incorrect. Incorrect: merging unverified LLM output or replacing human peer review with Copilot Code Review violates Responsible AI accountability.
- **B:** Incorrect. Incorrect: blindly installing hallucinated package names exposes builds to dependency confusion and slopsquatting.
- **C:** Correct. Correct order: constrained prompt -> manual logic & dependency check (`blocking slopsquatting`) -> automated tests/SAST -> human PR review.
- **D:** Incorrect. Incorrect: pasting real PII into prompts and bypassing human review violates privacy and Responsible AI governance.

### Question 13 — `B` (Use GitHub Copilot responsibly)

Correct answer: B (is correct). Syntactically valid AI completions can harbor subtle concurrency/resource leaks, making compiler warnings, static analysis (`CodeQL`), concurrency tests, and human review indispensable. [Skill 1.4: Explain the need to validate AI output | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)]

- **A:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **B:** Correct. Validating AI output (`1.4`) requires human code review, automated tests, and security scanning before merge.
- **C:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **D:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).

### Question 14 — `C` (Use GitHub Copilot responsibly)

Correct answer: C (is correct). Generative LLMs sample probabilistically (`non-deterministic` output), so engineers must validate correctness with deterministic unit tests rather than expecting byte-identical generations. [Skill 1.4: Explain the need to validate AI output | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)]

- **A:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Correct. Non-determinism (`1.4`, `3.5`) means syntactic plausibility never guarantees functional equivalence across repeated prompts.
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).

### Question 15 — `B` (Use GitHub Copilot responsibly)

Correct answer: B (is correct). No — `GET /orgs/{org}/copilot/metrics` returns privacy-preserving **aggregated** org/team adoption statistics (`requiring >=5 active users`) with zero per-user login names; query `GET /orgs/{org}/copilot/billing/seats` instead. [Skill 1.4: Explain the need to validate AI output | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)]

- **A:** Incorrect. Copilot Audit Logs and Metrics API (`2.14`) separate security/compliance event logs from anonymized (`>=5`-user) adoption telemetry.
- **B:** Correct. Per-seat dormancy audits (`2.14`, `2.15`) require `/copilot/billing/seats`, whereas `/copilot/metrics` aggregates anonymized adoption stats.
- **C:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **D:** Incorrect. The proposed GitHub Copilot configuration or workflow violates at least one stated governance, privacy, or technical requirement. No — `GET /orgs/{org}/copilot/metrics` returns privacy-preserving **aggregated** org/team adoption statistics (`requiring >=5 active users`) with zero per-user login names; query `GET /orgs/{org}/copilot/billing/seats` instead.

### Question 16 — `D` (Use GitHub Copilot responsibly)

Correct answer: D (is correct). Configure Content Exclusions for `- "/propulsion/itar-tables/**"`, never paste export-controlled data or secrets into prompts, keep public-code duplication set to `Block`, and enforce human PR reviews. [Skill 1.5: Identify how to operate GitHub Copilot responsibly | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use)]

- **A:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **B:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **C:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **D:** Correct. Responsible Copilot operation (`1.5`) pairs duplication filtering, Content Exclusions, zero-PII prompting, and mandatory human PR review.

### Question 17 — `D` (Use GitHub Copilot responsibly)

Correct answer: D (is correct). Yes — manual tool/write approval prompts, environment-variable log redaction, and human diff review enforce responsible human-in-the-loop operation in Copilot CLI. [Skill 1.5: Identify how to operate GitHub Copilot responsibly | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use)]

- **A:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **B:** Incorrect. Only **Agent Mode** (or **Copilot CLI**, `2.2`, `2.9`) autonomously edits multiple files and runs terminal verification loops.
- **C:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **D:** Correct. Evaluate whether every stated plan tier, CLI/IDE mechanism, context scope, and Enterprise/Org policy requirement is genuinely met.

### Question 18 — `C` (Use GitHub Copilot responsibly)

Correct answer: C (is correct). Redact or replace live tokens/credentials with fake structural tokens (`e.g., <REDACTED_TOKEN>`) before prompting—never paste active secrets or regulated data into AI prompts. [Skill 1.5: Identify how to operate GitHub Copilot responsibly | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use)]

- **A:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **B:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **C:** Correct. Data minimization in prompts (`1.3`, `1.5`) prevents accidental exposure of regulated personal data or live secrets.
- **D:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).

### Question 19 — `A` (Use GitHub Copilot features)

Correct answer: A (is correct). Yes — a user's GitHub Copilot seat is tied to their GitHub identity (`not locked to a single machine or single IDE`), working across VS Code, Visual Studio, JetBrains IDEs, Xcode, Eclipse, Neovim, and Copilot CLI. [Skill 2.1: Enable Copilot in the IDE | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/quickstart)]

- **A:** Correct. Enabling Copilot in the IDE (`2.1`) requires installing the IDE extension, authenticating with GitHub, and holding an active Copilot plan.
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Incorrect. Copilot Audit Logs and Metrics API (`2.14`) separate security/compliance event logs from anonymized (`>=5`-user) adoption telemetry.
- **D:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).

### Question 20 — `C` (Use GitHub Copilot features)

Correct answer: C (is correct). **Copilot Business** (`$19/user/month`) is available to GitHub Organizations without requiring GHEC (`whereas Copilot Enterprise requires GitHub Enterprise Cloud`). [Skill 2.1: Enable Copilot in the IDE | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/quickstart)]

- **A:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **B:** Incorrect. Individual Copilot tiers (`2.1`, `2.15`) serve single accounts without Organization policy management or Org Content Exclusions.
- **C:** Correct. Organization/Enterprise Copilot tiers (`2.1`, `2.15`, `6.2`) add centralized governance, Content Exclusions, audit logs, and IP Indemnity.
- **D:** Incorrect. Content Exclusions (`2.3`, `6.1`) are only enforced for seats governed under Copilot Business or Copilot Enterprise.

### Question 21 — `C` (Use GitHub Copilot features)

Correct answer: C (is correct). **Inline Chat** (`Ctrl+I` on Windows/Linux, `Cmd+I` on macOS) opens an in-editor prompt directly at the cursor/selection and previews an inline diff you can Accept or Discard. [Skill 2.2: Trigger Copilot through inline suggestions, chat, CLI, and agent mode | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot)]

- **A:** Incorrect. Only **Agent Mode** (or **Copilot CLI**, `2.2`, `2.9`) autonomously edits multiple files and runs terminal verification loops.
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Correct. Triggering Copilot across surfaces (`2.2`) matches Inline Chat, `Ask`, `Edit`, Agent Mode, and Copilot CLI to task complexity.
- **D:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).

### Question 22 — `A, E` (Use GitHub Copilot features)

Correct answers: A and E (are correct). Use `Alt+]` / `Alt+[` (`Option+]` on macOS) or the Completions panel (`Ctrl+Enter`) to inspect inline alternatives, and use **Copilot Edits / Agent Mode** to apply coordinated multi-file working-set changes. [Skill 2.2: Trigger Copilot through inline suggestions, chat, CLI, and agent mode | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot)]

- **A:** Correct. Triggering Copilot across surfaces (`2.2`) matches Inline Chat, `Ask`, `Edit`, Agent Mode, and Copilot CLI to task complexity.
- **B:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **E:** Correct. Inline completions and Next Edit Suggestions (`2.2`, `5.1`) accelerate localized cursor-level coding and follow-on edits.

### Question 23 — `C` (Use GitHub Copilot features)

Correct answer: C (is correct). Inline code completions in supported IDEs, IDE Copilot Chat (`including @workspace / Agent Mode`), and GitHub.com Copilot features (`such as Copilot Code Review`) all omit excluded files from prompts. [Skill 2.3: Configure content exclusions for specific files or repositories (app knowledge) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion)]

- **A:** Incorrect. False: Copilot Content Exclusions apply strictly to **GitHub Copilot** features—they never restrict Git repository ACLs, Actions workflows, or `CodeQL` (`6.1`).
- **B:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **C:** Correct. IDE/repo content exclusion awareness (`2.3`) prevents specified paths from being read into Copilot prompts on Business and Enterprise plans.
- **D:** Incorrect. Adding a tracked path to `.gitignore` (`6.1`) does NOT stop Copilot from reading that file in the IDE or on GitHub.com.

### Question 24 — `D` (Use GitHub Copilot features)

Correct answer: D (is correct). No — although Copilot never directly reads excluded `CryptoTypes.hpp`, IDE language-server (`LSP`) semantic hover/type definitions surfaced inside non-excluded `TelemetrySender.cpp` can still inform completions. [Skill 2.3: Configure content exclusions for specific files or repositories (app knowledge) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion)]

- **A:** Incorrect. False: Copilot Content Exclusions apply strictly to **GitHub Copilot** features—they never restrict Git repository ACLs, Actions workflows, or `CodeQL` (`6.1`).
- **B:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **C:** Incorrect. The proposed GitHub Copilot configuration or workflow violates at least one stated governance, privacy, or technical requirement. No — although Copilot never directly reads excluded `CryptoTypes.hpp`, IDE language-server (`LSP`) semantic hover/type definitions surfaced inside non-excluded `TelemetrySender.cpp` can still inform completions.
- **D:** Correct. GitHub documents that IDE semantic/LSP hover information (`6.1`) is outside direct Content Exclusion file-read blocking when symbols are imported.

### Question 25 — `B` (Use GitHub Copilot features)

Correct answer: B (is correct). It provides a full agentic terminal workflow directly in the shell—reading compiler/log output, editing source & `CMakeLists.txt` files, running verification commands with approval prompts, and managing PRs/issues without a GUI IDE. [Skill 2.4: Define GitHub Copilot CLI and how it benefits developers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-cli)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Correct. GitHub Copilot CLI (`2.4`) brings agentic file editing, command execution, and GitHub workflow integration directly to the terminal.
- **C:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **D:** Incorrect. Copilot Audit Logs and Metrics API (`2.14`) separate security/compliance event logs from anonymized (`>=5`-user) adoption telemetry.

### Question 26 — `C` (Use GitHub Copilot features)

Correct answer: C (is correct). Installing `@github/copilot` (`or WinGet GitHub.Copilot`), `cd`ing into the project and launching `copilot`, running `/login` for GitHub OAuth, and confirming directory trust + `/permissions show` is the exact onboarding flow. [Skill 2.5: Identify the steps for installing GitHub Copilot CLI | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/get-started/cli-quickstart)]

- **A:** Incorrect. Incorrect: `/login` runs inside interactive `copilot`, npm installs require Node.js `22+`, and `config.json` never stores plaintext passwords.
- **B:** Incorrect. Incorrect: `~/.copilot/logs/` stores session logs, and Copilot CLI requires approval before modifying files in default mode.
- **C:** Correct. Correct order: install `@github/copilot` -> `cd` to project & start `copilot` -> authenticate via `/login` -> confirm folder trust & inspect tool permissions.
- **D:** Incorrect. Incorrect: disabling the org Copilot CLI policy blocks access, and authentication must precede non-interactive execution.

### Question 27 — `C` (Use GitHub Copilot features)

Correct answer: C (is correct). When a user receives their Copilot seat from an Organization, the **`Copilot in the CLI`** policy must be set to **`Enabled`** in the Organization's (`and parent Enterprise's`) Copilot policies. [Skill 2.5: Identify the steps for installing GitHub Copilot CLI | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/get-started/cli-quickstart)]

- **A:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **B:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **C:** Correct. Installing GitHub Copilot CLI (`2.5`) uses `@github/copilot` (`Node 22+`), WinGet, or Homebrew, followed by `/login` OAuth and directory trust confirmation.
- **D:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).

### Question 28 — `C` (Use GitHub Copilot features)

Correct answer: C (is correct). Passing `--fleet` (`or running /fleet interactively`) enables **fleet mode**, dispatching parallel subagents across independent sub-tasks to accelerate large refactors. [Skill 2.6: Describe key GitHub Copilot CLI features and commands | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/copilot-cli-reference/cli-programmatic-reference)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Incorrect. False: `#runSubagent` runs autonomously in its **own isolated context window** without pausing for user feedback, returning only the distilled result (`2.9`).
- **C:** Correct. Copilot CLI programmatic flags (`2.6`) control non-interactive scripting (`-p`, `-s`, `--output-format=json`), tool permissions, and `--fleet` parallelism.
- **D:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).

### Question 29 — `B, C` (Use GitHub Copilot features)

Correct answers: B and C (are correct). Pass `--output-format=json` to emit JSONL output (`and --model=MODEL to pin the model`), and place user-editable preferences in `~/.copilot/settings.json` (`never internal runtime config.json`). [Skill 2.6: Describe key GitHub Copilot CLI features and commands | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/copilot-cli-reference/cli-programmatic-reference)]

- **A:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **B:** Correct. Copilot CLI interactive slash commands and `~/.copilot/settings.json` (`2.6`, `2.8`) govern tool approvals and model selection (`config.json` is internal runtime state).
- **C:** Correct. Copilot CLI programmatic flags (`2.6`) control non-interactive scripting (`-p`, `-s`, `--output-format=json`), tool permissions, and `--fleet` parallelism.
- **D:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **E:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).

### Question 30 — `D` (Use GitHub Copilot features)

Correct answer: D (is correct). Passing `--continue` (`most recent session`) or `--resume` (`choose/specify session ID from ~/.copilot/session-state/`) restores conversation history, plans, and checkpoints. [Skill 2.7: Use GitHub Copilot CLI interactively and in sessions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-cli/cli-best-practices)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **C:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **D:** Correct. Interactive Copilot CLI sessions (`2.7`) persist plans, compaction checkpoints, and artifacts in `~/.copilot/session-state/` for `--resume`.

### Question 31 — `A` (Use GitHub Copilot features)

Correct answer: A (is correct). Running `/chronicle reindex` inside Copilot CLI reconstructs `~/.copilot/session-store.db` and synchronizes session metadata with your GitHub account. [Skill 2.7: Use GitHub Copilot CLI interactively and in sessions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-cli/cli-best-practices)]

- **A:** Correct. Interactive Copilot CLI sessions (`2.7`) persist plans, compaction checkpoints, and artifacts in `~/.copilot/session-state/` for `--resume`.
- **B:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **C:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **D:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.

### Question 32 — `D` (Use GitHub Copilot features)

Correct answer: D (is correct). `--trust-folder` trusts workspace hooks and MCP servers for a single new non-interactive `-p` session without persisting to `trustedFolders` and without bypassing tool, path, or URL permission checks. [Skill 2.8: Generate scripts and manage files with GitHub Copilot CLI | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/copilot-cli-reference/cli-config-dir-reference)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **C:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **D:** Correct. Copilot CLI file and script management (`2.8`) enforces explicit write/command approval, `--add-dir` path boundaries, and secret redaction (`GITHUB_TOKEN` redacted by default).

### Question 33 — `D` (Use GitHub Copilot features)

Correct answer: D (is correct). Setting `"kind": "mcp"` with `"serverName": "flight-db"` and `"toolName": "telemetry_query"` in `permissions-config.json` scopes approval to that exact MCP tool (`whereas toolName: null approves the whole server`). [Skill 2.8: Generate scripts and manage files with GitHub Copilot CLI | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/copilot-cli-reference/cli-config-dir-reference)]

- **A:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **B:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Correct. Copilot CLI file and script management (`2.8`) enforces explicit write/command approval, `--add-dir` path boundaries, and secret redaction (`GITHUB_TOKEN` redacted by default).

### Question 34 — `D` (Use GitHub Copilot features)

Correct answer: D (is correct). Registering the MCP server in `.vscode/mcp.json`, delegating broad lookup to isolated `#runSubagent`, applying multi-file edits + `cargo test` in Agent Mode, and reviewing/`Keep`ing verified diffs keeps main chat lean. [Skill 2.9: Use Agent Mode, Copilot Edits, and MCP for enhanced development and workflows; manage Agent Sessions and delegate tasks to Sub-Agents for optimized context usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp)]

- **A:** Incorrect. Incorrect: `.git/HEAD` is Git metadata (not `.vscode/mcp.json`), and diffs must be reviewed before commit.
- **B:** Incorrect. Incorrect: `Ask` mode cannot autonomously edit files or execute terminal loops, and `Keep` should follow diff & test verification.
- **C:** Incorrect. Incorrect: never commit secrets to `.github/copilot-instructions.md`, and `#runSubagent` runs autonomously in isolated context without pausing for user input.
- **D:** Correct. Correct order: register `.vscode/mcp.json` tools -> isolate noisy research via `#runSubagent` -> iterate edits/tests in Agent Mode -> inspect & `Keep` verified diffs.

### Question 35 — `A` (Use GitHub Copilot features)

Correct answer: A (is correct). The unified **`Agent Sessions`** sidebar view in VS Code acts as mission control across local IDE, CLI, and cloud coding agents, allowing mid-run course correction via tabbed chat editors. [Skill 2.9: Use Agent Mode, Copilot Edits, and MCP for enhanced development and workflows; manage Agent Sessions and delegate tasks to Sub-Agents for optimized context usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp)]

- **A:** Correct. Agent Sessions and `#runSubagent` (`2.9`) provide unified multi-agent orchestration and isolated sub-agent context windows.
- **B:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **C:** Incorrect. False: `#runSubagent` runs autonomously in its **own isolated context window** without pausing for user feedback, returning only the distilled result (`2.9`).
- **D:** Incorrect. Only **Agent Mode** (or **Copilot CLI**, `2.2`, `2.9`) autonomously edits multiple files and runs terminal verification loops.

### Question 36 — `B, C, E` (Use GitHub Copilot features)

Correct answers: B, C, and E (are correct). `#runSubagent` executes autonomously in its own isolated context window, `.vscode/mcp.json` exposes external tools to Agent Mode, and the cloud coding agent runs in an ephemeral Actions sandbox opening a draft PR on `copilot/*`. [Skill 2.9: Use Agent Mode, Copilot Edits, and MCP for enhanced development and workflows; manage Agent Sessions and delegate tasks to Sub-Agents for optimized context usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp)]

- **A:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **B:** Correct. Copilot coding agent (`2.9`) executes asynchronous repository tasks in an isolated cloud sandbox and opens a draft PR without merging autonomously.
- **C:** Correct. Agent Mode + MCP (`2.9`) connects Copilot to external tools/APIs via `.vscode/mcp.json` and iterates across edits and terminal runs autonomously.
- **D:** Incorrect. Only **Agent Mode** (or **Copilot CLI**, `2.2`, `2.9`) autonomously edits multiple files and runs terminal verification loops.
- **E:** Correct. Sub-Agent delegation (`2.9`) prevents raw search results from bloating and confusing the primary Agent Mode conversation.
- **F:** Incorrect. False: `#runSubagent` runs autonomously in its **own isolated context window** without pausing for user feedback, returning only the distilled result (`2.9`).

### Question 37 — `A` (Use GitHub Copilot features)

Correct answer: A (is correct). Copilot Code Review posts inline review comments containing fenced GitHub **`suggestion` diff blocks** (`Commit suggestion` / `Add suggestion to batch`), which the human author reviews and commits. [Skill 2.10: Use Copilot for code review and coding assistance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/configure-code-review)]

- **A:** Correct. Copilot Code Review (`2.10`) posts `Comment` reviews with `suggestion` blocks—never counting toward required human merge approvals.
- **B:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **C:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **D:** Incorrect. Copilot Code Review (`1.4`, `2.10`) supplements—never replaces—required human pull-request approvals.

### Question 38 — `B` (Use GitHub Copilot features)

Correct answer: B (is correct). No — `excludeAgent: "code-review"` explicitly blocks **Copilot Code Review** from reading that instruction file (`omit excludeAgent so both code-review and cloud-agent apply it, or set excludeAgent: "cloud-agent" if review-only`). [Skill 2.10: Use Copilot for code review and coding assistance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/configure-code-review)]

- **A:** Incorrect. The proposed GitHub Copilot configuration or workflow violates at least one stated governance, privacy, or technical requirement. No — `excludeAgent: "code-review"` explicitly blocks **Copilot Code Review** from reading that instruction file (`omit excludeAgent so both code-review and cloud-agent apply it, or set excludeAgent: "cloud-agent" if review-only`).
- **B:** Correct. `excludeAgent: "code-review"` (`2.11`) tells GitHub.com to omit that instruction file during Copilot Code Review.
- **C:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **D:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).

### Question 39 — `B` (Use GitHub Copilot features)

Correct answer: B (is correct). Placing `AGENTS.md` in the repository root (`or nested subdirectories`) provides portable agent instructions discovered automatically by GitHub Copilot CLI, coding agent, and IDE agents. [Skill 2.11: Utilize Spaces, Spark, Pull Request summaries, and customizable review standards via instructions files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)]

- **A:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **B:** Correct. PR Summaries and custom instruction files (`2.11`) automate reviewer context and tailor Copilot code generation/review (`without affecting raw inline ghost text where unsupported`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).

### Question 40 — `D` (Use GitHub Copilot features)

Correct answer: D (is correct). No — repository sources attached to a **Copilot Space** stay dynamically synchronized with the live GitHub repository (`respecting viewer repository permissions`), avoiding stale copied docs. [Skill 2.11: Utilize Spaces, Spark, Pull Request summaries, and customizable review standards via instructions files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)]

- **A:** Incorrect. GitHub Spark (`2.11`) accelerates full-stack micro-app prototyping and deployment directly from natural language and visual controls.
- **B:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **C:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **D:** Correct. Copilot Spaces (`2.11`) organize shareable, always-synced multi-repo project context so responses stay grounded in team architecture.

### Question 41 — `A, C` (Use GitHub Copilot features)

Correct answers: A and C (are correct). Use **Copilot Pull Request Summaries** in the GitHub.com PR description toolbar, and create `.github/instructions/hal-unsafe.instructions.md` with frontmatter `applyTo: "crates/hal/**/*.rs"`. [Skill 2.11: Utilize Spaces, Spark, Pull Request summaries, and customizable review standards via instructions files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)]

- **A:** Correct. PR Summaries and custom instruction files (`2.11`) automate reviewer context and tailor Copilot code generation/review (`without affecting raw inline ghost text where unsupported`).
- **B:** Incorrect. `excludeAgent: "code-review"` (`2.11`) tells GitHub.com to omit that instruction file during Copilot Code Review.
- **C:** Correct. Path-scoped `.instructions.md` files (`2.11`) automatically inject targeted coding and review rules only when matching files are touched.
- **D:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **E:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).

### Question 42 — `A` (Use GitHub Copilot features)

Correct answer: A (is correct). The `@vscode` chat participant grounds answers specifically in Visual Studio Code commands, settings, keybindings, and editor APIs (`whereas @workspace queries project code and @terminal queries shell output`). [Skill 2.12: Understand the limits, options, feedback, and commands of GitHub Copilot Chat; include prompt file reuse for consistent responses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/configure-custom-instructions-in-your-ide/add-repository-instructions-in-your-ide)]

- **A:** Correct. Copilot Chat participants, slash commands, `#` context variables, and feedback ratings (`2.12`) focus intent and report quality signals.
- **B:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **C:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 43 — `D, E` (Use GitHub Copilot features)

Correct answers: D and E (are correct). `.prompt.md` files support YAML frontmatter (`description`, `agent`, `model`, `tools`) + `#file:` references invoked via `/triage-crash`, and thumbs-up/down ratings in Chat help teams/GitHub evaluate response quality. [Skill 2.12: Understand the limits, options, feedback, and commands of GitHub Copilot Chat; include prompt file reuse for consistent responses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/configure-custom-instructions-in-your-ide/add-repository-instructions-in-your-ide)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **C:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **D:** Correct. Workspace `.prompt.md` prompt files (`2.12`) standardize repeatable task prompts across VS Code and JetBrains teams.
- **E:** Correct. Copilot Chat participants, slash commands, `#` context variables, and feedback ratings (`2.12`) focus intent and report quality signals.

### Question 44 — `D` (Use GitHub Copilot features)

Correct answer: D (is correct). Enable **`Only allow Copilot code review to be triggered by authorized users`** in Organization Copilot Code Review settings (`which repo admins cannot disable`). [Skill 2.13: Configure organization-wide policy management; enable Copilot Code Review policies and manage feature availability across IDEs and github.com | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/block-agentic-features)]

- **A:** Incorrect. Content Exclusions (`2.3`, `6.1`) are only enforced for seats governed under Copilot Business or Copilot Enterprise.
- **B:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **C:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **D:** Correct. Organization/Enterprise Copilot policy management (`2.13`) governs IDE/GitHub.com features, CLI/MCP access, and repo-level agent blocks.

### Question 45 — `D` (Use GitHub Copilot features)

Correct answer: D (is correct). The **Copilot Metrics API** requires **at least `5` active Copilot users** in the queried organization/team on a given day before returning aggregated breakdown metrics, preventing individual de-anonymization. [Skill 2.14: Utilize audit log events | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-audit-logs-for-copilot-business)]

- **A:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **B:** Incorrect. Per-seat dormancy audits (`2.14`, `2.15`) require `/copilot/billing/seats`, whereas `/copilot/metrics` aggregates anonymized adoption stats.
- **C:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **D:** Correct. Copilot Audit Logs and Metrics API (`2.14`) separate security/compliance event logs from anonymized (`>=5`-user) adoption telemetry.

### Question 46 — `C` (Use GitHub Copilot features)

Correct answer: C (is correct). Authorizing `manage_billing:copilot` + selected-team access, `POST`ing to `/orgs/{org}/copilot/billing/selected_teams`, auditing `last_activity_at` on `GET .../billing/seats`, and `DELETE`ing idle users automates seat lifecycle cleanly. [Skill 2.15: Manage subscriptions using the REST API | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/rest/copilot/copilot-user-management)]

- **A:** Incorrect. Incorrect: personal Copilot Free/Pro/Pro+ plans do NOT inherit Organization Content Exclusions.
- **B:** Incorrect. Incorrect: `/copilot/metrics` returns aggregated anonymized stats (`>=5` active users), whereas `/copilot/billing/seats` exposes per-user `last_activity_at`.
- **C:** Correct. Correct order: authorize `manage_billing:copilot` -> assign via `POST .../selected_teams` (or `selected_users`) -> audit `/seats` -> `DELETE` dormant assignments.
- **D:** Incorrect. Incorrect: Copilot seat REST endpoints live under `/orgs/{org}/copilot/billing/...` and require `manage_billing:copilot` billing authorization.

### Question 47 — `B` (Understand GitHub Copilot data and architecture)

Correct answer: B (is correct). All network traffic between IDE/CLI clients and GitHub Copilot cloud endpoints is encrypted in transit over **`HTTPS / TLS 1.2+`**. [Skill 3.1: Explain data usage, flow, and sharing | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-copilot-policies-as-an-individual-subscriber)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Correct. Copilot Business/Enterprise data handling (`3.1`) guarantees `TLS 1.2+` encryption and zero foundational-model training on customer code (`Free/Pro provide a training opt-out toggle`).
- **C:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 48 — `B` (Understand GitHub Copilot data and architecture)

Correct answer: B (is correct). Inline completion prompts are discarded ephemerally from memory after inference, whereas GitHub.com Chat (`and synced CLI sessions`) persists conversation history encrypted in your account workspace so you can resume threads (`still never used for base-model training`). [Skill 3.1: Explain data usage, flow, and sharing | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-copilot-policies-as-an-individual-subscriber)]

- **A:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **B:** Correct. Copilot Business/Enterprise data handling (`3.1`) guarantees `TLS 1.2+` encryption and zero foundational-model training on customer code (`Free/Pro provide a training opt-out toggle`).
- **C:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **D:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).

### Question 49 — `B` (Understand GitHub Copilot data and architecture)

Correct answer: B (is correct). Operational acceptance telemetry (`accepted line/suggestion counts, language: rust, editor, timestamp`) is recorded in encrypted telemetry stores, while the raw proprietary Rust code snippet itself is NOT stored for model training. [Skill 3.1: Explain data usage, flow, and sharing | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-copilot-policies-as-an-individual-subscriber)]

- **A:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **B:** Correct. Data flow architecture (`3.1`) separates operational/metrics telemetry from ephemeral prompt/completion payloads.
- **C:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 50 — `B` (Understand GitHub Copilot data and architecture)

Correct answer: B (is correct). It prioritizes **currently open tabs in the IDE** (`especially files sharing the same language or overlapping token/Jaccard similarity`), alongside cursor prefix + suffix (`FIM`) and file path metadata. [Skill 3.2: Describe input processing and prompt building | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot)]

- **A:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **B:** Correct. Input processing and prompt building (`3.2`) combines cursor prefix + suffix (`FIM`), relevant open-tab snippets, and repository instructions.
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).

### Question 51 — `A` (Understand GitHub Copilot data and architecture)

Correct answer: A (is correct). Custom instructions (`copilot-instructions.md` / `.instructions.md`) automatically enrich **Chat, Agent Mode, CLI, and Code Review**, whereas `.prompt.md` files are **on-demand** Chat templates (`neither .prompt.md nor MCP servers run on passive ghost-text keystrokes`). [Skill 3.2: Describe input processing and prompt building | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot)]

- **A:** Correct. Input processing and prompt building (`3.2`) combines cursor prefix + suffix (`FIM`), relevant open-tab snippets, and repository instructions.
- **B:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **C:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 52 — `B, E` (Understand GitHub Copilot data and architecture)

Correct answers: B and E (are correct). Code **before and after the cursor (`FIM`)** (`plus language ID and relative filepath`) and high-similarity snippets drawn from **open neighbor tabs** in the IDE. [Skill 3.2: Describe input processing and prompt building | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Correct. Input processing and prompt building (`3.2`) combines cursor prefix + suffix (`FIM`), relevant open-tab snippets, and repository instructions.
- **C:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **D:** Incorrect. False: Copilot Content Exclusions apply strictly to **GitHub Copilot** features—they never restrict Git repository ACLs, Actions workflows, or `CodeQL` (`6.1`).
- **E:** Correct. Fill-in-the-Middle (`FIM`, `3.2`) enables inline completions to align return types and variable names with surrounding downstream lines.

### Question 53 — `B` (Understand GitHub Copilot data and architecture)

Correct answer: B (is correct). Multi-stage **Responsible AI (`RAI`) content moderation and prompt-shield filters** inspect both inbound prompts and outbound completions inside the proxy. [Skill 3.3: Explain proxy filtering and post-processing | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-chat-in-your-ide)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Correct. Proxy filtering and post-processing (`3.3`) enforces auth, RAI moderation, public-code duplication checks, and stop-token trimming.
- **C:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).

### Question 54 — `C` (Understand GitHub Copilot data and architecture)

Correct answer: C (is correct). Syntactic **stop-token truncation and indentation normalization** prevent runaway completions from spilling past the current block or duplicating code already present in the `FIM` suffix. [Skill 3.3: Explain proxy filtering and post-processing | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-chat-in-your-ide)]

- **A:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **B:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **C:** Correct. Proxy filtering and post-processing (`3.3`) enforces auth, RAI moderation, public-code duplication checks, and stop-token trimming.
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 55 — `B, E` (Understand GitHub Copilot data and architecture)

Correct answers: B and E (are correct). The proxy's **Responsible AI prompt-injection/harm classifier** blocks jailbreak prompts, and the **`~150-character` public-code duplication filter** suppresses completions matching public GitHub code. [Skill 3.3: Explain proxy filtering and post-processing | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-chat-in-your-ide)]

- **A:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **B:** Correct. Cloud-proxy post-processing (`3.3`, `3.4`) enforces both RAI content safety and public-code matching policies prior to displaying ghost text.
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **E:** Correct. Proxy filtering and post-processing (`3.3`) enforces auth, RAI moderation, public-code duplication checks, and stop-token trimming.

### Question 56 — `B` (Understand GitHub Copilot data and architecture)

Correct answer: B (is correct). IDE FIM + open-tab assembly (`minus exclusions`) -> `TLS 1.2+` proxy request & token check -> RAI moderation, LLM generation & `~150+` char duplication check -> ghost-text render & zero training retention. [Skill 3.4: Visualize code suggestion lifecycle | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/paths/copilot/)]

- **A:** Incorrect. Incorrect: Copilot LLM inference and public-code duplication checks execute in the cloud proxy over authenticated TLS.
- **B:** Correct. Correct order: IDE FIM/tab assembly (respecting exclusions) -> TLS proxy auth -> RAI + LLM + public-code filter -> ghost-text render & zero training retention.
- **C:** Incorrect. Incorrect: Content Exclusions block excluded paths from entering prompts, and prompts are never published to Gists.
- **D:** Incorrect. Incorrect: inline completion sends scoped editor context over TLS, never runs tests on inference GPUs, and Business/Enterprise never trains base models on customer prompts.

### Question 57 — `A` (Understand GitHub Copilot data and architecture)

Correct answer: A (is correct). The IDE extension **cancels / discards stale in-flight completion requests** (`and re-debounces from the updated cursor state`) so outdated completions do not overwrite newer typing. [Skill 3.4: Visualize code suggestion lifecycle | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/paths/copilot/)]

- **A:** Correct. Code suggestion lifecycle (`3.4`) traces a completion from keystroke pause through IDE context assembly, cloud proxy inference/filtering, and ghost-text display.
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **D:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).

### Question 58 — `A` (Understand GitHub Copilot data and architecture)

Correct answer: A (is correct). An LLM has **no live network access to private runtime infrastructure** unless explicitly connected to an authorized telemetry tool (`such as an MCP server or Copilot Extension`). [Skill 3.5: Describe limitations of LLMs and Copilot | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-coding-agent)]

- **A:** Correct. LLM and Copilot limitations (`3.5`) explain why models hallucinate post-cutoff APIs, vary across runs, truncate overflow tokens, and need tests/MCP.
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.

### Question 59 — `C` (Understand GitHub Copilot data and architecture)

Correct answer: C (is correct). Token-predicting LLMs perform approximate pattern matching rather than symbolic bit-level execution, so low-level bitwise/endian arithmetic must always be verified with unit tests and known byte vectors. [Skill 3.5: Describe limitations of LLMs and Copilot | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-coding-agent)]

- **A:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **B:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **C:** Correct. LLM and Copilot limitations (`3.5`) explain why models hallucinate post-cutoff APIs, vary across runs, truncate overflow tokens, and need tests/MCP.
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).

### Question 60 — `B` (Understand GitHub Copilot data and architecture)

Correct answer: B (is correct). Lexical and embedding-based **RAG workspace retrieval** ranks text/semantic chunks within a finite top-K token budget rather than executing full dynamic runtime program analysis. [Skill 3.5: Describe limitations of LLMs and Copilot | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-coding-agent)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Correct. Retrieval-augmented generation (`RAG`, `3.2`) selects the highest-relevance code slices that fit within the model's context token budget.
- **C:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **D:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).

### Question 61 — `D` (Apply prompt engineering and context crafting)

Correct answer: D (is correct). **Explicit architectural & error-handling constraints** (`no_std`, zero heap allocation, and typed `Result<Self, FrameError>` without `unwrap()`). [Skill 4.1: Describe prompt structure and context | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **C:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **D:** Correct. Prompt structure (`4.1`) combines clear intent, grounded workspace context, explicit constraints, and expected output format.

### Question 62 — `D` (Apply prompt engineering and context crafting)

Correct answer: D (is correct). Strong C++23 types (`std::expected`, `Quaterniond`, `std::chrono::nanoseconds`, `noexcept`) constrain units, error semantics, and exception safety directly in the FIM prefix. [Skill 4.1: Describe prompt structure and context | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Incorrect. Copilot Audit Logs and Metrics API (`2.14`) separate security/compliance event logs from anonymized (`>=5`-user) adoption telemetry.
- **C:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **D:** Correct. In-editor context signals (`4.1`, `4.4`) anchor Fill-in-the-Middle inline completions without leaving the code buffer.

### Question 63 — `B` (Apply prompt engineering and context crafting)

Correct answer: B (is correct). `#sym:computeMachNumber` resolves and attaches that exact workspace symbol definition into the Chat prompt (`complementing #file:, #selection, and #codebase`). [Skill 4.2: Understand how context is determined | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Correct. Context determination (`4.2`) controls which open tabs, `#` chat variables, workspace indexes, and path-matched instructions enter the prompt.
- **C:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **D:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).

### Question 64 — `C` (Apply prompt engineering and context crafting)

Correct answer: C (is correct). Expand the **`References`** (`Used N references`) dropdown at the top of Copilot Chat's response to inspect every instruction file, `#file:`, and workspace chunk injected into that turn. [Skill 4.2: Understand how context is determined | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **C:** Correct. Context determination (`4.2`) controls which open tabs, `#` chat variables, workspace indexes, and path-matched instructions enter the prompt.
- **D:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).

### Question 65 — `A, D` (Apply prompt engineering and context crafting)

Correct answers: A and D (are correct). Verify the file sits in `.github/instructions/*.instructions.md` with a matching `applyTo:` glob (`e.g., "firmware/**/*.c"`), and close unrelated Python/web tabs while opening `imu.h` so editor context aligns. [Skill 4.2: Understand how context is determined | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)]

- **A:** Correct. Curating open tabs and `#file:` attachments (`4.2`, `4.4`) directly improves prompt signal-to-noise ratio.
- **B:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **C:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **D:** Correct. Context determination (`4.2`) controls which open tabs, `#` chat variables, workspace indexes, and path-matched instructions enter the prompt.
- **E:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).

### Question 66 — `D` (Apply prompt engineering and context crafting)

Correct answer: D (is correct). **Few-shot prompting** supplies a small number (`2–3`) of concrete input-to-output examples so the model mirrors bespoke macro formatting and scaling conventions accurately. [Skill 4.3: Use zero-shot and few-shot prompting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat)]

- **A:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **B:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **C:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **D:** Correct. Zero-shot vs few-shot prompting (`4.3`) reserves token-heavier exemplars for custom team patterns that general pretraining cannot infer.

### Question 67 — `A` (Apply prompt engineering and context crafting)

Correct answer: A (is correct). When examples are lengthy, outdated, or unnecessary for standard library tasks (`wasting scarce context-window tokens or anchoring the model onto irrelevant edge patterns from the example`). [Skill 4.3: Use zero-shot and few-shot prompting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat)]

- **A:** Correct. Zero-shot vs few-shot prompting (`4.3`) reserves token-heavier exemplars for custom team patterns that general pretraining cannot infer.
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **D:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).

### Question 68 — `A` (Apply prompt engineering and context crafting)

Correct answer: A (is correct). Paste the exact `TSan` diagnostic (`or attach @terminal`) alongside `#selection` and instruct Copilot to fix the memory ordering on `std::atomic<size_t> head_` (`acquire/release`) and add a multi-threaded stress test. [Skill 4.4: Apply best practices for prompt crafting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)]

- **A:** Correct. Prompt-crafting best practices (`4.4`) favor incremental decomposition, version pinning, and feedback-driven iteration.
- **B:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **C:** Incorrect. Clean editor tabs, `/clear` between topics, and `#runSubagent` isolation (`4.2`, `4.6`) prevent context confusion.
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).

### Question 69 — `C` (Apply prompt engineering and context crafting)

Correct answer: C (is correct). Descriptive domain identifiers encode units and encoding (`ARINC-429 octal label bits`) directly in the local prefix, steering token probabilities without extra chat turns. [Skill 4.4: Apply best practices for prompt crafting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **C:** Correct. Prompt-crafting best practices (`4.4`) favor incremental decomposition, version pinning, and feedback-driven iteration.
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 70 — `A` (Apply prompt engineering and context crafting)

Correct answer: A (is correct). Enabling `"chat.promptFiles": true` + creating `.github/prompts/icd-decoder.prompt.md`, linking `#file:` exemplars in Git, invoking `/icd-decoder` with clean open tabs, and running `/clear` before switching topics standardizes output. [Skill 4.5: Explain prompt engineering principles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/paths/gh-copilot-2/)]

- **A:** Correct. Correct order: create `.github/prompts/*.prompt.md` -> link few-shot exemplars -> invoke `/api` with clean tab context -> reset chat on topic switch.
- **B:** Incorrect. Incorrect: reusable prompt files end in `.prompt.md` under `.github/prompts/` (`whereas applyTo: belongs to *.instructions.md`).
- **C:** Incorrect. Incorrect: never embed secrets in repository prompt files, and one-word prompts lack actionable context.
- **D:** Incorrect. Incorrect: `.github/workflows/*.yml` defines Actions workflows (not `.github/prompts/*.prompt.md`), and stale tabs + long threads cause context drift.

### Question 71 — `C` (Apply prompt engineering and context crafting)

Correct answer: C (is correct). Committing `.github/copilot-instructions.md` automatically injects repository-wide coding, build, and architecture conventions into Copilot Chat, Agent Mode, CLI, and Code Review. [Skill 4.5: Explain prompt engineering principles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/paths/gh-copilot-2/)]

- **A:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **B:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **C:** Correct. Prompt engineering principles (`4.5`) emphasize specificity, positive constraints, authoritative grounding, and reusable templates.
- **D:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).

### Question 72 — `A` (Apply prompt engineering and context crafting)

Correct answer: A (is correct). The subagent executes those 28 file reads inside an **isolated temporary context window** and returns only a concise summary, preserving the main chat's token budget for code implementation. [Skill 4.6: Describe prompt process flow and chat history usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)]

- **A:** Correct. Prompt process flow and chat history management (`4.6`) prevent context drift and token-window eviction across unrelated tasks.
- **B:** Incorrect. False: `#runSubagent` runs autonomously in its **own isolated context window** without pausing for user feedback, returning only the distilled result (`2.9`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).

### Question 73 — `B, E` (Apply prompt engineering and context crafting)

Correct answers: B and E (are correct). Start a fresh session (`/clear` or new Chat editor) per crate/feature, and offload broad read-only codebase searches to `#runSubagent` (`or use Copilot CLI infinite-session checkpoints`). [Skill 4.6: Describe prompt process flow and chat history usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Correct. Resetting chat history on task switches (`4.6`) avoids context confusion and token-window truncation.
- **C:** Incorrect. Clean editor tabs, `/clear` between topics, and `#runSubagent` isolation (`4.2`, `4.6`) prevent context confusion.
- **D:** Incorrect. False: `#runSubagent` runs autonomously in its **own isolated context window** without pausing for user feedback, returning only the distilled result (`2.9`).
- **E:** Correct. Prompt process flow and chat history management (`4.6`) prevent context drift and token-window eviction across unrelated tasks.

### Question 74 — `C` (Improve developer productivity with GitHub Copilot)

Correct answer: C (is correct). Use **Copilot Edits / Agent Mode** (`with one canonical formatter attached as a few-shot #file: exemplar`) to generate consistent `fmt::formatter` and serializer implementations across the working set, then compile and test. [Skill 5.1: Use Copilot for code generation, refactoring, and documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/developer-use-cases-for-ai-with-github-copilot/)]

- **A:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **B:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **C:** Correct. Code generation, refactoring, and documentation (`5.1`) accelerates boilerplate, structural cleanup, and API docs while preserving behavior.
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).

### Question 75 — `B` (Improve developer productivity with GitHub Copilot)

Correct answer: B (is correct). GitHub Flavored Markdown renders fenced `mermaid` (`stateDiagram-v2`, `sequenceDiagram`, `flowchart`) code blocks natively in READMEs, Issues, PRs, and Wikis. [Skill 5.1: Use Copilot for code generation, refactoring, and documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/developer-use-cases-for-ai-with-github-copilot/)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Correct. Code generation, refactoring, and documentation (`5.1`) accelerates boilerplate, structural cleanup, and API docs while preserving behavior.
- **C:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **D:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.

### Question 76 — `D` (Improve developer productivity with GitHub Copilot)

Correct answer: D (is correct). **Next Edit Suggestions (`NES`)** tracks your recent edit intent and proposes cascaded follow-up edits at related locations across the file. [Skill 5.1: Use Copilot for code generation, refactoring, and documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/developer-use-cases-for-ai-with-github-copilot/)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **C:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **D:** Correct. Inline completions and Next Edit Suggestions (`2.2`, `5.1`) accelerate localized cursor-level coding and follow-on edits.

### Question 77 — `C` (Improve developer productivity with GitHub Copilot)

Correct answer: C (is correct). Running `@terminal /fix` (`or /explain` on the compiler diagnostic) analyzes the exact terminal error alongside source context and suggests an idiomatic lifetime/ownership fix in place. [Skill 5.2: Accelerate learning and reduce context switching | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/copilot-chat-cookbook)]

- **A:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Correct. Accelerating learning and reducing context switching (`5.2`) keeps developers productive inside the IDE and terminal.
- **D:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).

### Question 78 — `A` (Improve developer productivity with GitHub Copilot)

Correct answer: A (is correct). Select the script in the editor and invoke `/explain` (`asking specifically about edge cases with whitespace and exit statuses`) to get a line-by-line walkthrough grounded in the workspace. [Skill 5.2: Accelerate learning and reduce context switching | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/copilot-chat-cookbook)]

- **A:** Correct. Accelerating learning and reducing context switching (`5.2`) keeps developers productive inside the IDE and terminal.
- **B:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **C:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **D:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).

### Question 79 — `B` (Improve developer productivity with GitHub Copilot)

Correct answer: B (is correct). Prompt Copilot (`or have it write a deterministic Python/Rust generator script with a fixed RNG seed`) using public ADS-B bit-layout specs to synthesize realistic test frames containing zero restricted flight logs. [Skill 5.3: Generate sample data and modernize legacy code | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/tutorials/modernize-legacy-code)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Correct. Sample data generation and legacy modernization (`5.3`) combine synthetic non-PII fixtures with test-backed incremental upgrades.
- **C:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **D:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).

### Question 80 — `A` (Improve developer productivity with GitHub Copilot)

Correct answer: A (is correct). Incremental module-by-module refactoring fits comfortably inside Copilot's context window and lets existing characterization tests immediately pinpoint any lifetime or behavioral regression. [Skill 5.3: Generate sample data and modernize legacy code | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/tutorials/modernize-legacy-code)]

- **A:** Correct. Sample data generation and legacy modernization (`5.3`) combine synthetic non-PII fixtures with test-backed incremental upgrades.
- **B:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **C:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **D:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).

### Question 81 — `A` (Improve developer productivity with GitHub Copilot)

Correct answer: A (is correct). Yes — locking legacy behavior with `pytest`, scoping target-version rules via `.instructions.md`, and running iterative `pytest` + `mypy --strict` checks in Agent Mode delivers safe modernization. [Skill 5.3: Generate sample data and modernize legacy code | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/tutorials/modernize-legacy-code)]

- **A:** Correct. Evaluate whether every stated plan tier, CLI/IDE mechanism, context scope, and Enterprise/Org policy requirement is genuinely met.
- **B:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **C:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **D:** Incorrect. Only **Agent Mode** (or **Copilot CLI**, `2.2`, `2.9`) autonomously edits multiple files and runs terminal verification loops.

### Question 82 — `B` (Improve developer productivity with GitHub Copilot)

Correct answer: B (is correct). Instruct `/tests` to inject a deterministic mock/fake `I2cBus` implementation (`simulating both valid sensor bytes and I2C NACK/timeout errors`) while testing real `AltimeterService` logic. [Skill 5.4: Generate unit and integration tests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/develop-unit-tests-using-github-copilot-tools/)]

- **A:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **B:** Correct. Generating unit and integration tests (`5.4`) automates test scaffolding, dependency isolation, and parameterized coverage.
- **C:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **D:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).

### Question 83 — `B, C` (Improve developer productivity with GitHub Copilot)

Correct answers: B and C (are correct). Use parameterized/table-driven (`or proptest property-based`) cases with mocked hardware I/O boundaries, and write characterization tests on legacy functions before refactoring them. [Skill 5.4: Generate unit and integration tests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/develop-unit-tests-using-github-copilot-tools/)]

- **A:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **B:** Correct. Characterization testing (`5.3`, `5.4`) guarantees legacy modernization preserves subtle business edge cases.
- **C:** Correct. Generating unit and integration tests (`5.4`) automates test scaffolding, dependency isolation, and parameterized coverage.
- **D:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **E:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).

### Question 84 — `A` (Improve developer productivity with GitHub Copilot)

Correct answer: A (is correct). Add explicit assertions for `0.0`, `-0.0`, `360.0` (`must wrap to 0.0, not 360.0`), negative angles (`-0.0001`, `-720.0`), `std::numeric_limits<double>::quiet_NaN()`, and `±infinity`. [Skill 5.5: Identify edge cases and write assertions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/copilot-chat-cookbook)]

- **A:** Correct. Edge-case identification and assertion quality (`5.5`) ensures tests catch real boundary defects rather than inflating superficial coverage.
- **B:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **C:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).

### Question 85 — `B, C, F` (Improve developer productivity with GitHub Copilot)

Correct answers: B, C, and F (are correct). Verify assertions check exact return values/error variants (`never tautologies`), exercise boundary/NaN/timeout/concurrency edge cases with isolated I/O fakes, and validate `CodeQL` Autofix patches with regression + SAST runs. [Skill 5.5: Identify edge cases and write assertions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/copilot-chat-cookbook)]

- **A:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **B:** Correct. Verified security remediation (`5.6`) confirms Autofix patches eliminate root-cause injection sinks without breaking callers.
- **C:** Correct. Generating unit and integration tests (`5.4`) automates test scaffolding, dependency isolation, and parameterized coverage.
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **E:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **F:** Correct. Edge-case identification and assertion quality (`5.5`) ensures tests catch real boundary defects rather than inflating superficial coverage.

### Question 86 — `B` (Improve developer productivity with GitHub Copilot)

Correct answer: B (is correct). Keeping `Suggestions matching public code = Block`, inspecting the `CodeQL` Copilot Autofix diff & explanation, validating behavior & imports, and passing `CodeQL` + tests + human PR approval secures the fix. [Skill 5.6: Suggest security improvements and performance optimizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/responsible-use-autofix-code-scanning)]

- **A:** Incorrect. Incorrect: Content Exclusions do not block `CodeQL`, and secrets must never be pasted into PR comments.
- **B:** Correct. Correct order: enforce public-code `Block` policy -> inspect CodeQL Copilot Autofix -> validate logic & dependencies -> pass CI + human PR approval.
- **C:** Incorrect. Incorrect: GitHub IP indemnity requires keeping the public-code duplication filter enabled (`Block`), and Autofix patches require testing and review.
- **D:** Incorrect. Incorrect: Copilot does not provide legal license sign-off, and dismissing real vulnerabilities leaves exploits open.

### Question 87 — `D` (Improve developer productivity with GitHub Copilot)

Correct answer: D (is correct). Replace `std::system` shell string concatenation with a safe non-shell archive/execve API (`eliminating command injection`) and switch inner-loop slices to zero-copy `std::string_view` / `std::span` (`verified by benchmarks`). [Skill 5.6: Suggest security improvements and performance optimizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/responsible-use-autofix-code-scanning)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **C:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **D:** Correct. Security and performance optimization (`5.6`) pairs Copilot/Autofix patches with profiler benchmarks and SAST re-scans.

### Question 88 — `A` (Configure privacy, content exclusions, and safeguards)

Correct answer: A (is correct). Adding `fnmatch` YAML globs in `Content exclusion`, allowing `<=30 min` (`or reloading IDE`) for sync, verifying the crossed-out Copilot icon + `copilot.content_exclusion_changed` audit log, and avoiding cross-file LSP hover leaks completes deployment. [Skill 6.1: Configure content exclusions and editor settings | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion)]

- **A:** Correct. Correct order: configure YAML `fnmatch` globs -> allow `<=30 min` IDE sync -> verify crossed-out icon & audit log -> mind IDE LSP type-hover nuance.
- **B:** Incorrect. Incorrect: Repository admins CANNOT override or remove Organization-level Content Exclusions (`rules combine additively`), and sync takes `<=30 minutes`.
- **C:** Incorrect. Incorrect: Content Exclusions require **Copilot Business or Enterprise**, use `fnmatch` globs, and govern Copilot context—not Git ACLs or Actions.
- **D:** Incorrect. Incorrect: `.gitignore` does not exclude already-tracked repository files from Copilot context.

### Question 89 — `C` (Configure privacy, content exclusions, and safeguards)

Correct answer: C (is correct). Updated Repository or Organization **Content Exclusions** propagate to connected IDE clients within **up to `30` minutes** (`or immediately on window reload / sign-in refresh`). [Skill 6.1: Configure content exclusions and editor settings | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion)]

- **A:** Incorrect. False: Copilot Content Exclusions apply strictly to **GitHub Copilot** features—they never restrict Git repository ACLs, Actions workflows, or `CodeQL` (`6.1`).
- **B:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **C:** Correct. Content Exclusion configuration (`6.1`) enforces additive Org + Repo `fnmatch` path exclusions across Business and Enterprise seats.
- **D:** Incorrect. Content Exclusions (`2.3`, `6.1`) are only enforced for seats governed under Copilot Business or Copilot Enterprise.

### Question 90 — `B` (Configure privacy, content exclusions, and safeguards)

Correct answer: B (is correct). No — Copilot Content Exclusions apply exclusively to **GitHub Copilot** context gathering; GitHub Actions workflows, `CodeQL` code scanning, Secret Scanning, and `git clone` continue reading the repository normally. [Skill 6.1: Configure content exclusions and editor settings | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion)]

- **A:** Incorrect. False: Copilot Content Exclusions apply strictly to **GitHub Copilot** features—they never restrict Git repository ACLs, Actions workflows, or `CodeQL` (`6.1`).
- **B:** Correct. Content Exclusion scope limits (`2.3`, `6.1`) distinguish Copilot prompt blocking from IDE LSP type inference, Git ACLs, and CI scanners.
- **C:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 91 — `C` (Configure privacy, content exclusions, and safeguards)

Correct answer: C (is correct). No — Repository administrators can only add **additional** repository exclusions; they cannot remove or weaken Organization-level Content Exclusions (`which remain enforced across matching org repos`). [Skill 6.1: Configure content exclusions and editor settings | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion)]

- **A:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **B:** Incorrect. The proposed GitHub Copilot configuration or workflow violates at least one stated governance, privacy, or technical requirement. No — Repository administrators can only add **additional** repository exclusions; they cannot remove or weaken Organization-level Content Exclusions (`which remain enforced across matching org repos`).
- **C:** Correct. Organization Content Exclusions (`6.1`, `6.4`) establish a floor that repository settings can only expand, never weaken.
- **D:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).

### Question 92 — `B` (Configure privacy, content exclusions, and safeguards)

Correct answer: B (is correct). No — IP Indemnity protects unmodified Copilot Business/Enterprise usage (`with Public code = Block`) against unintended third-party IP claims, and explicitly excludes intentional circumvention or deliberate reproduction of third-party IP. [Skill 6.2: Describe ownership and limitations of outputs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/about-github-copilot/plans-for-github-copilot)]

- **A:** Incorrect. Content Exclusions (`2.3`, `6.1`) are only enforced for seats governed under Copilot Business or Copilot Enterprise.
- **B:** Correct. Output ownership and IP Indemnity (`6.2`) require Business/Enterprise licensing with the public-code duplication filter enabled (`Block`).
- **C:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **D:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).

### Question 93 — `C` (Configure privacy, content exclusions, and safeguards)

Correct answer: C (is correct). Only **Copilot Business** and **Copilot Enterprise** (`with Suggestions matching public code set to Block`) include GitHub's contractual IP Indemnity protection; Individual plans do not. [Skill 6.2: Describe ownership and limitations of outputs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/about-github-copilot/plans-for-github-copilot)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **C:** Correct. Output ownership and IP Indemnity (`6.2`) require Business/Enterprise licensing with the public-code duplication filter enabled (`Block`).
- **D:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).

### Question 94 — `D` (Configure privacy, content exclusions, and safeguards)

Correct answer: D (is correct). No — on Copilot Business and Enterprise, code-snippet retention for foundational model training is **off at the platform/plan level** and cannot be turned on by individual developers. [Skill 6.2: Describe ownership and limitations of outputs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/about-github-copilot/plans-for-github-copilot)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **C:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **D:** Correct. Individual privacy settings (`3.1`, `6.1`) govern optional snippet training on personal plans (`whereas Business/Enterprise disable code-snippet training by default`).

### Question 95 — `D` (Configure privacy, content exclusions, and safeguards)

Correct answer: D (is correct). `No policy` at the Enterprise level delegates control to each child Organization, so `stratosflight`'s **`Block`** policy is enforced on all its seat holders. [Skill 6.3: Enable suggestions matching public code filtering | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/finding-public-code-that-matches-github-copilot-suggestions)]

- **A:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **B:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Correct. Public-code duplication filtering and Code Referencing (`6.3`) either block `~150+` char verbatim public matches or surface repo/license provenance.

### Question 96 — `D` (Configure privacy, content exclusions, and safeguards)

Correct answer: D (is correct). No — Code Referencing only triggers when public-code matches are **allowed** (`Allow`), which simultaneously **disqualifies** those suggestions from Copilot IP Indemnity; regulated orgs needing IP Indemnity must set **`Block`**. [Skill 6.3: Enable suggestions matching public code filtering | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/finding-public-code-that-matches-github-copilot-suggestions)]

- **A:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **B:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **C:** Incorrect. The proposed GitHub Copilot configuration or workflow violates at least one stated governance, privacy, or technical requirement. No — Code Referencing only triggers when public-code matches are **allowed** (`Allow`), which simultaneously **disqualifies** those suggestions from Copilot IP Indemnity; regulated orgs needing IP Indemnity must set **`Block`**.
- **D:** Correct. Enabling `Block` on public-code duplication (`6.2`, `6.3`) is a mandatory condition for GitHub Copilot IP Indemnity protection.

### Question 97 — `D, E` (Configure privacy, content exclusions, and safeguards)

Correct answers: D and E (are correct). The duplication filter compares completions of `~150+` characters against an index of public GitHub repositories, and keeping that filter set to **`Block`** on Business/Enterprise is required for IP Indemnity. [Skill 6.3: Enable suggestions matching public code filtering | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/finding-public-code-that-matches-github-copilot-suggestions)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Correct. Public-code duplication filtering and Code Referencing (`6.3`) either block `~150+` char verbatim public matches or surface repo/license provenance.
- **E:** Correct. Output ownership and IP Indemnity (`6.2`) require Business/Enterprise licensing with the public-code duplication filter enabled (`Block`).

### Question 98 — `A` (Configure privacy, content exclusions, and safeguards)

Correct answer: A (is correct). A Repository or Organization **Content Exclusion** glob (`such as - "**/*.yaml"`) matches `config.yaml`, intentionally disabling Copilot only on matching paths (`working as designed`). [Skill 6.4: Resolve issues with suggestions and content exclusions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot)]

- **A:** Correct. Troubleshooting Copilot (`6.4`) checks multi-org policy precedence (`most restrictive wins`), Content Exclusion icons, filetype settings, and proxy/TLS trust.
- **B:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).

### Question 99 — `D` (Configure privacy, content exclusions, and safeguards)

Correct answer: D (is correct). In VS Code user/workspace settings, `github.copilot.enable` maps language IDs (`e.g., {"*": true, "markdown": false, "plaintext": false}`) and disables inline ghost text for any language set to `false`. [Skill 6.4: Resolve issues with suggestions and content exclusions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot)]

- **A:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **B:** Incorrect. False: Copilot Content Exclusions apply strictly to **GitHub Copilot** features—they never restrict Git repository ACLs, Actions workflows, or `CodeQL` (`6.1`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Correct. Troubleshooting Copilot (`6.4`) checks multi-org policy precedence (`most restrictive wins`), Content Exclusion icons, filetype settings, and proxy/TLS trust.

### Question 100 — `B, C` (Configure privacy, content exclusions, and safeguards)

Correct answers: B and C (are correct). Engineer A's second org `acme-defense` has Chat set to `Disabled` (`most restrictive org policy wins`), and Engineer B's IDE lacks authenticated corporate proxy/TLS settings to reach `*.githubcopilot.com`. [Skill 6.4: Resolve issues with suggestions and content exclusions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot)]

- **A:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **B:** Correct. Multi-organization policy resolution (`2.13`, `6.4`) always applies the strictest safeguard across a user's active memberships.
- **C:** Correct. Troubleshooting Copilot (`6.4`) checks multi-org policy precedence (`most restrictive wins`), Content Exclusion icons, filetype settings, and proxy/TLS trust.
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **E:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
