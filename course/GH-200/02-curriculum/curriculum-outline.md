# Curriculum Outline — Microsoft / GitHub Exam GH-200: GitHub Actions (`January 2026` Study Guide)

- **Official Study Guide:** `https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-200` (*Skills measured as of January 2026 · Last updated February 5, 2026*)
- **Official Certification Page:** `https://learn.microsoft.com/en-us/credentials/certifications/github-actions/` (*Updated August 7, 2026*)
- **Exam Delivery:** `100 minutes` exam time (`120 minutes` seat duration) · `$99 USD` · Pearson VUE · `700 / 1000` scaled passing score · **2-year validity** · **Closed-book** (no Microsoft Learn / GitHub Docs access) · **0 case studies / 0 live labs** · Languages: `English, Spanish, Portuguese (Brazil), Korean, Japanese`

---

## Six-Exam Architectural Progression (`6 × 100 = 600` Questions)

| Set | Enterprise Organization Persona | Architectural Focus | MC (`S`+`O`) | MS (`M2`+`M3`) | `____` | `Proposed solution:` |
|:---:|---|---|:---:|:---:|:---:|:---:|
| **1** | **KestrelPay Clearing** (`Rust/Go payment rails`) | Polyglot Monorepo CI & Matrix Orchestration — Event Filters, YAML Anchors (`&`/`*`/`<<:`), Service Containers, Artifacts v4 & VS Code Extension | `84` | `16` | `23` | `6` |
| **2** | **HeliosGrid Telemetry** (`C++/Python smart-grid IoT`) | Workflow Consumption, Log Diagnostics & Reusable Pipelines — Debug Secrets, Matrix Re-Runs, Starter Templates & Nested `workflow_call` | `84` | `16` | `21` | `8` |
| **3** | **VireoBio Genomics** (`TypeScript/Rust bioinformatics`) | Custom Action Engineering & Marketplace Distribution — Node 20 Bundling (`@vercel/ncc`), Docker vs Composite, Immutable Actions & SemVer | `84` | `16` | `22` | `8` |
| **4** | **AegisRail Logistics** (`Java/PostGIS GHEC enterprise`) | Enterprise Runner Fleet & Private Cloud Networking — Ruleset Required Workflows, Kubernetes ARC Scale Sets, Azure VNet & Secrets REST API | `84` | `16` | `22` | `8` |
| **5** | **SolsticeCloud Media** (`FFmpeg/Go zero-trust media`) | Zero-Trust Supply Chain & Passwordless Cloud Deployments — Script Injection Defense, OIDC Subject Claims, SHA Pinning & SLSA Attestations | `84` | `16` | `24` | `8` |
| **6** | **BorealSim Robotics** (`ROS 2/C++23 simulation FinOps`) | High-Scale FinOps, Caching & Runner Fleet Optimization — Cache Eviction, REST Retention Pruning, OS Multipliers, `ubuntu-slim` & Concurrency | `84` | `16` | `22` | `8` |

---

## Complete 48-Skill Allocation Per Practice Set

### Domain 1 — Author and manage workflows (`20–25%` -> `24` items/set · `144` total)
- `1.1` (`2/set`): Configure workflows for scheduled, manual, and webhook events
- `1.2` (`2/set`): Define workflow scope, permissions, event filters, and concurrency controls
- `1.3` (`2/set`): Design workflows using inputs and reusable configuration patterns
- `1.4` (`2/set`): Structure jobs, steps, conditional logic, timeouts, and error-handling behavior
- `1.5` (`2/set`): Manage job dependencies and execution order
- `1.6` (`2/set`): Use workflow commands and environment files to control job execution
- `1.7` (`2/set`): Configure service containers and containerized job environments
- `1.8` (`2/set`): Implement matrix strategies to run workflows across multiple configurations
- `1.9` (`1/set`): Simplify workflow definitions using YAML anchors and aliases within a workflow file
- `1.10` (`2/set`): Reference actions and workflows using appropriate contexts and immutable references
- `1.11` (`1/set`): Write expressions using built-in functions and conditional operators
- `1.12` (`1/set`): Author and validate workflows using IDE extensions and developer tooling
- `1.13` (`1/set`): Configure dependency caching and manage workflow artifacts and retention
- `1.14` (`1/set`): Pass data between steps and jobs using outputs, environment variables, and artifacts
- `1.15` (`1/set`): Publish job summaries and configure workflow status badges

### Domain 2 — Consume and troubleshoot workflows (`15–20%` -> `19` items/set · `114` total)
- `2.1` (`2/set`): Predict workflow behavior based on event payloads, triggers, and configuration
- `2.2` (`3/set`): Enable and interpret step and runner diagnostic logs to identify failures
- `2.3` (`2/set`): Interpret workflows that use YAML anchors and aliases during execution
- `2.4` (`2/set`): Analyze matrix-driven runs and re-run failed or targeted jobs
- `2.5` (`2/set`): Locate workflow runs and logs via the GitHub UI, CLI, and REST API
- `2.6` (`2/set`): Access and download workflow artifacts from completed runs
- `2.7` (`2/set`): Consume organization-level reusable workflows in downstream repositories
- `2.8` (`2/set`): Use public and non-public starter workflow templates across repositories
- `2.9` (`2/set`): Manage workflow lifecycle states including disabling, enabling, and deleting workflows

### Domain 3 — Author and maintain actions (`15–20%` -> `19` items/set · `114` total)
- `3.1` (`3/set`): Create and configure JavaScript actions
- `3.2` (`3/set`): Create and configure Docker container and composite actions, and select the appropriate action type
- `3.3` (`2/set`): Troubleshoot action failures and adopt immutable action distribution practices
- `3.4` (`3/set`): Define action metadata, inputs, outputs, and branding in action configuration files
- `3.5` (`2/set`): Implement workflow commands, exit codes, and output handling within actions
- `3.6` (`2/set`): Select an appropriate distribution model for public, private, and enterprise actions
- `3.7` (`2/set`): Publish actions to GitHub Marketplace
- `3.8` (`2/set`): Create and manage action releases, tags, and versioning strategies for consumers

### Domain 4 — Manage GitHub Actions for the enterprise (`20–25%` -> `24` items/set · `144` total)
- `4.1` (`3/set`): Configure and govern enterprise-level reuse of actions and reusable workflows
- `4.2` (`3/set`): Control access and sharing policies for actions and workflows across repositories and organizations
- `4.3` (`3/set`): Enforce enterprise and organization policies for allowed actions and workflow execution
- `4.4` (`3/set`): Plan, deploy, and scale GitHub-hosted and self-hosted runners (including ephemeral and Kubernetes-based runners)
- `4.5` (`3/set`): Configure runner networking, IP allow lists, proxies, and private networking (including Azure VNet integration)
- `4.6` (`3/set`): Organize runner groups, restrict access, and monitor or troubleshoot runner health and performance
- `4.7` (`2/set`): Customize, preconfigure, and maintain runner images and software dependencies
- `4.8` (`2/set`): Define scope, precedence, and access controls for encrypted secrets and configuration variables at enterprise, organization, repository, and environment levels
- `4.9` (`2/set`): Manage secrets programmatically and in workflows using the GitHub REST API and secure handling practices

### Domain 5 — Secure and optimize automation (`10–15%` -> `14` items/set · `84` total)
- `5.1` (`2/set`): Configure deployment environments, protection rules, required reviewers, and vet Marketplace actions
- `5.2` (`2/set`): Identify and mitigate untrusted input and script injection risks in workflows and actions
- `5.3` (`2/set`): Apply least-privilege permissions to GITHUB_TOKEN and manage cross-repository authentication tokens
- `5.4` (`2/set`): Configure OpenID Connect (OIDC) for federated authentication to cloud providers and external vaults
- `5.5` (`2/set`): Enforce action pinning, supply-chain security controls, and artifact attestations
- `5.6` (`2/set`): Optimize workflow execution time and storage using caching, artifact policies, and selective execution
- `5.7` (`2/set`): Reduce runner cost and resource consumption using concurrency controls, runner sizing, and matrix optimization
