"""Option bank for the AWS Certified Cloud Practitioner (CLF-C02) practice sets.

Every option label is either an AWS service name or a plain-language decision, so
an item can ask which service or which choice fits a stated requirement without
the distractor collapsing into a definition. Keys are authoring identifiers only
and never appear in an export.
"""

TERMS = {}


def t(key, label, meaning):
    if key in TERMS:
        raise ValueError(f"duplicate option key: {key}")
    TERMS[key] = (label, meaning)


# --- Cloud value and economics ---------------------------------------------
t('benefit_elasticity', 'Elasticity: scale capacity with demand',
  'Capacity is added and removed as demand changes, so the company pays only for what it uses.')
t('benefit_global_reach', 'Global reach: deploy into multiple Regions quickly',
  'A global infrastructure lets a company put workloads near its users without building facilities.')
t('benefit_agility', 'Agility: provision resources in minutes',
  'New environments are created in minutes, which shortens the time to test an idea.')
t('benefit_trade_capex', 'Trade capital expense for variable expense',
  'Up-front data-centre investment is replaced by usage-based spending.')
t('benefit_no_heavy_lifting', 'Stop spending on undifferentiated heavy lifting',
  'AWS operates the facilities, hardware and managed platforms so the team can focus on its product.')
t('benefit_reliability', 'Reliability through managed, redundant infrastructure',
  'Managed services remove single points of failure that a company would otherwise have to engineer.')
t('capex_model', 'Buy servers up front and depreciate them',
  'The company pays for hardware before it is used and carries the depreciation and refresh risk.')
t('opex_model', 'Pay only for what is consumed each month',
  'Costs follow usage, so the bill rises and falls with demand rather than with a purchase decision.')
t('on_prem_tco', 'Estimate total cost of ownership including facilities and staff',
  'A like-for-like comparison includes power, space, cooling, hardware refresh and the people who run it.')
t('datacenter_ownership', 'Keep ownership of the physical data centre',
  'The company remains responsible for the building, power and hardware lifecycle.')
t('pay_as_you_go', 'Pay-as-you-go pricing',
  'There is no up-front commitment and the meter runs only while the resource exists.')
t('volume_discount', 'Volume discounts that grow with usage',
  'Aggregated usage across an organisation lowers the effective rate.')
t('per_second_billing', 'Billing per second for compute that exists briefly',
  'Short-lived compute is charged for the seconds it runs rather than a minimum period.')
t('egress_cost', 'Data transfer out to the internet carries a charge',
  'Traffic leaving AWS for the internet is billed, which an on-premises design never had to count.')
t('over_provisioning', 'Buy for the busiest day and leave the rest idle',
  'Sizing for the annual peak means paying all year for capacity that mostly sits unused.')
t('fixed_monthly_fee', 'A flat monthly fee that does not change with usage',
  'A flat fee removes the usage signal from the bill but does not track demand.')

# --- Well-Architected Framework --------------------------------------------
t('wa_operational_excellence', 'Operational excellence pillar',
  'The pillar about running and improving workloads, including automation and small reversible changes.')
t('wa_security', 'Security pillar',
  'The pillar about protecting data, systems and assets through identity and detective controls.')
t('wa_reliability', 'Reliability pillar',
  'The pillar about recovering from failure and meeting demand consistently.')
t('wa_performance', 'Performance efficiency pillar',
  'The pillar about using resources efficiently as demand and technology change.')
t('wa_cost', 'Cost optimization pillar',
  'The pillar about delivering value at the lowest price that meets the requirement.')
t('wa_sustainability', 'Sustainability pillar',
  'The pillar about minimising the environmental impact of running a workload.')
t('wa_tool_review', 'Review the workload against the Well-Architected Tool',
  'The tool records answers against each pillar and produces improvement items.')
t('wa_pillar_unused', 'Treat the pillars as naming conventions only',
  'The pillars are design guidance, and each one asks different questions of the same workload.')

# --- Adoption, migration and governance ------------------------------------
t('caf_business', 'Business perspective of the AWS Cloud Adoption Framework',
  'The perspective that connects cloud work to business outcomes and value.')
t('caf_people', 'People perspective of the AWS Cloud Adoption Framework',
  'The perspective about skills, roles and organisational change.')
t('caf_governance', 'Governance perspective of the AWS Cloud Adoption Framework',
  'The perspective about prioritising, budgeting and measuring the cloud programme.')
t('caf_platform', 'Platform perspective of the AWS Cloud Adoption Framework',
  'The perspective about the technical architecture and the platform that workloads run on.')
t('caf_security', 'Security perspective of the AWS Cloud Adoption Framework',
  'The perspective about meeting security and compliance objectives.')
t('caf_operations', 'Operations perspective of the AWS Cloud Adoption Framework',
  'The perspective about running, monitoring and supporting workloads day to day.')
t('migrate_rehost', 'Rehost: move the application as it is',
  'The application moves without code change, which is the fastest path but captures few cloud benefits.')
t('migrate_replatform', 'Replatform: change a few managed components on the way',
  'Small changes, such as moving a database to a managed engine, capture benefit with limited rework.')
t('migrate_refactor', 'Refactor: redesign the application for cloud architecture',
  'The application is rewritten to take advantage of managed and elastic services.')
t('migrate_repurchase', 'Repurchase: move to a different product',
  'The company replaces the application with a commercially available equivalent.')
t('migrate_retain', 'Retain: keep the workload where it is',
  'The workload stays in place because moving it is not justified yet.')
t('migrate_retire', 'Retire: switch the workload off',
  'The workload is no longer needed, so it is decommissioned instead of migrated.')
t('migrate_relocate', 'Relocate: move the platform to a cloud-native equivalent',
  'The whole platform moves to a hosted equivalent without changing the application itself.')
t('caf_skip', 'Skip the migration assessment and move everything at once',
  'Without an assessment there is no inventory, no prioritisation and no agreed success measure.')

# --- Global infrastructure --------------------------------------------------
t('region_az', 'Regions and Availability Zones',
  'A Region is a geographic area and each Availability Zone within it is an isolated group of data centres.')
t('edge_location', 'Edge locations for content delivery',
  'Points of presence that cache content close to users rather than in a Region.')
t('local_zone', 'Local Zones for very low latency',
  'An extension of a Region placed close to a large population or industry centre.')
t('outposts', 'AWS Outposts for on-premises capacity',
  'A rack of AWS infrastructure installed in the customer facility and operated through AWS.')
t('wavelength', 'AWS Wavelength for carrier networks',
  'Compute placed inside a telecommunications provider network for ultra-low latency to mobile devices.')
t('single_az_design', 'Place everything in one Availability Zone',
  'One Zone is a single failure domain, so a Zone event takes the workload with it.')
t('multi_region_count', 'Count Regions as separate data centres inside one city',
  'Regions are geographically separate, and each holds multiple isolated Availability Zones.')

# --- Resiliency and architecture patterns ----------------------------------
t('multi_az_deploy', 'Deploy across multiple Availability Zones',
  'Two or more Zones give the workload a survivor when one Zone fails.')
t('elastic_scaling', 'Scale out automatically as demand rises',
  'Capacity follows the measured demand rather than a forecast.')
t('automation_over_manual', 'Automate repeated provisioning instead of rebuilding by hand',
  'Environments are created from a script or template, so they are consistent and disposable.')
t('loose_coupling', 'Loose coupling with a queue between tiers',
  'A queue decouples the producer from the consumer so a slow tier does not fail the whole flow.')
t('tight_coupling', 'Direct synchronous calls between every tier',
  'A synchronous chain means one slow or failed component fails everything behind it.')
t('microservices', 'Break the application into small independent services',
  'Independent services can be deployed and scaled separately.')
t('serverless_pattern', 'Serverless compute for intermittent work',
  'No server is provisioned, and the service runs only when it is invoked.')
t('monolith_scale', 'Scale the single monolith vertically only',
  'Vertical scaling hits a machine-size ceiling and cannot absorb a spiky workload cheaply.')
t('disaster_recovery_plan', 'Define a recovery objective and test the recovery path',
  'A recovery time and recovery point objective turn disaster recovery from an intention into a design.')

# --- Shared responsibility model -------------------------------------------
t('srm_aws_hardware', 'AWS is responsible for the physical facilities and hardware',
  'AWS operates the buildings, power, network fabric and the hardware underneath the service.')
t('srm_aws_managed_service', 'AWS is responsible for patching a managed service such as Amazon S3',
  'The service itself is operated by AWS, including its underlying platform patches.')
t('srm_customer_data', 'The customer is responsible for the data it stores in AWS',
  'Classification, access and protection of the data remain with the customer.')
t('srm_customer_guest_os', 'The customer is responsible for patching the guest operating system on Amazon EC2',
  'The instance is the customer layer, so its operating system and applications are the customer job.')
t('srm_customer_iam', 'The customer is responsible for configuring IAM permissions',
  'Identity and access configuration is a customer responsibility in every model.')
t('srm_shared_controls', 'Some controls are shared, such as patch awareness',
  'AWS patches the infrastructure while the customer patches what it runs on top of it.')
t('srm_aws_customer_data', 'AWS is responsible for encrypting customer data by default',
  'Data protection choices such as encryption and key custody belong to the customer.')
t('srm_customer_facility', 'The customer is responsible for the data-centre building',
  'Physical facilities are AWS operated, not customer operated.')

# --- Identity and access ----------------------------------------------------
t('iam_user', 'Create an IAM user with long-lived credentials',
  'A user is an identity for a person or application with its own credentials.')
t('iam_role', 'Create an IAM role and let the workload assume it',
  'A role hands out temporary credentials, so nothing long-lived is stored.')
t('iam_group', 'Put the users in a group and attach the policy to the group',
  'A group is a collection of users that share permissions, which keeps the policy in one place.')
t('iam_policy_json', 'Attach a JSON policy that allows only the required actions',
  'A policy document states which actions are allowed on which resources.')
t('iam_mfa', 'Require multi-factor authentication',
  'A second factor makes a stolen password insufficient on its own.')
t('iam_least_privilege', 'Grant only the permissions the task needs',
  'Starting from the minimum and adding as needed keeps the blast radius small.')
t('iam_admin_default', 'Give every engineer administrator access for convenience',
  'Broad standing access means one mistaken action or stolen credential can change anything.')
t('identity_federation', 'Federate the company directory into AWS',
  'Existing corporate identities are used instead of a separate set of AWS credentials.')
t('root_use_daily', 'Use the root user for daily administration',
  'The root user cannot be restricted by policy, so daily use magnifies any mistake.')
t('root_mfa_delete', 'Enable MFA and delete the root access keys',
  'The root user is the most privileged identity, so it is protected and its keys are removed.')
t('root_shared_team', 'Share the root credentials with the operations team',
  'Sharing root credentials removes accountability and cannot be limited by policy.')
t('access_key_rotation', 'Rotate access keys on a schedule',
  'A rotation schedule limits how long a leaked key stays useful.')

# --- Network and perimeter security ---------------------------------------
t('security_group', 'Use a security group as a stateful instance firewall',
  'The group allows inbound or outbound traffic and remembers the connection state.')
t('nacl', 'Use a network ACL as a stateless subnet filter',
  'The ACL filters traffic at the subnet boundary and evaluates each direction independently.')
t('waf', 'Use AWS WAF to block web attack patterns',
  'WAF inspects HTTP requests and applies rules for injection, scripting and similar attacks.')
t('shield', 'Use AWS Shield for DDoS protection',
  'Shield absorbs distributed denial-of-service traffic before it reaches the application.')
t('network_firewall', 'Use AWS Network Firewall for VPC-level inspection',
  'A managed firewall inspects traffic entering and leaving the VPC.')
t('open_all_ports', 'Open every port to the internet and rely on the application',
  'An open perimeter exposes every service on the host, including ones nobody meant to publish.')

# --- Encryption and secrets ------------------------------------------------
t('kms', 'Use AWS KMS to create and control encryption keys',
  'A managed key service creates, stores and audits the keys used to encrypt data.')
t('sse_s3', 'Rely on server-side encryption with Amazon S3 managed keys',
  'S3 encrypts the object at rest with keys it manages on the customer behalf.')
t('encryption_transit', 'Encrypt data in transit with TLS',
  'Traffic is protected while it crosses the network, not only while it sits on disk.')
t('acm', 'Use AWS Certificate Manager for TLS certificates',
  'Certificates are issued, renewed and deployed to integrated services without manual work.')
t('secrets_manager', 'Store the database credential in AWS Secrets Manager and rotate it',
  'The secret is held centrally and can be rotated on a schedule.')
t('hardcoded_secret', 'Put the password in the application source code',
  'A credential in source code is copied to every environment and cannot be rotated quietly.')
t('customer_managed_key', 'Use a customer managed key for the required control',
  'The customer controls the key policy and can revoke access by disabling the key.')

# --- Compliance and audit ---------------------------------------------------
t('aws_artifact', 'Download the compliance reports from AWS Artifact',
  'Artifact provides AWS audit reports and agreements on demand.')
t('aws_config', 'Use AWS Config to record resource configuration changes',
  'Config keeps a history of configuration and evaluates it against rules.')
t('cloudtrail', 'Use AWS CloudTrail to record API activity',
  'CloudTrail logs who called which API, when and from where.')
t('audit_manager', 'Use AWS Audit Manager to collect evidence for an audit',
  'Audit Manager assembles evidence against a chosen framework.')
t('trusted_advisor_security', 'Read the security checks in AWS Trusted Advisor',
  'Trusted Advisor inspects the account and reports insecure or wasteful settings.')
t('compliance_inherit', 'Inherit AWS compliance reports for the shared controls',
  'Controls AWS operates can be evidenced with its reports rather than re-tested by the customer.')

# --- Threat detection -------------------------------------------------------
t('guardduty', 'Use Amazon GuardDuty to detect suspicious activity',
  'GuardDuty analyses account, network and DNS activity for signs of compromise.')
t('inspector', 'Use Amazon Inspector to scan workloads for vulnerabilities',
  'Inspector finds software vulnerabilities and unintended network exposure on the resources it scans.')
t('macie', 'Use Amazon Macie to find sensitive data in Amazon S3',
  'Macie classifies objects and reports where personal or sensitive data is stored.')
t('security_hub', 'Use AWS Security Hub to aggregate findings in one place',
  'Security Hub collects findings from the security services and scores them against a standard.')
t('detective', 'Use Amazon Detective to investigate a finding',
  'Detective builds a behaviour graph that helps explain how a finding happened.')

# --- Federation and organisation guardrails --------------------------------
t('organizations_scp', 'Apply a service control policy in AWS Organizations',
  'An SCP sets the maximum permissions available to the accounts under it.')
t('iam_identity_center', 'Use IAM Identity Center for workforce sign-in',
  'Workforce users sign in once and receive permission sets for the accounts they use.')
t('cognito', 'Use Amazon Cognito for customer sign-in',
  'Cognito handles sign-up, sign-in and tokens for an application end users.')
t('verified_access', 'Use AWS Verified Access for application-level access',
  'Access to an internal application is granted per request after identity and device checks.')
t('scp_permission_grant', 'Use a service control policy to grant permissions to a team',
  'An SCP only limits permissions; it never grants them.')

# --- Compute ---------------------------------------------------------------
t('ec2', 'Amazon EC2 instances',
  'Virtual servers where the customer controls the operating system and the runtime.')
t('lambda', 'AWS Lambda',
  'Run code on an event without provisioning or managing a server.')
t('containers', 'Amazon ECS or Amazon EKS with AWS Fargate',
  'Managed container orchestration where the platform runs the hosts.')
t('beanstalk', 'AWS Elastic Beanstalk',
  'Upload the application and let the platform provision and manage the environment.')
t('lightsail', 'Amazon Lightsail',
  'A simplified bundle of compute, storage and networking for small projects at a predictable price.')
t('batch', 'AWS Batch',
  'Queue and run batch computing jobs without managing the scheduler infrastructure.')
t('app_runner', 'AWS App Runner',
  'Run a containerised web service without choosing or managing the underlying capacity.')
t('ec2_patching_aws', 'Expect AWS to patch the operating system on Amazon EC2 for the customer',
  'The guest operating system on an instance belongs to the customer layer.')

# --- Storage ---------------------------------------------------------------
t('s3_standard', 'Amazon S3 Standard',
  'Object storage for frequently accessed data with high durability and availability.')
t('s3_standard_ia', 'Amazon S3 Standard-IA',
  'Object storage for data that is accessed less often but must be available immediately.')
t('s3_glacier', 'Amazon S3 Glacier storage classes',
  'Archive storage for data that is rarely read and tolerates retrieval time.')
t('s3_intelligent', 'Amazon S3 Intelligent-Tiering',
  'Object storage that moves objects between access tiers as usage changes.')
t('ebs', 'Amazon EBS volumes',
  'Block storage attached to a single instance, used for an operating system or database files.')
t('efs', 'Amazon EFS file system',
  'A shared file system that many Linux instances can mount at the same time.')
t('fsx', 'Amazon FSx file systems',
  'Managed file systems for Windows or high-performance workloads.')
t('storage_gateway', 'AWS Storage Gateway',
  'A hybrid file, volume or tape interface that keeps frequently used data on premises.')
t('snowball', 'AWS Snowball devices',
  'Physical devices that move large datasets into AWS when the network is the bottleneck.')
t('backup', 'AWS Backup',
  'A managed service that centralises and automates backups across supported services.')
t('s3_bucket_policy', 'An Amazon S3 bucket policy that grants public read',
  'A public bucket policy exposes every object in the bucket to anyone on the internet.')

# --- Databases ------------------------------------------------------------
t('rds', 'Amazon RDS',
  'A managed relational database where AWS handles patching, backups and failover options.')
t('aurora', 'Amazon Aurora',
  'A managed relational engine compatible with MySQL or PostgreSQL with higher throughput.')
t('dynamodb', 'Amazon DynamoDB',
  'A managed key-value and document store for high-volume, predictable-latency access.')
t('redshift', 'Amazon Redshift',
  'A managed data warehouse for analytical queries over large datasets.')
t('elasticache', 'Amazon ElastiCache',
  'A managed in-memory cache for sub-millisecond reads of hot data.')
t('neptune', 'Amazon Neptune',
  'A managed graph database for highly connected data.')
t('documentdb', 'Amazon DocumentDB',
  'A managed document database compatible with MongoDB workloads.')
t('rds_manual_patch', 'Patch the database engine and host yourself on Amazon EC2',
  'That is the self-managed option, where every maintenance task belongs to the customer.')

# --- Networking and delivery ---------------------------------------------
t('vpc', 'Amazon VPC',
  'A logically isolated virtual network in which the customer places its resources.')
t('route53', 'Amazon Route 53',
  'A managed DNS service that also supports health checks and routing policies.')
t('cloudfront', 'Amazon CloudFront',
  'A content delivery network that caches content at edge locations near users.')
t('direct_connect', 'AWS Direct Connect',
  'A dedicated private network connection from a customer facility into AWS.')
t('site_to_site_vpn', 'AWS Site-to-Site VPN',
  'An encrypted tunnel over the internet between a customer network and a VPC.')
t('elb', 'Elastic Load Balancing',
  'Distributes incoming traffic across multiple targets in one or more Availability Zones.')
t('api_gateway', 'Amazon API Gateway',
  'A managed front door for APIs with throttling, authorisation and usage plans.')
t('transit_gateway', 'AWS Transit Gateway',
  'A central router that connects many VPCs and on-premises networks.')
t('privatelink', 'AWS PrivateLink',
  'Private connectivity to a service through an endpoint inside the VPC.')
t('global_accelerator', 'AWS Global Accelerator',
  'Anycast addresses that route traffic over the AWS global network to the closest healthy endpoint.')
t('internet_open_vpc', 'Put the database in a public subnet with a route to the internet',
  'A public path to a database removes the network boundary the VPC is there to provide.')

# --- Management and governance -------------------------------------------
t('cloudwatch', 'Amazon CloudWatch',
  'Metrics, logs and alarms for the resources and applications in the account.')
t('cloudformation', 'AWS CloudFormation',
  'Infrastructure defined as a template and created or updated as a stack.')
t('systems_manager', 'AWS Systems Manager',
  'Operations tooling for patching, running commands and inventory across managed nodes.')
t('trusted_advisor', 'AWS Trusted Advisor',
  'Checks an account against best practices for cost, security, limits and resilience.')
t('service_catalog', 'AWS Service Catalog',
  'A curated catalogue of approved products that teams can launch themselves.')
t('control_tower', 'AWS Control Tower',
  'A landing zone that applies baseline controls across an organisation.')
t('health_dashboard', 'AWS Health Dashboard',
  'Service health and event notifications that affect the account.')

# --- Integration and messaging -------------------------------------------
t('sqs', 'Amazon SQS',
  'A managed queue that decouples producers from consumers and buffers bursts.')
t('sns', 'Amazon SNS',
  'A pub/sub topic that fans a message out to many subscribers.')
t('eventbridge', 'Amazon EventBridge',
  'An event bus that routes events from AWS services and applications to targets by rule.')
t('step_functions', 'AWS Step Functions',
  'A state machine that coordinates multi-step workflows with retries and branching.')
t('kinesis', 'Amazon Kinesis',
  'Streaming data ingestion and processing for continuous records.')
t('mq', 'Amazon MQ',
  'A managed message broker for existing protocols such as AMQP or MQTT.')

# --- Analytics, AI and developer tools -----------------------------------
t('sagemaker', 'Amazon SageMaker',
  'Build, train and deploy machine learning models through a managed platform.')
t('bedrock', 'Amazon Bedrock',
  'Access foundation models through an API without operating the model infrastructure.')
t('athena', 'Amazon Athena',
  'Query data in Amazon S3 with SQL and no infrastructure to manage.')
t('glue', 'AWS Glue',
  'A managed data catalogue and extract-transform-load service.')
t('emr', 'Amazon EMR',
  'Managed clusters for big-data frameworks such as Spark and Hadoop.')
t('quicksight', 'Amazon QuickSight',
  'A managed business intelligence service for dashboards and reports.')
t('codepipeline', 'AWS CodePipeline',
  'Orchestrates the build, test and deploy stages of a release.')
t('codebuild', 'AWS CodeBuild',
  'Compiles code and runs tests in a managed build environment.')
t('codedeploy', 'AWS CodeDeploy',
  'Automates the deployment of application revisions to instances and services.')
t('cloud9', 'AWS Cloud9',
  'A cloud-based integrated development environment that runs in the browser.')
t('xray', 'AWS X-Ray',
  'Traces requests through a distributed application to find where time is spent.')

# --- Pricing ---------------------------------------------------------------
t('on_demand', 'On-Demand Instances',
  'Capacity billed by the second or hour with no commitment.')
t('reserved_instances', 'Reserved Instances',
  'A one- or three-year commitment in exchange for a lower hourly rate.')
t('spot_instances', 'Spot Instances',
  'Spare capacity at a steep discount that can be reclaimed with short notice.')
t('savings_plans', 'Savings Plans',
  'A commitment to a spend level per hour in exchange for a discount across eligible usage.')
t('dedicated_hosts', 'Dedicated Hosts',
  'A physical server dedicated to one customer, used for licensing or compliance requirements.')
t('spot_for_database', 'Run the production database on Spot Instances',
  'Reclaimable capacity is unsuitable for work that cannot be interrupted.')

# --- Cost management ------------------------------------------------------
t('cost_explorer', 'AWS Cost Explorer',
  'Visualise and analyse past spend and forecast what is coming.')
t('budgets', 'AWS Budgets',
  'Set a spending or usage threshold and alert or act when it is crossed.')
t('cost_usage_report', 'AWS Cost and Usage Report',
  'The most granular billing dataset, delivered to a bucket for analysis.')
t('pricing_calculator', 'AWS Pricing Calculator',
  'Estimate the cost of a planned architecture before it is built.')
t('cost_anomaly', 'Cost Anomaly Detection',
  'Machine learning alerts on spending that deviates from the expected pattern.')
t('cost_allocation_tags', 'Tag resources and activate cost allocation tags',
  'Activated tags split the one bill by department, project or cost centre.')
t('invoice_only', 'Wait for the monthly invoice and reconcile it afterwards',
  'A retrospective invoice reveals overspend only after the money is gone.')

# --- Support --------------------------------------------------------------
t('support_basic', 'AWS Basic Support',
  'Account and billing support with documentation and health checks, at no charge.')
t('support_developer', 'AWS Developer Support',
  'Business-hours email support for development and test workloads.')
t('support_business', 'AWS Business Support',
  'Production support with 24/7 access, faster response and Trusted Advisor checks.')
t('support_enterprise', 'AWS Enterprise Support',
  'Mission-critical support with a designated technical account manager and the fastest response.')
t('tam', 'A designated Technical Account Manager',
  'A named advisor who understands the account and helps with planning and escalation.')
t('consolidated_billing', 'Consolidated billing in AWS Organizations',
  'One bill for all accounts, with usage aggregated so volume discounts are shared.')
t('separate_bills', 'Keep a separate bill and separate discounts per account',
  'Separate accounts do not pool usage, so each misses the discounts the total would earn.')
t('free_tier', 'The AWS Free Tier allowances',
  'Limited monthly usage at no charge for eligible services on a new or qualifying account.')
t('basic_support_sla', 'Expect a one-hour response on production issues from Basic Support',
  'Basic Support covers account and billing questions, not production incident response.')

# --- Guidance and self-service resources ---------------------------------
t('aws_docs', 'Read the AWS documentation and service user guides',
  'The reference documentation states what a service does and how it is configured.')
t('re_post', 'Search AWS re:Post for an answered question',
  'The community knowledge base holds answers to common service and account questions.')
t('solutions_library', 'Start from an AWS Solutions Library reference deployment',
  'A vetted reference architecture shortens design work for a common workload.')
t('partner_network', 'Engage an AWS Partner for the delivery work',
  'Partners are third-party firms with AWS-validated skills for implementation work.')
t('marketplace', 'Buy the software through AWS Marketplace',
  'Marketplace purchases are billed on the AWS invoice and can draw on committed spend.')

# --- Data handling --------------------------------------------------------
t('data_classification', 'Classify the data and tag each store by sensitivity',
  'A classification decides which controls and retention rules apply to each dataset.')
t('public_snapshot', 'Share the snapshot publicly so partners can download it',
  'A public snapshot exposes the whole dataset to anyone who finds it.')
t('retention_policy', 'Set a retention period and delete expired copies',
  'A retention rule stops data from being kept forever by default.')
t('lifecycle_policy', 'Set an S3 lifecycle rule to expire old objects',
  'A lifecycle rule moves or deletes objects automatically as they age.')
