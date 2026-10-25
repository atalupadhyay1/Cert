# Official sources and coverage notes

Reviewed October 2026 against the **exam guide v1.0** and the certification page. Product names, preview status, and prices change, so re-check before publishing or scheduling.

## Primary references

| Purpose | URL |
|---|---|
| Certification page (length, fee, format, languages, prerequisites) | https://cloud.google.com/learn/certification/data-practitioner |
| Exam guide v1.0 (four sections and their weights) | https://services.google.com/fh/files/misc/v1.0_associate_data_practitioner_exam_guide_english.pdf |
| BigQuery documentation | https://cloud.google.com/bigquery/docs |
| BigQuery ML introduction | https://cloud.google.com/bigquery/docs/bqml-introduction |
| Cloud Storage documentation | https://cloud.google.com/storage/docs |
| Storage Transfer Service | https://cloud.google.com/storage-transfer/docs/overview |
| Database Migration Service | https://cloud.google.com/database-migration/docs |
| BigQuery Data Transfer Service | https://cloud.google.com/bigquery/docs/dts-introduction |
| Dataflow | https://cloud.google.com/dataflow/docs |
| Dataproc | https://cloud.google.com/dataproc/docs |
| Cloud Data Fusion | https://cloud.google.com/data-fusion/docs |
| Cloud Composer | https://cloud.google.com/composer/docs |
| Dataform | https://cloud.google.com/dataform/docs |
| Cloud Scheduler | https://cloud.google.com/scheduler/docs |
| Eventarc | https://cloud.google.com/eventarc/docs |
| Pub/Sub | https://cloud.google.com/pubsub/docs |
| Looker and Looker Studio | https://cloud.google.com/looker/docs |
| Colab Enterprise | https://cloud.google.com/colab/docs |
| Analytics Hub | https://cloud.google.com/analytics-hub/docs |
| Cloud KMS | https://cloud.google.com/kms/docs |
| IAM roles and least privilege | https://cloud.google.com/iam/docs/understanding-roles |

## Verified exam facts

| Fact | Value |
|---|---|
| Domains and weights | 1) Data Preparation and Ingestion ~30%; 2) Data Analysis and Presentation ~27%; 3) Data Pipeline Orchestration ~18%; 4) Data Management ~25% |
| Length | 2 hours |
| Fee | $125 USD plus applicable tax |
| Format | 50–60 multiple choice and multiple select questions |
| Case studies | **None.** The certification page and the guide describe no case-study component and no case-study weighting |
| Passing score | **Not published** — the exam reports pass or fail |
| Languages | English and Japanese |
| Prerequisites | **None**; 6+ months of hands-on experience with Google Cloud data products is recommended |
| Branding notice | The certification page states the exam "will soon be updated to reflect recent branding changes", so product names need a re-check before publication |

The length, fee, question range, languages, and prerequisites above are Google-published; the **passing score is not published**, and this package therefore never states a target percentage or converts a practice score into a pass mark.

Not claimed anywhere in this package: that the practice exams contain the live item count, that they reproduce lab tasks or any interactive console component, that they reproduce case studies (there are none to reproduce), or that completing the course earns the certification.

## Domain coverage and package weights

| Domain | Official weight | Per exam | Percent | Package total |
|---|---:|---:|---:|---:|
| 1. Data Preparation and Ingestion | ~30% | 30 | 30% | 180 |
| 2. Data Analysis and Presentation | ~27% | 27 | 27% | 162 |
| 3. Data Pipeline Orchestration | ~18% | 18 | 18% | 108 |
| 4. Data Management | ~25% | 25 | 25% | 150 |

The four published weights total **exactly 100%**, so they can be copied straight into a 100-item exam and they are: **30 / 27 / 18 / 25**. No count was adjusted, unlike the Professional-level courses in this repository, whose six published weights sum to 101% and required a one-item correction. `build.py` asserts equality rather than a tolerance band, so a future guide revision that breaks the 100% total will fail the build instead of being absorbed.

## Coverage against the published sections

The guide's bullets were read directly and mapped into 42 local study areas. The table records practice emphasis across all 600 items; counts describe this bank, not official weighting.

| Local ID | Study area | Items | Official bullets it supports |
|---|---|---:|---|
| 1.1 | ETL, ELT, and ETLT Methodologies | 24 | 1.1 ETL, ELT and ETLT, and where the transform runs |
| 1.2 | Data Quality Assessment and Cleaning | 24 | 1.1 data quality assessment and cleaning with Data Fusion, BigQuery, SQL or Dataflow |
| 1.3 | Transfer Tool Selection | 24 | 1.1 Storage Transfer Service and Transfer Appliance for a bulk move |
| 1.4 | Data Formats | 24 | 1.2 CSV, JSON, Parquet and Avro as source and sink formats |
| 1.5 | Extraction Tool Selection | 18 | 1.2 Dataflow, BigQuery Data Transfer Service, Database Migration Service and Data Fusion as extraction paths |
| 1.6 | Storage Solution Selection | 24 | 1.2 storage choice among Cloud Storage, BigQuery, Cloud SQL, Firestore, Bigtable and Spanner |
| 1.7 | Storage Location Types | 18 | 1.2 regional, dual-regional, multi-regional and zonal location types |
| 1.8 | Structured, Semi-Structured, and Unstructured Data | 12 | 1.2 structured, semi-structured and unstructured data |
| 1.9 | Loading with CLIs and Client Libraries | 12 | 1.2 loading with the gcloud and bq CLIs and with client libraries |
| 2.1 | BigQuery SQL for Reporting | 24 | 2.1 BigQuery SQL for reporting and analysis |
| 2.2 | Colab Enterprise and Jupyter Notebooks | 12 | 2.1 Jupyter and Colab Enterprise notebooks over warehouse data |
| 2.3 | Business Question Analysis | 12 | 2.1 answering a business question from the warehouse |
| 2.4 | Looker Dashboards | 18 | 2.2 Looker dashboards and delivery |
| 2.5 | Looker and Looker Studio Comparison | 12 | 2.2 Looker versus Looker Studio for a stated audience |
| 2.6 | LookML Parameters | 18 | 2.2 LookML explores, measures and parameters |
| 2.7 | BigQuery ML and AutoML Use Cases | 18 | 2.3 BigQuery ML and AutoML use cases |
| 2.8 | Remote Gemini Models in BigQuery | 12 | 2.3 remote Gemini models in BigQuery |
| 2.9 | ML Project Planning | 12 | 2.3 ML project planning |
| 2.10 | BigQuery ML Training and Evaluation | 12 | 2.3 BigQuery ML training and `ML.EVALUATE` |
| 2.11 | BigQuery ML Inference | 6 | 2.3 BigQuery ML inference with `ML.PREDICT` |
| 2.12 | Model Registry | 6 | 2.3 Model Registry for version approval |
| 3.1 | Transformation Tool Selection | 24 | 3.1 Dataproc, Dataflow, Data Fusion, Composer and Dataform tool choice |
| 3.2 | ELT and ETL Pipeline Design | 12 | 3.1 ETL versus ELT pipeline design |
| 3.3 | Scheduled Queries and Job Scheduling | 18 | 3.2 scheduled queries, Cloud Scheduler and job scheduling |
| 3.4 | Dataflow Job Monitoring | 12 | 3.2 the Dataflow job interface and what it reports |
| 3.5 | Logs and Monitoring Review | 12 | 3.2 Cloud Logging and Cloud Monitoring review |
| 3.6 | Orchestration Solution Selection | 18 | 3.2 Composer, Workflow Templates and Workflows for dependency and retry |
| 3.7 | Event-Driven Ingestion with Pub/Sub | 6 | 3.2 Pub/Sub to BigQuery for event-driven ingestion |
| 3.8 | Eventarc Triggers | 6 | 3.2 Eventarc triggers for storage events |
| 4.1 | IAM Least Privilege | 18 | 4.1 IAM least privilege |
| 4.2 | Basic, Predefined, and Custom Roles | 12 | 4.1 basic, predefined and custom roles |
| 4.3 | Cloud Storage Access Control | 12 | 4.1 Cloud Storage access control and uniform bucket-level access |
| 4.4 | Analytics Hub Data Sharing | 12 | 4.1 Analytics Hub for data sharing |
| 4.5 | Cloud Storage Classes | 18 | 4.2 Cloud Storage classes and autoclass |
| 4.6 | Lifecycle Rules and Expiration | 12 | 4.2 delete-after-period and lifecycle rules |
| 4.7 | Archiving Services | 12 | 4.2 archiving services and nearline or coldline placement |
| 4.8 | Backup and Recovery | 12 | 4.3 backup and recovery for Cloud Storage and Cloud SQL |
| 4.9 | Replication | 12 | 4.3 replication |
| 4.10 | Primary and Secondary Locations | 6 | 4.3 primary and secondary locations for recovery |
| 4.11 | CMEK, CSEK, and GMEK | 12 | 4.4 CMEK, CSEK and GMEK |
| 4.12 | Cloud KMS | 6 | 4.4 Cloud KMS key rings, rotation and separation by environment |
| 4.13 | Encryption in Transit and at Rest | 6 | 4.4 encryption in transit and at rest |

These IDs are internal study aids. Google names objectives without this numbering, and no claim is made that the bank is psychometrically calibrated against the live exam.

## Deliberate omissions and disclosures

| Excluded element | Why it is excluded | How the package compensates |
|---|---|---|
| Case studies | The published ADP format has no case-study component | Nothing is imitated; the absence is stated in the README, landing page, curriculum, and package checks |
| Sequencing items | The published format is multiple choice and multiple select only | No sequencing stems, no `→` options, and `validate.py` rejects them |
| Lab and interactive console tasks | Require a live project | Configuration is presented as text and read, not typed |
| Live item count | The live exam samples 50–60 questions | Each exam is labelled a 100-item expanded bank |
| Passing score | Google does not publish one | No target percentage is stated anywhere |

## Licensing, capability, and pricing statements

Every item is answerable without a project. Where a scenario depends on a capability that requires a paid edition, a specific region, or an allowlisted feature, the explanation names that dependency rather than implying the capability is free or universal. No item asserts a current price, quota, or regional availability; the only price in the package is the published $125 registration fee, cited as published and subject to change.
