# Curriculum outline — AB-410 practice course

**Six 100-item mock exams · 600 original questions · 120-minute rehearsal or untimed first pass**

This outline turns the bank into a study sequence. Each exam is blueprint-weighted **28 / 28 / 44**, so the order below is about scenario complexity and topic reinforcement, not about weighting.

Microsoft publishes a **120-minute** duration but no item count for AB-410, and a 100-item exam is deliberately larger than a comfortable sitting. `6 × 100 = 600` lets each blueprint be drilled twice without repeating a question, so treat the clock as a rehearsal of the published duration rather than a model of the live item count.

## Learning arc

| Phase | Exam | What it stresses | Study goal |
|---|---|---|---|
| Foundation | 1 | Requirements, agents, environments, ALM, tables, relationships, prompt columns, views, security | Establish the vocabulary: table, column, relationship, view, form, role, solution |
| Applied build | 2 | Managed solutions, field security, generative pages, app access, dashboards, canvas apps, components | Connect a build decision to the failure it prevents |
| Automation | 3 | Triggers, connectors, approvals, Compose, conditions, loops, troubleshooting | Decide between similar-sounding controls using the constraint in the stem |
| AI and rules | 4 | Prompt templates, inputs, knowledge, model choice, consumption, business rules, process flows, calculated columns | Choose the mechanism that holds where the rule must hold |
| Scale | 5 | Multi-unit ALM, custom connectors, delegation, reusable functions, table-scope validation | Make a solution maintainable across subsidiaries |
| Integration | 6 | Everything, at group scale | Perform under a 120-minute clock with mixed item formats |

## Exam-by-exam study plan

### Exam 1 — Foundations, data models, and dispatch (100 items)
- Official split: 28 / 28 / 44.
- Case studies: Northwind Freight, Adatum Legal, Fabrikam Manufacturing, Tailspin Toys.
- Focus: requirements mapped to the smallest component set, built-in agents before custom ones, environment types and licensing boundaries, publisher prefixes, solution layers, custom tables in the data workspace, standard tables and table properties, global choices and auto-numbers, lookups and one-to-many relationships, prompt columns and row summaries, public views and main forms, security roles, teams, business units, and field security profiles.
- Target skill: name the constraint in the stem before reading the options.

### Exam 2 — Regulated delivery and app governance (100 items)
- Case studies: Woodgrove Insurance, Litware Health, Proseware Consulting, Contoso Real Estate.
- Focus: managed solutions and predictable removal, form scripts versus business rules, view filters and columns, generative pages reviewed before release, sitemaps and app access, dashboards bound to view filters, canvas apps generated from data, delegation and responsive containers, named formulas, component libraries, global variables, IfError, Test Studio, and Monitor.
- Target skill: place the governance control where an error becomes unauthorized access or an unreleasable solution.

### Exam 3 — Field service and public sector (100 items)
- Case studies: Alpine Ski House, City of Riverside, Consolidated Courier, Blue Yonder Airlines.
- Focus: automated, manual, and filtered triggers, standard versus premium versus custom connectors, sequential and parallel approvals, Compose and Parse JSON, Apply to each, condition and switch branches, Do until with a count limit, run history, real-payload testing, scope and run-after failure handling, and when resubmit is safe.
- Target skill: choose the control that makes the failure visible instead of silent.

### Exam 4 — Retail, media, and hospitality (100 items)
- Case studies: Coho Winery, Trey Research, Nod Publishers, Fourth Coffee.
- Focus: prompt templates versus blank prompts, prompt inputs and knowledge, model selection and cost, consuming prompts and models in apps and flows, prompt copies that drift, business rules and their scope, business process flows with branching, calculated, formula, and rollup columns, and the mechanism choice between business logic options.
- Target skill: separate "where the rule must hold" from "which feature is easiest to build".

### Exam 5 — Distribution and multi-unit enterprises (100 items)
- Case studies: Wide World Importers, VanArsdel Manufacturing, Margie Travel, Lakeshore Retail Group.
- Focus: one standard across subsidiaries, ALM pipelines and clones, custom connectors for partner APIs, delegated searches over large tables, reusable user-defined functions, table-scope validation, approvals that pause a cross-site transfer, and prompt-driven summaries written back to the record.
- Target skill: keep maintainability, performance, and governance as three separate arguments.

### Exam 6 — Cross-industry capstone (100 items)
- Case studies: Tahoma Winery Group, Munson Sporting Goods, Relecloud Telecom, Bellows College.
- Focus: business units that separate districts, charts bound to view filters, models consumed inside flows, generative page drafts, standard tables extended rather than rebuilt, rubric scoring with user-defined functions, and the full design-build-release-observe loop.
- Recommended: attempt under a 120-minute timer with no notes, then review every explanation.
- Target skill: hold many constraints at once without collapsing them into one "best practice".

## Item formats and how to rehearse them

| Format | Per exam | How to practise |
|---|---:|---|
| Single-choice | 76 | Decide the constraint first, then eliminate options that solve a different problem |
| Multi-select | 16 | Count the required selections before reading options; reject "true but not asked" statements |
| Sequencing (exported as multiple-choice) | 8 | Find the step that cannot move — design before build, build before secure, secure before release — and anchor the rest |
| Case study | 4 × 3 | Read once, write the three or four hard constraints, then answer each item against them |

## Suggested eight-week schedule

| Week | Work | Deliverable |
|---|---|---|
| 1 | Study domain 1 objectives, take Exam 1 in two halves | Mistake log by local skill |
| 2 | Study domain 2 objectives, take Exam 2 untimed | A one-page diagram of one app's components, from table to app to release |
| 3 | Re-read missed explanations from Exams 1–2, retake both timed | Two timed scores plus error categories |
| 4 | Domain 3, flows half: take Exam 3 | A flow checklist: trigger, filter, connector, branch, loop limit, failure path |
| 5 | Domain 3, prompts and logic half: take Exam 4 | A logic table: rule, where it must hold, mechanism chosen, why |
| 6 | Take Exam 5; review delegation, ALM, and approval items | A multi-unit release plan with environments and approvals |
| 7 | Take Exam 6 under a 120-minute clock | Timed score plus pace per item |
| 8 | Retake the weakest exam, review every explanation | Final readiness note, no score conversion |

## Scoring your own attempt

1. Score each item as correct or incorrect; there is no partial credit for multi-select.
2. Group misses by local skill ID, not by exam number.
3. Classify each miss: unknown capability, misread constraint, plausible-but-wrong option, or rushed guess.
4. Only the last two categories improve with more practice tests; the first two need documentation study or hands-on work.
5. Re-attempt the same exam after a week before trusting an improvement.

A practice percentage is not a scaled exam score. Microsoft reports 700/1000 on a scaled scale and does not publish a raw percentage equivalent.

## Time budget inside a 100-item exam

| Segment | Items | Suggested time (120-minute clock) |
|---|---:|---:|
| First pass, multiple-choice and multi-select | 76 | 76 minutes |
| Sequencing items (multiple-choice) | 8 | 12 minutes |
| Case studies | 12 | 22 minutes |
| Review of flagged items | 4 | 10 minutes |

Microsoft publishes a 120-minute duration for AB-410 but no item count, so a 100-item attempt already exceeds the live item count in principle. The budget above is a deliberate per-item discipline for practice, not a claim about how long the real appointment will feel. Confirm the current appointment length on the certification page before you book.
