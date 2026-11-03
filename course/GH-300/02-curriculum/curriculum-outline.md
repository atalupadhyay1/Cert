# Curriculum Outline — Microsoft / GitHub Exam GH-300: GitHub Copilot (`August 7, 2026` Study Guide)

- **Official Study Guide:** `https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-300` (*Skills measured as of August 7, 2026 · Last updated July 9, 2026*)
- **Official Certification Page:** `https://learn.microsoft.com/en-us/credentials/certifications/github-copilot/` (*Updated August 7, 2026*)
- **Exam Delivery:** `100 minutes` exam time (`120 minutes` seat duration) · `$99 USD` · Pearson VUE · `700 / 1000` scaled passing score · **2-year validity** · **Closed-book** (no Microsoft Learn / GitHub Docs access) · **0 case studies / 0 live labs** · Languages: `English, Spanish, Portuguese (Brazil), Korean, Japanese`

---

## Six-Exam Architectural Progression (`6 × 100 = 600` Questions)

| Set | Enterprise Organization Persona | Architectural Focus | MC (`S`+`O`) | MS (`M2`+`M3`) | `____` | `Proposed solution:` |
|:---:|---|---|:---:|:---:|:---:|:---:|
| **1** | **VesperaPay Ledger** (`Go/TypeScript PCI-DSS fintech`) | Responsible AI Governance, IDE Inline/Chat Workflows & Cloud Proxy Architecture — FIM, RAG, Plan Tiers & Public-Code Blocking | `84` | `16` | `23` | `7` |
| **2** | **StratosFlight Avionics** (`Rust/C++20 DO-178C telemetry`) | Agentic GitHub Copilot CLI (`@github/copilot`), Agent Mode, Sub-Agents (`#runSubagent`), `.vscode/mcp.json` & Agent Sessions | `84` | `16` | `22` | `7` |
| **3** | **Clarivance Health** (`Python/FastAPI HIPAA clinical`) | Copilot Spaces, GitHub Spark, Custom Instructions (`applyTo:` / `excludeAgent:`), `.prompt.md` Templates & Copilot Code Review | `84` | `16` | `20` | `7` |
| **4** | **MeridiaGrid Energy** (`Java 21/Kotlin smart-grid OT/IT`) | Prompt Engineering, Context Crafting, Zero-Shot vs Few-Shot, FIM Prefix/Suffix Steering & Chat Token Window Hygiene | `84` | `16` | `20` | `8` |
| **5** | **ThalassaMarine Logistics** (`.NET 9/C# port & vessel ERP`) | Legacy Modernization, Characterization Suites, Boundary/Edge-Case Unit Testing & `CodeQL` Copilot Autofix Remediation | `84` | `16` | `20` | `6` |
| **6** | **ArdentBio Therapeutics** (`Python/TS/R genomics GHEC`) | GHEC Privacy, `fnmatch` Content Exclusions, Public-Code Duplication (`Block` vs `Code Referencing`), IP Indemnity & REST Seat APIs | `84` | `16` | `20` | `8` |

---

## Complete 41-Skill Allocation Per Practice Set

### Domain 1 — Use GitHub Copilot responsibly (`15–20%` -> `18` items/set · `108` total)
- `1.1` (`4/set`): Understand the risks and limitations of generative AI
- `1.2` (`4/set`): Apply ethical and responsible AI usage principles
- `1.3` (`3/set`): Identify potential harms and apply mitigation strategies
- `1.4` (`4/set`): Recognize the need to validate AI-generated output
- `1.5` (`3/set`): Operate GitHub Copilot responsibly

### Domain 2 — Use GitHub Copilot features (`25–30%` -> `28` items/set · `168` total)
- `2.1` (`2/set`): Enable GitHub Copilot in an IDE
- `2.2` (`2/set`): Trigger inline suggestions, chat, CLI, and agent mode
- `2.3` (`2/set`): Apply knowledge of content exclusions in the IDE
- `2.4` (`1/set`): Define the GitHub Copilot CLI and its key benefits
- `2.5` (`2/set`): Install and get started with the GitHub Copilot CLI
- `2.6` (`2/set`): Apply GitHub Copilot CLI features and commands
- `2.7` (`2/set`): Use interactive and session-based CLI workflows
- `2.8` (`2/set`): Generate scripts and manage file operations with the CLI
- `2.9` (`3/set`): Use Agent Mode, Copilot Edits, Model Context Protocol (MCP), Agent Sessions, and Sub-Agents
- `2.10` (`2/set`): Request code reviews and coding assistance from GitHub Copilot
- `2.11` (`3/set`): Use Copilot Spaces, GitHub Spark, pull request summaries, and custom instructions for code review
- `2.12` (`2/set`): Navigate Copilot Chat limitations, configuration options, feedback mechanisms, commands, and prompt file reuse
- `2.13` (`1/set`): Configure organization-wide Copilot policies, Code Review policies, and feature availability across IDEs and github.com
- `2.14` (`1/set`): Review GitHub Copilot audit log events at the organization level
- `2.15` (`1/set`): Manage GitHub Copilot subscriptions via the REST API

### Domain 3 — Understand GitHub Copilot data and architecture (`10–15%` -> `14` items/set · `84` total)
- `3.1` (`3/set`): Understand how GitHub Copilot uses, flows, and shares data
- `3.2` (`3/set`): Describe input processing and prompt building in GitHub Copilot
- `3.3` (`3/set`): Explain proxy server filtering and post-processing mechanisms
- `3.4` (`2/set`): Trace the code suggestion lifecycle from editor to model and back
- `3.5` (`3/set`): Recognize the limitations of large language models and GitHub Copilot

### Domain 4 — Apply prompt engineering and context crafting (`10–15%` -> `13` items/set · `78` total)
- `4.1` (`2/set`): Understand the fundamentals of prompt structure and context
- `4.2` (`3/set`): Explain how context is determined for GitHub Copilot
- `4.3` (`2/set`): Apply zero-shot and few-shot prompting techniques
- `4.4` (`2/set`): Apply prompt crafting best practices for code generation
- `4.5` (`2/set`): Apply prompt engineering principles to real-world scenarios
- `4.6` (`2/set`): Understand prompt process flow and how chat history is used

### Domain 5 — Improve developer productivity with GitHub Copilot (`10–15%` -> `14` items/set · `84` total)
- `5.1` (`3/set`): Use GitHub Copilot for code generation, refactoring, and documentation
- `5.2` (`2/set`): Accelerate learning and reduce context switching with GitHub Copilot
- `5.3` (`3/set`): Generate sample data and modernize legacy applications
- `5.4` (`2/set`): Generate and improve unit and integration tests with GitHub Copilot
- `5.5` (`2/set`): Identify edge cases and strengthen test assertions using GitHub Copilot
- `5.6` (`2/set`): Apply GitHub Copilot for security improvements and performance optimizations

### Domain 6 — Configure privacy, content exclusions, and safeguards (`10–15%` -> `13` items/set · `78` total)
- `6.1` (`4/set`): Configure content exclusions at repository and organization levels, and manage editor privacy settings
- `6.2` (`3/set`): Understand ownership of GitHub Copilot outputs and intellectual property indemnity limits
- `6.3` (`3/set`): Configure and validate code duplication detection filters (suggestions matching public code)
- `6.4` (`3/set`): Troubleshoot missing code suggestions and content exclusion configurations
