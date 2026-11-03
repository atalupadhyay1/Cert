# Microsoft / GitHub Exam GH-300: GitHub Copilot — Full-Length Mock Exam 5

**Theme:** Developer Productivity, Legacy Modernization, Edge-Case Unit Testing & Security Autofix  
**Credential:** `GitHub Copilot` *(Intermediate · **no prerequisite** · **2-year validity** transitioning to Microsoft Learn recertification)*  
**Study guide baseline:** `August 7, 2026 (Last updated July 9, 2026)` (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300)  
**Questions:** `100` (`84` `multiple-choice` balanced `21/21/21/21` across A–D + `16` `multi-select`; `0` case studies)  
**Recommended timing:** `100 minutes` (matching Microsoft’s published `100-minute` GH-300 assessment duration · **closed-book: no Microsoft Learn or GitHub Docs access**)

> **Disclaimer:** Independent educational material authored from public Microsoft Learn and GitHub Copilot documentation — not affiliated with or endorsed by Microsoft Corporation or GitHub, Inc. Practice percentages do not equate to Microsoft’s `700 / 1000` scaled score.

## Questions

---

## Domain 1 — Use GitHub Copilot responsibly (15–20% official weight · 18 questions)

### 1. A .NET 9 naval-architecture engineer at ThalassaMarine uses GitHub Copilot to draft container-stowage metacentric height (`GM`) stability math in C#. Why must maritime domain engineers verify every hydrostatic formula regardless of clean `dotnet build` output?

- **A.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** Generative AI models predict statistically probable token sequences (`not proven correctness`), risking hallucinated APIs, outdated idioms, training-data bias, and subtle security bugs
- **D.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)

### 2. In `thalassa/edifact-baplie`, Copilot suggests `<PackageReference Include="Edifact.Baplie.NetCore" Version="3.1.0" />` inside a `.csproj` file. What check prevents **slopsquatting** before running `dotnet restore`?

- **A.** Verify every AI-suggested package name, publisher, and version in your trusted registry (`preventing slopsquatting / hallucinated dependency attacks`) before installing
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** Inspect **Audit Logs** (`category:copilot`, e.g., `copilot.cfb_seat_created`, `copilot.content_exclusion_changed`) for admin changes and `GET /orgs/{org}/copilot/metrics` (`>=5 active users`) for aggregated usage
- **D.** Use **GitHub Spark** to build, iterate on, and share AI-powered full-stack micro-apps (`with natural-language prompts, live preview, managed KV persistence, and optional GitHub repository sync`)

### 3. After rolling out Copilot across 80 C# developers, ThalassaMarine notices reviewers skimming 400-line customs-tariff PRs in under 60 seconds (`automation ____`). What engineering practice counteracts this human-factors risk?

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **C.** Install `@github/copilot` via `npm install -g @github/copilot` (`Node.js 22+`), `winget install GitHub.Copilot`, or Homebrew, launch `copilot` in your repo, run `/login`, and confirm folder trust
- **D.** Guard against **automation bias / complacency** (`over-trusting plausible-looking AI completions`) by reviewing edge cases, error paths, and security invariants manually

### 4. ThalassaMarine's maritime software safety standard lists core failure modes of generative AI coding assistants. Which two statements belong in that standard? Select two.

- **A.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** Generative AI models predict statistically probable token sequences (`not proven correctness`), risking hallucinated APIs, outdated idioms, training-data bias, and subtle security bugs
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **E.** Guard against **automation bias / complacency** (`over-trusting plausible-looking AI completions`) by reviewing edge cases, error paths, and security invariants manually

### 5. ThalassaMarine designs a berth-allocation optimizer with GitHub Copilot so vessels carrying perishable cold-chain medicine fail over safely during port sensor outages. Complete the Responsible AI principle focused on graceful degradation and verified bounds: `____ & Safety`.

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** Apply the six Responsible AI principles—**Fairness**, **Reliability & Safety**, **Privacy & Security**, **Inclusiveness**, **Transparency**, and **Accountability**
- **C.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **D.** Use `copilot -p "..."` for non-interactive runs (`-s` for clean stdout, `--output-format=json` for JSONL), `--available-tools` / `--deny-tool` for tool scoping, and `--fleet` for parallel subagents

### 6. During an IMO maritime software audit, inspectors ask who holds legal and engineering responsibility for C# customs-declaration logic generated with GitHub Copilot. Complete the principle: `____` (`human engineers & organization`).

- **A.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **B.** Maintain **Transparency** and **Accountability** by disclosing AI assistance per team norms, honoring open-source licenses, and ensuring humans own every committed line
- **C.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free

### 7. ThalassaMarine's port-terminal Blazor tablet app is used in bright sunlight by crane operators wearing gloves and by multilingual port clerks. Which Responsible AI principle guides high-contrast UI, large touch targets, screen-reader ARIA roles, and UTF-8 character support?

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **C.** Evaluate AI-generated UI copy, validation rules, and domain models for **Fairness** and **Inclusiveness** (`avoiding demographic stereotyping, exclusionary naming, or accessibility regressions`)
- **D.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions

### 8. ThalassaMarine's CTO publishes Responsible AI acceptance gates for port-terminal applications built with Copilot. Which three gates align with Microsoft and GitHub's framework? Select three.

- **A.** Require a human engineer to review, test, and approve every AI-assisted pull request—never delegating final merge accountability to an LLM
- **B.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **C.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **D.** Apply the six Responsible AI principles—**Fairness**, **Reliability & Safety**, **Privacy & Security**, **Inclusiveness**, **Transparency**, and **Accountability**
- **E.** Evaluate AI-generated UI copy, validation rules, and domain models for **Fairness** and **Inclusiveness** (`avoiding demographic stereotyping, exclusionary naming, or accessibility regressions`)
- **F.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review

### 9. In a legacy ASP.NET controller, Copilot suggests `BinaryFormatter.Deserialize(stream)` (`deprecated and vulnerable to remote code execution in .NET`). How should ThalassaMarine prevent insecure serialization patterns from entering commits?

- **A.** Mitigate AI harms (`historical dataset bias, weak crypto/SQL defaults, PII exposure, and insecure scaffolding`) using RAI filters, `CodeQL` SAST, secret scanning, and diverse test suites
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **D.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions

### 10. A ThalassaMarine developer uses an MCP connector to read external shipping-manifest emails inside Agent Mode, and one crafted email body instructs the agent to modify `nuget.config` to point at an external attacker feed. What is this attack?

- **A.** `#runSubagent` merges every raw intermediate grep output directly into the main chat's token window and pauses mid-search to interview the user after every file read
- **B.** Treat untrusted external content (`issues, PR bodies, web pages, third-party MCP tool outputs`) as **indirect prompt injection** risks and require human approval on tool actions
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`

### 11. ThalassaMarine processes crew passport manifests (`PII`) and customs EDI signing keys. Which two controls prevent sensitive data exposure during AI-assisted development? Select two.

- **A.** Never paste live customer PII, PHI, production database dumps, or active credentials/private keys into Copilot prompts or sample fixtures
- **B.** Enforce automated CI guardrails (`CodeQL` code scanning, Secret Scanning Push Protection, and Dependabot) on every branch containing AI-generated code
- **C.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **D.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **E.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions

### 12. A ThalassaMarine C# engineer uses GitHub Copilot to implement hazardous-cargo (`IMDG`) segregation rules. Place the Responsible AI verification steps in exact order before merging to `main`.

- **A.** Merge Copilot output directly to `main` → Run `CodeQL` weekly in production → Check package names only if builds fail → Skip human review when Copilot Code Review leaves zero comments
- **B.** Set public-code filtering to `Allow` → Paste live customer PII into Chat as sample fixtures → Run unit tests locally → Self-approve your own pull request
- **C.** Prompt Copilot with explicit security & type constraints → Review logic & verify suggested packages exist in trusted registries → Run unit/edge-case tests plus `CodeQL` & secret scanning → Complete human peer PR review before merging
- **D.** Approve an empty PR branch first → Disable `CodeQL` to speed up Copilot completions → Install unfamiliar suggested packages blindly from public registries → Deploy without unit tests

### 13. Copilot generates an async C# method calling `.Result` synchronously on `HttpClient.GetAsync(...)`, risking thread-pool starvation under peak vessel-arrival bursts. How do you catch concurrency anti-patterns that compile without errors?

- **A.** Treat Copilot as a **pair-programming assistant (`not an oracle`)**: review diffs line-by-line, execute unit/integration/edge-case tests, and scan with `CodeQL` and Dependabot
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **D.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases

### 14. Two ThalassaMarine engineers run the identical prompt `"Create C# customs tariff lookup"` on their laptops and receive slightly different `Dictionary` vs `FrozenDictionary` implementations. Which inherent LLM property explains this?

- **A.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Because LLM sampling is **stochastic (`non-deterministic`)**, identical prompts can yield varying implementations whose runtime behavior, complexity, and thread safety must be verified

### 15. ThalassaMarine's branch ruleset on `thalassa/vessel-traffic` requires `2` approving reviews before merging. Proposed solution: Enable Automatic Copilot Code Review expecting Copilot's review to count as `1` of the `2` required approvals so only `1` human engineer needs to approve. Does this meet the goal?

- **A.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements
- **B.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **C.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **D.** No — **Copilot Code Review** posts `Comment` reviews (`never Approve` reviews that satisfy required human branch-protection approver counts); a human reviewer must still approve

### 16. What end-to-end governance posture represents responsible **Copilot Business** operation across ThalassaMarine's `.NET` repositories?

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **C.** Operate Copilot responsibly by keeping `Suggestions matching public code = Block`, configuring Content Exclusions, omitting PII/secrets from prompts, and enforcing human PR review
- **D.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins

### 17. ThalassaMarine modernizes a legacy `.NET Framework 4.7.2` WCF freight calculator to `.NET 9` gRPC. Proposed solution: First build xUnit characterization tests using synthetic cargo fixtures (`zero real customer manifests`), then convert one service contract per VS Code Agent Mode session (`with #file:freight.proto`), run `dotnet test` + `CodeQL`, and require human PR approval. Does this meet the goal?

- **A.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements
- **B.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **C.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **D.** No — Copilot Chat **`Ask` mode** only answers questions and proposes snippets in chat; autonomous multi-file workspace edits with iterative terminal test execution require **Agent Mode** (`or Copilot CLI`)

### 18. In NuGet `nuget.config`, which NuGet feature (`paired with private upstream feeds and lockfiles packages.lock.json`) helps ThalassaMarine block untrusted public packages sharing internal namespace prefixes like `Thalassa.*`? (**Package Source `____`**)

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** Verify every AI-suggested package name, publisher, and version in your trusted registry (`preventing slopsquatting / hallucinated dependency attacks`) before installing
- **C.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **D.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins

---

## Domain 2 — Use GitHub Copilot features (25–30% official weight · 28 questions)

### 19. ThalassaMarine C# developers use **Visual Studio 2022 (`17.10+`)**, **VS Code (`C# Dev Kit`)**, and **JetBrains Rider**. In modern Visual Studio 2022 (`17.10+`), how are GitHub Copilot completions and Copilot Chat packaged?

- **A.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **B.** Install the official GitHub Copilot extension in a supported IDE (`VS Code, Visual Studio, JetBrains, Xcode, Eclipse, or Neovim`), sign in via GitHub OAuth, and verify an active seat
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Inspect **Audit Logs** (`category:copilot`, e.g., `copilot.cfb_seat_created`, `copilot.content_exclusion_changed`) for admin changes and `GET /orgs/{org}/copilot/metrics` (`>=5 active users`) for aggregated usage

### 20. A maritime university student contributor exploring open-source AIS parsers has **GitHub Copilot Free** (`no paid subscription`). What usage boundary applies to **Copilot Free** compared with paid plans?

- **A.** No — Repository and Organization **Content Exclusions** require **Copilot Business or Copilot Enterprise**; personal Copilot Free/Pro/Pro+ plans do not support Org Content Exclusions
- **B.** Choose **Copilot Business** (`Org policies, Content Exclusions, IP Indemnity, zero model training`) or **Copilot Enterprise** (`adds GHEC Copilot Spaces/Knowledge Bases & org-wide GitHub.com grounding`)
- **C.** Choose **Copilot Free** for capped monthly completions/chats or **Copilot Pro / Pro+** for individual developers needing unlimited completions, higher premium-model quotas, and **GitHub Spark**
- **D.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models

### 21. A C# engineer renames property ` GrossTons` to `GrossMetricTonnes` on `VesselSummaryDto.cs`, and VS Code immediately highlights the next two mapping lines in the file offering `Tab`-to-jump-and-apply updates. Complete the feature name: **Next `____` Suggestions (`NES`)**.

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** Use **Inline ghost-text completions** (`Tab` to accept, `Alt+]` / `Option+]` to cycle) and **Next Edit Suggestions (`NES`)** to predict subsequent ripple edits across nearby lines
- **C.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **D.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke

### 22. ThalassaMarine developers match Copilot interfaces to daily `.NET` workflows. Which two pairings are accurate? Select two.

- **A.** Match interaction surfaces to scope: **Inline Chat (`Ctrl+I` / `Cmd+I`)** for in-place file edits, **Chat `Ask`** for Q&A, **Copilot Edits** for multi-file working sets, and **Agent Mode / CLI** for autonomous loops
- **B.** GitHub Copilot CLI (`copilot`) is a terminal-native AI coding agent that understands shell context, edits files, executes commands with approval prompts, and automates multi-step repo workflows
- **C.** No — Copilot Chat **`Ask` mode** only answers questions and proposes snippets in chat; autonomous multi-file workspace edits with iterative terminal test execution require **Agent Mode** (`or Copilot CLI`)
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **E.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke

### 23. In `thalassa/port-customs`, an admin configures Repository Content Exclusion `- "/Customs/TariffKeys/*.pfx"` and `- "/Customs/BilateralRates.json"`. Within at most how many minutes (`<= ____ minutes`) do connected IDEs enforce updated Content Exclusion rules?

- **A.** Configure Repository or Organization **Content Exclusions** (`Settings -> Copilot -> Content exclusion`) so IDEs omit matched sensitive files across completions, Chat, and code review
- **B.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **C.** No — `.gitignore` only prevents untracked files from being staged by Git; excluding tracked repository files from Copilot requires **Copilot Content Exclusions** (`Settings -> Copilot -> Content exclusion`)
- **D.** Configuring Copilot Content Exclusions also blocks `git clone`, GitHub Actions runners, and `CodeQL` security scans from reading the excluded files

### 24. When a C# developer opens `Customs/BilateralRates.json` (`matched by Content Exclusions`) in Visual Studio or VS Code, how does the IDE visually confirm that Copilot is blocked on that tab?

- **A.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** Configuring Copilot Content Exclusions also blocks `git clone`, GitHub Actions runners, and `CodeQL` security scans from reading the excluded files
- **D.** Configure Repository or Organization **Content Exclusions** (`Settings -> Copilot -> Content exclusion`) so IDEs omit matched sensitive files across completions, Chat, and code review

### 25. ThalassaMarine operates headless Linux container hosts in Rotterdam port data centers (`SSH-only, no GUI IDE`). Why does **GitHub Copilot CLI (`copilot`)** fit these engineers directly?

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **C.** GitHub Copilot CLI (`copilot`) is a terminal-native AI coding agent that understands shell context, edits files, executes commands with approval prompts, and automates multi-step repo workflows
- **D.** Inspect **Audit Logs** (`category:copilot`, e.g., `copilot.cfb_seat_created`, `copilot.content_exclusion_changed`) for admin changes and `GET /orgs/{org}/copilot/metrics` (`>=5 active users`) for aggregated usage

### 26. A ThalassaMarine Windows DevOps engineer installs **GitHub Copilot CLI** (`via WinGet or npm on Node 22+`) and launches it inside `C:\src\vessel-scheduler`. Place the onboarding steps in order.

- **A.** Run `/login` in raw Bash before installing `@github/copilot` → Pass `--allow-all` on `/` root filesystem → Write plaintext passwords into `~/.copilot/config.json` → Downgrade to Node.js `14`
- **B.** Install `@github/copilot` → Delete `~/.copilot/session-store.db` before signing in → Disable the Organization Copilot CLI policy → Run `copilot -p` unauthenticated
- **C.** Clone the repo inside `~/.copilot/logs/` → Set `Suggestions matching public code` to `Allow` → Run `gh auth logout` → Expect silent file edits without permission prompts
- **D.** Install Node.js `22+` (or WinGet/Homebrew) & `npm install -g @github/copilot` → `cd` into the project directory & launch `copilot` → Enter `/login` to complete GitHub OAuth authentication → Confirm directory trust & verify `/permissions show`

### 27. If a developer installs `@github/copilot` via `npm` on a machine running legacy **Node.js 18**, why does installation/startup fail, and which minimum Node.js version is required? (`Node.js ____+`)

- **A.** Install `@github/copilot` via `npm install -g @github/copilot` (`Node.js 22+`), `winget install GitHub.Copilot`, or Homebrew, launch `copilot` in your repo, run `/login`, and confirm folder trust
- **B.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **C.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 28. A ThalassaMarine build script runs `copilot -p "List nullable reference warnings in Directory.Build.props" -s --output-format=____` so downstream `jq` parsing receives structured newline-delimited JSON events without spinner chrome. Complete the format value.

- **A.** Use `copilot -p "..."` for non-interactive runs (`-s` for clean stdout, `--output-format=json` for JSONL), `--available-tools` / `--deny-tool` for tool scoping, and `--fleet` for parallel subagents
- **B.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`

### 29. A ThalassaMarine engineer uses interactive slash commands and CLI flags to switch models and reset tool approvals mid-session. Which two commands work as documented in **GitHub Copilot CLI**? Select two.

- **A.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **B.** Use `copilot -p "..."` for non-interactive runs (`-s` for clean stdout, `--output-format=json` for JSONL), `--available-tools` / `--deny-tool` for tool scoping, and `--fleet` for parallel subagents
- **C.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **D.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **E.** Inside interactive Copilot CLI, use `/permissions show` or `/permissions manual` to inspect/set approval mode, `--model` to pin a model, and `~/.copilot/settings.json` for user preferences

### 30. A developer SSHes back into their jump host after lunch and wants to immediately reopen **only the single most recently closed** local Copilot CLI session without picking from an interactive picker list. Complete the CLI flag: `copilot --____`.

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** Use Copilot CLI **infinite sessions** (auto-compaction under `~/.copilot/session-state/{id}/`), inspect `/session plan`, `/session checkpoints`, and `/session files`, and resume via `--resume` or `--continue`
- **C.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **D.** `#runSubagent` merges every raw intermediate grep output directly into the main chat's token window and pauses mid-search to interview the user after every file read

### 31. Inside an interactive `copilot` CLI session, a developer divides a 12-project `.NET` solution upgrade into independent sub-tasks that can execute in parallel across subagents. Complete the interactive slash command: `/____`.

- **A.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **B.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **C.** Use Copilot CLI **infinite sessions** (auto-compaction under `~/.copilot/session-state/{id}/`), inspect `/session plan`, `/session checkpoints`, and `/session files`, and resume via `--resume` or `--continue`
- **D.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`

### 32. ThalassaMarine stores shared `.proto` contracts in `../shared-protos` (`one directory above ./vessel-api`). When running `copilot` inside `./vessel-api`, which CLI flag grants file-access permission to `../shared-protos` without running `--allow-all-paths`? (`--add-____`)

- **A.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **B.** Configuring Copilot Content Exclusions also blocks `git clone`, GitHub Actions runners, and `CodeQL` security scans from reading the excluded files
- **C.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **D.** Generate scripts and edit files safely in Copilot CLI via interactive **permission prompts** (`write`, `commands`), `--add-dir` for extra paths, `--secret-env-vars` redaction, and `--share` / `--share-gist`

### 33. Where on disk does **GitHub Copilot CLI** store its cross-session searchable **SQLite database** (`allowing Copilot CLI to search across past local sessions`)? (`~/.copilot/____.db`)

- **A.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **B.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **C.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **D.** Generate scripts and edit files safely in Copilot CLI via interactive **permission prompts** (`write`, `commands`), `--add-dir` for extra paths, `--secret-env-vars` redaction, and `--share` / `--share-gist`

### 34. A ThalassaMarine C# lead configures a SQL Server schema **MCP** server in `.vscode/mcp.json` and uses **`#runSubagent`** to inventory 50 legacy stored procedures before Agent Mode scaffolds EF Core 9 repositories. Order the steps.

- **A.** Define MCP servers inside `.git/HEAD` → Run `/clear` after every single edit so Agent Mode loses its plan → Skip working-set diff inspection → Force-push to `main`
- **B.** Register the MCP server in `.vscode/mcp.json` & verify tools → Delegate broad codebase search to isolated `#runSubagent` → Apply multi-file edits & run terminal tests in Agent Mode → Inspect working-set diffs & `Keep` verified changes
- **C.** Commit plaintext MCP API keys to `.github/copilot-instructions.md` → Expect `#runSubagent` to pause mid-run for interactive Q&A → Disable all workspace tools → Auto-push unreviewed edits to `main`
- **D.** Accept (`Keep`) all generated edits before running tests → Add `.vscode/mcp.json` after closing VS Code → Attach 80 unrelated files to main chat → Switch to `Ask` mode expecting autonomous test loops

### 35. When ThalassaMarine assigns GitHub Issue `#519` (`"Add UN/LOCODE port-code checksum validator + xUnit tests"`) to **`@copilot`** on GitHub.com, where does the **Copilot coding agent** build and run `dotnet test`, and how does it deliver its work?

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **C.** No — Copilot Chat **`Ask` mode** only answers questions and proposes snippets in chat; autonomous multi-file workspace edits with iterative terminal test execution require **Agent Mode** (`or Copilot CLI`)
- **D.** Assign a GitHub Issue or PR comment (`@copilot`) to the **Copilot coding agent (`cloud agent`)**, which runs in an ephemeral Actions sandbox, pushes to `copilot/*`, and opens a draft PR for human review

### 36. ThalassaMarine compares **Copilot Edits (`Edit` mode)**, **Agent Mode + `#runSubagent`**, and the **Copilot cloud coding agent**. Which three statements accurately distinguish them? Select three.

- **A.** Assign a GitHub Issue or PR comment (`@copilot`) to the **Copilot coding agent (`cloud agent`)**, which runs in an ephemeral Actions sandbox, pushes to `copilot/*`, and opens a draft PR for human review
- **B.** Use **Agent Mode** with `.vscode/mcp.json` **Model Context Protocol (`MCP`)** servers to query external tools, edit multiple files, read compiler/terminal diagnostics, and self-heal until tests pass
- **C.** No — Copilot Chat **`Ask` mode** only answers questions and proposes snippets in chat; autonomous multi-file workspace edits with iterative terminal test execution require **Agent Mode** (`or Copilot CLI`)
- **D.** `#runSubagent` merges every raw intermediate grep output directly into the main chat's token window and pauses mid-search to interview the user after every file read
- **E.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **F.** Invoke `#runSubagent` in VS Code Agent Mode so multi-file exploration runs in an isolated context window and returns only a concise summary to main chat

### 37. After a ThalassaMarine developer pushes 3 follow-up commits addressing feedback on an open pull request, Copilot Code Review automatically reviews the newly pushed commits as well. Which ruleset sub-option controls that behavior? (`Review new ____`)

- **A.** Run **Copilot Code Review** locally on uncommitted IDE diffs or on GitHub.com PRs (`with Automatic Copilot code review, Review new pushes, and Review draft pull requests`), paired with human approval
- **B.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **C.** No — **Copilot Code Review** posts `Comment` reviews (`never Approve` reviews that satisfy required human branch-protection approver counts); a human reviewer must still approve
- **D.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review

### 38. In VS Code (`GitHub Pull Requests / Source Control view`), can a developer run a **Copilot Code Review on uncommitted staged/unstaged local changes** BEFORE even pushing a branch to GitHub.com?

- **A.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **B.** Run **Copilot Code Review** locally on uncommitted IDE diffs or on GitHub.com PRs (`with Automatic Copilot code review, Review new pushes, and Review draft pull requests`), paired with human approval
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)

### 39. ThalassaMarine wants automatic **Copilot Code Review** on every PR in `thalassa/*`, enforcing EF Core migration safety rules on `src/Migrations/**/*.cs` (`and db/**/*.sql`) while preserving human approvals. Order the four steps.

- **A.** Save rules in `/tmp/review.txt` without `applyTo:` frontmatter → Block Copilot Code Review in Enterprise `AI controls` → Open a draft PR with draft reviews disabled → Expect automatic Copilot comments
- **B.** Commit a 500-page binary `.pdf` in `.github/prompts/` → Disable repository custom instructions in Settings → Trigger inline Tab completion → Expect PRs to auto-merge
- **C.** Add `.github/instructions/sql.instructions.md` (`applyTo: "db/**/*.sql"`) → Merge SQL rules to the default branch → Enable `Automatically request Copilot code review` in an Org Ruleset → Resolve Copilot comments alongside human PR approval
- **D.** Set `excludeAgent: "code-review"` in `sql.instructions.md` → Expect Copilot Code Review to apply that file anyway → Remove human approvers so Copilot unlocks merges → Leave the instructions file untracked

### 40. ThalassaMarine's EDIFACT integration guild curates 5 repositories (`thalassa/edifact-core`, `baplie-parser`, `cuscar-api`, `port-codes`, `adr-docs`) plus custom instructions into a single shared workspace on GitHub.com so every squad gets grounded cross-repo answers. Complete the feature name: **Copilot `____`**.

- **A.** Use **GitHub Spark** to build, iterate on, and share AI-powered full-stack micro-apps (`with natural-language prompts, live preview, managed KV persistence, and optional GitHub repository sync`)
- **B.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **C.** Curate **Copilot Spaces** on GitHub.com (`grouping specific repositories, files, PRs, issues, free-text notes, and custom instructions`) to ground team Q&A and IDE MCP queries on authoritative org context
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 41. ThalassaMarine maintains `.github/copilot-instructions.md` and three `.github/instructions/*.instructions.md` files in `thalassa/vessel-api`. Which two configuration details govern how GitHub.com applies them? Select two.

- **A.** Generate **Copilot Pull Request Summaries** on GitHub.com and enforce coding/review standards via `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` (`applyTo:`, `excludeAgent:`), and `AGENTS.md`
- **B.** No — setting `excludeAgent: "code-review"` in `.instructions.md` frontmatter explicitly **prevents** Copilot Code Review from using that file (`use applyTo: without excluding code-review`)
- **C.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **D.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **E.** Create modular `.github/instructions/*.instructions.md` files with YAML frontmatter `applyTo:` globs (`and optional excludeAgent: "code-review" | "cloud-agent"`) for path-specific standards

### 42. After Copilot Chat outputs an unhelpful suggestion that hallucinated a removed EF Core 6 method, how can a ThalassaMarine developer submit structured quality feedback directly from the Chat UI (`without sharing secrets`)?

- **A.** Scope Copilot Chat with participants (`@workspace`, `@github`, `@vscode`, `@terminal`), slash commands (`/explain`, `/fix`, `/tests`, `/doc`, `/new`, `/clear`), `#file:`/`#codebase` variables, and thumbs feedback
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **D.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke

### 43. ThalassaMarine commits `.github/prompts/modernize-wcf.prompt.md` (`with agent: 'agent'` in YAML frontmatter) for `.NET 9` migrations. Which two capabilities do `.prompt.md` files provide? Select two.

- **A.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **B.** Store reusable `.github/prompts/*.prompt.md` templates (`enabled via "chat.promptFiles": true`) with `agent`, `model`, and `tools` frontmatter for on-demand `/prompt-name` invocation
- **C.** Enable `"chat.promptFiles": true` and commit reusable `.github/prompts/*.prompt.md` files (`YAML frontmatter: description, agent, model, tools` + Markdown `#file:` links) invoked via `/prompt-name`
- **D.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **E.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically

### 44. In Organization `thalassa`, public contributors occasionally open pull requests on an open-source AIS SDK repo (`thalassa/ais-dotnet`), and admins want to prevent external non-seat contributors from consuming `thalassa`'s premium Copilot Code Review quota. Which Org Copilot setting enforces this?

- **A.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **B.** No — Repository and Organization **Content Exclusions** require **Copilot Business or Copilot Enterprise**; personal Copilot Free/Pro/Pro+ plans do not support Org Content Exclusions
- **C.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **D.** Enforce Enterprise/Org Copilot policies (`Enabled`, `Disabled`, `No policy`), Branch Ruleset automatic Copilot Code Review (`authorized users only`), and Enterprise `AI controls -> Agents` repo-wide blocks

### 45. ThalassaMarine's compliance officer exports Organization Audit Logs (`category:copilot`) before an external maritime cyber-audit. Which three event types appear in that audit log stream?

- **A.** No — `GET /orgs/{org}/copilot/metrics` returns **aggregated, anonymized** team/org usage (`requiring >=5 active users`), NOT per-developer `last_activity_at` usernames; query `GET /orgs/{org}/copilot/billing/seats`
- **B.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **C.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **D.** Inspect **Audit Logs** (`category:copilot`, e.g., `copilot.cfb_seat_created`, `copilot.content_exclusion_changed`) for admin changes and `GET /orgs/{org}/copilot/metrics` (`>=5 active users`) for aggregated usage

### 46. Complete the GitHub REST API endpoint used to list all currently assigned **Copilot Business/Enterprise** seats (`including assignee login, assigning_team, and last_activity_at` + `last_activity_editor`) for organization `thalassa`: `GET /orgs/thalassa/copilot/____/seats`.

- **A.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **B.** No — `GET /orgs/{org}/copilot/metrics` returns **aggregated, anonymized** team/org usage (`requiring >=5 active users`), NOT per-developer `last_activity_at` usernames; query `GET /orgs/{org}/copilot/billing/seats`
- **C.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **D.** Choose **Copilot Free** for capped monthly completions/chats or **Copilot Pro / Pro+** for individual developers needing unlimited completions, higher premium-model quotas, and **GitHub Spark**

---

## Domain 3 — Understand GitHub Copilot data and architecture (10–15% official weight · 14 questions)

### 47. Under **GitHub Copilot Business**, are C# code completions or Visual Studio Chat prompts from `thalassa/vessel-scheduler` ever added to the training corpus of future foundation models?

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** On **Copilot Business & Enterprise**, prompts and completions travel over `TLS 1.2+`, process ephemerally in memory for inline completions, and are **never retained to train foundational models**
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models

### 48. ThalassaMarine's VP of Engineering inspects the Copilot Metrics dashboard showing `C#: 34% acceptance rate, SQL: 41% acceptance rate` across 75 active Visual Studio/VS Code seats. Which data stream populates those acceptance percentages?

- **A.** Distinguish **user engagement telemetry** (`acceptance/dismissal counts, latency, IDE version, encrypted at rest`) from **source-code prompts/suggestions** (`discarded after inline inference on Business/Enterprise`)
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **D.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models

### 49. When a developer invokes the **Copilot cloud coding agent** on GitHub.com (`assigning an issue to @copilot`), where does repository checkout and `dotnet test` execution happen?

- **A.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **B.** On **Copilot Business & Enterprise**, prompts and completions travel over `TLS 1.2+`, process ephemerally in memory for inline completions, and are **never retained to train foundational models**
- **C.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **D.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins

### 50. In `StowagePlanner.cs`, lines 1–40 declare `ContainerBay` and `ReeferPlug`, line 45 has the cursor inside `AssignReeferSlot(...)`, and lines 60–85 return `Result<SlotAllocation, StowageError>`. How does **FIM** leverage lines 60–85?

- **A.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** The IDE extension constructs prompts from **Fill-in-the-Middle (`FIM`)** cursor prefix + suffix, language/filepath metadata, Jacobi/Jaccard-ranked snippets from open tabs, and custom instructions
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 51. Why does `@workspace` (`or #codebase`) retrieve top-ranked chunks via **RAG** rather than concatenating all 1,800 `.cs` files of `thalassa/port-erp` into every Chat request?

- **A.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **B.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** For `@workspace` and GitHub.com repository chat, Copilot uses **lexical and semantic (`embedding`) retrieval (`RAG`)** to inject top-ranked code chunks into the prompt rather than sending entire gigabyte repos

### 52. ThalassaMarine's `.NET` architects review how Copilot gathers context locally versus across workspace searches. Which two statements are accurate? Select two.

- **A.** Include both code **before** the cursor (`prefix`) and code **after** the cursor (`suffix`) via Fill-in-the-Middle (`FIM`) alongside matching open-tab symbols
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** For `@workspace` and GitHub.com repository chat, Copilot uses **lexical and semantic (`embedding`) retrieval (`RAG`)** to inject top-ranked code chunks into the prompt rather than sending entire gigabyte repos
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **E.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models

### 53. Why does the GitHub Copilot cloud proxy apply **syntactic stop-sequence / block-boundary trimming** to inline completion tokens before sending ghost text to Visual Studio?

- **A.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **B.** The Copilot **cloud proxy** validates entitlement tokens, applies inbound/outbound **RAI safety filters** (`hate speech, violence, sexual content, PII, prompt injection`), and runs the `~150-char` public-code filter
- **C.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 54. At which exact point in the inline suggestion pipeline does the **`~150-character` public-code duplication filter** execute?

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** GitHub Copilot CLI requires Python 2.7, executes every `rm -rf` and file write silently without permission prompts by default, and stores plaintext passwords in `~/.copilot/config.json`
- **C.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **D.** The Copilot **cloud proxy** validates entitlement tokens, applies inbound/outbound **RAI safety filters** (`hate speech, violence, sexual content, PII, prompt injection`), and runs the `~150-char` public-code filter

### 55. Which two server-side safeguards run in the **GitHub Copilot cloud proxy** on every Business/Enterprise completion request? Select two.

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **C.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **D.** The Copilot **cloud proxy** validates entitlement tokens, applies inbound/outbound **RAI safety filters** (`hate speech, violence, sexual content, PII, prompt injection`), and runs the `~150-char` public-code filter
- **E.** Pass generated tokens through cloud-proxy Responsible AI toxicity/harm classifiers and the `~150-character` public-code duplication filter before IDE rendering

### 56. Order the end-to-end **inline code suggestion lifecycle** when a ThalassaMarine developer edits `BerthAllocator.cs` in Visual Studio 2022 under Copilot Business.

- **A.** IDE gathers FIM prefix/suffix & open tabs (minus exclusions) → Client sends `TLS 1.2+` prompt to proxy & checks seat token → Proxy runs RAI filters, LLM & `~150+` char duplication check → IDE renders ghost text & Business skips model training
- **B.** IDE uploads your entire disk (`~/.ssh` & closed repos) over HTTP → Cloud GPUs execute your local unit tests → Copilot commits directly to `main` without ghost text → Copilot Business trains shared base LLMs on your prompt
- **C.** IDE bypasses Organization Content Exclusions → Forwards raw files to unauthenticated endpoints → Skips toxicity & prompt-injection filters → Publishes prompts to public GitHub Gists
- **D.** Public-code duplication filter runs offline with network unplugged → LLM generates code before receiving file language or cursor prefix → IDE validates seat tokens once per decade → Proxy disables TLS encryption

### 57. Why does the Copilot IDE extension wait a brief **typing debounce interval** (`~tens of milliseconds`) when a developer is typing rapidly before dispatching an inline completion request?

- **A.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **B.** Suggestion lifecycle: typing debounce -> IDE FIM/tab context assembly -> `TLS` request to Copilot proxy -> RAI pre-filter & LLM generation -> post-filter & duplication check -> ghost-text render -> telemetry
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free

### 58. A ThalassaMarine developer asks Copilot Chat (`without MCP/web access`) `"What breaking API change was merged into our private sibling repo thalassa/customs-gateway 10 minutes ago?"` Why cannot local IDE Chat answer from thin air?

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **C.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **D.** Account for LLM & Copilot architectural limits: **finite context windows**, **pre-training knowledge cutoffs**, **stochastic sampling**, **no runtime execution** during inline completion, and unseen unindexed external systems

### 59. In a `.NET 9` project targeting preview C# 13 features (`params ReadOnlySpan<T>`), Copilot occasionally suggests older `params T[]` syntax unless guided. What explains this?

- **A.** Account for LLM & Copilot architectural limits: **finite context windows**, **pre-training knowledge cutoffs**, **stochastic sampling**, **no runtime execution** during inline completion, and unseen unindexed external systems
- **B.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **C.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **D.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review

### 60. Can an LLM inline completion alone verify whether two concurrent SQL Server transactions in `BerthBookingService.cs` can deadlock under `RepeatableRead` isolation?

- **A.** Account for LLM & Copilot architectural limits: **finite context windows**, **pre-training knowledge cutoffs**, **stochastic sampling**, **no runtime execution** during inline completion, and unseen unindexed external systems
- **B.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free

---

## Domain 4 — Apply prompt engineering and context crafting (10–15% official weight · 13 questions)

### 61. Compare `"Fix parser"` with `"In #file:ImoNumberValidator.cs (.NET 9), implement TryValidateImo(ReadOnlySpan<char> input, out int imo) verifying 'IMO' prefix + 7 digits where check digit equals sum(d_i * (8-i)) mod 10; zero heap allocations."` Why does the second prompt succeed immediately?

- **A.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **B.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **C.** Structure effective prompts with **Role/Goal**, **Grounded Context** (`#file`, `#selection`, versions), **Explicit Constraints** (`security, error handling, edge cases`), and **Output Format** (`types, signatures`)
- **D.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically

### 62. In C#, why does enabling `<Nullable>enable</Nullable>` and writing `public async Task<VesselBerth?> FindAvailableBerthAsync(LengthMeters loa, DraftMeters draft, CancellationToken ct)` dramatically improve inline completions?

- **A.** Guide inline completions directly inside source files using **top-of-file architecture comments**, **explicit parameter/return type annotations**, and **domain-specific function/variable names**
- **B.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **C.** Inspect **Audit Logs** (`category:copilot`, e.g., `copilot.cfb_seat_created`, `copilot.content_exclusion_changed`) for admin changes and `GET /orgs/{org}/copilot/metrics` (`>=5 active users`) for aggregated usage
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 63. In VS Code Copilot Chat, a C# engineer wants to reference a specific interface symbol `ICustomsClearancePolicy` directly without attaching the entire 900-line file containing six other interfaces. Complete the context reference prefix: `#____:ICustomsClearancePolicy` (`or #symbol`).

- **A.** Curate Copilot's active context: open target interface/DTO tabs (`closing unrelated files`), attach `#file:`, `#selection`, `#sym:`, or **Copilot Spaces**, and scope `.instructions.md` with `applyTo:` globs
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **D.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models

### 64. ThalassaMarine stores C# conventions in `.github/instructions/dotnet.instructions.md` (`applyTo: "**/*.cs"`) and Blazor UI rules in `.github/instructions/blazor.instructions.md` (`applyTo: "**/*.razor"`). Which instruction file(s) load when editing `Components/BerthGrid.razor`?

- **A.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **B.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **C.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **D.** Curate Copilot's active context: open target interface/DTO tabs (`closing unrelated files`), attach `#file:`, `#selection`, `#sym:`, or **Copilot Spaces**, and scope `.instructions.md` with `applyTo:` globs

### 65. Before modernizing `LegacyEdifactReader.cs` into `BaplieSpanParser.cs`, which two IDE context-hygiene steps give Copilot the cleanest signal? Select two.

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **C.** Close unrelated editor tabs and open the exact target interfaces/DTOs (`or pin them via #file:`) so neighbor-tab ranking injects clean, relevant types
- **D.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **E.** Curate Copilot's active context: open target interface/DTO tabs (`closing unrelated files`), attach `#file:`, `#selection`, `#sym:`, or **Copilot Spaces**, and scope `.instructions.md` with `applyTo:` globs

### 66. ThalassaMarine converts raw UN/EDIFACT `LOC+9+NLRTM:139:6'` segments into C# `PortCallLocation("Port of Load", "NLRTM")` records across 18 qualifier codes (`9, 11, 61, 88...`). Which prompting technique prevents Copilot from misformatting segment delimiters?

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **C.** Use **zero-shot prompting** for standard algorithms/APIs, and **few-shot prompting** (`1–3 concrete input -> output examples`) when teaching proprietary schemas, custom DSLs, or bespoke test conventions
- **D.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions

### 67. When asking Copilot Chat `"Convert this C# switch statement into a C# switch expression"` on a 12-line `#selection`, why is **zero-shot prompting** ideal?

- **A.** Use **zero-shot prompting** for standard algorithms/APIs, and **few-shot prompting** (`1–3 concrete input -> output examples`) when teaching proprietary schemas, custom DSLs, or bespoke test conventions
- **B.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **C.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **D.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)

### 68. ThalassaMarine needs to replace a 2,400-line legacy `SqlConnection` / `DataTable` class `PortInvoiceDal.cs` with EF Core 9 + Dapper read queries. What iterative prompt workflow avoids truncated or broken code?

- **A.** Decompose complex epics into small, testable steps, state exact framework/SDK versions (`preventing pre-cutoff API drift`), and iterate in follow-up turns using compiler or test output
- **B.** No — keeping dozens of unrelated tabs open and reusing one marathon chat thread across unrelated tasks causes **context pollution and token truncation**; close stale tabs and use `/clear` or `#runSubagent`
- **C.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **D.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free

### 69. Why does stating positive target constraints (`"Return ProblemDetails RFC 9457 via TypedResults.ValidationProblem; use FluentValidation"`) outperform vague complaints (`"Don't write messy error handling"`)?

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** Decompose complex epics into small, testable steps, state exact framework/SDK versions (`preventing pre-cutoff API drift`), and iterate in follow-up turns using compiler or test output
- **D.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases

### 70. ThalassaMarine creates `.github/prompts/xunit-characterization.prompt.md` so every squad locks legacy `.NET Framework` behavior identically before refactoring to `.NET 9`. Order the four workflow steps.

- **A.** Embed production PATs inside `.github/prompts/deploy.prompt.md` → Publish private prompts to public npm → Send one-word `'fix'` with zero file context → Skip code review
- **B.** Place prompt templates in `.github/workflows/prompt.yml` expecting `/prompt` in Chat → Keep 45 unrelated legacy files open in tabs → Reuse one 200-turn chat thread across 12 services → Omit output types and error rules
- **C.** Save `prompt.txt` outside the workspace → Add `applyTo: "false"` so nothing matches → Type `@terminal` expecting inline ghost text in closed files → Commit unreviewed output
- **D.** Set `"chat.promptFiles": true` & add `.github/prompts/api.prompt.md` → Link exemplars (`#file:`) & commit to Git → Close unrelated tabs & invoke `/api` in Chat with inputs → Run `/clear` (or open a new chat) before switching topics

### 71. When authoring `.github/prompts/grpc-service.prompt.md`, why should the prompt link `#file:src/Protos/common.proto` rather than copying and pasting 200 lines of `.proto` definitions inline into the `.prompt.md` body?

- **A.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **B.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **C.** Write **positive, specific constraints** (`'use parameterized pg queries with $1 parameters'`) rather than vague negations, ground domain rules via `#file:`, and codify standards in `.prompt.md` / `.instructions.md`
- **D.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically

### 72. During a long Copilot CLI session, context approaches the model's window limit and Copilot CLI creates automatic compaction checkpoints. Complete the slash command to inspect compaction checkpoints: `/session ____ [NUMBER]`.

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** Copilot Chat appends prior turns from the active thread up to its **token context limit**; run `/clear` (or open a new chat) on topic switches and use `#runSubagent` to keep noisy exploration out of history
- **C.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **D.** `#runSubagent` merges every raw intermediate grep output directly into the main chat's token window and pauses mid-search to interview the user after every file read

### 73. ThalassaMarine's `.NET` guild documents chat-history hygiene for Visual Studio and VS Code engineers. Which two habits prevent context dilution and wasted tokens? Select two.

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** Copilot Chat appends prior turns from the active thread up to its **token context limit**; run `/clear` (or open a new chat) on topic switches and use `#runSubagent` to keep noisy exploration out of history
- **C.** Run `/clear` or start a new Chat session when pivoting to an unrelated module so stale conversation turns do not consume token budget or bias new answers
- **D.** No — keeping dozens of unrelated tabs open and reusing one marathon chat thread across unrelated tasks causes **context pollution and token truncation**; close stale tabs and use `/clear` or `#runSubagent`
- **E.** `#runSubagent` merges every raw intermediate grep output directly into the main chat's token window and pauses mid-search to interview the user after every file read

---

## Domain 5 — Improve developer productivity with GitHub Copilot (10–15% official weight · 14 questions)

### 74. ThalassaMarine publishes NuGet SDK `Thalassa.Edifact.Abstractions` (`with <GenerateDocumentationFile>true</GenerateDocumentationFile>`) and needs accurate `/// <summary>`, `<param>`, and `<exception>` XML doc comments across 35 public interfaces. How can Copilot accelerate this?

- **A.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** Use `Inline Chat`, `Copilot Edits`, **Next Edit Suggestions**, and `/doc` to scaffold repetitive DTOs/validators, extract pure functions to reduce cyclomatic complexity, and generate JSDoc/OpenAPI/Mermaid docs
- **D.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically

### 75. A legacy C# class `VesselManifestProcessor` instantiates `new SmtpClient()`, `new SqlConnection()`, and `DateTime.Now` directly inside business methods, making unit testing impossible. Which refactoring should you prompt Copilot Edits to perform?

- **A.** Use `Inline Chat`, `Copilot Edits`, **Next Edit Suggestions**, and `/doc` to scaffold repetitive DTOs/validators, extract pure functions to reduce cyclomatic complexity, and generate JSDoc/OpenAPI/Mermaid docs
- **B.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)
- **C.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic

### 76. A C# engineer wants Copilot in VS Code to upgrade 8 `.csproj` files from `net6.0` to `net9.0`, update NuGet package versions in `Directory.Packages.props`, run `dotnet build`, inspect a breaking package API rename, and patch the 3 affected `.cs` files automatically. Proposed solution: Run the request inside **`Ask` mode** without switching to **Agent Mode** (`or Copilot CLI`). Does this meet the goal?

- **A.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** No — Copilot Chat **`Ask` mode** only answers questions and proposes snippets in chat; autonomous multi-file workspace edits with iterative terminal test execution require **Agent Mode** (`or Copilot CLI`)
- **D.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review

### 77. A `.NET` backend engineer is asked to fix a bug in a legacy VB.NET (`Visual Basic`) customs-duty module written in 2011 (`Option Strict Off`, late-bound `Object` casts). How does Copilot accelerate comprehension and safe translation?

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **C.** Minimize context switching by running `/explain` on complex regexes/SQL/legacy modules, `@terminal` + `/fix` (`or Copilot CLI`) on shell/build errors, and `@workspace` / **Spaces** for repo onboarding
- **D.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions

### 78. During local Kubernetes debugging (`kubectl logs` / `dotnet test` in the VS Code integrated terminal), an unhandled `Npgsql.PostgresException: 42883` appears. How do you diagnose it in 5 seconds without switching windows?

- **A.** Minimize context switching by running `/explain` on complex regexes/SQL/legacy modules, `@terminal` + `/fix` (`or Copilot CLI`) on shell/build errors, and `@workspace` / **Spaces** for repo onboarding
- **B.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **C.** Save prompt files as `.git/hooks/pre-commit.yml` with `on: workflow_dispatch` so Copilot Chat automatically runs them on every keystroke
- **D.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)

### 79. ThalassaMarine modernizes a 2013 `.NET Framework 4.5` ASMX XML Web Service (`DemurrageCalculator.asmx.cs`) into an ASP.NET Core `.NET 9` Minimal API. Place the four modernization stages in safe order.

- **A.** Paste live customer SSNs and card numbers into Chat to build fixtures → Translate raw SQL string concatenation verbatim into the new language → Disable `CodeQL` alerts → Deploy without review
- **B.** Map legacy behavior & invariants via `/explain` and `@workspace` → Build characterization & boundary tests (`/tests`) until green → Refactor incrementally via Copilot Edits / Agent Mode → Re-run tests, `CodeQL` & benchmarks to verify parity
- **C.** Delete the legacy repo & prompt Copilot once to rewrite 80,000 lines from scratch → Delete failing tests so CI passes → Skip null/timezone/overflow checks → Switch production traffic immediately
- **D.** Upgrade production servers before compiling → Generate tautological `expect(true).toBe(true)` tests → Ignore concurrency and boundary cases → Merge without running CI

### 80. ThalassaMarine QA needs 1,000 synthetic `VesselArrival` and `CrewMember` C# records (`valid IMO check digits, UN/LOCODE ports, synthetic passport format, zero real crew PII`) for staging load tests. Which C# approach with Copilot is safest?

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **C.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **D.** Generate schema-valid **synthetic test fixtures** (`zero real customer PII`) and modernize legacy code (`e.g., Java 8 -> 21, Python 2 -> 3.12, callbacks -> async/await`) incrementally behind characterization tests

### 81. A ThalassaMarine architect wants to convert a 45,000-line WinForms + stored-procedure desktop application into Blazor + EF Core 9. Proposed solution: Paste all 42 `.cs` forms and 60 `.sql` procedures into a single Copilot Chat prompt asking `"Rewrite the entire app in Blazor"` in one shot. Does this meet the goal?

- **A.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **B.** No — keeping dozens of unrelated tabs open and reusing one marathon chat thread across unrelated tasks causes **context pollution and token truncation**; close stale tabs and use `/clear` or `#runSubagent`
- **C.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements
- **D.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically

### 82. When generating ASP.NET Core `.NET 9` HTTP integration tests (`testing middleware, model binding, auth policies, and ProblemDetails JSON serialization`) with Copilot `/tests`, which standard `.NET` test host should you specify? (`WebApplication____<Program>`)

- **A.** Use `/tests` (paired with testing `.instructions.md` conventions) to generate unit and integration tests with isolated I/O mocks/stubs, parameterized table cases, and deterministic teardown
- **B.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **C.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **D.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases

### 83. ThalassaMarine's `.github/instructions/testing.instructions.md` governs xUnit test generation across 30 `.NET` microservices. Which two rules belong in that file? Select two.

- **A.** When assigned an Issue, the Copilot coding agent (`cloud agent`) pushes commits directly to protected `main`, bypasses branch rulesets, and merges its own PR without human review
- **B.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **C.** Use `/tests` (paired with testing `.instructions.md` conventions) to generate unit and integration tests with isolated I/O mocks/stubs, parameterized table cases, and deterministic teardown
- **D.** Lock existing legacy behavior with characterization and boundary-value unit tests **before** refactoring idioms with Copilot Edits or Agent Mode
- **E.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions

### 84. A developer reviews an xUnit test generated by Copilot for `DemurrageService.CalculateFee(arrivalUtc, departureUtc, freeHours)` and sees `mockCalculator.CalculateFee(...).Returns(500m); Assert.Equal(500m, mockCalculator.CalculateFee(...));`. What is fatally wrong with that test?

- **A.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** Prompt explicitly for **boundary and adversarial edge cases** (`null/empty, 0/-1/MAX_INT, leap-year/DST timestamps, Unicode, timeouts, race conditions`) and assert concrete outputs/errors (`never tautologies`)
- **D.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically

### 85. ThalassaMarine's C# engineering checklist defines quality bars for AI-assisted code, tests, and security fixes. Which three checks are mandatory? Select three.

- **A.** Lock existing legacy behavior with characterization and boundary-value unit tests **before** refactoring idioms with Copilot Edits or Agent Mode
- **B.** Prompt explicitly for **boundary and adversarial edge cases** (`null/empty, 0/-1/MAX_INT, leap-year/DST timestamps, Unicode, timeouts, race conditions`) and assert concrete outputs/errors (`never tautologies`)
- **C.** Validate that security fixes (`such as CodeQL Copilot Autofix`) replace string-concatenated queries/commands with parameterized APIs and pass full regression + SAST checks
- **D.** Export 10,000 real production patient PHI and credit-card records into `.github/copilot-instructions.md` so `/tests` generates realistic integration assertions
- **E.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **F.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases

### 86. In `thalassa/document-archive`, `CodeQL` flags a **path traversal (`CWE-22`)** vulnerability on `Path.Combine(baseDir, userSuppliedFileName)` and generates a **Copilot Autofix** patch normalizing with `Path.GetFullPath(...)` and verifying `.StartsWith(fullBaseDir, StringComparison.Ordinal)`. What must the developer do before merging?

- **A.** Use Copilot Chat and **CodeQL Copilot Autofix** to remediate vulnerabilities (`SQLi -> parameterized queries, XSS -> encoding, path traversal, SSRF`) and eliminate `O(n^2)` loops or `N+1` ORM queries
- **B.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **C.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **D.** Configuring Copilot Content Exclusions also blocks `git clone`, GitHub Actions runners, and `CodeQL` security scans from reading the excluded files

### 87. A C# AIS NMEA sentence parser calls `sentence.Split(',')` allocating millions of `string[]` arrays per minute during port replay. Which `.NET 9` optimization can Copilot apply (`verified with BenchmarkDotNet`)?

- **A.** Open all 90 repository files in editor tabs and send the single-word prompt `optimize` in a 150-turn chat thread so Copilot infers your exact latency SLA automatically
- **B.** Mock the function under test itself to return `200 OK` and assert `expect(true).toBe(true)` so test coverage reaches `100%` without exercising edge cases
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Use Copilot Chat and **CodeQL Copilot Autofix** to remediate vulnerabilities (`SQLi -> parameterized queries, XSS -> encoding, path traversal, SSRF`) and eliminate `O(n^2)` loops or `N+1` ORM queries

---

## Domain 6 — Configure privacy, content exclusions, and safeguards (10–15% official weight · 13 questions)

### 88. ThalassaMarine configures Organization **Content Exclusions** (`- "/customs-bonds/**"`) across `thalassa` and validates IDE status and audit logs. Place the four steps in exact order.

- **A.** List tracked `secrets.yaml` in `.gitignore` expecting Copilot to exclude it → Set `Suggestions matching public code = Allow` → Disable IDE TLS verification → Share one seat login across 10 engineers
- **B.** Put exclusion rules in `package.json` → Wait 14 days for policy propagation → Have a Repo Admin delete Organization-level Content Exclusions → Disable Enterprise Audit Logs
- **C.** Add `fnmatch` globs (`- "/secrets/**"`) in `Content exclusion` → Allow `<=30 min` (or reload IDE) for policy sync → Verify crossed-out icon & `copilot.content_exclusion_changed` log → Avoid cross-file imports where IDE LSP hover types surface
- **D.** Configure Content Exclusions on a personal Copilot Free plan → Write PCRE lookbehind regexes instead of `fnmatch` globs → Expect exclusions to block `git clone` and Actions runs → Ignore IDE status icons

### 89. Is `fnmatch` path matching in GitHub Copilot **Content Exclusions** case-sensitive or case-insensitive when matching `/Customs/Tariff.json` vs `/customs/tariff.json`?

- **A.** Configuring Copilot Content Exclusions also blocks `git clone`, GitHub Actions runners, and `CodeQL` security scans from reading the excluded files
- **B.** Configure **Content Exclusions** (`Copilot Business & Enterprise`) in Repo/Org settings with YAML `fnmatch` globs (`- "/secrets/**"`); rules combine additively (`Repo cannot weaken Org`) and sync in `<=30 min`
- **C.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **D.** No — Repository and Organization **Content Exclusions** require **Copilot Business or Copilot Enterprise**; personal Copilot Free/Pro/Pro+ plans do not support Org Content Exclusions

### 90. ThalassaMarine adds `- "/deploy/aks-prod-secrets.yaml"` to Copilot Content Exclusions. Will their **GitHub Actions** workflow `.github/workflows/deploy.yml` still be able to read `/deploy/aks-prod-secrets.yaml` during CI/CD?

- **A.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** Configuring Copilot Content Exclusions also blocks `git clone`, GitHub Actions runners, and `CodeQL` security scans from reading the excluded files
- **D.** Excluded files are omitted from inline completions, IDE Chat, and Copilot Code Review, **but** IDE language-server (`LSP`) hover types from imported symbols can still surface, and `git`/`CodeQL`/Actions are unaffected

### 91. A ThalassaMarine repo admin wants Copilot Business to ignore tracked legacy tariff rate tables in `Data/ProprietaryRates.csv`. Proposed solution: Add `Data/ProprietaryRates.csv` to `.gitignore` (`without configuring Repository or Organization Copilot Content Exclusions`). Does this meet the goal?

- **A.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements
- **B.** No — `.gitignore` only prevents untracked files from being staged by Git; excluding tracked repository files from Copilot requires **Copilot Content Exclusions** (`Settings -> Copilot -> Content exclusion`)
- **C.** Configuring Copilot Content Exclusions also blocks `git clone`, GitHub Actions runners, and `CodeQL` security scans from reading the excluded files
- **D.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files

### 92. What are the two core eligibility requirements for **GitHub Copilot IP Indemnity** protection on unmodified Copilot suggestions?

- **A.** No — Repository and Organization **Content Exclusions** require **Copilot Business or Copilot Enterprise**; personal Copilot Free/Pro/Pro+ plans do not support Org Content Exclusions
- **B.** Customers retain ownership of their code (`GitHub claims no copyright over suggestions`), and **Copilot Business / Enterprise** provide **IP Indemnity** when `Suggestions matching public code` is set to **`Block`**
- **C.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **D.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits

### 93. If a ThalassaMarine developer takes a 5-line Copilot suggestion and heavily rewrites it to copy verbatim a third-party commercial competitor's leaked SDK manual, does GitHub's Copilot IP Indemnity cover the developer's manual infringement?

- **A.** Because GitHub Copilot compiles and formally proves every completion inside a cloud sandbox before rendering ghost text, accepted suggestions are guaranteed deterministic and bug-free
- **B.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **C.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **D.** Customers retain ownership of their code (`GitHub claims no copyright over suggestions`), and **Copilot Business / Enterprise** provide **IP Indemnity** when `Suggestions matching public code` is set to **`Block`**

### 94. In VS Code `settings.json`, a developer wants Copilot inline completions active for C# (`"csharp": true`) and disabled on `.env` and plaintext `.txt` notes (`"plaintext": false`). Complete the setting object key: `github.copilot.____`.

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** On Individual plans (`Copilot Free / Pro / Pro+`), disable `Allow GitHub to use my code snippets from the code editor for product improvements` in GitHub Copilot settings to opt out of model training
- **C.** Copilot Business and Enterprise automatically retain every private repository prompt for 90 days to fine-tune GitHub's shared public foundational models
- **D.** Automate seat lifecycle via `GET /orgs/{org}/copilot/billing`, `GET .../billing/seats` (`last_activity_at`), and `POST`/`DELETE /orgs/{org}/copilot/billing/selected_users` or `selected_teams` (`manage_billing:copilot`)

### 95. Approximately how many consecutive matching characters (`~____` characters, ignoring surrounding whitespace) trigger GitHub Copilot's **public-code duplication filter**?

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **C.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **D.** Set **`Suggestions matching public code = Block`** to suppress `~150+` char matches against public GitHub repos; when set to **`Allow`**, **Code Referencing** logs matched repo URLs and licenses in the IDE

### 96. ThalassaMarine's open-source sandbox org sets `Suggestions matching public code = Allow` so engineers can inspect **Code Referencing** license links in VS Code. Proposed solution: Merge suggestions produced under that `Allow` policy into ThalassaMarine's commercial flagship product while assuming full GitHub Copilot IP Indemnity applies to them. Does this meet the goal?

- **A.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **B.** Yes — this design satisfies all stated GitHub Copilot technical, governance, security, and privacy requirements
- **C.** No — GitHub's **Copilot IP Indemnity** on Business/Enterprise ceases to cover suggestions when `Suggestions matching public code` is set to **`Allow`**; set the filter to **`Block`**
- **D.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins

### 97. A ThalassaMarine consultant belongs to `thalassa-prod` (`Public code = Block`) and a partner org `port-hackathon` (`Public code = Allow`). Which two statements accurately describe policy evaluation and filtering for that consultant? Select two.

- **A.** When a user receives Copilot policies from multiple Organizations (or Enterprise + Org), GitHub enforces the **most restrictive** policy (`Block overrides Allow; Disabled overrides Enabled`)
- **B.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **C.** Setting `Suggestions matching public code = Allow` automatically grants Apache-2.0 relicensing and full GitHub IP Indemnity over any verbatim GPL-3.0 code Copilot emits
- **D.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **E.** Set **`Suggestions matching public code = Block`** to suppress `~150+` char matches against public GitHub repos; when set to **`Allow`**, **Code Referencing** logs matched repo URLs and licenses in the IDE

### 98. A ThalassaMarine developer adds `- "Customs/*.json"` (`without a leading / or **/`) vs `- "/Customs/*.json"` in Content Exclusions and notices nested `/src/Customs/rates.json` still gets completions! Which `fnmatch` pattern matches `Customs/*.json` at **any** directory depth?

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins
- **C.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **D.** Diagnose missing completions or unexpected exclusions via **Copilot Diagnostics / Output logs**: verify seat assignment, filetype toggle, active exclusion icon (`most restrictive org wins`), and TLS proxy allowlists (`*.githubcopilot.com`)

### 99. A developer edits a file inside a freshly initialized local folder (`git init`, with **zero Git `origin` remote URL configured**) and wonders why Repository Content Exclusions from `github.com/thalassa/vessel-api` have NOT triggered. Why?

- **A.** Configuring Copilot Content Exclusions also blocks `git clone`, GitHub Actions runners, and `CodeQL` security scans from reading the excluded files
- **B.** Diagnose missing completions or unexpected exclusions via **Copilot Diagnostics / Output logs**: verify seat assignment, filetype toggle, active exclusion icon (`most restrictive org wins`), and TLS proxy allowlists (`*.githubcopilot.com`)
- **C.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **D.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files

### 100. On shipboard satellite VDI workstations behind a strict Zscaler/Squid corporate proxy, Visual Studio Copilot fails with TLS handshake and proxy errors. Which two steps resolve connectivity? Select two.

- **A.** GitHub Copilot runs a 70-billion-parameter LLM and the public-code duplication index entirely offline inside the local VS Code extension with zero network traffic
- **B.** Allow outbound `HTTPS (TCP 443)` with valid TLS trust (`NODE_EXTRA_CA_CERTS` / OS trust store for SSL-inspecting proxies) to GitHub's documented `*.githubcopilot.com` and `github.com` endpoints
- **C.** Diagnose missing completions or unexpected exclusions via **Copilot Diagnostics / Output logs**: verify seat assignment, filetype toggle, active exclusion icon (`most restrictive org wins`), and TLS proxy allowlists (`*.githubcopilot.com`)
- **D.** Listing `- "!/secrets/**"` inside `.github/copilot-instructions.md` overrides Organization Content Exclusions and forces Copilot to read excluded credential files
- **E.** When a developer belongs to two GitHub Organizations with conflicting Copilot policies (`one Block, one Allow`), the most permissive (`Allow`) policy always wins

---

## Answer Key and Explanations

### Question 1 — `C` (Use GitHub Copilot responsibly)

Correct answer: C (is correct). LLMs predict statistically probable token sequences rather than solving physical stability equations; subtle sign or unit (`metric tonnes` vs `long tons`) errors can compile cleanly while violating maritime safety limits. [Skill 1.1: Describe risks and limitations of Generative AI tools | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/responsible-ai-with-github-copilot/)]

- **A:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Correct. Generative AI risks and limitations (`1.1`) address probabilistic next-token prediction, hallucinations, outdated APIs, and bias—not IDE installation or REST seat billing.
- **D:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.

### Question 2 — `A` (Use GitHub Copilot responsibly)

Correct answer: A (is correct). Confirm `Edifact.Baplie.NetCore` exists on ThalassaMarine's vetted internal NuGet feed (`or nuget.org with verified prefix reservation, publisher history, and vulnerability scan`), since LLMs can invent package names. [Skill 1.1: Describe risks and limitations of Generative AI tools | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/responsible-ai-with-github-copilot/)]

- **A:** Correct. Package hallucination / slopsquatting verification (`1.1`, `1.4`) protects dependency supply chains—not Markdown PR summaries or status badges.
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Incorrect. Copilot Audit Logs and Metrics API (`2.14`) separate security/compliance event logs from anonymized (`>=5`-user) adoption telemetry.
- **D:** Incorrect. GitHub Spark (`2.11`) accelerates full-stack micro-app prototyping and deployment directly from natural language and visual controls.

### Question 3 — `D` (Use GitHub Copilot responsibly)

Correct answer: D (is correct). Counter **automation complacency (`automation bias`)** by keeping PRs small and enforcing explicit review verification of domain edge cases, nullability, SQL parameterization, and package provenance. [Skill 1.1: Describe risks and limitations of Generative AI tools | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/responsible-ai-with-github-copilot/)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **C:** Incorrect. Installing GitHub Copilot CLI (`2.5`) uses `@github/copilot` (`Node 22+`), WinGet, or Homebrew, followed by `/login` OAuth and directory trust confirmation.
- **D:** Correct. Automation bias (`1.1`, `1.4`) occurs when developers accept syntactically clean completions without verifying business logic or security invariants.

### Question 4 — `C, E` (Use GitHub Copilot responsibly)

Correct answers: C and E (are correct). LLMs optimize token plausibility (`not formal semantic proof`) and polished AI code can induce **automation complacency** unless teams enforce adversarial human review. [Skill 1.1: Describe risks and limitations of Generative AI tools | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/responsible-ai-with-github-copilot/)]

- **A:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Correct. Generative AI risks and limitations (`1.1`) address probabilistic next-token prediction, hallucinations, outdated APIs, and bias—not IDE installation or REST seat billing.
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **E:** Correct. Automation bias (`1.1`, `1.4`) occurs when developers accept syntactically clean completions without verifying business logic or security invariants.

### Question 5 — `B` (Use GitHub Copilot responsibly)

Correct answer: B (is correct). **Reliability & Safety** requires rigorous testing, fault tolerance, and bounded operational behavior under degraded sensor or network conditions. [Skill 1.2: Describe ethical and responsible AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-code-completion)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Correct. Microsoft/GitHub Responsible AI (`1.2`) centers on Fairness, Reliability & Safety, Privacy & Security, Inclusiveness, Transparency, and human Accountability.
- **C:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **D:** Incorrect. Copilot CLI programmatic flags (`2.6`) control non-interactive scripting (`-p`, `-s`, `--output-format=json`), tool permissions, and `--fleet` parallelism.

### Question 6 — `B` (Use GitHub Copilot responsibly)

Correct answer: B (is correct). Under **Accountability**, human authors, code reviewers, and the deploying organization retain full engineering responsibility for every merged line of code. [Skill 1.2: Describe ethical and responsible AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-code-completion)]

- **A:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **B:** Correct. Ethical AI governance (`1.2`) requires human ownership, license respect, and transparent review—never treating Copilot as an autonomous merge authority.
- **C:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).

### Question 7 — `C` (Use GitHub Copilot responsibly)

Correct answer: C (is correct). **Inclusiveness** (`paired with Fairness`) ensures software interfaces accommodate diverse physical environments, assistive technologies, and global scripts. [Skill 1.2: Describe ethical and responsible AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-code-completion)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **C:** Correct. Fairness and Inclusiveness (`1.2`, `1.3`) ensure AI-assisted software serves diverse users equitably and meets accessibility standards.
- **D:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).

### Question 8 — `A, D, E` (Use GitHub Copilot responsibly)

Correct answers: A, D, and E (are correct). Evaluate features against all six Responsible AI principles, test accessibility and multilingual character equity (`Inclusiveness & Fairness`), and require accountable human verification prior to merge. [Skill 1.2: Describe ethical and responsible AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-code-completion)]

- **A:** Correct. Human-in-the-loop accountability (`1.2`, `1.4`) ensures engineers remain responsible for correctness, security, and license compliance.
- **B:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **C:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **D:** Correct. Microsoft/GitHub Responsible AI (`1.2`) centers on Fairness, Reliability & Safety, Privacy & Security, Inclusiveness, Transparency, and human Accountability.
- **E:** Correct. Fairness and Inclusiveness (`1.2`, `1.3`) ensure AI-assisted software serves diverse users equitably and meets accessibility standards.
- **F:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).

### Question 9 — `A` (Use GitHub Copilot responsibly)

Correct answer: A (is correct). Forbid `BinaryFormatter` in `.github/instructions/csharp-security.instructions.md` (`requiring System.Text.Json with strict types`) and enforce **`CodeQL` + .NET Roslyn security analyzers (`CA2300`)** in CI. [Skill 1.3: Identify potential harms and mitigation strategies of AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/overview)]

- **A:** Correct. Harm mitigation (`1.3`) combines RAI safety filters, bias testing, SAST scanning, and privacy controls—not disabling code review.
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **D:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).

### Question 10 — `B` (Use GitHub Copilot responsibly)

Correct answer: B (is correct). **Indirect prompt injection** embedded in untrusted external data; mitigate it via tool-permission boundaries, human review of workspace file diffs (`nuget.config`), and CI lockfile/source checks. [Skill 1.3: Identify potential harms and mitigation strategies of AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/overview)]

- **A:** Incorrect. False: `#runSubagent` runs autonomously in its **own isolated context window** without pausing for user feedback, returning only the distilled result (`2.9`).
- **B:** Correct. Indirect prompt-injection defense (`1.3`, `1.5`) guards Agent Mode and MCP tool invocations against malicious instructions hidden in external data.
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).

### Question 11 — `A, B` (Use GitHub Copilot responsibly)

Correct answers: A and B (are correct). Never paste real crew passport PII or live EDI keys into prompts (`use synthetic fixtures + Content Exclusions`), and enforce **Secret Scanning Push Protection + `CodeQL` + Dependabot** in GitHub. [Skill 1.3: Identify potential harms and mitigation strategies of AI usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/overview)]

- **A:** Correct. Data minimization in prompts (`1.3`, `1.5`) prevents accidental exposure of regulated personal data or live secrets.
- **B:** Correct. Automated security gates (`1.3`, `1.4`) catch vulnerable patterns, leaked credentials, and known CVEs introduced during rapid AI code generation.
- **C:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **D:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **E:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).

### Question 12 — `C` (Use GitHub Copilot responsibly)

Correct answer: C (is correct). Prompting with explicit security/type constraints -> inspecting IMDG logic & verifying NuGet packages -> running xUnit edge-case tests + `CodeQL` -> completing human peer PR review. [Skill 1.4: Explain the need to validate AI output | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)]

- **A:** Incorrect. Incorrect: merging unverified LLM output or replacing human peer review with Copilot Code Review violates Responsible AI accountability.
- **B:** Incorrect. Incorrect: pasting real PII into prompts and bypassing human review violates privacy and Responsible AI governance.
- **C:** Correct. Correct order: constrained prompt -> manual logic & dependency check (`blocking slopsquatting`) -> automated tests/SAST -> human PR review.
- **D:** Incorrect. Incorrect: blindly installing hallucinated package names exposes builds to dependency confusion and slopsquatting.

### Question 13 — `A` (Use GitHub Copilot responsibly)

Correct answer: A (is correct). Pair `.instructions.md` async/await rules (`forbid .Result / .Wait()`) with Roslyn analyzer rules (`VSTHRD002`), load/concurrency tests, and human PR code review. [Skill 1.4: Explain the need to validate AI output | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)]

- **A:** Correct. Validating AI output (`1.4`) requires human code review, automated tests, and security scanning before merge.
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **D:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).

### Question 14 — `D` (Use GitHub Copilot responsibly)

Correct answer: D (is correct). **Non-determinism (`probabilistic token sampling`)** means identical prompts can yield varied outputs across runs, reinforcing why deterministic xUnit test suites are mandatory. [Skill 1.4: Explain the need to validate AI output | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)]

- **A:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Correct. Non-determinism (`1.4`, `3.5`) means syntactic plausibility never guarantees functional equivalence across repeated prompts.

### Question 15 — `D` (Use GitHub Copilot responsibly)

Correct answer: D (is correct). No — Copilot Code Review posts `Comment` reviews only and **never** counts toward required merge approvals; `2` human reviewers are still required. [Skill 1.4: Explain the need to validate AI output | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)]

- **A:** Incorrect. The proposed GitHub Copilot configuration or workflow violates at least one stated governance, privacy, or technical requirement. No — Copilot Code Review posts `Comment` reviews only and **never** counts toward required merge approvals; `2` human reviewers are still required.
- **B:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **C:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **D:** Correct. Copilot Code Review (`1.4`, `2.10`) supplements—never replaces—required human pull-request approvals.

### Question 16 — `C` (Use GitHub Copilot responsibly)

Correct answer: C (is correct). Enable `Suggestions matching public code = Block`, configure Content Exclusions on customs credentials/contracts, mandate synthetic crew/vessel test data, and gate merges on xUnit + `CodeQL` + human review. [Skill 1.5: Identify how to operate GitHub Copilot responsibly | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **C:** Correct. Responsible Copilot operation (`1.5`) pairs duplication filtering, Content Exclusions, zero-PII prompting, and mandatory human PR review.
- **D:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).

### Question 17 — `A` (Use GitHub Copilot responsibly)

Correct answer: A (is correct). Yes — characterization tests, synthetic non-PII fixtures, bounded per-contract Agent Mode conversion, automated `dotnet test`/`CodeQL` verification, and human review follow responsible modernization best practices. [Skill 1.5: Identify how to operate GitHub Copilot responsibly | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use)]

- **A:** Correct. Evaluate whether every stated plan tier, CLI/IDE mechanism, context scope, and Enterprise/Org policy requirement is genuinely met.
- **B:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **C:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **D:** Incorrect. Only **Agent Mode** (or **Copilot CLI**, `2.2`, `2.9`) autonomously edits multiple files and runs terminal verification loops.

### Question 18 — `B` (Use GitHub Copilot responsibly)

Correct answer: B (is correct). Enabling **NuGet Package Source Mapping** (`alongside packages.lock.json and Dependency Review`) ensures `Thalassa.*` and vetted packages resolve strictly from trusted feeds, blocking dependency-confusion and slopsquatting. [Skill 1.5: Identify how to operate GitHub Copilot responsibly | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Correct. Package hallucination / slopsquatting verification (`1.1`, `1.4`) protects dependency supply chains—not Markdown PR summaries or status badges.
- **C:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **D:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).

### Question 19 — `B` (Use GitHub Copilot features)

Correct answer: B (is correct). GitHub Copilot (`inline completions + Copilot Chat`) is integrated as a unified built-in workload/component in Visual Studio 2022 (`17.10+`), activated by signing in with a GitHub account holding an active Copilot license. [Skill 2.1: Enable Copilot in the IDE | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/quickstart)]

- **A:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **B:** Correct. Enabling Copilot in the IDE (`2.1`) requires installing the IDE extension, authenticating with GitHub, and holding an active Copilot plan.
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. Copilot Audit Logs and Metrics API (`2.14`) separate security/compliance event logs from anonymized (`>=5`-user) adoption telemetry.

### Question 20 — `C` (Use GitHub Copilot features)

Correct answer: C (is correct). Copilot Free enforces **capped monthly quotas** of inline code completions and Copilot Chat messages (`and lacks Organization policies, Content Exclusions, and IP Indemnity`). [Skill 2.1: Enable Copilot in the IDE | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/quickstart)]

- **A:** Incorrect. Content Exclusions (`2.3`, `6.1`) are only enforced for seats governed under Copilot Business or Copilot Enterprise.
- **B:** Incorrect. Organization/Enterprise Copilot tiers (`2.1`, `2.15`, `6.2`) add centralized governance, Content Exclusions, audit logs, and IP Indemnity.
- **C:** Correct. Individual Copilot tiers (`2.1`, `2.15`) serve single accounts without Organization policy management or Org Content Exclusions.
- **D:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).

### Question 21 — `B` (Use GitHub Copilot features)

Correct answer: B (is correct). **Next Edit Suggestions (`NES`)** anticipates follow-up edits across nearby lines from your most recent code modification so you can ripple changes with `Tab`. [Skill 2.2: Trigger Copilot through inline suggestions, chat, CLI, and agent mode | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Correct. Inline completions and Next Edit Suggestions (`2.2`, `5.1`) accelerate localized cursor-level coding and follow-on edits.
- **C:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **D:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).

### Question 22 — `A, B` (Use GitHub Copilot features)

Correct answers: A and B (are correct). Use **Inline Chat (`Ctrl+I` / `Alt+/`)** for surgical in-place refactoring of a selected C# method, and use **Agent Mode** (`or Copilot CLI`) when a task spans creating files, running `dotnet test`, and iterating on compiler errors. [Skill 2.2: Trigger Copilot through inline suggestions, chat, CLI, and agent mode | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot)]

- **A:** Correct. Triggering Copilot across surfaces (`2.2`) matches Inline Chat, `Ask`, `Edit`, Agent Mode, and Copilot CLI to task complexity.
- **B:** Correct. GitHub Copilot CLI (`2.4`) brings agentic file editing, command execution, and GitHub workflow integration directly to the terminal.
- **C:** Incorrect. Only **Agent Mode** (or **Copilot CLI**, `2.2`, `2.9`) autonomously edits multiple files and runs terminal verification loops.
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **E:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).

### Question 23 — `A` (Use GitHub Copilot features)

Correct answer: A (is correct). IDE clients synchronize updated Repository and Organization Content Exclusion policies within **up to 30 minutes** (`or immediately upon IDE reload / new session`). [Skill 2.3: Configure content exclusions for specific files or repositories (app knowledge) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion)]

- **A:** Correct. IDE/repo content exclusion awareness (`2.3`) prevents specified paths from being read into Copilot prompts on Business and Enterprise plans.
- **B:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **C:** Incorrect. Adding a tracked path to `.gitignore` (`6.1`) does NOT stop Copilot from reading that file in the IDE or on GitHub.com.
- **D:** Incorrect. False: Copilot Content Exclusions apply strictly to **GitHub Copilot** features—they never restrict Git repository ACLs, Actions workflows, or `CodeQL` (`6.1`).

### Question 24 — `D` (Use GitHub Copilot features)

Correct answer: D (is correct). The GitHub Copilot status bar icon displays a **crossed-out / disabled slash indicator** (`showing Content Exclusion matched on hover`), and inline ghost text is suppressed. [Skill 2.3: Configure content exclusions for specific files or repositories (app knowledge) | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion)]

- **A:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Incorrect. False: Copilot Content Exclusions apply strictly to **GitHub Copilot** features—they never restrict Git repository ACLs, Actions workflows, or `CodeQL` (`6.1`).
- **D:** Correct. IDE/repo content exclusion awareness (`2.3`) prevents specified paths from being read into Copilot prompts on Business and Enterprise plans.

### Question 25 — `C` (Use GitHub Copilot features)

Correct answer: C (is correct). It delivers an **agentic conversational and programmatic (`-p`) AI assistant natively inside the terminal**, inspecting logs/configs, generating PowerShell/Bash/C# scripts, and executing approved commands over SSH. [Skill 2.4: Define GitHub Copilot CLI and how it benefits developers | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-cli)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **C:** Correct. GitHub Copilot CLI (`2.4`) brings agentic file editing, command execution, and GitHub workflow integration directly to the terminal.
- **D:** Incorrect. Copilot Audit Logs and Metrics API (`2.14`) separate security/compliance event logs from anonymized (`>=5`-user) adoption telemetry.

### Question 26 — `D` (Use GitHub Copilot features)

Correct answer: D (is correct). Installing GitHub Copilot CLI (`winget install GitHub.Copilot` or `npm install -g @github/copilot`), `cd`ing to `C:\src\vessel-scheduler` & running `copilot`, authenticating via `/login`, and confirming folder trust + `/permissions show`. [Skill 2.5: Identify the steps for installing GitHub Copilot CLI | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/get-started/cli-quickstart)]

- **A:** Incorrect. Incorrect: `/login` runs inside interactive `copilot`, npm installs require Node.js `22+`, and `config.json` never stores plaintext passwords.
- **B:** Incorrect. Incorrect: disabling the org Copilot CLI policy blocks access, and authentication must precede non-interactive execution.
- **C:** Incorrect. Incorrect: `~/.copilot/logs/` stores session logs, and Copilot CLI requires approval before modifying files in default mode.
- **D:** Correct. Correct order: install `@github/copilot` -> `cd` to project & start `copilot` -> authenticate via `/login` -> confirm folder trust & inspect tool permissions.

### Question 27 — `A` (Use GitHub Copilot features)

Correct answer: A (is correct). The standalone `@github/copilot` npm distribution requires **Node.js `22` or later** (`alternatively install the native binary via Homebrew or WinGet`). [Skill 2.5: Identify the steps for installing GitHub Copilot CLI | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/get-started/cli-quickstart)]

- **A:** Correct. Installing GitHub Copilot CLI (`2.5`) uses `@github/copilot` (`Node 22+`), WinGet, or Homebrew, followed by `/login` OAuth and directory trust confirmation.
- **B:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **C:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 28 — `A` (Use GitHub Copilot features)

Correct answer: A (is correct). Combining `-s` (`--silent`) with `--output-format=json` emits clean JSONL (`newline-delimited JSON`) output suitable for automated script pipelines. [Skill 2.6: Describe key GitHub Copilot CLI features and commands | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/copilot-cli-reference/cli-programmatic-reference)]

- **A:** Correct. Copilot CLI programmatic flags (`2.6`) control non-interactive scripting (`-p`, `-s`, `--output-format=json`), tool permissions, and `--fleet` parallelism.
- **B:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).

### Question 29 — `B, E` (Use GitHub Copilot features)

Correct answers: B and E (are correct). Use `/model` (`or --model=MODEL`) to select the active AI model, and use `/permissions manual` (`or /permissions show`) to reset session auto-approvals back to manual confirmation prompts. [Skill 2.6: Describe key GitHub Copilot CLI features and commands | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/copilot-cli-reference/cli-programmatic-reference)]

- **A:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **B:** Correct. Copilot CLI programmatic flags (`2.6`) control non-interactive scripting (`-p`, `-s`, `--output-format=json`), tool permissions, and `--fleet` parallelism.
- **C:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **D:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **E:** Correct. Copilot CLI interactive slash commands and `~/.copilot/settings.json` (`2.6`, `2.8`) govern tool approvals and model selection (`config.json` is internal runtime state).

### Question 30 — `B` (Use GitHub Copilot features)

Correct answer: B (is correct). Running `copilot --continue` automatically resumes the most recently closed local session (`whereas copilot --resume opens an interactive session picker or accepts an explicit SESSION-ID`). [Skill 2.7: Use GitHub Copilot CLI interactively and in sessions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-cli/cli-best-practices)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Correct. Interactive Copilot CLI sessions (`2.7`) persist plans, compaction checkpoints, and artifacts in `~/.copilot/session-state/` for `--resume`.
- **C:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **D:** Incorrect. False: `#runSubagent` runs autonomously in its **own isolated context window** without pausing for user feedback, returning only the distilled result (`2.9`).

### Question 31 — `C` (Use GitHub Copilot features)

Correct answer: C (is correct). Invoking `/fleet` in an interactive Copilot CLI session decomposes complex multi-part work into parallel subagent tasks to accelerate execution. [Skill 2.7: Use GitHub Copilot CLI interactively and in sessions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-cli/cli-best-practices)]

- **A:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **B:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **C:** Correct. Interactive Copilot CLI sessions (`2.7`) persist plans, compaction checkpoints, and artifacts in `~/.copilot/session-state/` for `--resume`.
- **D:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).

### Question 32 — `D` (Use GitHub Copilot features)

Correct answer: D (is correct). Passing `--add-dir ../shared-protos` (`or interactive /add-dir`) grants explicit directory access to that sibling folder while keeping broader filesystem paths protected. [Skill 2.8: Generate scripts and manage files with GitHub Copilot CLI | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/copilot-cli-reference/cli-config-dir-reference)]

- **A:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **B:** Incorrect. False: Copilot Content Exclusions apply strictly to **GitHub Copilot** features—they never restrict Git repository ACLs, Actions workflows, or `CodeQL` (`6.1`).
- **C:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **D:** Correct. Copilot CLI file and script management (`2.8`) enforces explicit write/command approval, `--add-dir` path boundaries, and secret redaction (`GITHUB_TOKEN` redacted by default).

### Question 33 — `D` (Use GitHub Copilot features)

Correct answer: D (is correct). Copilot CLI maintains `~/.copilot/session-store.db` (`a SQLite index across local sessions`), alongside per-session directories under `~/.copilot/session-state/{session-id}/`. [Skill 2.8: Generate scripts and manage files with GitHub Copilot CLI | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/enterprise-cloud@latest/copilot/reference/copilot-cli-reference/cli-config-dir-reference)]

- **A:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **B:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **C:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **D:** Correct. Copilot CLI file and script management (`2.8`) enforces explicit write/command approval, `--add-dir` path boundaries, and secret redaction (`GITHUB_TOKEN` redacted by default).

### Question 34 — `B` (Use GitHub Copilot features)

Correct answer: B (is correct). Registering `.vscode/mcp.json` & verifying tools -> delegating stored-procedure inventory to `#runSubagent` -> applying EF Core edits + `dotnet test` in Agent Mode -> reviewing working-set diffs & `Keep`ing verified changes. [Skill 2.9: Use Agent Mode, Copilot Edits, and MCP for enhanced development and workflows; manage Agent Sessions and delegate tasks to Sub-Agents for optimized context usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp)]

- **A:** Incorrect. Incorrect: `.git/HEAD` is Git metadata (not `.vscode/mcp.json`), and diffs must be reviewed before commit.
- **B:** Correct. Correct order: register `.vscode/mcp.json` tools -> isolate noisy research via `#runSubagent` -> iterate edits/tests in Agent Mode -> inspect & `Keep` verified diffs.
- **C:** Incorrect. Incorrect: never commit secrets to `.github/copilot-instructions.md`, and `#runSubagent` runs autonomously in isolated context without pausing for user input.
- **D:** Incorrect. Incorrect: `Ask` mode cannot autonomously edit files or execute terminal loops, and `Keep` should follow diff & test verification.

### Question 35 — `D` (Use GitHub Copilot features)

Correct answer: D (is correct). It runs asynchronously inside an ephemeral **GitHub Actions** sandbox environment, pushes commits to a `copilot/*` branch, and opens a **Draft Pull Request** for human review (`never auto-merging to main`). [Skill 2.9: Use Agent Mode, Copilot Edits, and MCP for enhanced development and workflows; manage Agent Sessions and delegate tasks to Sub-Agents for optimized context usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **C:** Incorrect. Only **Agent Mode** (or **Copilot CLI**, `2.2`, `2.9`) autonomously edits multiple files and runs terminal verification loops.
- **D:** Correct. Copilot coding agent (`2.9`) executes asynchronous repository tasks in an isolated cloud sandbox and opens a draft PR without merging autonomously.

### Question 36 — `A, B, F` (Use GitHub Copilot features)

Correct answers: A, B, and F (are correct). `Edit` mode modifies a user-selected working set (`Agent Mode` adds autonomous tool/MCP/terminal loops), `#runSubagent` isolates research in its own context window, and the cloud coding agent opens draft PRs from GitHub Actions. [Skill 2.9: Use Agent Mode, Copilot Edits, and MCP for enhanced development and workflows; manage Agent Sessions and delegate tasks to Sub-Agents for optimized context usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/customizing-copilot/extending-copilot-chat-with-mcp)]

- **A:** Correct. Copilot coding agent (`2.9`) executes asynchronous repository tasks in an isolated cloud sandbox and opens a draft PR without merging autonomously.
- **B:** Correct. Agent Mode + MCP (`2.9`) connects Copilot to external tools/APIs via `.vscode/mcp.json` and iterates across edits and terminal runs autonomously.
- **C:** Incorrect. Only **Agent Mode** (or **Copilot CLI**, `2.2`, `2.9`) autonomously edits multiple files and runs terminal verification loops.
- **D:** Incorrect. False: `#runSubagent` runs autonomously in its **own isolated context window** without pausing for user feedback, returning only the distilled result (`2.9`).
- **E:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **F:** Correct. Sub-Agent delegation (`2.9`) prevents raw search results from bloating and confusing the primary Agent Mode conversation.

### Question 37 — `A` (Use GitHub Copilot features)

Correct answer: A (is correct). Enabling **`Review new pushes`** inside the `Automatically request Copilot code review` ruleset triggers fresh Copilot reviews whenever new commits are pushed to the PR. [Skill 2.10: Use Copilot for code review and coding assistance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/configure-code-review)]

- **A:** Correct. Copilot Code Review (`2.10`) posts `Comment` reviews with `suggestion` blocks—never counting toward required human merge approvals.
- **B:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **C:** Incorrect. Copilot Code Review (`1.4`, `2.10`) supplements—never replaces—required human pull-request approvals.
- **D:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).

### Question 38 — `B` (Use GitHub Copilot features)

Correct answer: B (is correct). Yes — Copilot Review Selection / Review Staged & Uncommitted Changes in the IDE lets developers catch logic, style, and security defects locally prior to `git push`. [Skill 2.10: Use Copilot for code review and coding assistance | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/configure-code-review)]

- **A:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **B:** Correct. Copilot Code Review (`2.10`) posts `Comment` reviews with `suggestion` blocks—never counting toward required human merge approvals.
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.

### Question 39 — `C` (Use GitHub Copilot features)

Correct answer: C (is correct). Creating `.github/instructions/migrations.instructions.md` (`applyTo:`), merging to the default branch, enabling `Automatically request Copilot code review` in an Org Ruleset, and resolving comments alongside human PR approval. [Skill 2.11: Utilize Spaces, Spark, Pull Request summaries, and customizable review standards via instructions files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)]

- **A:** Incorrect. Incorrect: blocking Copilot Code Review in Enterprise `AI controls` disables it across all enterprise repositories.
- **B:** Incorrect. Incorrect: custom instructions must be concise Markdown (`.instructions.md` / `copilot-instructions.md`), not binary PDFs.
- **C:** Correct. Correct order: author path-scoped `.instructions.md` (`applyTo:`) -> merge to default branch -> enable automatic Copilot review via Ruleset -> pair with human approval.
- **D:** Incorrect. Incorrect: `excludeAgent: "code-review"` excludes Copilot Code Review from reading that file, and Copilot comments never satisfy required human approvals.

### Question 40 — `C` (Use GitHub Copilot features)

Correct answer: C (is correct). **Copilot Spaces** lets teams organize repositories, code files, PRs, docs, and custom instructions into shareable, domain-grounded context hubs on GitHub.com. [Skill 2.11: Utilize Spaces, Spark, Pull Request summaries, and customizable review standards via instructions files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)]

- **A:** Incorrect. GitHub Spark (`2.11`) accelerates full-stack micro-app prototyping and deployment directly from natural language and visual controls.
- **B:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **C:** Correct. Copilot Spaces (`2.11`) organize shareable, always-synced multi-repo project context so responses stay grounded in team architecture.
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 41 — `A, E` (Use GitHub Copilot features)

Correct answers: A and E (are correct). `.github/copilot-instructions.md` provides repository-wide instructions (`and PR summary conventions`), while `.github/instructions/*.instructions.md` uses YAML `applyTo:` globs (`and optional excludeAgent: "code-review" | "cloud-agent"`). [Skill 2.11: Utilize Spaces, Spark, Pull Request summaries, and customizable review standards via instructions files | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)]

- **A:** Correct. PR Summaries and custom instruction files (`2.11`) automate reviewer context and tailor Copilot code generation/review (`without affecting raw inline ghost text where unsupported`).
- **B:** Incorrect. `excludeAgent: "code-review"` (`2.11`) tells GitHub.com to omit that instruction file during Copilot Code Review.
- **C:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **D:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **E:** Correct. Path-scoped `.instructions.md` files (`2.11`) automatically inject targeted coding and review rules only when matching files are touched.

### Question 42 — `A` (Use GitHub Copilot features)

Correct answer: A (is correct). Use the **thumbs-up / thumbs-down (`Helpful / Unhelpful`) feedback controls** on the Chat response to flag quality issues (`and refine repository .instructions.md rules to prevent repeats`). [Skill 2.12: Understand the limits, options, feedback, and commands of GitHub Copilot Chat; include prompt file reuse for consistent responses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/configure-custom-instructions-in-your-ide/add-repository-instructions-in-your-ide)]

- **A:** Correct. Copilot Chat participants, slash commands, `#` context variables, and feedback ratings (`2.12`) focus intent and report quality signals.
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **D:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).

### Question 43 — `B, C` (Use GitHub Copilot features)

Correct answers: B and C (are correct). They turn repeatable workflows (`with YAML agent/model/tools metadata and Markdown #file: links`) into version-controlled templates, invocable on demand in Chat as `/modernize-wcf`. [Skill 2.12: Understand the limits, options, feedback, and commands of GitHub Copilot Chat; include prompt file reuse for consistent responses | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/how-tos/configure-custom-instructions-in-your-ide/add-repository-instructions-in-your-ide)]

- **A:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **B:** Correct. Workspace `.prompt.md` files (`2.12`) turn repeatable scaffolding, review, and migration workflows into version-controlled slash commands.
- **C:** Correct. Workspace `.prompt.md` prompt files (`2.12`) standardize repeatable task prompts across VS Code and JetBrains teams.
- **D:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **E:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).

### Question 44 — `D` (Use GitHub Copilot features)

Correct answer: D (is correct). Enable **`Only allow Copilot code review to be triggered by authorized users`** (`restricting triggers on org repositories to users with paid/authorized Copilot code-review access`). [Skill 2.13: Configure organization-wide policy management; enable Copilot Code Review policies and manage feature availability across IDEs and github.com | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/administer-copilot/manage-for-enterprise/manage-agents/block-agentic-features)]

- **A:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **B:** Incorrect. Content Exclusions (`2.3`, `6.1`) are only enforced for seats governed under Copilot Business or Copilot Enterprise.
- **C:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **D:** Correct. Organization/Enterprise Copilot policy management (`2.13`) governs IDE/GitHub.com features, CLI/MCP access, and repo-level agent blocks.

### Question 45 — `D` (Use GitHub Copilot features)

Correct answer: D (is correct). Seat lifecycle events (`copilot.cfb_seat_created` / cancelled), Organization Copilot policy toggle changes, and Repository/Organization **Content Exclusion** creation or modification events (`copilot.content_exclusion_changed`). [Skill 2.14: Utilize audit log events | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-audit-logs-for-copilot-business)]

- **A:** Incorrect. Per-seat dormancy audits (`2.14`, `2.15`) require `/copilot/billing/seats`, whereas `/copilot/metrics` aggregates anonymized adoption stats.
- **B:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **C:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **D:** Correct. Copilot Audit Logs and Metrics API (`2.14`) separate security/compliance event logs from anonymized (`>=5`-user) adoption telemetry.

### Question 46 — `C` (Use GitHub Copilot features)

Correct answer: C (is correct). Calling `GET /orgs/{org}/copilot/billing/seats` returns per-seat assignment metadata and last-activity timestamps (`distinct from aggregated GET /orgs/{org}/copilot/metrics`). [Skill 2.15: Manage subscriptions using the REST API | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/rest/copilot/copilot-user-management)]

- **A:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **B:** Incorrect. Per-seat dormancy audits (`2.14`, `2.15`) require `/copilot/billing/seats`, whereas `/copilot/metrics` aggregates anonymized adoption stats.
- **C:** Correct. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **D:** Incorrect. Individual Copilot tiers (`2.1`, `2.15`) serve single accounts without Organization policy management or Org Content Exclusions.

### Question 47 — `B` (Understand GitHub Copilot data and architecture)

Correct answer: B (is correct). No — Copilot Business and Enterprise contractually exclude customer prompts, context, and completions from training foundation models. [Skill 3.1: Explain data usage, flow, and sharing | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-copilot-policies-as-an-individual-subscriber)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Correct. Copilot Business/Enterprise data handling (`3.1`) guarantees `TLS 1.2+` encryption and zero foundational-model training on customer code (`Free/Pro provide a training opt-out toggle`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).

### Question 48 — `A` (Understand GitHub Copilot data and architecture)

Correct answer: A (is correct). Aggregated **operational engagement telemetry** (`shown count vs Tab/apply acceptance count per language and editor`), recorded without retaining ThalassaMarine's private C# source code for model training. [Skill 3.1: Explain data usage, flow, and sharing | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-copilot-policies-as-an-individual-subscriber)]

- **A:** Correct. Data flow architecture (`3.1`) separates operational/metrics telemetry from ephemeral prompt/completion payloads.
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **D:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).

### Question 49 — `B` (Understand GitHub Copilot data and architecture)

Correct answer: B (is correct). Inside a transient, isolated **GitHub Actions** runner environment scoped to that repository (`respecting repository branch protections and never auto-merging`). [Skill 3.1: Explain data usage, flow, and sharing | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/managing-copilot-policies-as-an-individual-subscriber)]

- **A:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **B:** Correct. Copilot Business/Enterprise data handling (`3.1`) guarantees `TLS 1.2+` encryption and zero foundational-model training on customer code (`Free/Pro provide a training opt-out toggle`).
- **C:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **D:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).

### Question 50 — `C` (Understand GitHub Copilot data and architecture)

Correct answer: C (is correct). Lines 60–85 form the **FIM suffix**, letting Copilot synthesize lines 45–59 so variable names and return type `Result<SlotAllocation, StowageError>` match line 60 seamlessly. [Skill 3.2: Describe input processing and prompt building | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot)]

- **A:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Correct. Input processing and prompt building (`3.2`) combines cursor prefix + suffix (`FIM`), relevant open-tab snippets, and repository instructions.
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 51 — `D` (Understand GitHub Copilot data and architecture)

Correct answer: D (is correct). Concatenating 1,800 `.cs` files would vastly exceed the LLM's context token limit (`and degrade latency/attention`); **RAG** retrieves only the most semantically and lexically relevant code chunks. [Skill 3.2: Describe input processing and prompt building | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot)]

- **A:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **B:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Correct. Retrieval-augmented generation (`RAG`, `3.2`) selects the highest-relevance code slices that fit within the model's context token budget.

### Question 52 — `A, C` (Understand GitHub Copilot data and architecture)

Correct answers: A and C (are correct). Inline completions assemble **FIM (`prefix + suffix`)** plus Jacobi/Jaccard-matched snippets from open tabs (`excluding Content Exclusions`), while `@workspace` retrieves indexed code chunks via **RAG**. [Skill 3.2: Describe input processing and prompt building | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot)]

- **A:** Correct. Fill-in-the-Middle (`FIM`, `3.2`) enables inline completions to align return types and variable names with surrounding downstream lines.
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Correct. Retrieval-augmented generation (`RAG`, `3.2`) selects the highest-relevance code slices that fit within the model's context token budget.
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **E:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).

### Question 53 — `B` (Understand GitHub Copilot data and architecture)

Correct answer: B (is correct). Without block-boundary stop tokens (`such as closing braces } or method boundaries`), an inline completion could keep generating unrelated extra methods past the intended cursor block. [Skill 3.3: Explain proxy filtering and post-processing | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-chat-in-your-ide)]

- **A:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **B:** Correct. Proxy filtering and post-processing (`3.3`) enforces auth, RAI moderation, public-code duplication checks, and stop-token trimming.
- **C:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 54 — `D` (Understand GitHub Copilot data and architecture)

Correct answer: D (is correct). In **post-processing inside the Copilot cloud proxy** immediately after LLM candidate generation and **before** the completion is returned to the developer's IDE. [Skill 3.3: Explain proxy filtering and post-processing | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-chat-in-your-ide)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Incorrect. False: `@github/copilot` npm installs require **Node.js 22+**, prompt for explicit user permission before modifying files/running commands by default, and use OAuth `/login` (`2.5`, `2.8`).
- **C:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **D:** Correct. Proxy filtering and post-processing (`3.3`) enforces auth, RAI moderation, public-code duplication checks, and stop-token trimming.

### Question 55 — `D, E` (Understand GitHub Copilot data and architecture)

Correct answers: D and E (are correct). Seat/OAuth entitlement verification + **RAI harm/injection filtering**, and post-inference **`~150-character` public-code duplication checking**. [Skill 3.3: Explain proxy filtering and post-processing | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-chat-in-your-ide)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **C:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **D:** Correct. Proxy filtering and post-processing (`3.3`) enforces auth, RAI moderation, public-code duplication checks, and stop-token trimming.
- **E:** Correct. Cloud-proxy post-processing (`3.3`, `3.4`) enforces both RAI content safety and public-code matching policies prior to displaying ghost text.

### Question 56 — `A` (Understand GitHub Copilot data and architecture)

Correct answer: A (is correct). Visual Studio 2022 assembles `BerthAllocator.cs` FIM prefix/suffix & neighbor tabs (`excluding Content Exclusions`), validates the `TLS 1.2+` seat token at the proxy, runs RAI + `~150+` char public-code checks, and renders ghost text ephemerally. [Skill 3.4: Visualize code suggestion lifecycle | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/paths/copilot/)]

- **A:** Correct. Correct order: IDE FIM/tab assembly (respecting exclusions) -> TLS proxy auth -> RAI + LLM + public-code filter -> ghost-text render & zero training retention.
- **B:** Incorrect. Incorrect: inline completion sends scoped editor context over TLS, never runs tests on inference GPUs, and Business/Enterprise never trains base models on customer prompts.
- **C:** Incorrect. Incorrect: Content Exclusions block excluded paths from entering prompts, and prompts are never published to Gists.
- **D:** Incorrect. Incorrect: Copilot LLM inference and public-code duplication checks execute in the cloud proxy over authenticated TLS.

### Question 57 — `B` (Understand GitHub Copilot data and architecture)

Correct answer: B (is correct). Debouncing avoids firing redundant network/LLM requests on every single keystroke that would immediately become obsolete before arriving. [Skill 3.4: Visualize code suggestion lifecycle | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/paths/copilot/)]

- **A:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **B:** Correct. Code suggestion lifecycle (`3.4`) traces a completion from keystroke pause through IDE context assembly, cloud proxy inference/filtering, and ghost-text display.
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).

### Question 58 — `D` (Understand GitHub Copilot data and architecture)

Correct answer: D (is correct). Local IDE Copilot Chat sees only your open workspace/attached context (`and pre-training knowledge`), NOT unindexed commits in sibling private repositories unless grounded via a **Copilot Space** or **GitHub MCP** server. [Skill 3.5: Describe limitations of LLMs and Copilot | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-coding-agent)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **C:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **D:** Correct. LLM and Copilot limitations (`3.5`) explain why models hallucinate post-cutoff APIs, vary across runs, truncate overflow tokens, and need tests/MCP.

### Question 59 — `A` (Understand GitHub Copilot data and architecture)

Correct answer: A (is correct). Public training corpora contain over two decades of C# `params T[]` code compared with newer C# 13 `ReadOnlySpan<T>` patterns; pinning `<LangVersion>13</LangVersion>` and `.instructions.md` guidance steers modern syntax. [Skill 3.5: Describe limitations of LLMs and Copilot | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-coding-agent)]

- **A:** Correct. LLM and Copilot limitations (`3.5`) explain why models hallucinate post-cutoff APIs, vary across runs, truncate overflow tokens, and need tests/MCP.
- **B:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **C:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **D:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).

### Question 60 — `A` (Understand GitHub Copilot data and architecture)

Correct answer: A (is correct). No — inline token prediction performs zero lock-graph or concurrent execution verification; concurrency safety requires explicit transaction ordering, integration stress tests, and engineering review. [Skill 3.5: Describe limitations of LLMs and Copilot | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/responsible-use/copilot-coding-agent)]

- **A:** Correct. LLM and Copilot limitations (`3.5`) explain why models hallucinate post-cutoff APIs, vary across runs, truncate overflow tokens, and need tests/MCP.
- **B:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).

### Question 61 — `C` (Apply prompt engineering and context crafting)

Correct answer: C (is correct). It specifies **Target File (`#file:`)**, **Exact Method Signature (`ReadOnlySpan<char>`)**, **Domain Checksum Rule**, and **Zero-Allocation Constraint**. [Skill 4.1: Describe prompt structure and context | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat)]

- **A:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **B:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **C:** Correct. Prompt structure (`4.1`) combines clear intent, grounded workspace context, explicit constraints, and expected output format.
- **D:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).

### Question 62 — `A` (Apply prompt engineering and context crafting)

Correct answer: A (is correct). Strong domain value types (`LengthMeters`, `DraftMeters`), explicit nullable return `VesselBerth?`, and `CancellationToken ct` encode null-handling and async cancellation requirements right in the FIM signature. [Skill 4.1: Describe prompt structure and context | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat)]

- **A:** Correct. In-editor context signals (`4.1`, `4.4`) anchor Fill-in-the-Middle inline completions without leaving the code buffer.
- **B:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **C:** Incorrect. Copilot Audit Logs and Metrics API (`2.14`) separate security/compliance event logs from anonymized (`>=5`-user) adoption telemetry.
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 63 — `A` (Apply prompt engineering and context crafting)

Correct answer: A (is correct). Using `#sym:ICustomsClearancePolicy` (`#symbol`) injects the targeted symbol definition into the prompt without wasting context tokens on unrelated types in the file. [Skill 4.2: Understand how context is determined | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)]

- **A:** Correct. Context determination (`4.2`) controls which open tabs, `#` chat variables, workspace indexes, and path-matched instructions enter the prompt.
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **D:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).

### Question 64 — `D` (Apply prompt engineering and context crafting)

Correct answer: D (is correct). `.github/copilot-instructions.md` (`repo-wide`) plus `blazor.instructions.md` (`matching **/*.razor`), while `dotnet.instructions.md` (`**/*.cs`) stays unloaded unless a `.cs` code-behind file is also in context. [Skill 4.2: Understand how context is determined | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)]

- **A:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **B:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **C:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **D:** Correct. Context determination (`4.2`) controls which open tabs, `#` chat variables, workspace indexes, and path-matched instructions enter the prompt.

### Question 65 — `C, E` (Apply prompt engineering and context crafting)

Correct answers: C and E (are correct). Close unrelated SQL/YAML/old module tabs while keeping `IBaplieParser.cs` + `BaplieSegment.cs` open, and attach explicit `#file:` references in Chat/Edits. [Skill 4.2: Understand how context is determined | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **C:** Correct. Curating open tabs and `#file:` attachments (`4.2`, `4.4`) directly improves prompt signal-to-noise ratio.
- **D:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **E:** Correct. Context determination (`4.2`) controls which open tabs, `#` chat variables, workspace indexes, and path-matched instructions enter the prompt.

### Question 66 — `C` (Apply prompt engineering and context crafting)

Correct answer: C (is correct). Provide **few-shot prompting** (`2–3 exact raw EDIFACT segment -> PortCallLocation record input/output pairs`) plus the qualifier lookup table. [Skill 4.3: Use zero-shot and few-shot prompting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **C:** Correct. Zero-shot vs few-shot prompting (`4.3`) reserves token-heavier exemplars for custom team patterns that general pretraining cannot infer.
- **D:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).

### Question 67 — `A` (Apply prompt engineering and context crafting)

Correct answer: A (is correct). C# switch-expression conversion is a deterministic syntactic transformation well represented in pre-training, requiring zero extra example pairs. [Skill 4.3: Use zero-shot and few-shot prompting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/prompt-engineering-for-copilot-chat)]

- **A:** Correct. Zero-shot vs few-shot prompting (`4.3`) reserves token-heavier exemplars for custom team patterns that general pretraining cannot infer.
- **B:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **C:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **D:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.

### Question 68 — `A` (Apply prompt engineering and context crafting)

Correct answer: A (is correct). Decompose method-by-method: `(1)` generate xUnit characterization tests -> `(2)` define EF Core 9 entity/configuration -> `(3)` migrate and test `2–3` query/command methods per iteration. [Skill 4.4: Apply best practices for prompt crafting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)]

- **A:** Correct. Prompt-crafting best practices (`4.4`) favor incremental decomposition, version pinning, and feedback-driven iteration.
- **B:** Incorrect. Clean editor tabs, `/clear` between topics, and `#runSubagent` isolation (`4.2`, `4.6`) prevent context confusion.
- **C:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **D:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).

### Question 69 — `C` (Apply prompt engineering and context crafting)

Correct answer: C (is correct). Positive, concrete API targets (`TypedResults.ValidationProblem`, `FluentValidation`) anchor token probabilities directly to the desired `.NET 9` Minimal API classes. [Skill 4.4: Apply best practices for prompt crafting | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Correct. Prompt-crafting best practices (`4.4`) favor incremental decomposition, version pinning, and feedback-driven iteration.
- **D:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).

### Question 70 — `D` (Apply prompt engineering and context crafting)

Correct answer: D (is correct). Enabling `"chat.promptFiles": true` + creating `.github/prompts/xunit-characterization.prompt.md` -> linking `#file:` exemplars in Git -> invoking `/xunit-characterization` with clean tabs -> running `/clear` before switching tasks. [Skill 4.5: Explain prompt engineering principles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/paths/gh-copilot-2/)]

- **A:** Incorrect. Incorrect: never embed secrets in repository prompt files, and one-word prompts lack actionable context.
- **B:** Incorrect. Incorrect: `.github/workflows/*.yml` defines Actions workflows (not `.github/prompts/*.prompt.md`), and stale tabs + long threads cause context drift.
- **C:** Incorrect. Incorrect: reusable prompt files end in `.prompt.md` under `.github/prompts/` (`whereas applyTo: belongs to *.instructions.md`).
- **D:** Correct. Correct order: create `.github/prompts/*.prompt.md` -> link few-shot exemplars -> invoke `/api` with clean tab context -> reset chat on topic switch.

### Question 71 — `C` (Apply prompt engineering and context crafting)

Correct answer: C (is correct). Linking `#file:src/Protos/common.proto` dynamically pulls the **live current version** of `common.proto` at execution time (`preventing stale copy-pasted schema drift`). [Skill 4.5: Explain prompt engineering principles | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/paths/gh-copilot-2/)]

- **A:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **B:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **C:** Correct. Prompt engineering principles (`4.5`) emphasize specificity, positive constraints, authoritative grounding, and reusable templates.
- **D:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).

### Question 72 — `B` (Apply prompt engineering and context crafting)

Correct answer: B (is correct). Running `/session checkpoints` (`and /session checkpoints NUMBER`) lists and inspects session compaction snapshots created as conversational history grows. [Skill 4.6: Describe prompt process flow and chat history usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Correct. Prompt process flow and chat history management (`4.6`) prevent context drift and token-window eviction across unrelated tasks.
- **C:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **D:** Incorrect. False: `#runSubagent` runs autonomously in its **own isolated context window** without pausing for user feedback, returning only the distilled result (`2.9`).

### Question 73 — `B, C` (Apply prompt engineering and context crafting)

Correct answers: B and C (are correct). Run `/clear` (`New Chat`) whenever switching from one microservice or ticket to an unrelated task, and use `#runSubagent` for multi-file codebase discovery so main chat history stays lean. [Skill 4.6: Describe prompt process flow and chat history usage | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Correct. Prompt process flow and chat history management (`4.6`) prevent context drift and token-window eviction across unrelated tasks.
- **C:** Correct. Resetting chat history on task switches (`4.6`) avoids context confusion and token-window truncation.
- **D:** Incorrect. Clean editor tabs, `/clear` between topics, and `#runSubagent` isolation (`4.2`, `4.6`) prevent context confusion.
- **E:** Incorrect. False: `#runSubagent` runs autonomously in its **own isolated context window** without pausing for user feedback, returning only the distilled result (`2.9`).

### Question 74 — `C` (Improve developer productivity with GitHub Copilot)

Correct answer: C (is correct). Use `/doc` (`or Copilot Edits`) on each public interface so Copilot drafts XML documentation tags directly from method signatures and `throw` clauses, verified via `CS1591` compiler warnings. [Skill 5.1: Use Copilot for code generation, refactoring, and documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/developer-use-cases-for-ai-with-github-copilot/)]

- **A:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Correct. Code generation, refactoring, and documentation (`5.1`) accelerates boilerplate, structural cleanup, and API docs while preserving behavior.
- **D:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).

### Question 75 — `A` (Improve developer productivity with GitHub Copilot)

Correct answer: A (is correct). Extract `IEmailSender`, `IManifestRepository`, and .NET `TimeProvider` constructor-injected dependencies (`Dependency Inversion`), decoupling pure manifest business rules from infrastructure I/O. [Skill 5.1: Use Copilot for code generation, refactoring, and documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/developer-use-cases-for-ai-with-github-copilot/)]

- **A:** Correct. Code generation, refactoring, and documentation (`5.1`) accelerates boilerplate, structural cleanup, and API docs while preserving behavior.
- **B:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.
- **C:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).

### Question 76 — `C` (Improve developer productivity with GitHub Copilot)

Correct answer: C (is correct). No — `Ask` mode cannot autonomously edit multiple `.csproj`/`.cs` files or run iterative `dotnet build` terminal loops; use **Agent Mode** (`or Copilot CLI`). [Skill 5.1: Use Copilot for code generation, refactoring, and documentation | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/developer-use-cases-for-ai-with-github-copilot/)]

- **A:** Incorrect. The proposed GitHub Copilot configuration or workflow violates at least one stated governance, privacy, or technical requirement. No — `Ask` mode cannot autonomously edit multiple `.csproj`/`.cs` files or run iterative `dotnet build` terminal loops; use **Agent Mode** (`or Copilot CLI`).
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Correct. Only **Agent Mode** (or **Copilot CLI**, `2.2`, `2.9`) autonomously edits multiple files and runs terminal verification loops.
- **D:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).

### Question 77 — `C` (Improve developer productivity with GitHub Copilot)

Correct answer: C (is correct). Use `/explain` on the VB.NET procedures to surface implicit type coercions and rounding rules (`and generate characterization tests`) before translating to `Option Strict` C# 13. [Skill 5.2: Accelerate learning and reduce context switching | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/copilot-chat-cookbook)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **C:** Correct. Accelerating learning and reducing context switching (`5.2`) keeps developers productive inside the IDE and terminal.
- **D:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).

### Question 78 — `A` (Improve developer productivity with GitHub Copilot)

Correct answer: A (is correct). Highlight the error in the integrated terminal and invoke `@terminal /explain` or `@terminal /fix` (`attaching the relevant EF Core repository file`). [Skill 5.2: Accelerate learning and reduce context switching | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/copilot-chat-cookbook)]

- **A:** Correct. Accelerating learning and reducing context switching (`5.2`) keeps developers productive inside the IDE and terminal.
- **B:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **C:** Incorrect. False: reusable Copilot Chat prompt files are Markdown files (`*.prompt.md`) stored in `.github/prompts/` (`with "chat.promptFiles": true`) and invoked on-demand (`2.12`).
- **D:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.

### Question 79 — `B` (Improve developer productivity with GitHub Copilot)

Correct answer: B (is correct). Mapping legacy demurrage rules & invariants via `/explain` and `@workspace` -> building xUnit characterization & boundary tests -> refactoring incrementally via Copilot Edits / Agent Mode -> re-running `dotnet test`, `CodeQL` & benchmarks. [Skill 5.3: Generate sample data and modernize legacy code | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/tutorials/modernize-legacy-code)]

- **A:** Incorrect. Incorrect: always synthesize fake test data (`never real PII/PCI`) and replace SQL concatenation with parameterized queries.
- **B:** Correct. Correct order: map legacy behavior -> lock behavior with characterization/edge-case tests -> refactor incrementally -> verify parity, security & performance.
- **C:** Incorrect. Incorrect: monolithic rewrites exceed LLM context windows and deleting failing tests destroys regression safety.
- **D:** Incorrect. Incorrect: tautological assertions detect zero regressions; tests must assert real outputs and boundary conditions.

### Question 80 — `D` (Improve developer productivity with GitHub Copilot)

Correct answer: D (is correct). Attach ONLY the C# record definitions (`zero production crew exports`) and ask Copilot to write a seeded **Bogus (`Faker<T>`)** generator computing valid synthetic IMO checksums. [Skill 5.3: Generate sample data and modernize legacy code | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/tutorials/modernize-legacy-code)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **C:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **D:** Correct. Sample data generation and legacy modernization (`5.3`) combine synthetic non-PII fixtures with test-backed incremental upgrades.

### Question 81 — `B` (Improve developer productivity with GitHub Copilot)

Correct answer: B (is correct). No — 45,000 lines vastly exceed LLM input/output token limits and skip characterization testing; modernize slice-by-slice (`one vertical feature per clean Agent Mode session backed by tests`). [Skill 5.3: Generate sample data and modernize legacy code | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/tutorials/modernize-legacy-code)]

- **A:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **B:** Correct. Clean editor tabs, `/clear` between topics, and `#runSubagent` isolation (`4.2`, `4.6`) prevent context confusion.
- **C:** Incorrect. The proposed GitHub Copilot configuration or workflow violates at least one stated governance, privacy, or technical requirement. No — 45,000 lines vastly exceed LLM input/output token limits and skip characterization testing; modernize slice-by-slice (`one vertical feature per clean Agent Mode session backed by tests`).
- **D:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).

### Question 82 — `A` (Improve developer productivity with GitHub Copilot)

Correct answer: A (is correct). Prompt Copilot to use **`Microsoft.AspNetCore.Mvc.Testing.WebApplicationFactory<Program>`** (`paired with Testcontainers for Postgres/Redis`) so the full HTTP pipeline is exercised in-memory. [Skill 5.4: Generate unit and integration tests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/develop-unit-tests-using-github-copilot-tools/)]

- **A:** Correct. Generating unit and integration tests (`5.4`) automates test scaffolding, dependency isolation, and parameterized coverage.
- **B:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **C:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **D:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).

### Question 83 — `C, D` (Improve developer productivity with GitHub Copilot)

Correct answers: C and D (are correct). Write `[Theory]` / `[InlineData]` characterization tests locking legacy outputs before refactors, and mock external HTTP/SMTP interfaces (`NSubstitute` / `FakeTimeProvider`) while testing real domain classes. [Skill 5.4: Generate unit and integration tests | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://learn.microsoft.com/en-us/training/modules/develop-unit-tests-using-github-copilot-tools/)]

- **A:** Incorrect. False: the Copilot coding agent works on an isolated `copilot/*` branch, opens a **draft pull request**, respects branch protections, and requires human review (`2.9`, `2.10`).
- **B:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **C:** Correct. Generating unit and integration tests (`5.4`) automates test scaffolding, dependency isolation, and parameterized coverage.
- **D:** Correct. Characterization testing (`5.3`, `5.4`) guarantees legacy modernization preserves subtle business edge cases.
- **E:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).

### Question 84 — `C` (Improve developer productivity with GitHub Copilot)

Correct answer: C (is correct). It is a **tautological mock test** that mocks the system under test itself (`proving only that NSubstitute returns 500m` while exercising zero production code in `DemurrageService`)! [Skill 5.5: Identify edge cases and write assertions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/copilot-chat-cookbook)]

- **A:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Correct. Edge-case identification and assertion quality (`5.5`) ensures tests catch real boundary defects rather than inflating superficial coverage.
- **D:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).

### Question 85 — `A, B, C` (Improve developer productivity with GitHub Copilot)

Correct answers: A, B, and C (are correct). Test boundary values (`0 free hours, departure < arrival, DateTimeOffset offset mismatches, decimal.MaxValue, cancellation`), preserve legacy invariants with characterization tests, and verify `CodeQL` Autofix patches use parameterized SQL/EF queries. [Skill 5.5: Identify edge cases and write assertions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/copilot-chat-cookbook)]

- **A:** Correct. Characterization testing (`5.3`, `5.4`) guarantees legacy modernization preserves subtle business edge cases.
- **B:** Correct. Edge-case identification and assertion quality (`5.5`) ensures tests catch real boundary defects rather than inflating superficial coverage.
- **C:** Correct. Verified security remediation (`5.6`) confirms Autofix patches eliminate root-cause injection sinks without breaking callers.
- **D:** Incorrect. False: never place real PII/PHI/PCI data in prompts or repository instruction files; ask Copilot to generate schema-conforming **synthetic** fixtures instead (`1.3`, `5.3`).
- **E:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **F:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).

### Question 86 — `A` (Improve developer productivity with GitHub Copilot)

Correct answer: A (is correct). Review the Autofix diff (`confirming trailing directory separator handling so /var/data-evil doesn't match /var/data`), add xUnit `../` traversal regression tests, and confirm `CodeQL` passes. [Skill 5.6: Suggest security improvements and performance optimizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/responsible-use-autofix-code-scanning)]

- **A:** Correct. Security and performance optimization (`5.6`) pairs Copilot/Autofix patches with profiler benchmarks and SAST re-scans.
- **B:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **C:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **D:** Incorrect. False: Copilot Content Exclusions apply strictly to **GitHub Copilot** features—they never restrict Git repository ACLs, Actions workflows, or `CodeQL` (`6.1`).

### Question 87 — `D` (Improve developer productivity with GitHub Copilot)

Correct answer: D (is correct). Refactor `Split(',')` to zero-allocation `ReadOnlySpan<char>` range enumeration (`MemoryExtensions.Split` in .NET 9) and measure heap allocations (`[MemoryDiagnoser]`) with **BenchmarkDotNet**. [Skill 5.6: Suggest security improvements and performance optimizations | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/code-security/code-scanning/managing-code-scanning-alerts/responsible-use-autofix-code-scanning)]

- **A:** Incorrect. False: vague one-word prompts combined with dozens of noisy tabs and stale chat history degrade relevance (`4.1`, `4.4`, `4.6`).
- **B:** Incorrect. False: mocking the unit under test or writing tautological assertions provides zero behavioral verification (`1.4`, `5.4`, `5.5`).
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Correct. Security and performance optimization (`5.6`) pairs Copilot/Autofix patches with profiler benchmarks and SAST re-scans.

### Question 88 — `C` (Configure privacy, content exclusions, and safeguards)

Correct answer: C (is correct). Configuring `fnmatch` globs for `/customs-bonds/**` in `Content exclusion`, waiting `<=30 min` (`or reloading Visual Studio/VS Code`), verifying the disabled Copilot icon + `copilot.content_exclusion_changed` audit event, and preventing cross-file LSP leaks completes rollout. [Skill 6.1: Configure content exclusions and editor settings | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion)]

- **A:** Incorrect. Incorrect: `.gitignore` does not exclude already-tracked repository files from Copilot context.
- **B:** Incorrect. Incorrect: Repository admins CANNOT override or remove Organization-level Content Exclusions (`rules combine additively`), and sync takes `<=30 minutes`.
- **C:** Correct. Correct order: configure YAML `fnmatch` globs -> allow `<=30 min` IDE sync -> verify crossed-out icon & audit log -> mind IDE LSP type-hover nuance.
- **D:** Incorrect. Incorrect: Content Exclusions require **Copilot Business or Enterprise**, use `fnmatch` globs, and govern Copilot context—not Git ACLs or Actions.

### Question 89 — `B` (Configure privacy, content exclusions, and safeguards)

Correct answer: B (is correct). Copilot Content Exclusion `fnmatch` rules are evaluated **case-insensitively**, so `- "/customs/tariff.json"` protects `/Customs/Tariff.json` as well. [Skill 6.1: Configure content exclusions and editor settings | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion)]

- **A:** Incorrect. False: Copilot Content Exclusions apply strictly to **GitHub Copilot** features—they never restrict Git repository ACLs, Actions workflows, or `CodeQL` (`6.1`).
- **B:** Correct. Content Exclusion configuration (`6.1`) enforces additive Org + Repo `fnmatch` path exclusions across Business and Enterprise seats.
- **C:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **D:** Incorrect. Content Exclusions (`2.3`, `6.1`) are only enforced for seats governed under Copilot Business or Copilot Enterprise.

### Question 90 — `D` (Configure privacy, content exclusions, and safeguards)

Correct answer: D (is correct). Yes — Copilot Content Exclusions apply strictly to **GitHub Copilot features**; they never block Git checkouts, **GitHub Actions** runners, or `CodeQL` scans. [Skill 6.1: Configure content exclusions and editor settings | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion)]

- **A:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Incorrect. False: Copilot Content Exclusions apply strictly to **GitHub Copilot** features—they never restrict Git repository ACLs, Actions workflows, or `CodeQL` (`6.1`).
- **D:** Correct. Content Exclusion scope limits (`2.3`, `6.1`) distinguish Copilot prompt blocking from IDE LSP type inference, Git ACLs, and CI scanners.

### Question 91 — `B` (Configure privacy, content exclusions, and safeguards)

Correct answer: B (is correct). No — `.gitignore` neither untrack already-committed Git files nor configures Copilot Content Exclusions; configure `- "/Data/ProprietaryRates.csv"` in Copilot **Content exclusion** settings. [Skill 6.1: Configure content exclusions and editor settings | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/managing-copilot/configuring-and-auditing-content-exclusion)]

- **A:** Incorrect. The proposed GitHub Copilot configuration or workflow violates at least one stated governance, privacy, or technical requirement. No — `.gitignore` neither untrack already-committed Git files nor configures Copilot Content Exclusions; configure `- "/Data/ProprietaryRates.csv"` in Copilot **Content exclusion** settings.
- **B:** Correct. Adding a tracked path to `.gitignore` (`6.1`) does NOT stop Copilot from reading that file in the IDE or on GitHub.com.
- **C:** Incorrect. False: Copilot Content Exclusions apply strictly to **GitHub Copilot** features—they never restrict Git repository ACLs, Actions workflows, or `CodeQL` (`6.1`).
- **D:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).

### Question 92 — `B` (Configure privacy, content exclusions, and safeguards)

Correct answer: B (is correct). The customer must use **Copilot Business or Copilot Enterprise** AND keep the **`Suggestions matching public code`** filter enabled (**`Block`**) without disabling filtering controls. [Skill 6.2: Describe ownership and limitations of outputs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/about-github-copilot/plans-for-github-copilot)]

- **A:** Incorrect. Content Exclusions (`2.3`, `6.1`) are only enforced for seats governed under Copilot Business or Copilot Enterprise.
- **B:** Correct. Output ownership and IP Indemnity (`6.2`) require Business/Enterprise licensing with the public-code duplication filter enabled (`Block`).
- **C:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **D:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).

### Question 93 — `D` (Configure privacy, content exclusions, and safeguards)

Correct answer: D (is correct). No — IP Indemnity covers **unmodified eligible GitHub Copilot suggestions** (`generated with Block enabled`), never intentional infringement or code manually introduced/modified by users. [Skill 6.2: Describe ownership and limitations of outputs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/about-github-copilot/plans-for-github-copilot)]

- **A:** Incorrect. False: inline completions are probabilistic token predictions (`non-deterministic`) and are NOT compiled or formally verified prior to rendering (`1.1`, `3.5`).
- **B:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **C:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **D:** Correct. Output ownership and IP Indemnity (`6.2`) require Business/Enterprise licensing with the public-code duplication filter enabled (`Block`).

### Question 94 — `B` (Configure privacy, content exclusions, and safeguards)

Correct answer: B (is correct). Configuring `"github.copilot.enable": { "*": true, "plaintext": false, "dotenv": false }` toggles inline completions per language identifier in VS Code. [Skill 6.2: Describe ownership and limitations of outputs | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/about-github-copilot/plans-for-github-copilot)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Correct. Individual privacy settings (`3.1`, `6.1`) govern optional snippet training on personal plans (`whereas Business/Enterprise disable code-snippet training by default`).
- **C:** Incorrect. False: Copilot Business and Enterprise **never** use customer prompts or suggestions to train shared foundational models (`3.1`).
- **D:** Incorrect. Copilot User Management REST API (`2.15`) provisions seats, audits `last_activity_at` dormancy, and cancels seats cleanly.

### Question 95 — `D` (Configure privacy, content exclusions, and safeguards)

Correct answer: D (is correct). Approximately **`150` characters** (`~150+` chars) of lexical overlap with public GitHub code triggers duplication filtering (`suppressing under Block, or logging repo/license citations in Code Referencing under Allow`). [Skill 6.3: Enable suggestions matching public code filtering | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/finding-public-code-that-matches-github-copilot-suggestions)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **C:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **D:** Correct. Public-code duplication filtering and Code Referencing (`6.3`) either block `~150+` char verbatim public matches or surface repo/license provenance.

### Question 96 — `C` (Configure privacy, content exclusions, and safeguards)

Correct answer: C (is correct). No — suggestions generated while the public-code filter is set to **`Allow`** are **not** covered by GitHub Copilot IP Indemnity; commercial production orgs must enforce **`Block`**. [Skill 6.3: Enable suggestions matching public code filtering | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/finding-public-code-that-matches-github-copilot-suggestions)]

- **A:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **B:** Incorrect. The proposed GitHub Copilot configuration or workflow violates at least one stated governance, privacy, or technical requirement. No — suggestions generated while the public-code filter is set to **`Allow`** are **not** covered by GitHub Copilot IP Indemnity; commercial production orgs must enforce **`Block`**.
- **C:** Correct. Enabling `Block` on public-code duplication (`6.2`, `6.3`) is a mandatory condition for GitHub Copilot IP Indemnity protection.
- **D:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).

### Question 97 — `A, E` (Configure privacy, content exclusions, and safeguards)

Correct answers: A and E (are correct). The **most restrictive** active organization policy (**`Block`**) governs the consultant's IDE sessions, and any candidate completion matching `~150+` characters of public GitHub code is suppressed before reaching the editor. [Skill 6.3: Enable suggestions matching public code filtering | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/using-github-copilot/finding-public-code-that-matches-github-copilot-suggestions)]

- **A:** Correct. Multi-organization policy resolution (`2.13`, `6.4`) always applies the strictest safeguard across a user's active memberships.
- **B:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **C:** Incorrect. False: `Allow` permits public-code matches (`logging licenses via Code Referencing`) and **voids** public-code IP Indemnity coverage; open-source licenses still govern matched code (`6.2`, `6.3`).
- **D:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **E:** Correct. Public-code duplication filtering and Code Referencing (`6.3`) either block `~150+` char verbatim public matches or surface repo/license provenance.

### Question 98 — `D` (Configure privacy, content exclusions, and safeguards)

Correct answer: D (is correct). Use `- "**/Customs/*.json"` so `fnmatch` matches `Customs/*.json` both at the repo root and inside nested subdirectories like `/src/Customs/`. [Skill 6.4: Resolve issues with suggestions and content exclusions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
- **C:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **D:** Correct. Troubleshooting Copilot (`6.4`) checks multi-org policy precedence (`most restrictive wins`), Content Exclusion icons, filetype settings, and proxy/TLS trust.

### Question 99 — `B` (Configure privacy, content exclusions, and safeguards)

Correct answer: B (is correct). Repository-specific Content Exclusions identify the target repository via its **Git remote URL (`origin`)**; without a matching GitHub remote, the IDE cannot map the local folder to that repository's exclusion rules (`though Org-wide "*" exclusions still protect org seat holders where applicable — always verify git remote -v`). [Skill 6.4: Resolve issues with suggestions and content exclusions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot)]

- **A:** Incorrect. False: Copilot Content Exclusions apply strictly to **GitHub Copilot** features—they never restrict Git repository ACLs, Actions workflows, or `CodeQL` (`6.1`).
- **B:** Correct. Troubleshooting Copilot (`6.4`) checks multi-org policy precedence (`most restrictive wins`), Content Exclusion icons, filetype settings, and proxy/TLS trust.
- **C:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **D:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).

### Question 100 — `B, C` (Configure privacy, content exclusions, and safeguards)

Correct answers: B and C (are correct). Configure the IDE/OS HTTP proxy + trust the corporate TLS root CA (`Windows Certificate Store / NODE_EXTRA_CA_CERTS`), and allowlist outbound `HTTPS 443` to GitHub Copilot endpoints (`*.githubcopilot.com`, `api.github.com`, `github.com`). [Skill 6.4: Resolve issues with suggestions and content exclusions | Study Guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300 | Reference: GitHub Copilot Documentation (https://docs.github.com/en/copilot/troubleshooting-github-copilot/troubleshooting-common-issues-with-github-copilot)]

- **A:** Incorrect. False: GitHub Copilot performs LLM inference and public-code duplication filtering in GitHub's cloud service over `TLS 1.2+` (`3.2`–`3.4`).
- **B:** Correct. Network & SSL-proxy configuration (`6.4`) resolves connection blocks and certificate trust errors in corporate IDEs.
- **C:** Correct. Troubleshooting Copilot (`6.4`) checks multi-org policy precedence (`most restrictive wins`), Content Exclusion icons, filetype settings, and proxy/TLS trust.
- **D:** Incorrect. False: `.github/copilot-instructions.md` provides natural-language coding guidance and can **never** bypass Organization or Repository Content Exclusions (`2.11`, `6.1`).
- **E:** Incorrect. False: across multiple organization policies, GitHub always enforces the **most restrictive** policy (`Block` overrides `Allow`; `Disabled` overrides `Enabled`, `6.4`).
