"""Option bank for the Cloud Digital Leader practice course.

One label and one meaning per answer or distractor. Keys are stable and
referenced by questions/*.txt; build.py rejects an unknown key.

The exam is a business-and-foundations exam, so every option is either a named
Google Cloud product, a named business practice, or a plain-language concept.
No option is a console command or a configuration fragment.
"""
TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f'Duplicate term: {key}')
    TERMS[key] = (label, meaning)


# ---------------------------------------------------- digital transformation
t('cloud_computing', 'Rent computing capacity over a network instead of owning the hardware',
  'Cloud computing moves the hardware into a provider service that is consumed on demand.')
t('digital_transformation', 'Change how the business operates and serves customers by using technology',
  'Digital transformation is an operating change, not a one-off migration of servers.')
t('agentic_ai_def', 'Software that plans several steps and takes action toward a goal',
  'Agentic AI decides and acts across steps, which is what separates it from a single answer.')
t('open_source_def', 'Software whose code anyone may inspect, change, and redistribute',
  'Open source lowers lock-in because the code can be examined and moved.')
t('open_standard_def', 'A published specification that any vendor is free to implement',
  'An open standard lets two products interoperate without a private agreement.')
t('on_prem_ownership', 'Buying and running the servers inside the company data centre',
  'On-premises ownership puts the purchase, the refresh cycle, and the patching on the company.')
t('scalability_benefit', 'Add capacity for a peak without buying hardware for it',
  'Scalability matches capacity to demand instead of to a forecast.')
t('agility_benefit', 'Release a new service in days because capacity is already available',
  'Agility is the shorter time from an idea to a running service.')
t('global_reach_benefit', 'Serve customers in new countries from the same deployment',
  'Global reach opens a market without building a local data centre first.')
t('cost_effectiveness_benefit', 'Pay for the capacity used rather than the capacity reserved',
  'Cost effectiveness turns a fixed asset into a variable charge.')
t('data_insights_benefit', 'Analyse the transactions the business already records',
  'The data value comes from insight that changes a decision.')
t('focus_benefit', 'Move staff from racking servers to customer-facing work',
  'Focus is the time a team regains when it stops operating infrastructure.')
t('security_benefit', 'Apply one hardened control set across every environment',
  'A shared control set replaces dozens of individually configured systems.')
t('driver_competitor_pressure', 'Rivals release weekly, so the company must change how it ships',
  'Competitive pressure is a market reason to transform.')
t('driver_customer_expectation', 'Customers now expect a same-day answer on any channel',
  'Changing customer expectations pull the business toward new services.')
t('driver_cost_reduction', 'The maintenance budget crowds out every new project',
  'Cost pressure is a financial reason to transform.')
t('driver_compliance_pressure', 'A regulation now requires auditable data handling',
  'Compliance pressure makes a control change unavoidable.')
t('challenge_skills_gap', 'Nobody on staff has run a migration of this size',
  'A skills gap stalls a programme even when the technology is available.')
t('challenge_legacy_dependency', 'The core system cannot be changed without stopping the business',
  'Legacy dependency limits how fast any change can be made.')
t('challenge_governance_gap', 'No one owns the decision, so each team waits for someone else',
  'A governance gap delays every choice without blocking any of them outright.')
t('challenge_culture_resistance', 'Teams defend the process they already know',
  'Cultural resistance slows adoption after the technology decision is made.')
t('risk_of_inaction', 'Competitors ship faster while the budget goes to maintenance',
  'The cost of standing still is the outcome the business loses by waiting.')
t('ai_leadership', 'Google builds the models and the infrastructure that run them',
  'AI leadership is having frontier models and the compute for them in one place.')
t('global_network_diff', 'Traffic between regions travels on a private backbone',
  'The private network is the differentiator behind consistent global latency.')
t('openness_diff', 'Interoperability with other vendors instead of a closed stack',
  'Openness keeps a multi-vendor option available.')
t('data_platform_diff', 'Analytics and AI run on data held in one place',
  'One data platform removes the copy step between storage and analysis.')
t('ai_hypercomputer_diff', 'Purpose-built compute and software for AI training and serving',
  'AI Hypercomputer is the bundled AI infrastructure position.')
t('security_diff', 'Security is built into the infrastructure the provider operates',
  'Security by design sits below anything the customer configures.')
t('private_cloud_arch', 'A cloud environment dedicated to one organisation',
  'A private cloud gives isolation, and the organisation still operates it.')
t('hybrid_cloud_arch', 'Some workloads stay on premises while others run in the cloud',
  'Hybrid keeps a plant or a mainframe where it is and moves what can move.')
t('multicloud_arch', 'Workloads run in more than one public cloud provider',
  'Multicloud trades simplicity for leverage and specific regional services.')
t('single_cloud_arch', 'Every workload runs in one provider environment',
  'A single cloud is simpler to govern at the cost of concentration.')
t('region_def', 'A geographic location that contains several isolated zones',
  'A region is the unit a residency commitment usually names.')
t('zone_def', 'An isolated deployment area inside a region',
  'Zones inside a region fail independently, which is why replicas spread across them.')
t('edge_location_def', 'A point of presence close to users that caches content',
  'An edge location shortens the distance to the user for cached content.')
t('latency_def', 'The delay between a request and its response',
  'Latency is what the user feels, independent of how much data moves.')
t('bandwidth_def', 'The volume of data a connection can carry in a period',
  'Bandwidth is capacity; latency is delay.')
t('dns_def', 'The service that maps a name to a network address',
  'DNS is the lookup that turns a hostname into an address.')
t('iaas_model', 'The provider supplies machines and storage, and the customer runs the rest',
  'IaaS leaves the operating system and the runtime to the customer.')
t('paas_model', 'The provider runs the platform while the customer deploys code',
  'PaaS removes runtime and patching work from the team.')
t('saas_model', 'The provider runs the whole application and the customer uses it',
  'SaaS is consumed, not operated.')

# --------------------------------------------------------------- data
t('data_supply_chain_def', 'The path from capture through processing and storage to analysis and use',
  'The supply chain is the whole route a record travels before it changes a decision.')
t('data_activation_def', 'Putting an analysed segment to work inside a business process',
  'Activation is the step where analysis reaches a customer touchpoint.')
t('data_silo_def', 'Data held in a system that other teams cannot reach',
  'A silo is reachable by its owner only, so it cannot inform the rest of the business.')
t('vendor_lockin_def', 'Data or tooling that cannot move to another provider',
  'Lock-in is the cost of leaving, expressed in migration effort.')
t('database_def', 'A system that stores records for day-to-day operations',
  'An operational database answers one customer at a time, quickly.')
t('warehouse_def', 'A system tuned for analytical queries across large volumes',
  'A warehouse is built for scanning and aggregating, not single-row writes.')
t('data_lake_def', 'A store that holds raw files in their original formats',
  'A lake keeps the data as it arrived so later processing can reinterpret it.')
t('structured_data', 'Rows and columns that follow a defined schema',
  'Structured data fits a table and a type per column.')
t('semi_structured_data', 'Records that carry keys or tags but no fixed table schema',
  'Semi-structured data is self-describing, which is what a JSON payload looks like.')
t('unstructured_data', 'Files such as images, audio, and documents with no row structure',
  'Unstructured data needs a model or a search index to be useful.')
t('first_party_data', 'Data the organisation collects itself',
  'First-party data comes from the company own customers and systems.')
t('third_party_data', 'Data bought or licensed from an outside provider',
  'Third-party data arrives under a licence that constrains its use.')
t('data_governance_def', 'The rules and owners that decide who may use which data and for what',
  'Governance answers the who and why, not the how.')
t('data_lineage_def', 'The record of where a value came from and what changed it',
  'Lineage makes a reported number defensible after the fact.')
t('interoperability_def', 'Products that read and write common formats so data can move',
  'Interoperability is what makes leaving a tool possible.')
t('data_quality_gate', 'A check that stops bad records before they reach a report',
  'A quality gate moves the discovery of a defect upstream of the consumer.')
t('cloud_storage_prod', 'Object storage for files and unstructured data',
  'Cloud Storage holds objects addressed by name rather than rows.')
t('bigquery_prod', 'A serverless analytical warehouse for large SQL workloads',
  'BigQuery runs the query without a cluster for the customer to size.')
t('cloud_sql_prod', 'A managed relational database for ordinary transactional workloads',
  'Cloud SQL runs a familiar engine with the patching handled by Google.')
t('spanner_prod', 'A relational database that scales horizontally with strong consistency',
  'Spanner keeps relational semantics while scaling beyond one machine.')
t('alloydb_prod', 'A managed PostgreSQL database for demanding transactional and analytical work',
  'AlloyDB targets PostgreSQL workloads that need more throughput than a single instance.')
t('bigtable_prod', 'A wide-column store for very high throughput at low latency',
  'Bigtable is chosen for scale and speed on one key, not for joins.')
t('firestore_prod', 'A document database for application data that syncs to clients',
  'Firestore keeps mobile and web clients synchronised with the stored documents.')
t('standard_class', 'Frequent access with no retrieval fee',
  'Standard suits data that is read often.')
t('nearline_class', 'Access about once a month at a lower storage price',
  'Nearline trades a retrieval fee for a lower storage charge.')
t('coldline_class', 'Access about once a quarter for data kept for recovery',
  'Coldline suits backups that are rarely read.')
t('archive_class', 'Long-term retention at the lowest storage price',
  'Archive is for the copy that exists to satisfy a retention rule.')
t('autoclass_class', 'Storage class moves automatically as access patterns change',
  'Autoclass removes the guess about which class an object belongs in.')
t('retrieval_fee', 'A charge for reading an object stored in a colder class',
  'The retrieval fee is the price of the cheaper storage.')
t('database_migration_service', 'A managed path to move an existing database engine into a managed service',
  'Database Migration Service handles the engine move with minimal application change.')
t('replatform_db', 'Move the database to a managed service with small application changes',
  'Replatform keeps the engine and gives up the server administration.')
t('refactor_db', 'Rewrite the data layer to use a cloud-native store',
  'Refactor changes the code, which is why it delivers the most and costs the most.')
t('looker_prod', 'A business intelligence platform with a governed semantic model',
  'Looker defines a measure once so every dashboard reports the same number.')
t('looker_studio_prod', 'A free reporting tool for quick dashboards',
  'Looker Studio is fast to start and leaves governance to the author.')
t('pubsub_prod', 'A messaging service that carries events between systems',
  'Pub/Sub decouples the producer of an event from its consumers.')
t('dataflow_prod', 'A managed service that runs streaming and batch pipelines from one definition',
  'Dataflow runs the same pipeline code for a stream and for a batch backfill.')
t('managed_spark_prod', 'A managed service for running Apache Spark jobs',
  'Managed Service for Apache Spark runs existing Spark code without cluster upkeep.')
t('streaming_analytics_value', 'Act on an event while it still matters to the customer',
  'Streaming analytics changes the outcome because the decision happens in time.')
t('dashboard_value', 'Put a governed number in front of a decision maker on a schedule',
  'A dashboard replaces a stack of exported spreadsheets.')

# ------------------------------------------------------------------- AI
t('ai_def', 'Systems that perform tasks that normally need human judgement',
  'AI is the broad category, from classifiers to assistants.')
t('ml_def', 'Models that learn patterns from examples rather than following written rules',
  'Machine learning derives the rule from the data.')
t('genai_def', 'Models that produce new text, images, or code from a prompt',
  'Generative AI creates content rather than only labelling it.')
t('agentic_ai_value', 'Systems that plan and act across steps instead of answering one question',
  'Agentic value comes from completing the task, not describing it.')
t('business_intelligence_def', 'Reporting that answers what already happened',
  'Business intelligence explains the past; prediction looks forward.')
t('data_analytics_def', 'Exploring data to explain what happened and why',
  'Analytics is the diagnostic step between raw data and a decision.')
t('ai_customer_support_value', 'Resolve a customer request faster with an assistant that has the history',
  'Support value is measured in resolution time and deflection.')
t('ai_operations_value', 'Catch a failing machine before it stops the line',
  'Operations value is avoided downtime.')
t('ai_workforce_value', 'Give staff a first draft so they spend time on judgement',
  'Workforce value is time returned to the employee.')
t('replace_rules_ml', 'Replace a rule set that has grown beyond anyone ability to audit',
  'A learned model absorbs the cases the rule set was never written for.')
t('scale_decisions_ml', 'Apply the same decision to millions of cases a day',
  'Scale is the argument when the decision logic already works but does not keep up.')
t('insight_from_unstructured', 'Derive insight from documents, images, or audio',
  'Unstructured content holds value that a table cannot expose.')
t('dq_completeness', 'Every required field is present',
  'Completeness is about the blanks.')
t('dq_uniqueness', 'One entity appears once rather than several times',
  'Uniqueness is about duplicates.')
t('dq_timeliness', 'The data reflects what is true now',
  'Timeliness is about staleness.')
t('dq_validity', 'Values fall inside the allowed format or range',
  'Validity is about format and domain.')
t('dq_accuracy', 'The value matches reality',
  'Accuracy is about correctness, which no format check can prove.')
t('dq_consistency', 'The same fact agrees across systems',
  'Consistency is about disagreement between sources.')
t('explainability_req', 'The business can justify a decision to a customer or a regulator',
  'Explainability is a business requirement when a decision must be defended.')
t('bias_review', 'Check that outcomes do not fall unfairly on one group',
  'A bias review compares outcomes across groups before release.')
t('human_review', 'A person confirms the model decision before it takes effect',
  'Human review is the control for a consequential decision.')
t('model_card_doc', 'A record of what a model is for, what it was trained on, and its limits',
  'A model card travels with the model so the next team knows its boundaries.')
t('responsible_ai_principle', 'Fairness, accountability, and transparency written into the process',
  'Responsible AI is a process commitment, not a model feature.')
t('pretrained_api_choice', 'Use a ready-made API when the task is common and speed matters',
  'A pre-trained API is the shortest path for a solved problem.')
t('automl_choice', 'Train a model on the company own labelled data without writing ML code',
  'AutoML gives custom accuracy without a data science team.')
t('custom_model_choice', 'Build a bespoke model when the problem itself is the differentiator',
  'A custom model is justified when accuracy on the problem is the advantage.')
t('gemini_choice', 'Use a general foundation model through a prompt for language work',
  'A foundation model covers language and reasoning tasks without training data.')
t('build_vs_buy_tradeoff', 'Weigh development effort against the differentiation the model creates',
  'The build-or-buy choice is settled by effort against advantage.')
t('bigquery_ml_choice', 'Train and score a model with SQL where the data already sits',
  'BigQuery ML keeps an analyst inside SQL and avoids a data export.')
t('agent_platform', 'A platform for building, deploying, and governing models and agents',
  'Gemini Enterprise Agent Platform is where the models and agents are operated.')
t('agent_studio', 'A point-and-click studio for assembling an agent from a model and tools',
  'Agent Studio lets a non-programmer assemble the agent.')
t('automl_platform', 'Train a model on your own data through a managed interface',
  'AutoML on Agent Platform handles the training pipeline behind an interface.')
t('model_garden_prod', 'A catalogue of first-party and open models to deploy',
  'Model Garden removes the integration work of trying several models.')
t('agent_governance', 'Register, evaluate, and monitor the agents in production',
  'Governance is how an agent fleet stays auditable.')
t('vision_api', 'Identify objects and read text in images',
  'Vision API answers a question about a picture.')
t('translation_api', 'Translate text between languages',
  'Translation localises content without a linguist per language.')
t('speech_to_text_api', 'Turn recorded audio into text',
  'Speech-to-Text makes audio searchable and analysable.')
t('gemini_multimodal', 'One model that handles text, images, and documents together',
  'A multimodal model reasons across formats in one request.')
t('document_ai', 'Extract structured fields from scanned documents',
  'Document AI turns a form into fields rather than a block of text.')
t('ai_hypercomputer', 'Purpose-built compute, software, and consumption models for AI work',
  'AI Hypercomputer is the integrated infrastructure position for AI.')
t('gpu_tpu_choice', 'Accelerators chosen for training throughput or inference cost',
  'The accelerator choice follows the workload and the budget.')
t('flexible_consumption', 'Pay for AI capacity only while the workload runs',
  'Flexible consumption removes the cost of idle accelerators.')

# ---------------------------------------------------------- infrastructure
t('retire_strategy', 'Switch off a workload nobody needs any more',
  'Retirement is the cheapest migration decision available.')
t('retain_strategy', 'Keep a workload where it is for now',
  'Retention is a deliberate deferral, not an oversight.')
t('rehost_strategy', 'Move the workload as it is to cloud machines',
  'Rehost changes the location and nothing else.')
t('replatform_strategy', 'Move to a managed service with small changes',
  'Replatform buys operational savings for a little code change.')
t('refactor_strategy', 'Rewrite the application to use cloud-native services',
  'Refactor buys the most capability for the most engineering effort.')
t('reimagine_strategy', 'Redesign the business process around a new capability',
  'Reimagine changes the process, not just the platform.')
t('discovery_assessment', 'Inventory and assess the estate before choosing a strategy',
  'Discovery produces the facts a migration plan needs.')
t('vm_def', 'A software-defined server the customer configures',
  'A virtual machine gives the customer the operating system.')
t('container_def', 'An application and its dependencies packaged to run anywhere',
  'A container fixes the runtime so it behaves the same everywhere.')
t('serverless_def', 'The provider runs the code and scales it with no server to manage',
  'Serverless removes the host from the operating model.')
t('microservices_def', 'Small services that communicate over a network',
  'Microservices let one part change without redeploying the whole application.')
t('autoscaling_def', 'Capacity adjusts with demand automatically',
  'Autoscaling matches spend to traffic through the day.')
t('load_balancing_def', 'Traffic is spread across healthy instances',
  'A load balancer removes the single instance from the request path.')
t('spot_vm', 'Spare capacity at a lower price that can be reclaimed',
  'Spot capacity is cheap because it can be taken back.')
t('managed_instance_group', 'A group that keeps a template instances healthy and scaled',
  'The instance group replaces a failed machine without a person noticing.')
t('compute_engine_value', 'Full control of the operating system for a lift-and-shift workload',
  'Compute Engine is the choice when the workload needs the machine.')
t('gke_value', 'A managed Kubernetes control plane for container workloads',
  'GKE runs the cluster control plane and leaves the workloads to the team.')
t('gke_autopilot', 'The platform manages the nodes and you pay for pods',
  'Autopilot removes node sizing and node patching.')
t('gke_enterprise', 'One policy and identity model across clusters and clouds',
  'GKE Enterprise is the fleet position for several environments.')
t('cloud_run_value', 'Run a container that scales to zero and needs no cluster',
  'Cloud Run serves a container without a cluster to operate.')
t('cloud_run_functions', 'Run a single function in response to an event',
  'Cloud Run functions is the smallest unit of deployable code.')
t('scale_to_zero', 'No charge when nothing is serving',
  'Scale to zero makes an idle service free.')
t('alloydb_omni', 'Run the same database engine outside Google Cloud',
  'AlloyDB Omni carries the engine to another environment.')
t('bigquery_omni', 'Query data that stays in another cloud',
  'BigQuery Omni analyses data where the regulator requires it to stay.')
t('api_def', 'A defined interface that one system uses to call another',
  'An API is the contract between two systems.')
t('apigee_value', 'Publish, secure, and analyse APIs with policy and usage data',
  'Apigee adds the governance layer around the API.')
t('api_monetisation', 'Charge partners for access to a published API',
  'Monetisation turns an interface into a revenue line.')
t('api_gateway_def', 'A single front door that validates and routes API calls',
  'A gateway centralises the checks every caller must pass.')

# --------------------------------------------------------------- security
t('ddos_attack', 'Overwhelming traffic that makes a service unavailable',
  'A denial-of-service attack attacks availability, not data.')
t('ransomware_attack', 'Malware that encrypts data and demands payment',
  'Ransomware attacks availability and holds the data hostage.')
t('phishing_attack', 'A message that tricks a person into giving up credentials',
  'Phishing attacks the person, not the system.')
t('misconfiguration_risk', 'A setting left open that exposes data',
  'Misconfiguration is the most common cause of an avoidable exposure.')
t('cryptomining_attack', 'Stolen compute used to mine cryptocurrency',
  'Cryptomining shows up as an unexplained bill before it shows up as an alert.')
t('llm_attack', 'Manipulated prompts or poisoned context that misuse a model',
  'An LLM attack turns the model against its own instructions.')
t('confidentiality_def', 'Only authorised people can see the data',
  'Confidentiality is about disclosure.')
t('integrity_def', 'The data has not been changed by anyone unauthorised',
  'Integrity is about alteration.')
t('availability_def', 'The service is there when the business needs it',
  'Availability is about access to the service.')
t('least_privilege', 'Each identity holds only the access its task requires',
  'Least privilege bounds what a stolen identity can reach.')
t('zero_trust', 'Every request is verified regardless of network location',
  'Zero trust removes the assumption that the internal network is safe.')
t('dlp_def', 'Detect and redact sensitive values before they spread',
  'Data loss prevention catches the value on its way out.')
t('security_posture', 'The measured state of an environment controls',
  'Posture is a measurement, which is why it can be reported and compared.')
t('encryption_at_rest', 'Data on the storage medium is unreadable without the key',
  'Encryption at rest protects a stolen disk.')
t('encryption_in_transit', 'Data on the network is unreadable in flight',
  'Encryption in transit protects the wire.')
t('encryption_in_use', 'Data stays protected in memory while it is processed',
  'Encryption in use protects the data from the machine that is processing it.')
t('authentication_def', 'Proving who the caller is',
  'Authentication answers who you are.')
t('authorization_def', 'Deciding what the caller may do',
  'Authorization answers what you may do.')
t('auditing_def', 'Recording what the caller did',
  'Auditing answers what happened and who did it.')
t('mfa_def', 'A second factor beyond the password',
  'A second factor survives a stolen password.')
t('iam_def', 'The service that answers who may do what on which resource',
  'IAM is the policy layer for every Google Cloud resource.')
t('decryption_def', 'Turning protected data back into readable form with the key',
  'Decryption is the step that needs the key.')
t('defense_in_depth', 'Several independent controls so one failure does not expose everything',
  'Depth assumes that any single control can fail.')
t('threat_intelligence_def', 'Curated knowledge about attackers and their methods',
  'Threat intelligence tells a defender what to look for.')
t('threat_response', 'The process that contains and removes an active threat',
  'Response is the action taken during an incident.')
t('security_operations', 'The platform that collects telemetry and drives detection and response',
  'Security operations is where the signals become a case.')
t('google_threat_intelligence', 'Threat insight drawn from Google visibility, Mandiant, and VirusTotal',
  'Google Threat Intelligence combines three distinct sources.')
t('scc_value', 'Find and prioritise misconfigurations and risks across the environment',
  'Security Command Center turns a long list into a ranked one.')
t('google_security_operations', 'A unified platform for telemetry, detection, and response',
  'Google Security Operations consolidates the tooling.')
t('mandiant_value', 'Front-line incident response expertise behind the product',
  'Mandiant contributes what years of responding to incidents teach.')
t('virustotal_value', 'Crowd-sourced file and URL reputation',
  'VirusTotal adds the reputation that many contributors produce.')
t('ai_protection', 'Discover and defend the AI workloads the organisation deploys',
  'AI Protection extends posture management to AI assets.')
t('model_armor', 'Screen prompts and responses against misuse and unsafe content',
  'Model Armor sits in front of the model.')
t('secure_ai_stack', 'Infrastructure, data, models, platform, and agents each get controls',
  'The stack model shows that AI security is more than the model.')
t('gemini_secops', 'An assistant that speeds investigation inside the security platform',
  'Gemini in Security Operations shortens the triage step.')
t('cloud_armor_value', 'Filter web traffic at the edge before it reaches the application',
  'Cloud Armor blocks at the edge, before backend capacity is spent.')
t('iap_value', 'Check identity and context for each request to an internal application',
  'Identity-Aware Proxy authorises the request, not the network path.')
t('vpc_def', 'A private network boundary for the resources in a project',
  'A VPC defines what can talk to what.')
t('confidential_computing', 'Encrypt memory while a workload is running',
  'Confidential computing covers the in-use state.')
t('sdp_value', 'Discover and de-identify sensitive data across the estate',
  'Sensitive Data Protection finds the data and then removes it from view.')
t('certificate_manager', 'Issue and manage the certificates that protect a service',
  'Certificate Manager keeps certificates from expiring unnoticed.')
t('transparency_report', 'A published account of government requests and how they are handled',
  'A transparency report is a disclosure commitment.')
t('third_party_audit', 'An independent assessment against a published standard',
  'An audit is only as useful as the independence of the auditor.')
t('digital_sovereignty', 'Control over where data sits and who can reach it',
  'Sovereignty is the broader claim; residency is one part of it.')
t('data_residency', 'A commitment that data stays in a stated location',
  'Residency is a location promise that can be tested.')
t('compliance_resource_manager', 'Map a regime controls to the services in use',
  'The compliance resource manager produces the mapping an auditor asks for.')
t('access_transparency', 'A log of provider access to customer content',
  'Access Transparency records the operator access.')

# --------------------------------------------------------------- operations
t('capex_def', 'A large up-front purchase of hardware',
  'Capital expenditure is paid before the capacity is used.')
t('opex_def', 'A recurring charge tied to what is used',
  'Operational expenditure follows the invoice rather than the purchase order.')
t('tco_def', 'The full cost of ownership across the life of the service',
  'Total cost of ownership includes people, licences, and downtime.')
t('idle_capacity_cost', 'Machines bought for a peak that sits unused the rest of the year',
  'Idle capacity is the part of the bill that produces nothing.')
t('cost_owner', 'A named person accountable for each budget',
  'An owner turns a cost report into a decision.')
t('billing_account', 'The account that ties spend to an organisation',
  'The billing account is where the invoice is issued.')
t('labels_cost', 'Tags that let spend be reported by team or product',
  'Labels are what make a shared invoice readable by product.')
t('committed_use_discount', 'A lower unit price in exchange for a usage commitment',
  'A commitment trades flexibility for price.')
t('organization_node', 'The root that holds every folder and project',
  'The organisation node is the top of the hierarchy.')
t('folder_node', 'A grouping that carries policy for the projects inside it',
  'A folder lets one attachment cover many projects.')
t('project_node', 'The unit that holds resources, billing, and access',
  'The project is where resources are created.')
t('inheritance_policy', 'A grant or constraint that flows down the hierarchy',
  'Inheritance is why a policy at the top applies at the bottom.')
t('budget_alert', 'A notification when spend crosses a threshold',
  'A budget alert informs without stopping anything.')
t('quota_def', 'A limit on how much of a resource may be used',
  'A quota caps usage and therefore caps the exposure.')
t('spot_vm_cost', 'Reclaimable capacity at a lower price for tolerant work',
  'Spot pricing suits work that can restart.')
t('dynamic_workload_scheduler', 'Queue flexible work into cheaper capacity windows',
  'The scheduler moves batch work to when capacity is cheapest.')
t('billing_report', 'A report that shows spend by service and by label',
  'A billing report is the review artefact.')
t('cloud_monitoring', 'Metrics and dashboards for the running system',
  'Monitoring shows the system is healthy now.')
t('cloud_logging', 'The record of events the services emit',
  'Logging keeps the detail for later.')
t('cloud_trace', 'The path of one request across services',
  'Tracing answers where the time went.')
t('error_reporting', 'Grouped application errors with the stack that produced them',
  'Error reporting groups the noise into one issue.')
t('redundancy_def', 'A second copy of a component so one failure is survivable',
  'Redundancy is the design answer to a single failure.')
t('backup_def', 'A restorable copy kept away from the primary',
  'A backup only counts if it has been restored once.')
t('sli_def', 'A measured number that describes service behaviour',
  'An indicator is the measurement itself.')
t('slo_def', 'A target for that measurement over a period',
  'An objective is the internal target.')
t('sla_def', 'A contractual commitment with consequences when it is missed',
  'An agreement is the external promise.')
t('error_budget', 'The amount of unreliability the target allows',
  'The budget is what makes the target actionable.')
t('devops_practice', 'One team builds and runs the service',
  'DevOps removes the handover that delays a fix.')
t('toil_reduction', 'Automate repeated operational work',
  'Removing toil is what buys time for reliability work.')
