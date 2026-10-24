# Official sources and coverage notes

Reviewed October 2026. All facts below were checked against the pages listed; product names, preview status, licensing, and prices change, so re-check before publishing or scheduling.

## Primary references

| Purpose | URL |
|---|---|
| DP-700 study guide (skills measured as of October 19, 2026) | https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/dp-700 |
| Fabric Data Engineer Associate certification page | https://learn.microsoft.com/en-us/credentials/certifications/fabric-data-engineer-associate/ |
| Data engineering in Microsoft Fabric | https://learn.microsoft.com/en-us/fabric/data-engineering/data-engineering-overview |
| Microsoft Fabric workspaces | https://learn.microsoft.com/en-us/fabric/fundamentals/workspaces |
| Lakehouse overview | https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-overview |
| Data warehouse in Microsoft Fabric | https://learn.microsoft.com/en-us/fabric/data-engineering/data-warehousing |
| Real-Time Intelligence overview | https://learn.microsoft.com/en-us/fabric/real-time-intelligence/overview |
| OneLake and shortcuts | https://learn.microsoft.com/en-us/fabric/onelake/onelake-shortcuts |
| Deployment pipelines | https://learn.microsoft.com/en-us/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines |
| Workspace and item permissions | https://learn.microsoft.com/en-us/fabric/fundamentals/roles-permissions |
| Delta table optimization in Fabric | https://learn.microsoft.com/en-us/fabric/data-engineering/delta-optimization-and-v-order |
| Monitoring hub | https://learn.microsoft.com/en-us/fabric/fundamentals/monitoring-hubs |
| Exam sandbox | https://aka.ms/examdemo |

## Verified exam facts

| Fact | Value |
|---|---|
| Domains and weights | 1) Implement and manage an analytics solution 30–35%; 2) Ingest and transform data 30–35%; 3) Monitor and optimize an analytics solution 30–35% |
| Passing score | 700 / 1000 scaled |
| Delivery | Proctored; the certification page states the exam may include interactive components |
| Prerequisites | None stated; the audience ingests and transforms data, secures and manages an analytics solution, and monitors and optimizes one |
| Level and role | Intermediate; Data Engineer |
| Skills assumed | SQL, PySpark, and Kusto Query Language (KQL) |
| Study aids | Microsoft publishes an exam sandbox and a separate practice assessment in AI Skills Navigator |
| Study guide baseline | Skills measured as of October 19, 2026 |
| Item count | Not published by Microsoft |
| Duration | 100 minutes, per the certification page |
| Fee | $165 USD, per the certification page (regional pricing varies) |
| Languages | English plus 10 other languages, per the certification page |
| Renewal | Annual free renewal assessment, per the certification page |

The duration and fee above are Microsoft-published on the certification page — unlike the item count, which Microsoft does not publish. The package therefore cites the clock and the price, and states plainly that a 100-item practice exam is an expanded bank rather than a length replica.

Not claimed anywhere in this package: that the practice exams contain the live item count, that they reproduce drag-and-drop, lab, or interactive portal formats, that a practice percentage maps to 700/1000, or that completing the course earns the credential.

## Domain coverage and package weights

| Domain | Official range | Per exam | Percent | Package total |
|---|---:|---:|---:|---:|
| 1. Implement and manage an analytics solution | 30–35% | 33 | 33% | 198 |
| 2. Ingest and transform data | 30–35% | 33 | 33% | 198 |
| 3. Monitor and optimize an analytics solution | 30–35% | 34 | 34% | 204 |

Because all six exams share the same allocation, every exam sits inside all three published ranges and the aggregate is exactly 33 / 33 / 34. A 100-item exam is deliberately large: the volume covers every sub-objective and lets the blueprint be drilled twice without repeating a question.

## Coverage against the published sub-objectives

The study guide's skill bullets were read directly and mapped into 40 local study areas. The table records practice emphasis across all 600 items; counts describe this bank, not official weighting.

| Local ID | Study area | Domain | Items | Official bullets it supports |
|---|---|---|---:|---|
| 1.1 | Spark Workspace Settings | 1 | 17 | Configure Spark workspace settings |
| 1.2 | Domain and OneLake Workspace Settings | 1 | 13 | Configure domain and OneLake workspace settings |
| 1.3 | Apache Airflow Workspace Settings | 1 | 12 | Configure Apache Airflow workspace settings |
| 1.4 | Version Control and Database Projects | 1 | 13 | Configure version control; implement database projects |
| 1.5 | Deployment Pipelines | 1 | 15 | Create and configure deployment pipelines |
| 1.6 | Workspace and Item-Level Access | 1 | 14 | Implement workspace-level and item-level access controls |
| 1.7 | Row, Column, Object, and File-Level Security | 1 | 19 | Implement row-level, column-level, object-level, and folder/file-level access controls |
| 1.8 | Dynamic Data Masking | 1 | 14 | Implement dynamic data masking |
| 1.9 | Sensitivity Labels and Endorsement | 1 | 17 | Apply sensitivity labels to items; endorse items |
| 1.10 | Fabric Audit Logs | 1 | 15 | Implement and use Microsoft Fabric audit logs |
| 1.11 | OneLake Security | 1 | 14 | Configure and implement OneLake security |
| 1.12 | Choosing Between Dataflow Gen2, Pipeline, and Notebook | 1 | 17 | Choose between Dataflow Gen2, a pipeline and a notebook |
| 1.13 | Schedules, Event Triggers, and Dynamic Parameters | 1 | 18 | Design and implement schedules and event-based triggers; orchestration patterns with parameters and dynamic expressions |
| 2.1 | Full and Incremental Load Patterns | 2 | 14 | Design and implement full and incremental data loads |
| 2.2 | Dimensional Model Preparation | 2 | 13 | Prepare data for loading into a dimensional model |
| 2.3 | Streaming Load Patterns | 2 | 8 | Design and implement a loading pattern for streaming data |
| 2.4 | Choosing a Data Store | 2 | 17 | Choose an appropriate data store |
| 2.5 | Choosing a Transformation Engine | 2 | 15 | Choose between Dataflows Gen2, notebooks, KQL, and T-SQL for transformation |
| 2.6 | OneLake Shortcuts | 2 | 12 | Create and manage OneLake shortcuts |
| 2.7 | Mirroring | 2 | 8 | Implement mirroring |
| 2.8 | Pipeline Ingestion | 2 | 18 | Ingest data by using pipelines |
| 2.9 | PySpark Transformation | 2 | 11 | Transform data by using PySpark |
| 2.10 | T-SQL and KQL Transformation | 2 | 10 | Transform data by using SQL and KQL |
| 2.11 | Denormalization, Grouping, and Aggregation | 2 | 13 | Denormalize data; group and aggregate data |
| 2.12 | Duplicate, Missing, and Late-Arriving Data | 2 | 18 | Handle duplicate, missing, and late-arriving data |
| 2.13 | Choosing a Streaming Engine | 2 | 16 | Choose an appropriate streaming engine |
| 2.14 | Eventstream and Spark Structured Streaming | 2 | 6 | Process data by using Eventstream; process data by using Spark structured streaming |
| 2.15 | Windowing and Real-Time Tables | 2 | 19 | Choose between native tables and OneLake shortcuts; query acceleration; create windowing functions |
| 3.1 | Monitoring Ingestion and Transformation | 3 | 15 | Monitor data ingestion and data transformation |
| 3.2 | Monitoring Semantic Model Refresh | 3 | 13 | Monitor semantic model refresh |
| 3.3 | Alerts and Data Activator | 3 | 20 | Configure alerts |
| 3.4 | Pipeline and Dataflow Gen2 Errors | 3 | 18 | Identify and resolve pipeline errors and Dataflow Gen2 errors |
| 3.5 | Notebook Errors | 3 | 17 | Identify and resolve notebook errors |
| 3.6 | Eventhouse and Eventstream Errors | 3 | 16 | Identify and resolve Eventhouse errors and Eventstream errors |
| 3.7 | T-SQL and Shortcut Errors | 3 | 15 | Identify and resolve T-SQL errors and OneLake shortcut errors |
| 3.8 | Optimizing Lakehouse Tables | 3 | 22 | Optimize a Lakehouse table |
| 3.9 | Optimizing Pipelines | 3 | 10 | Optimize a pipeline |
| 3.10 | Optimizing the Data Warehouse | 3 | 15 | Optimize a data warehouse |
| 3.11 | Optimizing Spark Performance | 3 | 20 | Optimize Spark performance |
| 3.12 | Optimizing Query and Real-Time Performance | 3 | 23 | Optimize query performance; optimize Eventstream and Eventhouse |

These IDs are internal study aids. Microsoft names objectives without this numbering. Counts describe practice emphasis, not official sub-objective weighting, and no claim is made that the bank is psychometrically calibrated against the live exam.

## Deliberate omissions and disclosures

| Excluded format | Why it is excluded | How the package compensates |
|---|---|---|
| Drag-and-drop ordering | Requires a drag-and-drop player | Sequencing is authored as four candidate sequences with one correct order, exported as multiple choice |
| Hot-area / image selection | Requires image hotspots | No item depends on pointing at a screenshot |
| Live labs and interactive portal components | Require a provisioned Fabric capacity | Configuration is presented as text and read, not typed |
| Adaptive problem-solution (yes/no) sets | Not representable in the importer | Case studies and multi-select items carry the multi-constraint load |
| Live item count | Microsoft does not publish one | Each exam is labelled a 100-item expanded bank |

## Licensing and capability statements

Every item is answerable without a tenant. Where a scenario depends on a capability that requires a paid capacity, a specific Fabric licence, an eventhouse, or a mirroring-supported source, the explanation names that dependency rather than implying the capability is unlimited or universally included. No item states a specific price, quota, or regional availability.
