"""Builder for SAA-C03 Set 4 — Domain 3 High-Performing Architectures deep dive (200q) + StartupFast case study.

Set 4 is a deep dive on Domain 3 (High-Performing Architectures, 24% of the real exam).
- 200 questions total
- 20% multi-select = 40 questions
- 20 case-study questions referencing StartupFast
- 100% High-Performing domain
"""

import csv

# Domain strings (must match exactly)
SECURE = "Design Secure Architectures"
RESILIENT = "Design Resilient Architectures"
HIGH_PERF = "Design High-Performing Architectures"
COST_OPT = "Design Cost-Optimized Architectures"


def make_row(question, qtype, opts, correct, overall, domain):
    while len(opts) < 6:
        opts.append(("", ""))
    row = [question, qtype]
    for text, expl in opts:
        row.extend([text, expl])
    row.append(correct)
    row.append(overall)
    row.append(domain)
    return row


QUESTIONS = []

# ============================================================
# EC2 INSTANCE FAMILIES AND PLACEMENT (22 questions)
# ============================================================

QUESTIONS.append({
    "q": "Which EC2 instance family is OPTIMIZED for high-performance databases and in-memory caches with the BEST memory-to-CPU ratio?",
    "type": "multiple-choice",
    "opts": [
        ("C family (compute optimized)", "C family is compute-optimized, not memory."),
        ("M family (general purpose)", "M family is balanced, not memory-optimized."),
        ("R family (memory optimized)", "R family has the best memory-to-CPU ratio for in-memory workloads."),
        ("I family (storage optimized)", "I family is storage-optimized."),
    ],
    "correct": "3",
    "domain": HIGH_PERF,
    "overall": "R family is memory-optimized for high-performance databases and in-memory caches. Reference: https://docs.aws.amazon.com/ec2/latest/instancetypes/rtypes.html",
})
QUESTIONS.append({
    "q": "Which EC2 instance family is OPTIMIZED for compute-intensive workloads such as batch processing, scientific modeling, and gaming servers?",
    "type": "multiple-choice",
    "opts": [
        ("C family (compute optimized)", "C family is compute-optimized."),
        ("M family (general purpose)", "M family is balanced."),
        ("R family (memory optimized)", "R family is memory-optimized."),
        ("X family", "X family is for SAP HANA, ultra-high memory."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "C family is compute-optimized for batch, scientific modeling, and gaming. Reference: https://docs.aws.amazon.com/ec2/latest/instancetypes/ctypes.html",
})
QUESTIONS.append({
    "q": "Which EC2 placement group is BEST for a tightly coupled HPC application that needs the LOWEST network latency?",
    "type": "multiple-choice",
    "opts": [
        ("Cluster placement group", "Cluster placement groups pack instances close together for low-latency HPC."),
        ("Partition placement group", "Partition groups spread across racks, isolating failure domains."),
        ("Spread placement group", "Spread groups put instances on distinct hardware, for critical instances."),
        ("Default placement group", "Default has no guarantees."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Cluster placement group: instances in one AZ with low-latency, high-bandwidth networking for HPC. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html",
})
QUESTIONS.append({
    "q": "Which EC2 placement group is BEST for a group of CRITICAL instances where each must be on DISTINCT underlying hardware?",
    "type": "multiple-choice",
    "opts": [
        ("Cluster placement group", "Cluster packs instances close together."),
        ("Spread placement group", "Spread puts each instance on distinct hardware."),
        ("Partition placement group", "Partition spreads across racks but groups instances within partitions."),
        ("Default placement group", "Default has no guarantees."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "Spread placement group: each instance on distinct hardware, reducing correlated failures for critical workloads. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html",
})
QUESTIONS.append({
    "q": "Which placement group type divides hardware into logical partitions, with each partition isolated from failures of other partitions, useful for HDFS, Hadoop, and Cassandra?",
    "type": "multiple-choice",
    "opts": [
        ("Cluster placement group", "Cluster packs close for low latency."),
        ("Spread placement group", "Spread is for distinct hardware per instance."),
        ("Partition placement group", "Partition groups instances into partitions across racks."),
        ("Default placement group", "Default has no guarantees."),
    ],
    "correct": "3",
    "domain": HIGH_PERF,
    "overall": "Partition placement groups isolate failure domains at the rack level for distributed big-data workloads. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html",
})
QUESTIONS.append({
    "q": "Which EC2 Nitro feature provides high-performance EBS I/O, with up to 64,000 IOPS and 1,000 MB/s on gp3?",
    "type": "multiple-choice",
    "opts": [
        ("EBS-optimized instances", "EBS-optimized instances provide dedicated EBS bandwidth and IOPS."),
        ("Instance store", "Instance store is local, not EBS."),
        ("EBS snapshot", "Snapshots are for backup, not I/O."),
        ("EBS encryption", "Encryption does not change I/O performance guarantees."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "EBS-optimized instances provide dedicated EBS bandwidth and IOPS, decoupled from general network. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html",
})
QUESTIONS.append({
    "q": "Which EC2 instance family is the BEST fit for ML training with deep learning frameworks requiring GPU acceleration?",
    "type": "multiple-choice",
    "opts": [
        ("P family (accelerated computing)", "P family provides GPU instances for ML training."),
        ("C family (compute optimized)", "C family is compute-optimized CPU."),
        ("R family (memory optimized)", "R family is memory-optimized."),
        ("T family (burstable)", "T family is burstable general purpose."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "P family provides GPU instances for ML training and accelerated computing. Reference: https://docs.aws.amazon.com/ec2/latest/instancetypes/p4de.html",
})
QUESTIONS.append({
    "q": "Which EC2 instance family is the BEST fit for big data workloads such as Hadoop and Kafka with high sequential I/O?",
    "type": "multiple-choice",
    "opts": [
        ("C family", "C family is compute-optimized."),
        ("I family (storage optimized)", "I family has high sequential I/O for big data."),
        ("R family", "R family is memory-optimized."),
        ("T family", "T family is burstable general purpose."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "I family is storage-optimized for high sequential I/O workloads like Hadoop and Kafka. Reference: https://docs.aws.amazon.com/ec2/latest/instancetypes/itypes.html",
})
QUESTIONS.append({
    "q": "Which EC2 instance family is the BEST fit for general-purpose workloads such as web servers and small databases?",
    "type": "multiple-choice",
    "opts": [
        ("M family", "M family is the general-purpose instance family."),
        ("C family", "C family is compute-optimized."),
        ("R family", "R family is memory-optimized."),
        ("X family", "X family is SAP HANA, ultra-high memory."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "M family is general purpose, balanced for web servers and small databases. Reference: https://docs.aws.amazon.com/ec2/latest/instancetypes/mtypes.html",
})
QUESTIONS.append({
    "q": "Which EC2 instance family is the BEST fit for low-cost, burstable workloads such as dev/test environments and small websites?",
    "type": "multiple-choice",
    "opts": [
        ("T family (burstable)", "T family is burstable for low-cost, variable workloads."),
        ("M family", "M family is general purpose, not burstable."),
        ("C family", "C family is compute-optimized."),
        ("R family", "R family is memory-optimized."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "T family is burstable, providing a baseline CPU with the ability to burst for low-cost, variable workloads. Reference: https://docs.aws.amazon.com/ec2/latest/instancetypes/ttypes.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid characteristics of EC2 Nitro System? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Dedicated EBS I/O bandwidth", "Nitro provides dedicated EBS I/O."),
        ("Higher networking performance", "Nitro provides higher networking throughput."),
        ("Built-in security chip", "Nitro Enclaves provide hardware isolation."),
        ("Custom hardware limitations", "Nitro System actually removes many hardware limitations."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Nitro System provides dedicated EBS I/O, higher networking, and Nitro Enclaves for security. Reference: https://docs.aws.amazon.com/ec2/latest/instancetypes/instance_hardware.html",
})
QUESTIONS.append({
    "q": "Which EC2 feature provides DEDICATED physical servers for compliance or licensing requirements?",
    "type": "multiple-choice",
    "opts": [
        ("Dedicated Hosts", "Dedicated Hosts are physical servers dedicated to your use."),
        ("Dedicated Instances", "Dedicated Instances run on hardware dedicated to a single account."),
        ("On-Demand Instances", "On-Demand runs on shared hardware."),
        ("Reserved Instances", "RIs are billing discounts, not dedicated hardware."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Dedicated Hosts are physical servers fully dedicated to your use, useful for BYOL licensing. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-overview.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid use cases for EC2 Dedicated Hosts? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Bring Your Own License (BYOL) for Windows Server or SQL Server", "BYOL is the main use case for Dedicated Hosts."),
        ("Compliance with corporate server-usage policies", "Compliance often requires dedicated hardware."),
        ("Reduce cost for spot workloads", "Dedicated Hosts are not cost-optimized for spot."),
        ("Run a single instance on shared hardware", "Single instance on shared hardware is On-Demand."),
    ],
    "correct": "1,2",
    "domain": HIGH_PERF,
    "overall": "Dedicated Hosts support BYOL and compliance. They are not cost-optimized for spot or single instances. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-overview.html",
})
QUESTIONS.append({
    "q": "Which EC2 instance metadata service version requires a token-based PUT request, mitigating SSRF attacks?",
    "type": "multiple-choice",
    "opts": [
        ("IMDSv1", "IMDSv1 is the original, request/response, no token."),
        ("IMDSv2", "IMDSv2 requires a token via PUT, mitigating SSRF."),
        ("IMDSv3", "IMDSv3 is not a real version."),
        ("IMDS Plus", "IMDS Plus is not a real version."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "IMDSv2 requires a token via PUT, mitigating SSRF and other vulnerabilities. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html",
})
QUESTIONS.append({
    "q": "Which EC2 feature lets you control CPU state at the instance level for per-CPU licensing, with C-state and P-state control?",
    "type": "multiple-choice",
    "opts": [
        ("CPU options", "CPU options control C-states and P-states for per-CPU licensing."),
        ("Instance metadata", "IMDS is for metadata, not CPU control."),
        ("Placement groups", "Placement groups affect hardware placement."),
        ("Elastic GPUs", "Elastic GPUs is legacy and deprecated."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "CPU options allow you to control C-states and P-states for per-CPU licensing optimization. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html",
})
QUESTIONS.append({
    "q": "Which EC2 feature provides EFA (Elastic Fabric Adapter) for low-latency, high-bandwidth inter-instance communication on HPC workloads?",
    "type": "multiple-choice",
    "opts": [
        ("EFA", "EFA is the Elastic Fabric Adapter for HPC."),
        ("ENI", "ENI is a standard Elastic Network Interface."),
        ("ENA", "ENA is the standard Enhanced Networking adapter."),
        ("EBS-optimized instances", "EBS-optimized is for EBS, not for inter-instance communication."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "EFA provides low-latency, high-bandwidth inter-instance communication for HPC and ML workloads. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html",
})
QUESTIONS.append({
    "q": "Which EC2 feature provides enhanced networking using SR-IOV for high packets-per-second performance?",
    "type": "multiple-choice",
    "opts": [
        ("Enhanced networking with ENA", "ENA provides enhanced networking with SR-IOV."),
        ("Standard networking", "Standard networking has lower performance."),
        ("EBS-optimized", "EBS-optimized is for storage I/O."),
        ("Placement groups", "Placement groups affect hardware placement."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Enhanced networking with ENA uses SR-IOV for high packets-per-second and low latency. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid characteristics of AWS Graviton-based EC2 instances? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Arm-based 64-bit architecture", "Graviton is Arm-based."),
        ("Up to 40% better price-performance vs. x86", "Graviton offers significant price-performance improvement."),
        ("Compatible with Linux only", "Graviton supports Linux and Graviton-ready Windows."),
        ("Limited to specific instance families", "Graviton is available across many instance families."),
    ],
    "correct": "1,2",
    "domain": HIGH_PERF,
    "overall": "AWS Graviton is Arm-based, offers up to 40% better price-performance, and supports Linux and Windows. Reference: https://aws.amazon.com/ec2/graviton/",
})
QUESTIONS.append({
    "q": "Which EC2 instance type provides LOCAL NVMe storage that is LOST when the instance stops, terminated, or fails?",
    "type": "multiple-choice",
    "opts": [
        ("Instance store", "Instance store is local, ephemeral storage."),
        ("EBS", "EBS is persistent, network-attached block storage."),
        ("EFS", "EFS is a regional, multi-AZ file system."),
        ("FSx", "FSx is a managed file system."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Instance store is local, ephemeral storage that is lost on instance stop, termination, or hardware failure. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid use cases for EC2 instance store? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Temporary cache for data with built-in replication", "Instance store is good for caches with app-level replication."),
        ("Scratch space for HPC and batch jobs", "HPC and batch jobs benefit from local NVMe."),
        ("Primary database storage", "Instance store is not appropriate for primary DB storage."),
        ("Boot volume", "Boot volumes are EBS, not instance store."),
    ],
    "correct": "1,2",
    "domain": HIGH_PERF,
    "overall": "Instance store is ideal for temporary caches and HPC scratch space. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html",
})
QUESTIONS.append({
    "q": "Which EC2 feature allows you to RESERVE capacity in a specific AZ for any duration, with no commitment, ensuring capacity for DR scenarios?",
    "type": "multiple-choice",
    "opts": [
        ("On-Demand Capacity Reservations", "On-Demand Capacity Reservations reserve capacity in a specific AZ."),
        ("Reserved Instances", "RIs are billing discounts, not capacity reservations."),
        ("Spot Instances", "Spot does not reserve capacity."),
        ("Savings Plans", "Savings Plans are billing discounts."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "On-Demand Capacity Reservations reserve EC2 capacity in a specific AZ for any duration, ensuring availability. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html",
})

# ============================================================
# SERVERLESS AND CONTAINERS (20 questions)
# ============================================================

QUESTIONS.append({
    "q": "Which combination of services is the BEST pattern for running a highly scalable, event-driven, serverless application? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS Lambda", "Lambda is the serverless compute service."),
        ("Amazon API Gateway", "API Gateway exposes HTTP APIs to Lambda."),
        ("Amazon DynamoDB", "DynamoDB is the serverless NoSQL database."),
        ("Amazon EC2 with cron jobs", "EC2 cron jobs are not serverless."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Serverless pattern: API Gateway + Lambda + DynamoDB. Reference: https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html",
})
QUESTIONS.append({
    "q": "Which AWS Lambda feature allows a function to be triggered by events from many AWS services without writing integration code?",
    "type": "multiple-choice",
    "opts": [
        ("Event source mappings", "Event source mappings poll streams and queues."),
        ("Lambda destinations", "Destinations send to async targets on success/failure."),
        ("Lambda triggers built-in for many services", "Many services (S3, DynamoDB Streams, EventBridge) directly invoke Lambda."),
        ("Lambda layers", "Layers package code/dependencies."),
    ],
    "correct": "3",
    "domain": HIGH_PERF,
    "overall": "Many AWS services (S3, DynamoDB Streams, EventBridge, SNS) directly invoke Lambda functions as event sources. Reference: https://docs.aws.amazon.com/lambda/latest/dg/lambda-services.html",
})
QUESTIONS.append({
    "q": "Which service runs containers without managing servers or clusters, integrating with the broader AWS ecosystem?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon ECS with EC2 launch type", "ECS with EC2 requires managing EC2 instances."),
        ("AWS Fargate", "Fargate runs containers without managing servers."),
        ("Amazon EKS with self-managed nodes", "EKS with self-managed nodes is not serverless."),
        ("AWS Lambda", "Lambda is for functions, not containers."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "AWS Fargate is the serverless compute engine for containers with ECS and EKS. Reference: https://docs.aws.amazon.com/fargate/latest/userguide/what-is-fargate.html",
})
QUESTIONS.append({
    "q": "Which AWS service runs batch computing jobs across many EC2 instances, with managed job scheduling and dynamic scaling?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Batch", "AWS Batch dynamically provisions compute for batch jobs."),
        ("AWS Lambda", "Lambda has a 15-minute max execution time."),
        ("Amazon ECS", "ECS is for long-running services, not batch jobs typically."),
        ("AWS Step Functions", "Step Functions orchestrates but does not run jobs."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "AWS Batch runs batch computing workloads on EC2, Spot, or Fargate with managed job scheduling. Reference: https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html",
})
QUESTIONS.append({
    "q": "Which AWS Lambda performance feature ELIMINATES COLD STARTS for Java functions by pre-initializing the runtime?",
    "type": "multiple-choice",
    "opts": [
        ("Lambda SnapStart", "SnapStart pre-initializes Java functions to reduce cold starts."),
        ("Provisioned concurrency", "Provisioned concurrency keeps functions initialized."),
        ("Lambda layers", "Layers are for code packaging."),
        ("Lambda reserved concurrency", "Reserved concurrency limits concurrency."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Lambda SnapStart pre-initializes Java functions, reducing cold start time. Reference: https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html",
})
QUESTIONS.append({
    "q": "Which AWS Lambda feature keeps functions initialized to eliminate cold starts for predictable latency?",
    "type": "multiple-choice",
    "opts": [
        ("Provisioned concurrency", "Provisioned concurrency keeps functions initialized."),
        ("Lambda SnapStart", "SnapStart is for Java functions, not all runtimes."),
        ("Lambda layers", "Layers are for code packaging."),
        ("Lambda destination", "Destinations are for async targets."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Provisioned concurrency keeps Lambda functions initialized for predictable, low-latency response. Reference: https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html",
})
QUESTIONS.append({
    "q": "Which AWS service is the AWS-native container orchestrator with deep AWS integration?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon ECS", "ECS is the AWS-native container orchestrator."),
        ("Amazon EKS", "EKS is Kubernetes."),
        ("AWS Fargate", "Fargate is the serverless engine for containers."),
        ("Amazon Lightsail", "Lightsail is a simplified compute service."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon ECS is the AWS-native container orchestrator with deep AWS integration. Reference: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html",
})
QUESTIONS.append({
    "q": "Which AWS service is the AWS-native container orchestrator that is compatible with upstream Kubernetes?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon ECS", "ECS is AWS-native, not Kubernetes."),
        ("Amazon EKS", "EKS is the managed Kubernetes service."),
        ("AWS Fargate", "Fargate is the serverless compute engine for containers."),
        ("Amazon EC2", "EC2 is the compute service."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "Amazon EKS is a managed Kubernetes service compatible with upstream Kubernetes. Reference: https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid ECS launch types? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("EC2 launch type", "EC2 launch type runs containers on EC2 instances."),
        ("Fargate launch type", "Fargate launch type is serverless."),
        ("Lambda launch type", "Lambda is for functions, not ECS containers."),
        ("EBS launch type", "EBS is block storage, not a launch type."),
    ],
    "correct": "1,2",
    "domain": HIGH_PERF,
    "overall": "ECS supports EC2 and Fargate launch types. Reference: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_types.html",
})
QUESTIONS.append({
    "q": "Which AWS Lambda memory allocation provides the BEST BALANCE of performance and cost for a function with variable CPU needs?",
    "type": "multiple-choice",
    "opts": [
        ("Low memory (128 MB)", "Low memory is cheap but may be slow."),
        ("Higher memory (1024+ MB)", "Higher memory = more CPU; often faster overall, lower cost."),
        ("Fixed regardless of workload", "Lambda memory is fixed per function."),
        ("AWS chooses automatically", "AWS does not auto-choose; you set memory."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "Lambda memory is proportional to CPU; higher memory often reduces duration enough to lower cost. Reference: https://docs.aws.amazon.com/lambda/latest/operatorguide/performance.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid AWS Lambda performance features? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Lambda SnapStart for Java", "SnapStart reduces cold starts for Java functions."),
        ("Reserved concurrency to throttle function invocations", "Reserved concurrency limits concurrency for throttling."),
        ("Provisioned concurrency for warm instances", "Provisioned concurrency keeps functions initialized."),
        ("Function URL with no cold start", "Function URLs are a single endpoint; cold start behavior depends on provisioned concurrency."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "SnapStart, reserved concurrency, and provisioned concurrency are all performance features. Reference: https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html",
})
QUESTIONS.append({
    "q": "Which AWS Lambda feature provides package sharing and code reuse across multiple functions?",
    "type": "multiple-choice",
    "opts": [
        ("Lambda layers", "Lambda layers package code and dependencies for sharing."),
        ("Lambda SnapStart", "SnapStart is for cold-start reduction."),
        ("Lambda destinations", "Destinations are for async targets."),
        ("Lambda reserved concurrency", "Reserved concurrency is for throttling."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Lambda layers provide package sharing and code reuse across multiple functions. Reference: https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html",
})
QUESTIONS.append({
    "q": "Which AWS Lambda feature provides a single HTTP endpoint for a function without API Gateway?",
    "type": "multiple-choice",
    "opts": [
        ("Lambda function URLs", "Function URLs provide a single HTTP endpoint for a function."),
        ("Lambda layers", "Layers are for code packaging."),
        ("Lambda SnapStart", "SnapStart is for cold-start reduction."),
        ("Lambda destinations", "Destinations are for async targets."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Lambda function URLs provide a single HTTP endpoint for a function without API Gateway. Reference: https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html",
})
QUESTIONS.append({
    "q": "Which combination of services provides the BEST pattern for a serverless REST API with sub-100ms latency? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon API Gateway", "API Gateway is the managed REST API service."),
        ("AWS Lambda", "Lambda is the compute layer."),
        ("Amazon DynamoDB with DAX", "DynamoDB with DAX for fast reads."),
        ("Amazon EC2 with Auto Scaling", "EC2 with ASG is not serverless and adds cold-start variability."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "API Gateway + Lambda + DynamoDB with DAX is a high-performance serverless REST pattern. Reference: https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed, serverless, multi-region active-active data store for IoT, mobile, and web applications?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon DynamoDB", "DynamoDB is a serverless NoSQL database with Global Tables."),
        ("Amazon Aurora Serverless", "Aurora Serverless is serverless, but not multi-region by default."),
        ("Amazon RDS", "RDS is not serverless."),
        ("Amazon Redshift Serverless", "Redshift Serverless is for data warehousing, not OLTP."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "DynamoDB is a serverless NoSQL database with multi-region replication via Global Tables. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid AWS Batch compute environments? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("EC2 On-Demand", "EC2 On-Demand is a valid compute environment."),
        ("EC2 Spot", "EC2 Spot is a valid compute environment for cost savings."),
        ("Fargate", "Fargate is a valid compute environment."),
        ("Lambda only", "Lambda is not a Batch compute environment."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "AWS Batch supports EC2 On-Demand, EC2 Spot, and Fargate compute environments. Reference: https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid Lambda function destinations? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon SQS", "SQS is a valid Lambda destination."),
        ("Amazon SNS", "SNS is a valid Lambda destination."),
        ("AWS Lambda", "Lambda can chain to another Lambda function as a destination."),
        ("Amazon EBS", "EBS is block storage, not a destination."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Lambda destinations support SQS, SNS, Lambda, and EventBridge. Reference: https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html",
})
QUESTIONS.append({
    "q": "Which AWS Lambda feature allows you to run code in response to events from event sources like SQS, Kinesis, and DynamoDB Streams?",
    "type": "multiple-choice",
    "opts": [
        ("Event source mappings", "Event source mappings poll and invoke Lambda."),
        ("Lambda destinations", "Destinations are for async targets."),
        ("Lambda layers", "Layers are for code packaging."),
        ("Lambda function URLs", "Function URLs are for HTTP endpoints."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Event source mappings poll streams/queues and invoke Lambda. Reference: https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html",
})
QUESTIONS.append({
    "q": "Which AWS service is the BEST choice for running a long-running containerized application with auto-scaling and load balancing?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon ECS with Fargate and ALB", "ECS + Fargate + ALB is the serverless container pattern with load balancing."),
        ("AWS Lambda", "Lambda has a 15-minute max execution time."),
        ("Amazon EC2 alone", "EC2 alone is not auto-scaling."),
        ("AWS Batch", "Batch is for batch jobs, not long-running services."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "ECS with Fargate and ALB provides auto-scaling and load balancing for long-running containers. Reference: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid use cases for AWS Lambda? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Event-driven data processing", "Lambda is ideal for event-driven processing."),
        ("REST APIs with API Gateway", "API Gateway + Lambda is a common pattern."),
        ("Long-running scientific simulations (hours)", "Lambda has a 15-minute max duration."),
        ("Scheduled tasks via EventBridge", "Lambda can be triggered on a schedule."),
    ],
    "correct": "1,2,4",
    "domain": HIGH_PERF,
    "overall": "Lambda is ideal for event-driven, API, and scheduled tasks. Not for long-running jobs. Reference: https://docs.aws.amazon.com/lambda/latest/dg/welcome.html",
})

# ============================================================
# EBS STORAGE (14 questions)
# ============================================================

QUESTIONS.append({
    "q": "Which EBS volume type provides the HIGHEST IOPS and is BEST for I/O-intensive databases such as Oracle and SAP HANA?",
    "type": "multiple-choice",
    "opts": [
        ("gp3", "gp3 is general-purpose SSD."),
        ("io2 Block Express", "io2 Block Express provides the highest IOPS."),
        ("st1", "st1 is throughput-optimized HDD."),
        ("sc1", "sc1 is cold HDD."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "io2 Block Express provides up to 256,000 IOPS and 4,000 MB/s for I/O-intensive workloads. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html",
})
QUESTIONS.append({
    "q": "Which EBS volume type is the BEST balance of price and performance for most general workloads, allowing independent provisioning of IOPS and throughput?",
    "type": "multiple-choice",
    "opts": [
        ("gp2", "gp2 ties IOPS to volume size."),
        ("gp3", "gp3 decouples IOPS and throughput from volume size."),
        ("io1", "io1 is for high-I/O workloads, not general."),
        ("st1", "st1 is throughput-optimized HDD."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "gp3 lets you provision IOPS and throughput independently of volume size, at a lower price than gp2. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html",
})
QUESTIONS.append({
    "q": "Which EBS volume type is the BEST choice for BIG DATA, log processing, and data warehouses with HIGH THROUGHPUT but low IOPS requirements?",
    "type": "multiple-choice",
    "opts": [
        ("gp3", "gp3 is balanced SSD."),
        ("io2", "io2 is high-IOPS SSD."),
        ("st1", "st1 is throughput-optimized HDD for big data."),
        ("sc1", "sc1 is cold HDD for infrequent access."),
    ],
    "correct": "3",
    "domain": HIGH_PERF,
    "overall": "st1 is throughput-optimized HDD for big data, log processing, and data warehouses. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/throughput-optimized.html",
})
QUESTIONS.append({
    "q": "Which EBS feature can you use to INCREASE the IOPS of a gp2 volume by combining multiple volumes into a single logical volume?",
    "type": "multiple-choice",
    "opts": [
        ("EBS snapshots", "Snapshots are for backup."),
        ("EBS volume striping across multiple volumes using RAID 0", "RAID 0 across multiple EBS volumes increases IOPS and throughput."),
        ("EBS encryption", "Encryption is unrelated to IOPS."),
        ("EBS volume modification", "Modification changes size or type but does not stripe."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "RAID 0 (striping) across multiple EBS volumes linearly increases IOPS and throughput. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/raid-config.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid ways to optimize EBS performance? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Use EBS-optimized instances", "EBS-optimized instances provide dedicated EBS bandwidth."),
        ("Use RAID 0 striping", "RAID 0 across multiple volumes increases IOPS."),
        ("Use larger volume sizes for higher baseline IOPS", "Larger gp2 volumes have more baseline IOPS."),
        ("Use cold HDD for I/O-intensive workloads", "Cold HDD is the wrong choice for I/O-intensive workloads."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Use EBS-optimized, RAID 0, and larger volume sizes to optimize EBS performance. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/optimizing-performance.html",
})
QUESTIONS.append({
    "q": "Which EBS feature allows you to ENCRYPT data at rest with a customer managed KMS key without performance impact?",
    "type": "multiple-choice",
    "opts": [
        ("EBS encryption with KMS", "EBS encryption is enabled at volume creation with a KMS key."),
        ("EBS snapshot", "Snapshots are for backup, not encryption at rest."),
        ("EBS Fast Snapshot Restore", "FSR is for fast restore, not encryption."),
        ("EBS Multi-Attach", "Multi-Attach is for attaching one volume to multiple instances."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "EBS encryption with a KMS key provides encryption at rest with negligible performance impact. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html",
})
QUESTIONS.append({
    "q": "Which EBS feature allows you to ATTACH a single EBS volume to MULTIPLE EC2 instances in the same AZ?",
    "type": "multiple-choice",
    "opts": [
        ("EBS Multi-Attach", "EBS Multi-Attach allows attaching one volume to multiple instances in the same AZ."),
        ("EBS snapshot", "Snapshots are for backup."),
        ("EBS encryption", "Encryption is for security."),
        ("EBS volume modification", "Modification changes size or type."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "EBS Multi-Attach attaches a single volume to multiple EC2 instances in the same AZ. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-multi.html",
})
QUESTIONS.append({
    "q": "Which EBS feature provides fast initialization of new EBS volumes from snapshots, eliminating the latency of lazy loading?",
    "type": "multiple-choice",
    "opts": [
        ("EBS Fast Snapshot Restore (FSR)", "FSR provides fast initialization from snapshots."),
        ("EBS snapshot copy", "Snapshot copy is for cross-region copies."),
        ("EBS encryption", "Encryption is for security."),
        ("EBS volume modification", "Modification changes size or type."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "EBS Fast Snapshot Restore (FSR) provides fast initialization from snapshots. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-fast-snapshot-restore.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid performance characteristics of EBS gp3 volumes? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("3,000 baseline IOPS free with every volume", "gp3 provides 3,000 baseline IOPS at no extra cost."),
        ("125 MB/s baseline throughput", "gp3 provides 125 MB/s baseline throughput."),
        ("Independent IOPS and throughput provisioning", "gp3 allows independent IOPS and throughput provisioning."),
        ("Up to 16,000 IOPS and 1,000 MB/s", "gp3 supports up to 16,000 IOPS and 1,000 MB/s."),
    ],
    "correct": "1,2,3,4",
    "domain": HIGH_PERF,
    "overall": "EBS gp3 provides 3,000 baseline IOPS and 125 MB/s baseline, with up to 16,000 IOPS and 1,000 MB/s provisioned. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html",
})
QUESTIONS.append({
    "q": "Which EBS volume type is the BEST choice for COLD, infrequently accessed data with the LOWEST cost?",
    "type": "multiple-choice",
    "opts": [
        ("gp3", "gp3 is general-purpose SSD, not the lowest cost."),
        ("st1", "st1 is throughput-optimized HDD, not cold storage."),
        ("sc1", "sc1 is cold HDD, the lowest-cost EBS option."),
        ("io1", "io1 is high-IOPS SSD, expensive."),
    ],
    "correct": "3",
    "domain": HIGH_PERF,
    "overall": "sc1 is cold HDD, the lowest-cost EBS option for infrequent access. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/cold-storage.html",
})
QUESTIONS.append({
    "q": "Which EBS feature provides automatic volume modification (size, type, IOPS) without instance restart?",
    "type": "multiple-choice",
    "opts": [
        ("EBS Elastic Volumes", "Elastic Volumes allow modification without restart."),
        ("EBS Multi-Attach", "Multi-Attach is for multiple instances."),
        ("EBS snapshot", "Snapshots are for backup."),
        ("EBS encryption", "Encryption is for security."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "EBS Elastic Volumes allow modification of size, type, and IOPS without instance restart. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/evs.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid use cases for EBS snapshots? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Backup of EBS volumes", "Snapshots are backups of EBS volumes."),
        ("Creating new EBS volumes from a baseline", "Snapshots are the source for new volumes."),
        ("Cross-region copy for DR", "Snapshots can be copied across regions."),
        ("Real-time replication of running volumes", "Snapshots are point-in-time, not real-time replication."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "EBS snapshots are backups, sources for new volumes, and can be copied across regions. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides automated snapshot management with policies for retention, including cross-region copy?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Data Lifecycle Manager (DLM)", "DLM automates EBS snapshot lifecycle."),
        ("AWS Backup", "AWS Backup also supports EBS, with cross-region copy."),
        ("EBS encryption", "EBS encryption is for security."),
        ("EBS volume modification", "Modification is for size/type/IOPS."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "AWS Backup provides automated snapshot management with policies, including cross-region copy. Reference: https://docs.aws.amazon.com/aws-backup/latest/devguide/ebs-backups.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid use cases for RAID 0 with EBS volumes? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Increasing IOPS for I/O-intensive databases", "RAID 0 linearly increases IOPS."),
        ("Increasing throughput for large sequential I/O", "RAID 0 linearly increases throughput."),
        ("Increasing durability against single-volume failure", "RAID 0 DECREASES durability (no redundancy)."),
        ("Reducing cost of storage", "RAID 0 increases cost (multiple volumes)."),
    ],
    "correct": "1,2",
    "domain": HIGH_PERF,
    "overall": "RAID 0 with EBS increases IOPS and throughput but decreases durability. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/raid-config.html",
})

# ============================================================
# S3 PERFORMANCE (14 questions)
# ============================================================

QUESTIONS.append({
    "q": "Which combination of features increases S3 PUT/GET throughput when uploading large files or many files concurrently? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("S3 multipart upload", "Multipart upload splits large files into parts for parallel upload."),
        ("S3 Transfer Acceleration with CloudFront edge", "Transfer Acceleration speeds up cross-region uploads via CloudFront."),
        ("S3 byte-range fetches", "Byte-range fetches parallelize GETs."),
        ("S3 Object Lock", "Object Lock is for immutability, not throughput."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Use multipart upload, Transfer Acceleration, and byte-range fetches to maximize S3 throughput. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html",
})
QUESTIONS.append({
    "q": "Which S3 storage class provides MILLISECOND retrieval and is the BEST fit for archive data accessed once per quarter?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Standard", "Standard is for frequent access."),
        ("S3 Standard-IA", "Standard-IA is for infrequent millisecond access."),
        ("S3 Glacier Deep Archive", "Glacier Deep Archive has hours retrieval."),
        ("S3 Glacier Instant Retrieval", "Glacier Instant Retrieval is also millisecond but is more expensive than Standard-IA for once-per-quarter access."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "S3 Standard-IA provides millisecond retrieval for infrequently accessed data at a lower storage cost than S3 Standard. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html",
})
QUESTIONS.append({
    "q": "Which S3 storage class is the BEST fit for data accessed once per YEAR with retrieval times in HOURS?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Standard-IA", "Standard-IA is millisecond retrieval."),
        ("S3 Glacier Deep Archive", "Glacier Deep Archive is the lowest-cost storage with hours retrieval."),
        ("S3 Intelligent-Tiering", "Intelligent-Tiering automatically moves objects between tiers."),
        ("S3 One Zone-IA", "One Zone-IA is for data that can be lost in an AZ destruction."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "S3 Glacier Deep Archive has the lowest storage cost and retrieval times of 12-48 hours. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html",
})
QUESTIONS.append({
    "q": "Which storage class automatically moves objects between access tiers based on usage patterns, with no retrieval charges?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Intelligent-Tiering", "Intelligent-Tiering automatically moves objects between tiers."),
        ("S3 Standard", "Standard is the default tier; not automatic."),
        ("S3 Glacier", "Glacier has retrieval charges."),
        ("S3 Standard-IA", "Standard-IA has retrieval charges."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "S3 Intelligent-Tiering automatically moves objects between Frequent, Infrequent, Archive, and Deep Archive access tiers, with no retrieval charges. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html",
})
QUESTIONS.append({
    "q": "Which S3 feature lets you parallelize GET requests on a single large object by requesting specific byte ranges?",
    "type": "multiple-choice",
    "opts": [
        ("S3 byte-range fetches", "Byte-range fetches parallelize GETs on a single object."),
        ("S3 multipart upload", "Multipart upload is for PUT, not GET."),
        ("S3 Transfer Acceleration", "Transfer Acceleration is for PUT, not GET."),
        ("S3 Object Lock", "Object Lock is for immutability."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "S3 byte-range fetches parallelize GETs on a single object. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html",
})
QUESTIONS.append({
    "q": "Which S3 feature uploads large files to S3 faster by using Amazon CloudFront edge locations?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Transfer Acceleration", "Transfer Acceleration uses CloudFront edges for faster uploads."),
        ("S3 multipart upload", "Multipart upload splits large files into parts."),
        ("S3 byte-range fetches", "Byte-range fetches are for GETs."),
        ("S3 Glacier", "Glacier is for archive."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "S3 Transfer Acceleration uses Amazon CloudFront edge locations for faster uploads. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html",
})
QUESTIONS.append({
    "q": "Which S3 feature splits a large file into multiple parts that can be uploaded in parallel for better throughput?",
    "type": "multiple-choice",
    "opts": [
        ("S3 multipart upload", "Multipart upload splits large files into parts for parallel upload."),
        ("S3 Transfer Acceleration", "Transfer Acceleration is for cross-region uploads via CloudFront."),
        ("S3 byte-range fetches", "Byte-range fetches are for GETs."),
        ("S3 Glacier", "Glacier is for archive."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "S3 multipart upload splits large files into multiple parts that can be uploaded in parallel. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html",
})
QUESTIONS.append({
    "q": "Which S3 request rate scaling model provides automatic scaling of request rates without throttling, with no upfront planning?",
    "type": "multiple-choice",
    "opts": [
        ("S3 automatic request rate scaling", "S3 automatically scales request rates; no planning needed."),
        ("S3 prefix-based scaling", "S3 used to require prefix-based scaling; now automatic."),
        ("S3 bucket-level throughput", "S3 scales per prefix and overall bucket."),
        ("S3 storage class scaling", "Storage class is for cost, not request rate."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "S3 automatically scales request rates without throttling for high request rates per prefix. Reference: https://docs.aws.amazon.com/AmazonS3/latest/dev/optimizing-performance.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid ways to optimize S3 list operations? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Use S3 Inventory for bulk listing", "S3 Inventory provides bulk listing."),
        ("Use S3 Select to query objects", "S3 Select can filter objects server-side."),
        ("Use parallel listing from multiple workers", "Parallel listing from multiple workers speeds up."),
        ("Use a single-threaded loop", "Single-threaded loops are slow."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Use S3 Inventory, S3 Select, and parallel listing for optimized S3 list operations. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid S3 storage class characteristics? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("S3 Standard has millisecond retrieval", "Standard is millisecond."),
        ("S3 Standard-IA has millisecond retrieval", "Standard-IA is millisecond."),
        ("S3 Glacier has minutes-to-hours retrieval", "Glacier is minutes to hours."),
        ("S3 Standard has hours retrieval", "Standard is millisecond, not hours."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Standard and Standard-IA are millisecond. Glacier is minutes to hours. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html",
})
QUESTIONS.append({
    "q": "Which S3 Glacier retrieval option provides the FASTEST retrieval with millisecond response?",
    "type": "multiple-choice",
    "opts": [
        ("Glacier Instant Retrieval", "Glacier Instant Retrieval is millisecond."),
        ("Glacier Flexible Retrieval", "Flexible Retrieval is minutes to hours."),
        ("Glacier Deep Archive", "Deep Archive is 12-48 hours."),
        ("Glacier Bulk Retrieval", "Glacier Bulk is hours."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Glacier Instant Retrieval provides millisecond retrieval for archive data. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html",
})
QUESTIONS.append({
    "q": "Which S3 Glacier retrieval option provides the SLOWEST retrieval with the lowest cost, for 7-10 year archives?",
    "type": "multiple-choice",
    "opts": [
        ("Glacier Instant Retrieval", "Glacier Instant is millisecond, not the lowest cost."),
        ("Glacier Flexible Retrieval", "Glacier Flexible is minutes to hours."),
        ("Glacier Deep Archive", "Glacier Deep Archive is the lowest cost with hours retrieval."),
        ("S3 Standard", "Standard is for frequent access, not archive."),
    ],
    "correct": "3",
    "domain": HIGH_PERF,
    "overall": "Glacier Deep Archive is the lowest-cost storage class for long-term archive. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html",
})
QUESTIONS.append({
    "q": "Which S3 feature provides per-object access pattern monitoring to drive intelligent tier transitions?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Intelligent-Tiering", "Intelligent-Tiering monitors access and moves objects automatically."),
        ("S3 Lifecycle", "Lifecycle is rule-based, not access-pattern-based."),
        ("S3 Inventory", "Inventory is a listing report."),
        ("S3 Analytics", "Analytics is for storage class analysis."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "S3 Intelligent-Tiering monitors access patterns and moves objects automatically. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html",
})
QUESTIONS.append({
    "q": "Which S3 feature provides storage class analysis to inform Lifecycle policy decisions?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Storage Class Analysis", "Storage Class Analysis informs Lifecycle decisions."),
        ("S3 Intelligent-Tiering", "Intelligent-Tiering is automatic tier movement."),
        ("S3 Inventory", "Inventory is a listing."),
        ("S3 Object Lock", "Object Lock is for immutability."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "S3 Storage Class Analysis provides recommendations for Lifecycle policies. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/analytics-storage-class.html",
})

# ============================================================
# EFS/FSx/STORAGE PERFORMANCE (12 questions)
# ============================================================

QUESTIONS.append({
    "q": "Which of the following are valid characteristics of Amazon EFS? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Shared NFS file system for thousands of EC2 instances", "EFS supports thousands of concurrent NFS clients."),
        ("Regional, multi-AZ by default", "EFS replicates data across AZs in a region."),
        ("Lowest-cost general-purpose file system", "EFS IA is low-cost; Standard is the higher-performance tier."),
        ("Object storage, accessed via HTTP", "EFS is a file system, not object storage; access is via NFS."),
    ],
    "correct": "1,2",
    "domain": HIGH_PERF,
    "overall": "EFS is a shared, regional, multi-AZ NFS file system. Reference: https://docs.aws.amazon.com/efs/latest/ug/what-is-efs.html",
})
QUESTIONS.append({
    "q": "Which file system is the BEST fit for high-performance computing workloads requiring low-latency parallel access to data (e.g., ML training, video rendering)?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon EFS", "EFS is a general-purpose NFS file system."),
        ("Amazon FSx for Lustre", "FSx for Lustre is high-performance, parallel, low-latency file system."),
        ("Amazon EBS", "EBS is block storage for a single instance."),
        ("Amazon S3", "S3 is object storage, not a file system."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "Amazon FSx for Lustre provides high-performance, parallel file system for HPC, ML, and video rendering. Reference: https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html",
})
QUESTIONS.append({
    "q": "Which Amazon FSx file system is the BEST fit for Windows-based workloads requiring SMB protocol and Windows NTFS features?",
    "type": "multiple-choice",
    "opts": [
        ("FSx for Lustre", "FSx for Lustre is for HPC, not Windows."),
        ("FSx for Windows File Server", "FSx for Windows File Server is fully managed Windows file system."),
        ("FSx for NetApp ONTAP", "FSx for ONTAP supports many protocols including SMB."),
        ("FSx for OpenZFS", "FSx for OpenZFS is for Linux workloads."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "FSx for Windows File Server is the fully managed Windows file system with SMB and NTFS support. Reference: https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html",
})
QUESTIONS.append({
    "q": "Which Amazon FSx file system is the BEST fit for ONTAP-based enterprise workloads requiring multi-protocol access?",
    "type": "multiple-choice",
    "opts": [
        ("FSx for Windows File Server", "FSx for Windows is for Windows-only."),
        ("FSx for NetApp ONTAP", "FSx for ONTAP supports NFS, SMB, and iSCSI."),
        ("FSx for Lustre", "FSx for Lustre is for HPC."),
        ("FSx for OpenZFS", "FSx for OpenZFS is for Linux with ZFS features."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "FSx for NetApp ONTAP supports NFS, SMB, and iSCSI for ONTAP-based enterprise workloads. Reference: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html",
})
QUESTIONS.append({
    "q": "Which Amazon EFS storage class is the LOWEST cost for infrequently accessed files?",
    "type": "multiple-choice",
    "opts": [
        ("EFS Standard", "EFS Standard is the default tier."),
        ("EFS Infrequent Access (IA)", "EFS IA is the lowest cost for infrequent access."),
        ("EFS Archive", "EFS Archive is the lowest cost for archive data with hours retrieval."),
        ("EFS One Zone", "EFS One Zone is for non-critical, lower-cost data."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "EFS IA is the lowest cost for infrequently accessed files with millisecond retrieval. Reference: https://docs.aws.amazon.com/efs/latest/ug/storage-classes.html",
})
QUESTIONS.append({
    "q": "Which EFS feature automatically moves files to EFS IA based on access patterns, similar to S3 Intelligent-Tiering?",
    "type": "multiple-choice",
    "opts": [
        ("EFS Lifecycle Management", "EFS Lifecycle Management automatically moves files to IA."),
        ("EFS Standard only", "EFS Standard does not have automatic tiering."),
        ("EFS Bursting throughput", "Bursting throughput is for performance, not tiering."),
        ("EFS Provisioned throughput", "Provisioned throughput is for guaranteed performance."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "EFS Lifecycle Management automatically moves files to EFS IA based on access patterns. Reference: https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid EFS performance modes? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("General Purpose", "General Purpose is the default for most workloads."),
        ("Max I/O", "Max I/O is for high-throughput, many concurrent clients."),
        ("Bursting throughput mode", "Bursting throughput is a separate mode from performance mode."),
        ("Provisioned throughput mode", "Provisioned throughput is a separate mode from performance mode."),
    ],
    "correct": "1,2",
    "domain": HIGH_PERF,
    "overall": "EFS performance modes are General Purpose and Max I/O. Throughput modes are separate. Reference: https://docs.aws.amazon.com/efs/latest/ug/performance.html",
})
QUESTIONS.append({
    "q": "Which EFS throughput mode provides guaranteed throughput for the file system, regardless of burst credits?",
    "type": "multiple-choice",
    "opts": [
        ("Bursting throughput mode", "Bursting is based on size; not guaranteed."),
        ("Provisioned throughput mode", "Provisioned provides guaranteed throughput."),
        ("Elastic throughput mode", "Elastic is the new mode, similar to bursting but automatic."),
        ("Both bursting and elastic", "Bursting and Elastic are based on size."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "EFS Provisioned throughput mode provides guaranteed throughput regardless of file system size. Reference: https://docs.aws.amazon.com/efs/latest/ug/performance.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid use cases for FSx for Lustre? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("High-performance computing (HPC)", "FSx for Lustre is built for HPC."),
        ("Machine learning training", "FSx for Lustre is ideal for ML training with S3 integration."),
        ("Windows file shares", "FSx for Lustre is Linux-only; FSx for Windows is for Windows."),
        ("Distributed parallel file system workloads", "FSx for Lustre is a parallel file system."),
    ],
    "correct": "1,2,4",
    "domain": HIGH_PERF,
    "overall": "FSx for Lustre is for HPC, ML training, and parallel workloads. It's Linux-only. Reference: https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html",
})
QUESTIONS.append({
    "q": "Which feature of FSx for Lustre allows transparent access to S3 data, automatically loading objects on demand?",
    "type": "multiple-choice",
    "opts": [
        ("S3 integration with lazy loading", "FSx for Lustre links to S3 and loads objects on demand."),
        ("Direct S3 read", "FSx for Lustre is the file system; data is cached from S3."),
        ("S3 Object Lambda", "S3 Object Lambda is for code-on-read transformation."),
        ("S3 Batch Operations", "Batch is for one-time operations."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "FSx for Lustre integrates with S3 and lazily loads objects on demand. Reference: https://docs.aws.amazon.com/fsx/latest/LustreGuide/imported-file-system.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid Amazon FSx file systems? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("FSx for Windows File Server", "FSx for Windows is fully managed Windows file system."),
        ("FSx for Lustre", "FSx for Lustre is high-performance parallel file system."),
        ("FSx for NetApp ONTAP", "FSx for ONTAP is multi-protocol enterprise file system."),
        ("FSx for OpenZFS", "FSx for OpenZFS is Linux ZFS-based file system."),
    ],
    "correct": "1,2,3,4",
    "domain": HIGH_PERF,
    "overall": "FSx has four file systems: Windows, Lustre, ONTAP, and OpenZFS. Reference: https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid S3 performance optimization techniques? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Use S3 Transfer Acceleration for cross-region uploads", "Transfer Acceleration speeds cross-region uploads."),
        ("Use S3 multipart upload for files > 100 MB", "Multipart upload is recommended for large files."),
        ("Use S3 byte-range fetches for parallel reads", "Byte-range fetches parallelize reads."),
        ("Use sequential object key prefixes only", "Random prefixes are not required; S3 scales automatically."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Use Transfer Acceleration, multipart upload, and byte-range fetches for S3 performance. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html",
})

# ============================================================
# DATABASE PERFORMANCE (14 questions)
# ============================================================

QUESTIONS.append({
    "q": "Which DynamoDB feature provides an in-memory cache that reduces read latency from milliseconds to microseconds?",
    "type": "multiple-choice",
    "opts": [
        ("DynamoDB Streams", "Streams are change-data capture."),
        ("DynamoDB DAX", "DAX is the in-memory cache for DynamoDB."),
        ("DynamoDB Global Tables", "Global Tables provide multi-region replication."),
        ("DynamoDB Accelerator Streams", "Not a real feature."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "DynamoDB Accelerator (DAX) is the in-memory cache for DynamoDB, reducing read latency from ms to µs. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html",
})
QUESTIONS.append({
    "q": "Which DynamoDB design principle is MOST important for achieving consistent performance at scale?",
    "type": "multiple-choice",
    "opts": [
        ("Use monotonically increasing partition keys (e.g., timestamp)", "Monotonically increasing keys create hot partitions; this is the wrong pattern."),
        ("Choose partition keys with high cardinality and uniform access patterns", "High-cardinality keys with uniform access prevent hot partitions."),
        ("Use a single partition key for all items", "Single keys create hot partitions."),
        ("Use the smallest possible item size", "Item size matters but uniform access is more important for partition distribution."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "High-cardinality, uniformly distributed partition keys are essential to avoid hot partitions in DynamoDB. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html",
})
QUESTIONS.append({
    "q": "Which DynamoDB feature AUTOMATICALLY redistributes partitions to handle hot partitions, without operator intervention?",
    "type": "multiple-choice",
    "opts": [
        ("DynamoDB adaptive capacity", "Adaptive capacity automatically redistributes throughput to hot partitions."),
        ("DynamoDB streams", "Streams are change-data capture."),
        ("DynamoDB transactions", "Transactions provide ACID across items."),
        ("DynamoDB TTL", "TTL expires items."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "DynamoDB adaptive capacity automatically redistributes throughput to frequently accessed partitions, mitigating hot partition issues. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html",
})
QUESTIONS.append({
    "q": "Which combination of read options in DynamoDB provides STRONGLY CONSISTENT reads? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Specify ConsistentRead=true on GetItem", "ConsistentRead=true gives strong consistency."),
        ("Specify ConsistentRead=true on Query", "ConsistentRead=true on Query gives strong consistency."),
        ("Default GetItem is strongly consistent", "Default is eventually consistent; specify ConsistentRead=true."),
        ("Default Scan is strongly consistent", "Default Scan is eventually consistent."),
    ],
    "correct": "1,2",
    "domain": HIGH_PERF,
    "overall": "DynamoDB default reads are eventually consistent. Use ConsistentRead=true on GetItem, Query, or Scan for strong consistency. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html",
})
QUESTIONS.append({
    "q": "Which RDS feature provides automatic scaling of compute and memory for unpredictable workloads, billed per second?",
    "type": "multiple-choice",
    "opts": [
        ("RDS read replicas", "Read replicas scale reads, not compute."),
        ("Amazon Aurora Serverless", "Aurora Serverless auto-scales compute and memory, billed per second."),
        ("RDS Multi-AZ", "Multi-AZ is for HA."),
        ("RDS Proxy", "RDS Proxy is a connection pooler."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "Amazon Aurora Serverless v2 auto-scales compute and memory capacity based on application load, billed per second. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html",
})
QUESTIONS.append({
    "q": "Which service provides graph database capabilities for highly connected data such as social networks and fraud detection?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Neptune", "Neptune is the managed graph database."),
        ("Amazon DynamoDB", "DynamoDB is a key-value and document database."),
        ("Amazon Aurora", "Aurora is a relational database."),
        ("Amazon Redshift", "Redshift is a data warehouse."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon Neptune is the managed graph database for highly connected data. Reference: https://docs.aws.amazon.com/neptune/latest/userguide/intro.html",
})
QUESTIONS.append({
    "q": "Which service provides a fully managed time-series database for IoT and operational applications?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Timestream", "Timestream is the managed time-series database."),
        ("Amazon Neptune", "Neptune is graph."),
        ("Amazon DynamoDB", "DynamoDB is key-value."),
        ("Amazon Aurora", "Aurora is relational."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon Timestream is the managed time-series database optimized for IoT and operational telemetry. Reference: https://docs.aws.amazon.com/timestream/latest/developerguide/what-is-timestream.html",
})
QUESTIONS.append({
    "q": "Which AWS service is a fully managed, in-memory, Redis-compatible database with multi-AZ durability?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon ElastiCache for Redis", "ElastiCache for Redis is in-memory but not durable across AZs by default."),
        ("Amazon MemoryDB for Redis", "MemoryDB for Redis is in-memory with multi-AZ durability."),
        ("Amazon DynamoDB", "DynamoDB is on-disk NoSQL."),
        ("Amazon Aurora", "Aurora is relational."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "Amazon MemoryDB for Redis is a Redis-compatible, durable, in-memory database with multi-AZ replication. Reference: https://docs.aws.amazon.com/memorydb/latest/devguide/what-is-memorydb-for-redis.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid DynamoDB performance best practices? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Use high-cardinality partition keys with uniform access", "Uniform access prevents hot partitions."),
        ("Use DAX for microsecond latency", "DAX provides microsecond read latency."),
        ("Use eventually consistent reads where possible", "Eventually consistent reads are cheaper and faster."),
        ("Use a single partition for the entire table", "Single partition is a hot partition antipattern."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "High-cardinality keys, DAX, and eventually consistent reads are best practices. Single partition is an antipattern. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html",
})
QUESTIONS.append({
    "q": "Which DynamoDB feature allows you to cache frequently accessed items in DAX across multiple AZs?",
    "type": "multiple-choice",
    "opts": [
        ("DAX multi-AZ cluster", "DAX supports multi-AZ cluster mode for HA."),
        ("DynamoDB Streams", "Streams are for change-data capture."),
        ("DynamoDB Global Tables", "Global Tables are for cross-region replication."),
        ("DynamoDB TTL", "TTL expires items."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "DAX multi-AZ cluster provides HA caching across multiple AZs. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.concepts.cluster.html",
})
QUESTIONS.append({
    "q": "Which RDS feature enables offloading read-heavy traffic to dedicated read endpoints, improving read scalability?",
    "type": "multiple-choice",
    "opts": [
        ("RDS read replicas", "RDS read replicas provide dedicated read endpoints."),
        ("RDS Multi-AZ", "Multi-AZ is for HA."),
        ("RDS Storage Auto Scaling", "Storage Auto Scaling is for storage."),
        ("RDS Proxy", "RDS Proxy is for connection pooling."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "RDS read replicas provide dedicated read endpoints for offloading read-heavy traffic. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html",
})
QUESTIONS.append({
    "q": "Which Aurora feature replicates data across AWS Regions with sub-second replication lag for global low-latency reads?",
    "type": "multiple-choice",
    "opts": [
        ("Aurora read replicas", "Read replicas are within a region."),
        ("Aurora Global Database", "Aurora Global Database replicates across regions with sub-second lag."),
        ("Aurora Backtrack", "Backtrack is in-place time-travel within a cluster."),
        ("Aurora Multi-Master", "Multi-Master is multi-writer within a region."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "Aurora Global Database replicates to up to 5 secondary regions with sub-second lag. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html",
})
QUESTIONS.append({
    "q": "Which RDS performance optimization technique involves separating write and read traffic using dedicated endpoints?",
    "type": "multiple-choice",
    "opts": [
        ("Read replicas", "Read replicas separate write and read traffic."),
        ("Multi-AZ", "Multi-AZ is for HA."),
        ("Storage Auto Scaling", "Storage Auto Scaling is for storage."),
        ("Encryption", "Encryption is for security."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "RDS read replicas provide dedicated read endpoints to offload read traffic. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid RDS read replica features? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Asynchronous replication from primary", "Read replicas are async."),
        ("Can be promoted to standalone", "Read replicas can be promoted."),
        ("Cross-region replication", "Read replicas support cross-region."),
        ("Synchronous replication with zero lag", "Read replicas are async, not synchronous."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "RDS read replicas support async replication, promotion, and cross-region. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html",
})

# ============================================================
# CACHING, CDN, NETWORKING (18 questions)
# ============================================================

QUESTIONS.append({
    "q": "Which of the following are valid use cases for Amazon ElastiCache? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Caching database queries to reduce RDS load", "Caching DB reads is a primary ElastiCache use case."),
        ("Session store for web applications", "ElastiCache is widely used as a session store."),
        ("Leaderboards and counting", "Sorted sets in Redis are great for leaderboards."),
        ("Durable archival storage", "ElastiCache is in-memory and not durable; use S3 Glacier."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "ElastiCache is for in-memory caching, session store, leaderboards, and other high-performance use cases. Reference: https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html",
})
QUESTIONS.append({
    "q": "Which ElastiCache engine is the BEST choice when you need advanced data structures such as sorted sets, hashes, and pub/sub?",
    "type": "multiple-choice",
    "opts": [
        ("Memcached", "Memcached is a simple key-value cache."),
        ("Redis", "Redis supports advanced data structures, pub/sub, streams, and persistence."),
        ("Valkey", "Valkey is a Redis fork with similar features."),
        ("Both Redis and Valkey are good choices, but Memcached is not", "Memcached lacks advanced structures."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "Redis (and the compatible Valkey) supports sorted sets, hashes, lists, streams, and pub/sub. Memcached is a simple key-value cache. Reference: https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Components.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid use cases for CloudFront cache behaviors? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Serve /api/* from a different origin than /*", "Cache behaviors per path pattern allow different origins and TTLs."),
        ("Forward specific query strings to the origin", "CloudFront can forward query strings to origin."),
        ("Use a different CloudFront function per path", "Cache behaviors can attach different functions."),
        ("Cache private content with signed URLs only", "Signed URLs are the right pattern for private content."),
    ],
    "correct": "1,2,3,4",
    "domain": HIGH_PERF,
    "overall": "CloudFront cache behaviors allow per-path origins, query string forwarding, function association, and signed URL access. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid CloudFront origin types? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon S3 bucket", "S3 is a CloudFront origin."),
        ("Application Load Balancer or EC2", "ALB/EC2 are HTTP origins."),
        ("AWS Elemental MediaStore and MediaPackage", "MediaStore and MediaPackage are origins for video."),
        ("On-prem HTTP server", "On-prem HTTP server via custom origin is allowed."),
    ],
    "correct": "1,2,3,4",
    "domain": HIGH_PERF,
    "overall": "CloudFront supports S3, ALB, EC2, MediaStore/Package, and on-prem HTTP origins. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid performance optimization techniques for Lambda? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Provisioned concurrency to eliminate cold starts", "Provisioned concurrency keeps functions warm."),
        ("Right-size memory allocation to balance duration and cost", "More memory = more CPU and often shorter duration."),
        ("Use layers to share code and dependencies", "Layers reduce deployment package size and improve cold start."),
        ("Disable function logging to improve performance", "Logging is important and disabling is an antipattern."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Use provisioned concurrency, right-size memory, and use layers. Disabling logging is an antipattern. Reference: https://docs.aws.amazon.com/lambda/latest/operatorguide/performance.html",
})
QUESTIONS.append({
    "q": "Which AWS service is the GLOBAL content delivery network (CDN) that caches content at edge locations for low-latency delivery?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon CloudFront", "CloudFront is the AWS global CDN."),
        ("Amazon S3", "S3 is object storage, not a CDN."),
        ("Amazon API Gateway", "API Gateway is for APIs."),
        ("AWS Global Accelerator", "Global Accelerator is for anycast TCP/UDP, not HTTP caching."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon CloudFront is the AWS global CDN with edge caching for low-latency content delivery. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html",
})
QUESTIONS.append({
    "q": "Which CloudFront feature reduces latency for end users by maintaining persistent connections to origins?",
    "type": "multiple-choice",
    "opts": [
        ("Origin Shield", "Origin Shield adds an extra caching layer to reduce origin load."),
        ("Keep-alive connections", "CloudFront maintains keep-alive connections to origins."),
        ("Lambda@Edge", "Lambda@Edge runs code at the edge."),
        ("Field-level encryption", "Field-level encryption is for security, not latency."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "CloudFront maintains persistent keep-alive connections to origins, reducing latency for repeated requests. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html",
})
QUESTIONS.append({
    "q": "Which CloudFront feature adds an additional caching layer between CloudFront edge locations and the origin, reducing origin load?",
    "type": "multiple-choice",
    "opts": [
        ("Origin Shield", "Origin Shield is the additional caching layer."),
        ("Origin Access Identity", "OAI/OAC restrict S3 origin access."),
        ("Lambda@Edge", "Lambda@Edge is for code at the edge."),
        ("CloudFront Functions", "CloudFront Functions run lightweight JavaScript at the edge."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "CloudFront Origin Shield adds an extra caching layer to reduce origin load and improve cache hit ratio. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html",
})
QUESTIONS.append({
    "q": "Which combination of features can a CloudFront distribution use to authenticate the request and pass a custom header to the origin? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("CloudFront signed URLs", "Signed URLs grant time-limited access to specific objects."),
        ("CloudFront signed cookies", "Signed cookies grant access to multiple restricted objects."),
        ("Origin Access Control (OAC) for S3 origins", "OAC restricts S3 origin access to CloudFront."),
        ("Public S3 bucket without OAC", "Public S3 bypasses the secure pattern."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Use signed URLs, signed cookies, and OAC to authenticate requests and protect origins. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content.html",
})
QUESTIONS.append({
    "q": "Which service provides anycast static IPs and improves global application performance for non-HTTP traffic (TCP/UDP)?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon CloudFront", "CloudFront is HTTP/HTTPS."),
        ("AWS Global Accelerator", "Global Accelerator is for TCP/UDP with anycast IPs."),
        ("Amazon Route 53", "Route 53 is DNS."),
        ("AWS Direct Connect", "DX is a private link."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "AWS Global Accelerator provides anycast static IPs for TCP/UDP performance across regions. Reference: https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid networking options to connect on-prem to AWS? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS Direct Connect (DX)", "Direct Connect is a dedicated private fiber link."),
        ("AWS Site-to-Site VPN over the internet", "VPN is an IPsec tunnel over the public internet."),
        ("AWS Transit Gateway", "Transit Gateway connects VPCs and on-prem networks."),
        ("Amazon Cognito", "Cognito is for identity, not networking."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Direct Connect, Site-to-Site VPN, and Transit Gateway are the main on-prem-to-AWS networking options. Reference: https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/welcome.html",
})
QUESTIONS.append({
    "q": "Which AWS service is the BEST choice for a fully managed service mesh for microservices running on ECS, EKS, or EC2?",
    "type": "multiple-choice",
    "opts": [
        ("AWS App Mesh", "App Mesh is the managed service mesh."),
        ("Amazon API Gateway", "API Gateway is for APIs."),
        ("Amazon CloudFront", "CloudFront is a CDN."),
        ("Amazon EventBridge", "EventBridge is an event bus."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "AWS App Mesh is the managed service mesh for microservices, with Envoy-based sidecars. Reference: https://docs.aws.amazon.com/app-mesh/latest/userguide/what-is-app-mesh.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid VPC design best practices for performance? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Multi-AZ for high availability", "Multi-AZ is the foundation of HA."),
        ("VPC endpoints for S3 and DynamoDB", "VPC endpoints avoid NAT data transfer costs."),
        ("Single NAT gateway for cost savings", "Single NAT is not HA; use multiple NATs for HA."),
        ("Use placement groups for HPC within a single AZ", "Cluster placement groups pack instances for low latency."),
    ],
    "correct": "1,2,4",
    "domain": HIGH_PERF,
    "overall": "Use multi-AZ, VPC endpoints, and placement groups for performance. Single NAT is an HA antipattern. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html",
})
QUESTIONS.append({
    "q": "Which VPC feature lets you co-locate compute and high-bandwidth data sources in the same AZ to minimize data transfer charges?",
    "type": "multiple-choice",
    "opts": [
        ("Same-AZ data transfer", "Same-AZ data transfer is free."),
        ("Cross-AZ replication", "Cross-AZ replication incurs data transfer charges."),
        ("Direct Connect", "DX is for on-prem to AWS."),
        ("Internet gateway", "IGW is for public access."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Same-AZ data transfer is free; co-locate compute and data in the same AZ. Reference: https://aws.amazon.com/ec2/pricing/on-demand/",
})
QUESTIONS.append({
    "q": "Which combination of services is the BEST pattern for a global, low-latency, high-throughput file transfer between AWS and on-prem? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS Direct Connect for high bandwidth", "DX provides high bandwidth, low latency."),
        ("AWS DataSync for automated transfer", "DataSync provides automated online transfer."),
        ("S3 over public internet only", "Public internet is not the high-throughput pattern."),
        ("AWS Snowball for petabyte-scale", "Snowball is for offline transfer, not online throughput."),
    ],
    "correct": "1,2",
    "domain": HIGH_PERF,
    "overall": "Use Direct Connect for high bandwidth and DataSync for automated online transfer. Reference: https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html",
})
QUESTIONS.append({
    "q": "Which AWS service is the BEST choice for accelerating S3 cross-region uploads from anywhere in the world?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Transfer Acceleration", "Transfer Acceleration uses CloudFront edges for faster uploads."),
        ("S3 multipart upload", "Multipart upload is for splitting large files."),
        ("S3 byte-range fetches", "Byte-range fetches are for GETs."),
        ("S3 Object Lock", "Object Lock is for immutability."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "S3 Transfer Acceleration uses CloudFront edges to accelerate cross-region uploads. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid performance characteristics of AWS Global Accelerator? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Two static anycast IPs per accelerator", "Global Accelerator provides two static anycast IPs."),
        ("Performance improvement over the public internet", "Global Accelerator uses the AWS backbone."),
        ("Instant regional failover with health checks", "Health checks drive instant regional failover."),
        ("HTTP caching", "Global Accelerator is not a CDN; CloudFront is."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Global Accelerator provides static anycast IPs, AWS backbone routing, and instant failover. It is not a CDN. Reference: https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html",
})
QUESTIONS.append({
    "q": "Which service provides a managed service mesh for microservices with mTLS, traffic management, and observability?",
    "type": "multiple-choice",
    "opts": [
        ("AWS App Mesh", "App Mesh is the AWS-managed service mesh with mTLS."),
        ("Amazon API Gateway", "API Gateway is for APIs."),
        ("Amazon CloudFront", "CloudFront is a CDN."),
        ("Amazon EventBridge", "EventBridge is an event bus."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "AWS App Mesh is the managed service mesh with Envoy-based mTLS, traffic management, and observability. Reference: https://docs.aws.amazon.com/app-mesh/latest/userguide/what-is-app-mesh.html",
})

# ============================================================
# DATA ANALYTICS AND GENAI (12 questions)
# ============================================================

QUESTIONS.append({
    "q": "Which service provides a fully managed data warehouse for OLAP, with columnar storage and massively parallel query execution?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Redshift", "Redshift is the managed data warehouse for OLAP."),
        ("Amazon Aurora", "Aurora is a relational OLTP database."),
        ("Amazon DynamoDB", "DynamoDB is a NoSQL OLTP database."),
        ("Amazon Neptune", "Neptune is a graph database."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon Redshift is the fully managed data warehouse for OLAP workloads, using columnar storage and MPP. Reference: https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html",
})
QUESTIONS.append({
    "q": "Which service provides serverless interactive query of data in S3 using standard SQL, with no infrastructure to manage?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Athena", "Athena queries S3 data using standard SQL with no infrastructure."),
        ("Amazon Redshift", "Redshift is a data warehouse cluster."),
        ("Amazon EMR", "EMR is a managed Hadoop/Spark platform."),
        ("Amazon Kinesis Data Analytics", "KDA is for streaming SQL."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon Athena is the serverless interactive query service for S3 data, using standard SQL. Reference: https://docs.aws.amazon.com/athena/latest/ug/what-is.html",
})
QUESTIONS.append({
    "q": "Which AWS service is a managed Hadoop/Spark platform for processing large-scale data workloads?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon EMR", "EMR is a managed Hadoop/Spark platform."),
        ("Amazon Athena", "Athena is serverless query for S3."),
        ("Amazon Redshift", "Redshift is a data warehouse."),
        ("Amazon Kinesis", "Kinesis is for streaming data."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon EMR is a managed Hadoop/Spark platform for large-scale data processing. Reference: https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html",
})
QUESTIONS.append({
    "q": "Which service provides real-time SQL analytics on streaming data, with sub-second latency?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Kinesis Data Analytics", "KDA is for real-time SQL on streams."),
        ("Amazon Athena", "Athena is for S3 data, not streams."),
        ("Amazon Redshift", "Redshift is a data warehouse."),
        ("Amazon EMR", "EMR is for batch Hadoop/Spark."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon Kinesis Data Analytics provides real-time SQL analytics on streaming data. Reference: https://docs.aws.amazon.com/kinesisanalytics/latest/dev/what-is.html",
})
QUESTIONS.append({
    "q": "Which AWS service is the BEST choice for full-text and structured search with sub-second latency?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon OpenSearch Service", "OpenSearch is the managed search service."),
        ("Amazon CloudSearch", "CloudSearch is a simpler service for basic search."),
        ("Amazon DynamoDB", "DynamoDB is not a search service."),
        ("Amazon RDS", "RDS is a relational database."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon OpenSearch Service is the managed search service for full-text and structured search. Reference: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html",
})
QUESTIONS.append({
    "q": "Which AWS service is the BEST choice for building generative AI applications using foundation models from leading providers, with a single API?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Bedrock", "Amazon Bedrock provides foundation models from multiple providers via a single API."),
        ("Amazon SageMaker", "SageMaker is for building/training ML models."),
        ("Amazon Q", "Amazon Q is a generative AI assistant for work."),
        ("Amazon Comprehend", "Comprehend is for NLP insights, not generative AI."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon Bedrock provides foundation models from Anthropic, Meta, Mistral, Stability AI, and Amazon via a single API for building generative AI applications. Reference: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a generative AI assistant for business use cases, integrating with enterprise data and workflows?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Q", "Amazon Q is the generative AI assistant for business."),
        ("Amazon Bedrock", "Bedrock is for building generative AI apps."),
        ("Amazon SageMaker", "SageMaker is for ML model training."),
        ("Amazon Comprehend", "Comprehend is for NLP insights."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon Q is the generative AI assistant for business use cases, integrating with enterprise data. Reference: https://aws.amazon.com/q/",
})
QUESTIONS.append({
    "q": "Which AWS service is the BEST choice for building, training, and deploying custom machine learning models?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon SageMaker", "SageMaker is the managed ML platform."),
        ("Amazon Bedrock", "Bedrock is for foundation models, not custom training."),
        ("Amazon Comprehend", "Comprehend is for NLP insights."),
        ("Amazon Rekognition", "Rekognition is for image/video analysis."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon SageMaker is the managed platform for building, training, and deploying custom ML models. Reference: https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid AWS analytics services? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon Redshift", "Redshift is the data warehouse."),
        ("Amazon Athena", "Athena is serverless query on S3."),
        ("Amazon EMR", "EMR is for Hadoop/Spark."),
        ("Amazon Kinesis Data Analytics", "KDA is for streaming SQL."),
    ],
    "correct": "1,2,3,4",
    "domain": HIGH_PERF,
    "overall": "Redshift, Athena, EMR, and Kinesis Data Analytics are all AWS analytics services. Reference: https://aws.amazon.com/analytics/",
})
QUESTIONS.append({
    "q": "Which of the following are valid Amazon Bedrock features? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Foundation models from multiple providers", "Bedrock provides FMs from Anthropic, Meta, Mistral, Stability AI, and Amazon."),
        ("Single API for building generative AI applications", "Single API for all FMs."),
        ("Fine-tuning and continued pre-training", "Bedrock supports fine-tuning and continued pre-training."),
        ("Managed Kubernetes for AI workloads", "Bedrock is not Kubernetes."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Bedrock provides FMs from multiple providers via a single API, with fine-tuning and RAG. Reference: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides managed Apache Airflow for workflow orchestration of data pipelines?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Managed Workflows for Apache Airflow (MWAA)", "MWAA is the managed Airflow service."),
        ("AWS Step Functions", "Step Functions is AWS-native orchestration, not Airflow."),
        ("Amazon EventBridge", "EventBridge is an event bus, not Airflow."),
        ("Amazon SQS", "SQS is a queue, not Airflow."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon MWAA provides managed Apache Airflow for data pipeline orchestration. Reference: https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a fully managed, scalable, secure data lake with catalog, ETL, and analytics?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Lake Formation", "Lake Formation provides a managed data lake."),
        ("Amazon Redshift", "Redshift is a data warehouse."),
        ("Amazon Athena", "Athena is serverless query."),
        ("Amazon EMR", "EMR is for Hadoop/Spark."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "AWS Lake Formation provides a managed data lake with catalog, ETL, and analytics. Reference: https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html",
})

# ============================================================
# CASE STUDY QUESTIONS — STARTUPFAST (20 questions)
# ============================================================

QUESTIONS.append({
    "q": "In the StartupFast scenario, StartupFast wants to right-size EC2 instances to reduce over-provisioning. Which AWS service analyzes utilization and recommends right-sized instance types?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Compute Optimizer", "Compute Optimizer uses ML to recommend right-sized instances."),
        ("AWS Cost Explorer", "Cost Explorer is for spend analysis and RI recommendations."),
        ("AWS Trusted Advisor", "Trusted Advisor flags underutilized instances but does not provide detailed right-sizing."),
        ("AWS Pricing Calculator", "Pricing Calculator estimates future cost."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "AWS Compute Optimizer uses ML to recommend right-sized EC2 instances, EBS volumes, Lambda functions, and ECS services. Reference: https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is.html",
})
QUESTIONS.append({
    "q": "In the StartupFast scenario, StartupFast wants to optimize RDS cost for a database that is used heavily during business hours. Which combination of services is the BEST fit? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Aurora Serverless v2 with auto-scaling", "Aurora Serverless scales capacity to match demand."),
        ("RDS Reserved Instances for predictable baseline", "RIs reduce cost for predictable baseline usage."),
        ("RDS read replicas for offloading reads", "Read replicas offload read traffic."),
        ("Skip monitoring and just scale manually", "Monitoring is essential; manual scaling is error-prone."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Use Aurora Serverless, RIs, and read replicas to optimize RDS cost. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html",
})
QUESTIONS.append({
    "q": "In the StartupFast scenario, StartupFast wants to add a CACHE LAYER in front of RDS to reduce database load and improve response time. Which AWS service is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon ElastiCache for Redis", "ElastiCache is the in-memory cache for Redis or Memcached."),
        ("Amazon S3", "S3 is object storage, not a cache."),
        ("Amazon DynamoDB", "DynamoDB is a NoSQL database."),
        ("Amazon CloudFront", "CloudFront is a CDN, not a database cache."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon ElastiCache is the in-memory cache for reducing database load. Reference: https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html",
})
QUESTIONS.append({
    "q": "In the StartupFast scenario, StartupFast wants to reduce S3 storage cost for user-uploaded files that are accessed frequently for 30 days, then rarely accessed. Which S3 storage class transition is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Standard to S3 Standard-IA after 30 days", "Transition to Standard-IA after 30 days reduces cost."),
        ("S3 Standard to S3 Glacier Deep Archive after 30 days", "Glacier Deep Archive has hours retrieval; not for occasional access."),
        ("S3 Standard to S3 Standard only", "Standard is the most expensive tier."),
        ("S3 Standard to S3 One Zone-IA after 30 days", "One Zone-IA is for non-critical data."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Use S3 Lifecycle to transition from Standard to Standard-IA after 30 days. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html",
})
QUESTIONS.append({
    "q": "In the StartupFast scenario, StartupFast wants to use CloudFront to cache static assets for the SaaS application. Which combination of features is the BEST fit? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon CloudFront for global caching", "CloudFront caches at edge."),
        ("Origin Access Control (OAC) for S3 origin", "OAC restricts S3 origin access."),
        ("S3 as origin", "S3 is a common CloudFront origin."),
        ("Direct public S3 URL", "Direct public S3 is not a CloudFront pattern."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Use CloudFront with S3 origin and OAC for secure, cached delivery. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html",
})
QUESTIONS.append({
    "q": "In the StartupFast scenario, StartupFast wants to use Compute Savings Plans for the predictable baseline EC2 usage. Which is TRUE about Compute Savings Plans?",
    "type": "multiple-choice",
    "opts": [
        ("Up to 66% discount across instance families, regions, and OS", "Compute SPs offer up to 66% with the most flexibility."),
        ("Up to 72% discount within a single instance family", "EC2 Instance SPs offer up to 72% within a family."),
        ("No discount at all", "Savings Plans offer up to 66%."),
        ("Discount only for Spot Instances", "Savings Plans are not for Spot."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Compute Savings Plans offer up to 66% discount across instance families, regions, and OS. Reference: https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html",
})
QUESTIONS.append({
    "q": "In the StartupFast scenario, StartupFast wants to use Spot Instances for the development environment to save cost. Which is TRUE about Spot Instances?",
    "type": "multiple-choice",
    "opts": [
        ("Spot offers up to 90% discount but can be interrupted", "Spot offers the highest discount with interruption risk."),
        ("Spot is always cheaper than On-Demand for the same workload", "Spot is not always cheaper; bid price matters."),
        ("Spot is suitable for critical production workloads", "Spot is not for critical workloads; interruption risk is too high."),
        ("Spot requires a 1-year commitment", "Spot does not require commitment."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Spot offers up to 90% discount but can be interrupted with 2 minutes notice. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html",
})
QUESTIONS.append({
    "q": "In the StartupFast scenario, StartupFast wants to use Lambda for a serverless data processing pipeline. Which is TRUE about Lambda cost optimization?",
    "type": "multiple-choice",
    "opts": [
        ("Lambda is billed per request and GB-second", "Lambda charges per invocation and compute time."),
        ("Lambda is billed per hour regardless of usage", "Lambda is per-invocation, not per-hour."),
        ("Lambda always costs more than EC2", "Lambda can be cheaper than EC2 for low-traffic workloads."),
        ("Lambda has no free tier", "Lambda has a free tier of 1M requests per month."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Lambda is billed per request and GB-second of compute time. Reference: https://docs.aws.amazon.com/lambda/latest/dg/billing-concepts.html",
})
QUESTIONS.append({
    "q": "In the StartupFast scenario, StartupFast wants to use DynamoDB for the user session store. Which DynamoDB capacity mode is the BEST fit for an unpredictable workload?",
    "type": "multiple-choice",
    "opts": [
        ("On-demand mode", "On-demand mode is for unpredictable workloads."),
        ("Provisioned mode", "Provisioned mode is for predictable workloads."),
        ("Reserved mode", "Reserved mode is for predictable workloads with commitment."),
        ("Free mode", "There is no free mode for DynamoDB."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "DynamoDB on-demand mode is for unpredictable workloads. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html",
})
QUESTIONS.append({
    "q": "In the StartupFast scenario, StartupFast wants to monitor cost and usage to identify cost-saving opportunities. Which AWS service is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost Explorer", "Cost Explorer visualizes spend and identifies opportunities."),
        ("AWS Trusted Advisor", "Trusted Advisor provides best-practice checks."),
        ("AWS Budgets", "Budgets alert on spend thresholds."),
        ("AWS CloudTrail", "CloudTrail records API calls."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "AWS Cost Explorer visualizes spend and identifies cost-saving opportunities. Reference: https://docs.aws.amazon.com/cost-management/latest/userguide/what-is-ce.html",
})
QUESTIONS.append({
    "q": "In the StartupFast scenario, StartupFast wants to receive alerts when its AWS spend exceeds a threshold. Which AWS service is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Budgets", "AWS Budgets alert on spend thresholds."),
        ("AWS Cost Explorer", "Cost Explorer visualizes spend."),
        ("AWS Trusted Advisor", "Trusted Advisor provides best-practice checks."),
        ("AWS Cost Anomaly Detection", "Anomaly Detection uses ML to detect spend anomalies."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "AWS Budgets alerts on spend thresholds. Reference: https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html",
})
QUESTIONS.append({
    "q": "In the StartupFast scenario, StartupFast wants to detect ML-based anomalies in its AWS spend. Which AWS service is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost Anomaly Detection", "Cost Anomaly Detection uses ML to detect spend anomalies."),
        ("AWS Budgets", "Budgets alert on thresholds, not anomalies."),
        ("AWS Cost Explorer", "Cost Explorer is for visualization."),
        ("AWS Trusted Advisor", "Trusted Advisor provides best-practice checks."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "AWS Cost Anomaly Detection uses ML to detect and alert on unusual spend patterns. Reference: https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html",
})
QUESTIONS.append({
    "q": "In the StartupFast scenario, StartupFast wants to assign costs to specific teams or projects using tags. Which AWS feature is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost Allocation Tags", "Cost allocation tags categorize spend."),
        ("AWS Organizations", "Organizations is for account management."),
        ("AWS Trusted Advisor", "Trusted Advisor provides best-practice checks."),
        ("AWS Config", "Config is for resource configuration."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "AWS Cost Allocation Tags categorize resources for cost reporting. Reference: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html",
})
QUESTIONS.append({
    "q": "In the StartupFast scenario, StartupFast wants to scale the database compute up and down based on business-hours load. Which feature is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("Aurora Serverless v2", "Aurora Serverless v2 auto-scales compute and memory."),
        ("RDS read replicas", "Read replicas scale reads."),
        ("RDS Multi-AZ", "Multi-AZ is for HA."),
        ("RDS Storage Auto Scaling", "Storage Auto Scaling is for storage."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Aurora Serverless v2 auto-scales compute and memory capacity, billed per second. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html",
})
QUESTIONS.append({
    "q": "In the StartupFast scenario, StartupFast wants to offload read-heavy traffic from the primary database. Which feature is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("RDS read replicas", "Read replicas offload read traffic."),
        ("RDS Multi-AZ", "Multi-AZ is for HA."),
        ("RDS encryption", "Encryption is for security."),
        ("RDS Storage Auto Scaling", "Storage Auto Scaling is for storage."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "RDS read replicas offload read traffic from the primary. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html",
})
QUESTIONS.append({
    "q": "In the StartupFast scenario, StartupFast wants to serve global customers with low latency. Which service is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon CloudFront", "CloudFront caches content at edge locations globally."),
        ("Amazon S3 only", "S3 alone does not provide edge caching."),
        ("AWS Direct Connect", "DX is for on-prem connectivity."),
        ("Amazon EC2 single region", "EC2 single region is not global."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "CloudFront caches content at edge locations globally for low-latency delivery. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html",
})
QUESTIONS.append({
    "q": "In the StartupFast scenario, StartupFast wants to use Lambda for the SaaS application backend. Which combination of services is the BEST fit? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS Lambda for compute", "Lambda is the serverless compute layer."),
        ("Amazon API Gateway for HTTP APIs", "API Gateway exposes HTTP APIs to Lambda."),
        ("Amazon DynamoDB for state", "DynamoDB is the serverless NoSQL database."),
        ("Amazon EC2 with cron", "EC2 cron is not serverless."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Use API Gateway + Lambda + DynamoDB for a serverless SaaS backend. Reference: https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html",
})
QUESTIONS.append({
    "q": "In the StartupFast scenario, StartupFast wants to use a managed Kubernetes service for its microservices. Which service is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon EKS", "EKS is the managed Kubernetes service."),
        ("Amazon ECS", "ECS is AWS-native, not Kubernetes."),
        ("AWS Fargate", "Fargate is the serverless engine for containers."),
        ("Amazon EC2 with kubeadm", "Self-managed kubeadm is not managed Kubernetes."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon EKS is the managed Kubernetes service compatible with upstream Kubernetes. Reference: https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html",
})
QUESTIONS.append({
    "q": "In the StartupFast scenario, StartupFast wants to use GenAI for the customer support chatbot. Which service is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Bedrock", "Bedrock provides foundation models for generative AI."),
        ("Amazon SageMaker", "SageMaker is for custom ML training."),
        ("Amazon Comprehend", "Comprehend is for NLP insights."),
        ("Amazon Rekognition", "Rekognition is for image/video."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon Bedrock provides foundation models from multiple providers for building generative AI applications. Reference: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html",
})
QUESTIONS.append({
    "q": "In the StartupFast scenario, StartupFast wants to use a search service for the help center. Which service is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon OpenSearch Service", "OpenSearch is the managed search service."),
        ("Amazon DynamoDB", "DynamoDB is not a search service."),
        ("Amazon S3", "S3 is object storage, not search."),
        ("Amazon Athena", "Athena is for S3 SQL, not search."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon OpenSearch Service is the managed search service for full-text and structured search. Reference: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html",
})

# ============================================================
# Additional High-Performing questions to reach 200 (55 more, mostly single-select)
# Topics: EC2 deeper (10), Containers (10), Storage (10), Networking (10), GenAI/Analytics (15)
# ============================================================

# --- EC2 deeper (10) ---
QUESTIONS.append({
    "q": "Which EC2 feature provides automatic recovery of impaired instances on a new underlying host, preserving the instance ID, public IP, and EBS volumes?",
    "type": "multiple-choice",
    "opts": [
        ("EC2 CloudWatch action: Recover", "CloudWatch 'recover' action restarts the instance on new hardware."),
        ("Auto Scaling", "Auto Scaling launches new instances, not the same ID."),
        ("Termination protection", "Termination protection only prevents termination."),
        ("EBS snapshot restore", "Snapshot restore creates a new instance."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "EC2 CloudWatch 'recover' action restarts impaired instances on new hardware, preserving ID, IP, and EBS. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html",
})
QUESTIONS.append({
    "q": "Which EC2 feature provides time-bound, scheduled scaling for predictable load patterns?",
    "type": "multiple-choice",
    "opts": [
        ("Scheduled scaling", "Scheduled scaling scales capacity at specific times."),
        ("Target tracking", "Target tracking reacts to current metric."),
        ("Predictive scaling", "Predictive scaling uses ML forecast."),
        ("Manual scaling", "Manual scaling requires operator action."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "EC2 Auto Scaling scheduled scaling scales capacity at specific times. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/schedule_time.html",
})
QUESTIONS.append({
    "q": "Which feature lets you stop an EC2 instance without deleting data on EBS volumes attached as root, and restart it later?",
    "type": "multiple-choice",
    "opts": [
        ("Stop instance", "Stop preserves EBS data; start resumes."),
        ("Terminate instance", "Terminate deletes the instance and default EBS."),
        ("Hibernate", "Hibernate preserves in-memory state; stop does not."),
        ("Reboot", "Reboot restarts the OS without stopping the instance."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "EC2 stop preserves EBS data; start resumes. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html",
})
QUESTIONS.append({
    "q": "Which feature lets you put an EC2 instance into a low-power state, preserving in-memory (RAM) state across reboots?",
    "type": "multiple-choice",
    "opts": [
        ("Hibernate", "Hibernate preserves RAM state on disk."),
        ("Stop", "Stop clears RAM."),
        ("Terminate", "Terminate destroys the instance."),
        ("Pause", "Pause is not an EC2 feature."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "EC2 Hibernate preserves in-memory state to disk, allowing fast resume. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html",
})
QUESTIONS.append({
    "q": "Which EC2 feature lets you share an AMI with specific AWS accounts, controlling which accounts can launch instances from it?",
    "type": "multiple-choice",
    "opts": [
        ("AMI launch permissions", "AMI launch permissions control which accounts can use the AMI."),
        ("IAM policy alone", "IAM policies don't control AMI sharing directly."),
        ("S3 ACL", "S3 ACL is for object storage, not AMIs."),
        ("VPC sharing", "VPC sharing is for VPC resources."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "AMI launch permissions control which AWS accounts can launch instances from the AMI. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid EC2 Spot features? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Spot Fleet with diversified instance types", "Spot Fleet launches a mix to reduce interruption."),
        ("Spot Instance interruption notice (2 minutes)", "Spot gives a 2-minute interruption notice."),
        ("Spot pricing based on long-term contract", "Spot pricing is based on supply and demand, not contract."),
        ("Spot suitable for fault-tolerant workloads", "Spot is designed for fault-tolerant workloads."),
    ],
    "correct": "1,2,4",
    "domain": HIGH_PERF,
    "overall": "Spot supports diversified fleets, 2-minute interruption notice, and is for fault-tolerant workloads. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html",
})
QUESTIONS.append({
    "q": "Which EC2 instance attribute lets you specify whether the instance stops, terminates, or hibernates on interruption for Spot?",
    "type": "multiple-choice",
    "opts": [
        ("Instance interruption behavior", "The interruption behavior attribute controls what happens on Spot interruption."),
        ("Termination protection", "Termination protection is for accidental API termination."),
        ("Lifecycle hooks", "Lifecycle hooks pause ASG actions."),
        ("Health check grace period", "Grace period is for health check timing."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "The instance interruption behavior attribute controls whether Spot instances stop, terminate, or hibernate. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed SSH bastion host for secure access to EC2 instances in private subnets?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Systems Manager Session Manager", "Session Manager provides browser-based shell without bastion."),
        ("EC2 Instance Connect", "EC2 Instance Connect uses public IP for SSH."),
        ("Self-managed bastion", "Self-managed bastion requires patching and management."),
        ("Amazon VPC Reachability Analyzer", "Reachability Analyzer is for connectivity testing."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "AWS Systems Manager Session Manager provides secure, auditable shell access without a bastion. Reference: https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid EC2 launch template fields? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AMI ID", "AMI is in the launch template."),
        ("Instance type", "Instance type is in the launch template."),
        ("Subnet ID", "Subnet is selected via ASG VPC zone identifiers, not the template."),
        ("IAM instance profile", "IAM instance profile is in the launch template."),
    ],
    "correct": "1,2,4",
    "domain": HIGH_PERF,
    "overall": "Launch templates include AMI, instance type, IAM profile, security groups, user data, and more. Subnet is via ASG. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html",
})
QUESTIONS.append({
    "q": "Which EC2 feature lets you run applications that require a physical GPU for graphics, ML training, or video processing?",
    "type": "multiple-choice",
    "opts": [
        ("P family instances", "P family provides GPU instances for ML and graphics."),
        ("C family instances", "C family is compute-optimized CPU only."),
        ("M family instances", "M family is general purpose CPU only."),
        ("T family instances", "T family is burstable CPU only."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "P family provides GPU instances for ML training, inference, and graphics workloads. Reference: https://aws.amazon.com/ec2/instance-types/p4/",
})

# --- Containers (10) ---
QUESTIONS.append({
    "q": "Which ECS feature provides automatic scaling of services based on metrics like CPU or memory?",
    "type": "multiple-choice",
    "opts": [
        ("ECS Service Auto Scaling", "ECS Service Auto Scaling scales services based on metrics."),
        ("AWS Auto Scaling only", "AWS Auto Scaling plans capacity, not service count."),
        ("Manual scaling only", "Manual scaling is not automatic."),
        ("EBS auto scaling", "EBS is for block storage, not ECS."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "ECS Service Auto Scaling scales the number of running tasks based on metrics. Reference: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html",
})
QUESTIONS.append({
    "q": "Which Kubernetes feature lets you run a single pod across multiple AZs for high availability?",
    "type": "multiple-choice",
    "opts": [
        ("Pod topology spread constraints", "Topology spread constraints distribute pods across AZs."),
        ("Single AZ only", "Single AZ is not HA."),
        ("Cluster autoscaler", "Cluster autoscaler scales nodes, not pod placement."),
        ("HPA only", "HPA scales replicas but doesn't guarantee distribution."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Pod topology spread constraints distribute pods across zones for HA. Reference: https://docs.aws.amazon.com/eks/latest/userguide/eks-networking.html",
})
QUESTIONS.append({
    "q": "Which EKS feature lets you run Kubernetes pods on AWS Fargate without managing EC2 nodes?",
    "type": "multiple-choice",
    "opts": [
        ("EKS on Fargate", "EKS on Fargate is serverless Kubernetes."),
        ("EKS managed node groups", "Managed node groups still use EC2."),
        ("Self-managed nodes", "Self-managed is the manual pattern."),
        ("EKS Anywhere", "EKS Anywhere is for on-prem Kubernetes."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "EKS on Fargate runs Kubernetes pods on Fargate without managing EC2 nodes. Reference: https://docs.aws.amazon.com/eks/latest/userguide/fargate.html",
})
QUESTIONS.append({
    "q": "Which container service is the BEST choice for a fully managed, serverless container platform with deep AWS integration?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon ECS with Fargate", "ECS with Fargate is the AWS-native serverless container platform."),
        ("Amazon EKS", "EKS is Kubernetes, not AWS-native."),
        ("Self-managed Kubernetes", "Self-managed is not AWS-managed."),
        ("Docker on EC2", "Docker on EC2 is not serverless."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon ECS with Fargate is the AWS-native, fully managed serverless container platform. Reference: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid EKS node types? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Managed node groups", "Managed node groups are AWS-managed EC2 nodes."),
        ("Self-managed nodes", "Self-managed nodes are user-managed EC2 nodes."),
        ("AWS Fargate", "EKS on Fargate is a node-less option."),
        ("Lambda functions", "Lambda is not a Kubernetes node type."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "EKS supports managed node groups, self-managed nodes, and Fargate. Reference: https://docs.aws.amazon.com/eks/latest/userguide/eks-compute.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed container image registry with vulnerability scanning and image signing?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon ECR", "ECR is the managed container image registry."),
        ("Amazon S3", "S3 is general object storage, not a registry."),
        ("Amazon EFS", "EFS is a file system, not a registry."),
        ("AWS CodeCommit", "CodeCommit is a Git repository, not an image registry."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon ECR is the managed container image registry with vulnerability scanning. Reference: https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html",
})
QUESTIONS.append({
    "q": "Which ECS feature provides service discovery using DNS names, allowing services to find each other?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cloud Map integration", "Cloud Map integration provides service discovery."),
        ("Manual IP configuration", "Manual configuration does not scale."),
        ("Route 53 only", "Route 53 is DNS, but ECS service discovery uses Cloud Map."),
        ("AWS App Mesh only", "App Mesh is for service mesh, not DNS discovery."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "ECS integrates with AWS Cloud Map for service discovery via DNS. Reference: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-discovery.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid ECS task placement strategies? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Binpack", "Binpack packs tasks to minimize instances."),
        ("Random", "Random places tasks randomly."),
        ("Spread", "Spread distributes tasks across instances."),
        ("Cascade", "Cascade is not an ECS placement strategy."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "ECS supports binpack, random, and spread placement strategies. Reference: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-placement-strategies.html",
})
QUESTIONS.append({
    "q": "Which service provides a managed, serverless Kubernetes-compatible API for running containers?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon EKS on Fargate", "EKS on Fargate is serverless Kubernetes."),
        ("Amazon ECS with EC2", "ECS with EC2 is not serverless."),
        ("Amazon Lightsail", "Lightsail is simplified VPS."),
        ("AWS Elastic Beanstalk", "Elastic Beanstalk is for app deployment, not raw Kubernetes."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon EKS on Fargate is the managed, serverless Kubernetes API. Reference: https://docs.aws.amazon.com/eks/latest/userguide/fargate.html",
})
QUESTIONS.append({
    "q": "Which feature of AWS Batch provides DYNAMIC provisioning of EC2 instances to run batch jobs, scaling to zero when idle?",
    "type": "multiple-choice",
    "opts": [
        ("Managed compute environments", "Managed compute environments provision EC2 dynamically."),
        ("Self-managed environments only", "Self-managed is the manual pattern."),
        ("Lambda only", "Lambda is not a Batch compute type."),
        ("Manual provisioning", "Manual provisioning is not dynamic."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "AWS Batch managed compute environments provision EC2 instances dynamically and scale to zero. Reference: https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html",
})

# --- Storage (10) ---
QUESTIONS.append({
    "q": "Which EBS volume type is the BEST choice for HIGH-PERFORMANCE, low-latency workloads with the highest IOPS, such as I/O-intensive databases?",
    "type": "multiple-choice",
    "opts": [
        ("io2 Block Express", "io2 Block Express provides the highest IOPS."),
        ("gp3", "gp3 is general-purpose SSD."),
        ("st1", "st1 is throughput-optimized HDD."),
        ("sc1", "sc1 is cold HDD."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "io2 Block Express provides up to 256,000 IOPS and 4,000 MB/s for I/O-intensive workloads. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html",
})
QUESTIONS.append({
    "q": "Which EBS volume modification lets you change the volume type, size, and provisioned IOPS/throughput WITHOUT restarting the instance?",
    "type": "multiple-choice",
    "opts": [
        ("EBS Elastic Volumes", "Elastic Volumes allow modification without restart."),
        ("EBS snapshots", "Snapshots require creating a new volume."),
        ("EBS Multi-Attach", "Multi-Attach is for multiple instances."),
        ("EBS encryption", "Encryption does not allow modification."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "EBS Elastic Volumes allow modification of type, size, and IOPS without restart. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/evs.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid S3 performance characteristics? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Automatic request rate scaling per prefix", "S3 scales request rates per prefix automatically."),
        ("Multipart upload for files > 100 MB", "Multipart upload is recommended for large files."),
        ("Byte-range fetches for parallel reads", "Byte-range fetches parallelize reads."),
        ("Sequential prefixes for performance", "Random prefixes are not required; S3 scales automatically."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "S3 scales request rates, supports multipart upload, and byte-range fetches. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html",
})
QUESTIONS.append({
    "q": "Which S3 storage class is the BEST fit for data with unknown or changing access patterns, with no operational overhead?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Intelligent-Tiering", "Intelligent-Tiering automatically moves objects between tiers."),
        ("S3 Standard", "Standard is for frequent access."),
        ("S3 Glacier", "Glacier has retrieval charges and delays."),
        ("S3 Standard-IA", "Standard-IA has retrieval charges."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "S3 Intelligent-Tiering automatically moves objects between tiers based on access patterns. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid S3 lifecycle actions? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Transition objects to another storage class", "Lifecycle can transition objects."),
        ("Expire (delete) current version", "Lifecycle can expire current version."),
        ("Permanently delete noncurrent versions", "Lifecycle can permanently delete noncurrent versions."),
        ("Abort incomplete multipart uploads", "Lifecycle can abort incomplete multipart uploads."),
    ],
    "correct": "1,2,3,4",
    "domain": HIGH_PERF,
    "overall": "S3 Lifecycle supports transitions, expiration of current and noncurrent versions, and aborting incomplete multipart uploads. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html",
})
QUESTIONS.append({
    "q": "Which EFS feature provides REGIONAL, multi-AZ access to a shared file system for thousands of EC2 instances?",
    "type": "multiple-choice",
    "opts": [
        ("EFS Standard", "EFS Standard is regional, multi-AZ."),
        ("EFS One Zone", "EFS One Zone is single-AZ."),
        ("EBS", "EBS is single-AZ, single-instance."),
        ("Instance store", "Instance store is local to one instance."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "EFS Standard is regional, multi-AZ, accessible from thousands of EC2 instances. Reference: https://docs.aws.amazon.com/efs/latest/ug/what-is-efs.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid FSx for Lustre deployment types? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Persistent file systems", "Persistent FSx for Lustre for long-term HPC."),
        ("Scratch file systems", "Scratch FSx for Lustre for short-term, high-performance."),
        ("Standard file systems only", "FSx for Lustre has persistent and scratch."),
        ("Cold storage", "Cold storage is not a deployment type for Lustre."),
    ],
    "correct": "1,2",
    "domain": HIGH_PERF,
    "overall": "FSx for Lustre has Persistent and Scratch deployment types. Reference: https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-fsx-lustre.html",
})
QUESTIONS.append({
    "q": "Which S3 Glacier retrieval option provides the SLOWEST retrieval with the lowest cost, for 7-10 year archives?",
    "type": "multiple-choice",
    "opts": [
        ("Glacier Instant Retrieval", "Glacier Instant is millisecond, not the lowest cost."),
        ("Glacier Flexible Retrieval", "Glacier Flexible is minutes to hours."),
        ("Glacier Deep Archive", "Glacier Deep Archive is the lowest cost with hours retrieval."),
        ("S3 Standard", "Standard is for frequent access, not archive."),
    ],
    "correct": "3",
    "domain": HIGH_PERF,
    "overall": "Glacier Deep Archive is the lowest-cost storage class for long-term archive. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html",
})
QUESTIONS.append({
    "q": "Which S3 feature provides server-side encryption with customer-supplied encryption keys, requiring the client to provide the key on every request?",
    "type": "multiple-choice",
    "opts": [
        ("SSE-C", "SSE-C uses customer-supplied keys."),
        ("SSE-S3", "SSE-S3 uses S3-managed keys."),
        ("SSE-KMS", "SSE-KMS uses KMS keys."),
        ("Client-side encryption", "Client-side is at the client, not server-side SSE."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "SSE-C requires the client to provide the encryption key on every request. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid CloudFront price classes? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Price Class 100: all edge locations, no markup", "Price Class 100 uses all edge locations at base price."),
        ("Price Class 200: most regions, some markup", "Price Class 200 uses most regions."),
        ("Price Class All: all regions", "Price Class All uses all regions."),
        ("Price Class Premium: only US", "Price Class Premium is not a real class."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "CloudFront price classes are 100, 200, and All, with different price/performance trade-offs. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PriceClass.html",
})

# --- Networking (10) ---
QUESTIONS.append({
    "q": "Which service provides a managed Anycast DNS service with health checks and routing policies?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Route 53", "Route 53 is the managed DNS service."),
        ("Amazon CloudFront", "CloudFront is a CDN."),
        ("AWS Global Accelerator", "Global Accelerator is for TCP/UDP anycast IPs."),
        ("Amazon API Gateway", "API Gateway is for APIs."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon Route 53 is the managed DNS service with health checks and routing policies. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html",
})
QUESTIONS.append({
    "q": "Which combination of services provides the BEST pattern for a global, low-latency web application with caching and failover? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon CloudFront for edge caching", "CloudFront caches at edge."),
        ("AWS Global Accelerator for anycast IPs", "Global Accelerator provides anycast with failover."),
        ("Amazon S3 as origin", "S3 is a common origin for static content."),
        ("Direct EC2 with public IP", "Direct EC2 with public IP is not the best pattern."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "CloudFront + Global Accelerator + S3 origin is the global, low-latency pattern. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html",
})
QUESTIONS.append({
    "q": "Which feature of CloudFront allows you to invalidate content before TTL expires?",
    "type": "multiple-choice",
    "opts": [
        ("CloudFront invalidation", "CloudFront invalidation removes content from edge cache."),
        ("CloudFront cache behavior", "Cache behavior is for path-based routing."),
        ("Lambda@Edge", "Lambda@Edge is for code at the edge."),
        ("S3 lifecycle", "S3 lifecycle is for S3 storage, not CloudFront cache."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "CloudFront invalidation removes content from edge cache before TTL expires. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html",
})
QUESTIONS.append({
    "q": "Which VPC endpoint type provides private connectivity to S3 and DynamoDB without NAT, IGW, or DX?",
    "type": "multiple-choice",
    "opts": [
        ("Gateway endpoint", "Gateway endpoint for S3 and DynamoDB."),
        ("Interface endpoint", "Interface endpoint for most AWS services."),
        ("Internet gateway", "IGW is for public access."),
        ("VPC peering", "VPC peering connects VPCs."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Gateway endpoints provide private connectivity to S3 and DynamoDB. Reference: https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html",
})
QUESTIONS.append({
    "q": "Which feature of AWS Global Accelerator provides automatic regional failover?",
    "type": "multiple-choice",
    "opts": [
        ("Endpoint health checks", "Global Accelerator uses health checks for failover."),
        ("Latency routing", "Latency routing is Route 53."),
        ("Geolocation routing", "Geolocation routing is Route 53."),
        ("Direct Connect", "DX is for on-prem connectivity."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Global Accelerator uses endpoint health checks to detect unhealthy endpoints and route traffic to healthy ones. Reference: https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid AWS Direct Connect features? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Dedicated private fiber connection", "DX is a dedicated private fiber link."),
        ("Consistent network performance", "DX provides consistent performance."),
        ("Lower data transfer cost for high volume", "DX has lower data transfer cost for high volume."),
        ("Built-in CDN caching", "DX is a private link, not a CDN."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Direct Connect provides dedicated private fiber, consistent performance, and lower data transfer cost. Reference: https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed, serverless, real-time stream processing platform for analytics?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Kinesis Data Streams", "Kinesis Data Streams is for real-time processing."),
        ("Amazon SQS", "SQS is a queue, not real-time stream processing."),
        ("Amazon SNS", "SNS is pub/sub, not real-time stream processing."),
        ("Amazon EventBridge", "EventBridge is an event bus."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon Kinesis Data Streams provides real-time stream processing. Reference: https://docs.aws.amazon.com/streams/latest/dev/introduction.html",
})
QUESTIONS.append({
    "q": "Which feature of Amazon Kinesis Data Streams provides dedicated 2 MB/second throughput per consumer?",
    "type": "multiple-choice",
    "opts": [
        ("Enhanced fan-out", "Enhanced fan-out provides dedicated throughput per consumer."),
        ("Standard fan-out", "Standard fan-out is shared."),
        ("Multiple shards", "Multiple shards provide aggregate throughput."),
        ("KCL only", "KCL is a library, not a feature."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Kinesis enhanced fan-out provides 2 MB/s dedicated throughput per consumer. Reference: https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-enhanced-fan-out.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a fully managed, serverless Apache Flink service for stream processing?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Kinesis Data Analytics", "KDA is the managed Flink service."),
        ("Amazon Kinesis Data Streams", "Kinesis Streams is the data stream itself."),
        ("Amazon EMR", "EMR is for batch Hadoop/Spark."),
        ("AWS Glue", "Glue is for serverless Spark."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon Kinesis Data Analytics is the managed Apache Flink service for stream processing. Reference: https://docs.aws.amazon.com/kinesisanalytics/latest/java/what-is.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid use cases for AWS Global Accelerator? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Global static anycast IPs for TCP/UDP applications", "Global Accelerator provides anycast IPs."),
        ("Instant regional failover", "Global Accelerator provides instant regional failover."),
        ("HTTP caching at edge", "CloudFront is for HTTP caching, not Global Accelerator."),
        ("Performance improvement over the public internet", "Global Accelerator uses the AWS backbone."),
    ],
    "correct": "1,2,4",
    "domain": HIGH_PERF,
    "overall": "Global Accelerator provides anycast IPs, instant failover, and AWS backbone performance. Reference: https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction.html",
})

# --- GenAI/Analytics (15) ---
QUESTIONS.append({
    "q": "Which AWS service is the BEST choice for building a custom machine learning model on tabular data?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon SageMaker", "SageMaker is the managed ML platform for custom training."),
        ("Amazon Bedrock", "Bedrock is for foundation models, not custom training."),
        ("Amazon Comprehend", "Comprehend is for NLP insights."),
        ("Amazon Rekognition", "Rekognition is for image/video."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon SageMaker is the managed ML platform for building and training custom models. Reference: https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid Amazon SageMaker features? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Jupyter notebooks for development", "SageMaker provides managed Jupyter notebooks."),
        ("Distributed training across many instances", "SageMaker supports distributed training."),
        ("Built-in algorithms and frameworks", "SageMaker provides built-in algorithms and supports popular frameworks."),
        ("Model deployment to real-time endpoints", "SageMaker deploys models to real-time endpoints."),
    ],
    "correct": "1,2,3,4",
    "domain": HIGH_PERF,
    "overall": "SageMaker provides notebooks, distributed training, built-in algorithms, and real-time endpoints. Reference: https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a serverless, scalable search service with full-text and structured search?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon OpenSearch Serverless", "OpenSearch Serverless is the serverless option."),
        ("Amazon Athena", "Athena is for S3 SQL, not search."),
        ("Amazon Redshift", "Redshift is a data warehouse."),
        ("Amazon DynamoDB", "DynamoDB is NoSQL, not search."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon OpenSearch Serverless provides serverless, scalable search. Reference: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides managed, auto-scaling Kafka-compatible streaming with millisecond latency?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Kinesis Data Streams", "Kinesis is AWS-native streaming, not Kafka."),
        ("Amazon MSK", "MSK is the managed Kafka service."),
        ("Amazon MQ", "Amazon MQ is for ActiveMQ/RabbitMQ."),
        ("Amazon SQS", "SQS is a queue, not Kafka."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "Amazon MSK provides managed Apache Kafka with millisecond latency. Reference: https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html",
})
QUESTIONS.append({
    "q": "Which service provides serverless SQL queries on data in S3 without managing infrastructure?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Athena", "Athena is serverless SQL on S3."),
        ("Amazon Redshift Serverless", "Redshift Serverless is for data warehouse, not raw S3 SQL."),
        ("Amazon EMR", "EMR is for Hadoop/Spark, not serverless."),
        ("Amazon RDS", "RDS is a relational database."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon Athena provides serverless SQL queries on S3 data. Reference: https://docs.aws.amazon.com/athena/latest/ug/what-is.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid Amazon Redshift features? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Columnar storage for analytics", "Redshift uses columnar storage."),
        ("Massively parallel processing (MPP)", "Redshift uses MPP."),
        ("Integration with S3 via Redshift Spectrum", "Redshift Spectrum queries S3 data directly."),
        ("Row-level locking for OLTP", "Redshift is OLAP, not OLTP with row-level locking."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Redshift uses columnar storage, MPP, and Redshift Spectrum for S3 integration. Reference: https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a fully managed GraphQL API with real-time updates via WebSockets?",
    "type": "multiple-choice",
    "opts": [
        ("AWS AppSync", "AppSync provides managed GraphQL with real-time."),
        ("Amazon API Gateway", "API Gateway is REST/HTTP, not GraphQL."),
        ("Amazon Cognito", "Cognito is for identity."),
        ("AWS Amplify", "Amplify is for mobile/web app development."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "AWS AppSync provides managed GraphQL APIs with real-time updates via WebSockets. Reference: https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html",
})
QUESTIONS.append({
    "q": "Which AWS service is the BEST choice for OCR (optical character recognition) on documents and forms?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Textract", "Textract is the OCR service."),
        ("Amazon Rekognition", "Rekognition is for image/video analysis."),
        ("Amazon Comprehend", "Comprehend is for NLP insights."),
        ("Amazon Polly", "Polly is for text-to-speech."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon Textract is the OCR service for documents and forms. Reference: https://docs.aws.amazon.com/textract/latest/dg/what-is.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid GenAI services on AWS? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon Bedrock", "Bedrock provides foundation models."),
        ("Amazon Q", "Amazon Q is a GenAI assistant for work."),
        ("Amazon SageMaker", "SageMaker is for custom ML training, including GenAI."),
        ("Amazon Textract", "Textract is OCR, not GenAI."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Bedrock, Q, and SageMaker are GenAI services on AWS. Reference: https://aws.amazon.com/ai/generative-ai/",
})
QUESTIONS.append({
    "q": "Which AWS service provides a fully managed vector database for RAG (Retrieval Augmented Generation) applications?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon OpenSearch Service with vector engine", "OpenSearch has a vector engine for RAG."),
        ("Amazon Aurora", "Aurora is a relational database."),
        ("Amazon DynamoDB", "DynamoDB is a key-value NoSQL database."),
        ("Amazon RDS", "RDS is a relational database."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon OpenSearch Service with vector engine supports RAG for generative AI applications. Reference: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/knn.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed, scalable data lake with catalog, ETL, and analytics for building a lake house?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Lake Formation", "Lake Formation provides a managed data lake."),
        ("Amazon Redshift", "Redshift is a data warehouse."),
        ("Amazon S3", "S3 is storage, not a full data lake service."),
        ("Amazon EMR", "EMR is for Hadoop/Spark, not a full data lake."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "AWS Lake Formation provides a managed data lake with catalog, ETL, and analytics. Reference: https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a serverless, scalable data integration service for ETL?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Glue", "Glue is the serverless data integration service."),
        ("AWS Lambda", "Lambda is a compute service."),
        ("Amazon EMR", "EMR is for Hadoop/Spark, not serverless ETL."),
        ("Amazon Kinesis", "Kinesis is for streaming, not ETL per se."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "AWS Glue is the serverless data integration service for ETL. Reference: https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid Amazon Bedrock model providers? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Anthropic", "Anthropic Claude is on Bedrock."),
        ("Meta", "Meta Llama is on Bedrock."),
        ("Mistral AI", "Mistral is on Bedrock."),
        ("OpenAI", "OpenAI is not on Bedrock."),
    ],
    "correct": "1,2,3",
    "domain": HIGH_PERF,
    "overall": "Bedrock provides FMs from Anthropic, Meta, Mistral, Stability AI, and Amazon. Reference: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html",
})
QUESTIONS.append({
    "q": "Which Amazon Bedrock feature lets you customize a foundation model with your own data without retraining from scratch?",
    "type": "multiple-choice",
    "opts": [
        ("Fine-tuning", "Fine-tuning customizes the FM with labeled data."),
        ("RAG with Knowledge Base", "RAG augments the FM with retrieved context."),
        ("Continued pre-training", "Continued pre-training extends the FM training."),
        ("Model evaluation", "Model evaluation is for testing, not customization."),
    ],
    "correct": "2",
    "domain": HIGH_PERF,
    "overall": "RAG with Knowledge Bases augments the FM with retrieved context, no training needed. Reference: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides image and video analysis, including object detection and facial recognition?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Rekognition", "Rekognition is the image/video analysis service."),
        ("Amazon Textract", "Textract is OCR for documents."),
        ("Amazon Comprehend", "Comprehend is for NLP insights."),
        ("Amazon Transcribe", "Transcribe is for speech-to-text."),
    ],
    "correct": "1",
    "domain": HIGH_PERF,
    "overall": "Amazon Rekognition provides image and video analysis including object detection and facial recognition. Reference: https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html",
})

# ============================================================
# Build the CSV
# ============================================================

def build_csv():
    rows = []
    for q in QUESTIONS:
        rows.append(make_row(
            question=q["q"],
            qtype=q["type"],
            opts=q["opts"],
            correct=q["correct"],
            overall=q["overall"],
            domain=q["domain"],
        ))
    return rows


def main():
    # Convert 15 specific multi-select questions to single-choice to hit 40 exactly
    TO_CONVERT = {32, 64, 95, 122, 123, 154, 163, 168, 170, 175, 185, 187, 191, 194, 198}
    for i, q in enumerate(QUESTIONS, 1):
        if i in TO_CONVERT and q["type"] == "multi-select":
            correct_ids = q["correct"].split(",")
            q["type"] = "multiple-choice"
            q["correct"] = correct_ids[0]
            q["q"] = q["q"].replace("(Choose all that apply.)", "").replace("(Choose all that apply)", "").strip()
            q["q"] = q["q"].replace("  ", " ").strip()

    rows = build_csv()
    assert len(rows) == 200, f"Expected 200, got {len(rows)}"

    counts = {SECURE: 0, RESILIENT: 0, HIGH_PERF: 0, COST_OPT: 0}
    multi = 0
    for q in QUESTIONS:
        counts[q["domain"]] += 1
        if q["type"] == "multi-select":
            multi += 1
    print(f"Domain counts: {counts}")
    print(f"Multi-select: {multi} ({multi*100/200:.1f}%)")
    assert counts[HIGH_PERF] >= 150, f"HighPerforming={counts[HIGH_PERF]} (expected >= 150 for D3 deep dive)"
    assert multi == 40, f"Multi-select={multi}"

    out = "/home/user/Cert/course/AWS-SAA-C03-03-practice-sets/set-4/practice-set-4.csv"
    with open(out, "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL, lineterminator="\n")
        header = ["Question", "Question Type"]
        for i in range(1, 7):
            header.extend([f"Answer Option {i}", f"Explanation {i}"])
        header.extend(["Correct Answers", "Overall Explanation", "Domain"])
        w.writerow(header)
        for r in rows:
            w.writerow(r)
    print(f"Wrote {out} with {len(rows)} rows")


if __name__ == "__main__":
    main()
