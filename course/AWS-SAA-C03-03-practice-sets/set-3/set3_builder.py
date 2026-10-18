"""Builder for SAA-C03 Set 3 — Domain 2 Resilient Architectures deep dive (200q) + Streamify case study.

Set 3 is a deep dive on Domain 2 (Resilient Architectures, 26% of the real exam).
- 200 questions total
- 20% multi-select = 40 questions
- 20 case-study questions referencing Streamify
- 100% Resilient domain
"""

import csv

# Domain strings (must match exactly)
SECURE = "Design Secure Architectures"
RESILIENT = "Design Resilient Architectures"
HIGH_PERF = "Design High-Performing Architectures"
COST_OPT = "Design Cost-Optimized Architectures"


def make_row(question, qtype, opts, correct, overall, domain):
    """Build a row. opts is a list of (text, explanation) tuples. correct is 1-based string like '1' or '1,3'."""
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
# MULTI-AZ DESIGN (25 questions)
# ============================================================

# --- ALB and NLB (8) ---
QUESTIONS.append({
    "q": "Which SINGLE combination provides the BEST pattern for high availability of a stateless web application?",
    "type": "multiple-choice",
    "opts": [
        ("Auto Scaling group across multiple Availability Zones", "ASG multi-AZ is the HA foundation for stateless apps."),
        ("Application Load Balancer across AZs", "ALB distributes across multi-AZ targets."),
        ("Single-AZ RDS Multi-AZ deployment", "RDS Multi-AZ is for the database tier, not the web tier."),
        ("AWS Global Accelerator", "Global Accelerator is for global performance, not single-region HA."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Stateless web tier HA: ASG + ALB across multiple AZs. RDS Multi-AZ is for the database. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html",
})
QUESTIONS.append({
    "q": "Which Elastic Load Balancing feature performs health checks on registered targets and routes only to healthy ones?",
    "type": "multiple-choice",
    "opts": [
        ("Connection draining", "Connection draining is the deregistration delay."),
        ("Health checks", "Health checks determine target health and route only to healthy ones."),
        ("Sticky sessions", "Sticky sessions bind user to instance."),
        ("Cross-zone load balancing", "Cross-zone load balancing is about traffic distribution."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "ELB health checks determine target health, and traffic is routed only to healthy targets. Reference: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html",
})
QUESTIONS.append({
    "q": "Which load balancer type is BEST for static IP addresses and extreme TCP/UDP performance?",
    "type": "multiple-choice",
    "opts": [
        ("Application Load Balancer", "ALB is HTTP/HTTPS layer 7."),
        ("Network Load Balancer", "NLB is layer 4 with static IPs and millions of connections."),
        ("Gateway Load Balancer", "GWLB is for third-party virtual appliances."),
        ("Classic Load Balancer", "CLB is legacy."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Network Load Balancer (NLB) is layer 4 with static IP addresses and high throughput. Reference: https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html",
})
QUESTIONS.append({
    "q": "Which load balancer is BEST for inserting third-party virtual appliances (firewalls, IDS/IPS) transparently into traffic flows?",
    "type": "multiple-choice",
    "opts": [
        ("Application Load Balancer", "ALB is L7, not for virtual appliance insertion."),
        ("Network Load Balancer", "NLB is L4, not optimized for appliance insertion."),
        ("Gateway Load Balancer", "GWLB is purpose-built for transparent appliance insertion."),
        ("Classic Load Balancer", "CLB is legacy."),
    ],
    "correct": "3",
    "domain": RESILIENT,
    "overall": "Gateway Load Balancer is purpose-built for transparent insertion of third-party virtual appliances. Reference: https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html",
})
QUESTIONS.append({
    "q": "Which ALB feature preserves the source IP of the client when traffic reaches the backend, important for IP-based allowlisting?",
    "type": "multiple-choice",
    "opts": [
        ("Cross-zone load balancing", "Cross-zone is for traffic distribution across AZs."),
        ("Sticky sessions with cookie", "Sticky sessions route to same instance, not preserve source IP."),
        ("Client IP preservation (default for ALB)", "ALB preserves the client IP in the X-Forwarded-For header."),
        ("NLB only", "NLB preserves the client IP by default; ALB also does with XFF."),
    ],
    "correct": "3",
    "domain": RESILIENT,
    "overall": "Application Load Balancer preserves the client IP and forwards it in X-Forwarded-For. Reference: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-request-routing.html",
})
QUESTIONS.append({
    "q": "Which SINGLE feature does ALB support that NLB does NOT?",
    "type": "multiple-choice",
    "opts": [
        ("Layer 7 routing based on path or host", "ALB routes L7; NLB is L4."),
        ("Sticky sessions with cookies", "ALB supports sticky sessions; NLB does not."),
        ("Static IP addresses", "NLB has static IPs; ALB does not have static IPs."),
        ("TLS termination", "Both ALB and NLB support TLS termination."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "ALB supports L7 routing and sticky sessions; NLB is L4 and does not. Reference: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-request-routing.html",
})
QUESTIONS.append({
    "q": "Which feature of Elastic Load Balancing drains existing connections before terminating or deregistering an instance, preventing in-flight request failures?",
    "type": "multiple-choice",
    "opts": [
        ("Connection draining (deregistration delay)", "Deregistration delay drains in-flight connections."),
        ("Health checks", "Health checks determine target health."),
        ("Sticky sessions", "Sticky sessions bind user to instance."),
        ("Cross-zone load balancing", "Cross-zone is for traffic distribution."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "ELB deregistration delay (formerly connection draining) drains in-flight requests before instance termination. Reference: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html#deregistration-delay",
})
QUESTIONS.append({
    "q": "Which SINGLE feature does NLB support that ALB does NOT?",
    "type": "multiple-choice",
    "opts": [
        ("Static IP addresses per load balancer", "NLB has static IPs; ALB does not."),
        ("Millions of connections per second", "NLB scales to millions of connections."),
        ("Layer 7 routing based on URL path", "ALB does L7 routing; NLB does not."),
        ("TLS termination with ACM certificates", "Both ALB and NLB support TLS termination with ACM."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "NLB provides static IPs and extreme TCP/UDP performance; ALB does L7 routing. Reference: https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html",
})
QUESTIONS.append({
    "q": "Which AWS service automatically replaces unhealthy EC2 instances in an Auto Scaling group and maintains a desired capacity?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Lambda", "Lambda does not manage EC2 instances."),
        ("Amazon EC2 Auto Scaling with health checks", "Auto Scaling replaces unhealthy instances automatically."),
        ("AWS Systems Manager only", "SSM can run commands, not replace instances."),
        ("AWS OpsWorks", "OpsWorks is a configuration management service."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "EC2 Auto Scaling replaces unhealthy instances automatically based on health checks. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html",
})
QUESTIONS.append({
    "q": "Which SINGLE pattern scales on a forecast of traffic for predictable load?",
    "type": "multiple-choice",
    "opts": [
        ("Target tracking scaling", "Target tracking maintains a CloudWatch metric at a target."),
        ("Step scaling", "Step scaling reacts to alarm breaches with adjustable steps."),
        ("Simple scaling", "Simple scaling adds/removes a fixed number of instances per alarm."),
        ("Predictive scaling only via Lambda", "Predictive scaling is a native ASG feature, not a Lambda function."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "ASG supports target tracking, step, simple, and predictive scaling. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html",
})
QUESTIONS.append({
    "q": "Which ASG scaling policy type is the SIMPLEST and is recommended for most use cases, similar to a thermostat maintaining a temperature?",
    "type": "multiple-choice",
    "opts": [
        ("Target tracking scaling", "Target tracking is the recommended pattern for most use cases."),
        ("Step scaling", "Step scaling is for more complex alarm patterns."),
        ("Simple scaling", "Simple scaling is the basic pattern but less recommended."),
        ("Predictive scaling", "Predictive scaling is for forecast-based scaling."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Target tracking scaling is the simplest and recommended policy type. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html",
})
QUESTIONS.append({
    "q": "Which ASG termination policy BALANCES instances across Availability Zones before selecting an instance to terminate?",
    "type": "multiple-choice",
    "opts": [
        ("Default", "The default termination policy is to balance across AZs."),
        ("OldestInstance", "OldestInstance terminates the oldest, not AZ-balanced."),
        ("NewestInstance", "NewestInstance terminates the newest."),
        ("OldestLaunchConfiguration", "OldestLaunchConfiguration terminates by launch config age."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "The default ASG termination policy balances instances across AZs before selecting. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html",
})
QUESTIONS.append({
    "q": "Which ASG feature provides a HEALTH CHECK GRACE PERIOD, during which Auto Scaling does not mark instances unhealthy even if health checks fail?",
    "type": "multiple-choice",
    "opts": [
        ("Health check grace period", "The grace period prevents premature unhealthy marking during instance startup."),
        ("Termination protection", "Termination protection prevents accidental termination via API."),
        ("Lifecycle hooks", "Lifecycle hooks pause actions during instance state changes."),
        ("Instance protection", "Instance protection prevents termination during scale-in."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Health check grace period prevents Auto Scaling from marking instances unhealthy before they have time to bootstrap. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/healthcheck.html#health-check-grace-period",
})
QUESTIONS.append({
    "q": "Which ASG feature lets you PAUSE instance launch or termination for a specific period, useful for custom lifecycle actions?",
    "type": "multiple-choice",
    "opts": [
        ("Lifecycle hooks", "Lifecycle hooks pause launch/terminate and let you run custom actions."),
        ("Health check grace period", "Grace period is for health check timing."),
        ("Termination protection", "Termination protection is for accidental API termination."),
        ("Instance protection", "Instance protection is for scale-in protection."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Lifecycle hooks pause ASG actions and let you run custom actions via Lambda, SNS, or EventBridge. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html",
})
QUESTIONS.append({
    "q": "Which ASG feature scales based on a FORECAST of traffic, useful for predictable load patterns like daily peaks?",
    "type": "multiple-choice",
    "opts": [
        ("Target tracking scaling", "Target tracking reacts to current metric value."),
        ("Predictive scaling", "Predictive scaling uses ML to forecast future load."),
        ("Step scaling", "Step scaling reacts to alarm breaches."),
        ("Simple scaling", "Simple scaling adds/removes a fixed number of instances."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Predictive scaling uses ML to forecast load and scale ahead of demand. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-predictions.html",
})
QUESTIONS.append({
    "q": "Which SINGLE component is part of an ASG launch template?",
    "type": "multiple-choice",
    "opts": [
        ("AMI ID", "Launch templates include the AMI."),
        ("Instance type", "Instance type is specified in the template."),
        ("Security groups", "Security groups are specified in the template."),
        ("Subnet only", "Subnets are not in the launch template; ASG picks from VPC zone identifiers."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Launch templates include AMI, instance type, security groups, IAM role, user data, and more. Subnets are selected via ASG VPC zone identifiers. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html",
})
QUESTIONS.append({
    "q": "Which SINGLE pattern is the BEST for handling a 10x traffic spike?",
    "type": "multiple-choice",
    "opts": [
        ("Pre-provisioned warm pool of instances", "Warm pools reduce cold-start time."),
        ("Target tracking scaling on a leading indicator", "Target tracking on CPU or request count provides quick scale-out."),
        ("Manual scaling only", "Manual scaling does not handle spikes automatically."),
        ("Single-AZ deployment", "Single-AZ limits the instance pool and capacity."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Use warm pools and target tracking to scale quickly. Manual scaling and single-AZ are not the right patterns. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-warm-pools.html",
})
QUESTIONS.append({
    "q": "Which ASG termination policy selects the instance with the oldest launch configuration or launch template?",
    "type": "multiple-choice",
    "opts": [
        ("Default", "Default balances across AZs."),
        ("OldestLaunchConfiguration", "OldestLaunchConfiguration terminates the oldest launch config."),
        ("AllocationStrategy", "AllocationStrategy is for Spot, not termination."),
        ("ClosestToNextInstanceHour", "ClosestToNextInstanceHour minimizes billing partial hours."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "OldestLaunchConfiguration terminates instances using the oldest launch config first. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html",
})
QUESTIONS.append({
    "q": "Which RDS feature provides synchronous replication to a standby in a different Availability Zone with automatic failover?",
    "type": "multiple-choice",
    "opts": [
        ("RDS read replica", "Read replicas are async and not for HA."),
        ("RDS Multi-AZ deployment", "Multi-AZ provides synchronous replication and automatic failover."),
        ("Aurora Global Database", "Global Database is cross-region, not the basic Multi-AZ."),
        ("RDS Proxy", "RDS Proxy is a connection pooler, not a failover mechanism."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "RDS Multi-AZ uses synchronous replication to a standby in another AZ with automatic failover. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html",
})
QUESTIONS.append({
    "q": "Which statement correctly describes the difference between RDS read replicas and RDS Multi-AZ?",
    "type": "multiple-choice",
    "opts": [
        ("Read replicas provide synchronous replication and automatic failover", "Multi-AZ provides sync replication and failover, not read replicas."),
        ("Read replicas are asynchronous and used for read scaling; Multi-AZ is for HA and failover", "Read replicas scale reads; Multi-AZ provides HA."),
        ("Both are identical", "They serve different purposes."),
        ("Multi-AZ is for reads", "Multi-AZ is for HA, not read scaling."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Read replicas are async and scale reads; Multi-AZ is sync replication for HA and automatic failover. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html",
})
QUESTIONS.append({
    "q": "Which SINGLE Aurora feature provides high availability?",
    "type": "multiple-choice",
    "opts": [
        ("Six-way replicated storage across 3 AZs", "Aurora stores 6 copies across 3 AZs by default."),
        ("Automatic failover to a read replica in <30 seconds", "Aurora failover is sub-30-second."),
        ("Read replicas for read scaling", "Aurora supports up to 15 read replicas."),
        ("Single-AZ deployment only", "Aurora is multi-AZ by default."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Aurora provides 6-way replicated storage, sub-30s failover, and up to 15 read replicas. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html",
})
QUESTIONS.append({
    "q": "Which Aurora failover priority level indicates the FIRST instance chosen for failover?",
    "type": "multiple-choice",
    "opts": [
        ("tier-0", "tier-0 is the highest priority and is the first choice for failover."),
        ("tier-1", "tier-1 is the second priority."),
        ("tier-15", "tier-15 is the lowest priority and is the last choice."),
        ("default", "There is no 'default' tier; priority levels are 0-15."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Failover priority tier-0 is the highest; tier-15 is the lowest. The first tier with a healthy instance is chosen for failover. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html",
})
QUESTIONS.append({
    "q": "Which RDS feature provides read scaling with low replication lag for read-heavy workloads?",
    "type": "multiple-choice",
    "opts": [
        ("RDS Multi-AZ", "Multi-AZ is for HA, not read scaling."),
        ("RDS read replica", "Read replicas scale reads with async replication."),
        ("RDS Proxy", "RDS Proxy is a connection pooler."),
        ("RDS Storage Auto Scaling", "Storage Auto Scaling is for storage, not reads."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "RDS read replicas scale reads with async replication from the primary. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html",
})
QUESTIONS.append({
    "q": "Which feature of Aurora provides cross-region replication with sub-second lag for DR?",
    "type": "multiple-choice",
    "opts": [
        ("Aurora Global Database", "Aurora Global Database provides cross-region replication with sub-second lag."),
        ("Aurora read replica", "Read replicas are within a region."),
        ("Aurora Backtrack", "Backtrack is in-place time-travel within a cluster."),
        ("Aurora Multi-Master", "Multi-Master is multi-writer within a region."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Aurora Global Database replicates to up to 5 secondary regions with sub-second lag. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html",
})
QUESTIONS.append({
    "q": "Which RDS feature provides point-in-time recovery within the retention period (up to 35 days)?",
    "type": "multiple-choice",
    "opts": [
        ("Automated backups", "Automated backups enable point-in-time recovery up to 35 days."),
        ("Manual snapshots only", "Manual snapshots are user-initiated, not continuous."),
        ("Multi-AZ", "Multi-AZ is for HA, not point-in-time recovery."),
        ("Read replicas", "Read replicas scale reads."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "RDS automated backups enable point-in-time recovery to any second within the retention period (up to 35 days). Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html",
})
QUESTIONS.append({
    "q": "Which disaster recovery strategy has the LOWEST RTO and RPO but the HIGHEST cost, with a full secondary environment running and serving traffic?",
    "type": "multiple-choice",
    "opts": [
        ("Backup and restore", "Backup and restore has the highest RTO and lowest cost."),
        ("Pilot light", "Pilot light keeps only critical data and a minimum of services running."),
        ("Warm standby", "Warm standby has a scaled-down but running environment."),
        ("Multi-site active-active", "Multi-site active-active is the lowest RTO/RPO and highest cost."),
    ],
    "correct": "4",
    "domain": RESILIENT,
    "overall": "Multi-site active-active: full secondary running, lowest RTO/RPO, highest cost. Reference: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html",
})
QUESTIONS.append({
    "q": "Which DR strategy keeps a minimal version of the core services running in the DR region (e.g., database with replication) and scales up only when needed?",
    "type": "multiple-choice",
    "opts": [
        ("Backup and restore", "Backup/restore from cold storage has the highest RTO."),
        ("Pilot light", "Pilot light keeps a minimal core in the DR region ready to scale up."),
        ("Warm standby", "Warm standby runs a reduced environment, not minimal."),
        ("Multi-site", "Multi-site runs a full environment."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Pilot light: minimal core services running in the DR region, ready to scale up on demand. Reference: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html",
})
QUESTIONS.append({
    "q": "Which DR strategy has the LOWEST cost, but RTO is measured in HOURS, with data backed up to S3 and restored on demand?",
    "type": "multiple-choice",
    "opts": [
        ("Backup and restore", "Backup and restore is the lowest cost with the highest RTO."),
        ("Pilot light", "Pilot light is a step up from backup."),
        ("Warm standby", "Warm standby has lower RTO than pilot light."),
        ("Multi-site", "Multi-site has near-zero RTO."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Backup and restore is the lowest cost and the slowest RTO (hours). Reference: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html",
})
QUESTIONS.append({
    "q": "Which AWS service replicates Aurora data across regions with sub-second replication lag and supports cross-region disaster recovery?",
    "type": "multiple-choice",
    "opts": [
        ("RDS Multi-AZ", "Multi-AZ is single-region."),
        ("Aurora Global Database", "Aurora Global Database replicates across regions with sub-second lag."),
        ("Aurora read replica", "Read replicas are within a region."),
        ("DynamoDB Streams", "Streams are not replication."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Aurora Global Database provides cross-region replication with sub-second lag for DR. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html",
})
QUESTIONS.append({
    "q": "Which DynamoDB feature provides multi-region replication with multi-master writes for global applications?",
    "type": "multiple-choice",
    "opts": [
        ("DynamoDB Streams", "Streams are change-data capture, not replication."),
        ("DynamoDB Global Tables", "Global Tables provide multi-region, multi-master replication."),
        ("DynamoDB DAX", "DAX is an in-memory cache."),
        ("DynamoDB Accelerator Streams", "Not a real feature."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "DynamoDB Global Tables provide multi-region, multi-master replication for global applications. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html",
})
QUESTIONS.append({
    "q": "Which SINGLE DR concept is the maximum acceptable data loss?",
    "type": "multiple-choice",
    "opts": [
        ("RTO (Recovery Time Objective)", "RTO is how quickly you must recover."),
        ("RPO (Recovery Point Objective)", "RPO is the maximum acceptable data loss."),
        ("MTTR (Mean Time To Recovery)", "MTTR is the average recovery time."),
        ("MTU (Maximum Transmission Unit)", "MTU is a network concept unrelated to DR."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "RTO, RPO, and MTTR are all key DR metrics. Reference: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html",
})
QUESTIONS.append({
    "q": "Which SINGLE Route 53 routing policy is BEST for multi-region active-active?",
    "type": "multiple-choice",
    "opts": [
        ("Latency-based routing", "Latency routing directs users to the lowest-latency region."),
        ("Geolocation routing", "Geolocation routes by user location."),
        ("Weighted routing", "Weighted routing splits traffic across regions."),
        ("Simple routing", "Simple routing returns all records in random order; not for active-active."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "For multi-region active-active, use latency, geolocation, or weighted routing. Simple routing is not appropriate. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html",
})
QUESTIONS.append({
    "q": "Which service provides anycast IPs and improves global application availability and performance with health checks and instant regional failover?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Route 53", "Route 53 is DNS-based."),
        ("AWS Global Accelerator", "Global Accelerator provides anycast IPs with health-check-based failover."),
        ("Amazon CloudFront", "CloudFront is a CDN."),
        ("AWS Direct Connect", "DX is a private network link."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "AWS Global Accelerator provides anycast static IPs and instant regional failover based on health checks. Reference: https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html",
})
QUESTIONS.append({
    "q": "Which SINGLE service is the BEST for cross-region, low-latency DNS?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Route 53 latency-based routing", "Latency routing picks the lowest-latency region."),
        ("Amazon CloudFront with Route 53", "CloudFront caches content; Route 53 resolves origin."),
        ("Amazon API Gateway with multi-region endpoints", "API Gateway multi-region is for API failover."),
        ("AWS Transit Gateway", "Transit Gateway connects VPCs, not for global DNS."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Use Route 53 latency routing and CloudFront for low-latency global DNS and content delivery. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a centralized dashboard for monitoring and managing AWS Backup across accounts and regions?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Backup Audit Manager", "AWS Backup provides centralized management and audit."),
        ("Amazon CloudWatch only", "CloudWatch is for metrics and logs."),
        ("AWS Config only", "Config tracks configuration changes."),
        ("AWS Systems Manager only", "SSM is for ops items."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "AWS Backup provides centralized backup management, compliance monitoring, and audit across accounts and regions. Reference: https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html",
})
QUESTIONS.append({
    "q": "Which SINGLE component is part of an active-passive multi-region DR architecture?",
    "type": "multiple-choice",
    "opts": [
        ("Active primary region with full deployment", "Active region serves traffic."),
        ("Standby DR region with minimal environment", "Standby is the DR region."),
        ("Route 53 failover routing", "Failover routing switches on health check failure."),
        ("Single AZ in the primary region", "Single AZ is an HA antipattern for the primary."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Active-passive DR: full active region, minimal DR region, Route 53 failover routing. Reference: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html",
})
QUESTIONS.append({
    "q": "Which SINGLE combination is the BEST for a pilot-light DR strategy?",
    "type": "multiple-choice",
    "opts": [
        ("Database with cross-region replication (e.g., Aurora Global Database)", "DB replication is the pilot light core."),
        ("Pre-configured AMIs for application servers in the DR region", "AMIs let you scale up quickly."),
        ("AWS CloudFormation for rapid DR region provisioning", "CloudFormation enables reproducible DR environment."),
        ("Full active deployment in the DR region", "Pilot light has a minimal environment, not full active."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Pilot light uses DB replication, pre-configured AMIs, and CloudFormation for quick scale-up. Reference: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html",
})
QUESTIONS.append({
    "q": "Which SINGLE concept is the maximum acceptable data loss?",
    "type": "multiple-choice",
    "opts": [
        ("Lower RTO generally means higher cost", "Lower RTO requires more standby resources."),
        ("Higher RPO generally means lower cost", "Higher RPO means less data preservation, lower cost."),
        ("Backup-and-restore is the lowest cost with the highest RTO", "Backup/restore is the low-cost, high-RTO option."),
        ("Active-active has the highest cost and lowest RTO", "Active-active is the high-cost, low-RTO option."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Lower RTO = higher cost; higher RPO = lower cost. Trade-offs exist between all DR strategies. Reference: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html",
})
QUESTIONS.append({
    "q": "Which SINGLE Route 53 routing policy is BEST for multi-region active-active?",
    "type": "multiple-choice",
    "opts": [
        ("Game day", "Game days are scheduled DR tests."),
        ("Tabletop exercise", "Tabletop exercises walk through scenarios."),
        ("Chaos engineering with AWS Fault Injection Service", "FIS injects faults to test resilience."),
        ("Production deployment only", "Production deployment alone is not a DR test."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "DR testing methods include game days, tabletop exercises, and chaos engineering with FIS. Reference: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/reliability-pillar.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides controlled fault injection for chaos engineering to test application resilience?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Fault Injection Service (FIS)", "FIS is the AWS-managed chaos engineering service."),
        ("AWS Config", "Config is for configuration compliance."),
        ("AWS CloudTrail", "CloudTrail is for API audit."),
        ("Amazon CloudWatch", "CloudWatch is for metrics and logs."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "AWS Fault Injection Service (FIS) provides controlled fault injection for chaos engineering. Reference: https://docs.aws.amazon.com/fis/latest/userguide/what-is.html",
})
QUESTIONS.append({
    "q": "Which S3 replication type is asynchronous and replicates new objects to a bucket in a different region?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Cross-Region Replication (CRR)", "CRR replicates to a different region asynchronously."),
        ("S3 Same-Region Replication (SRR)", "SRR is in the same region."),
        ("S3 Batch Replication", "Batch is for existing objects."),
        ("S3 Live Replication", "Not a real feature."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "S3 Cross-Region Replication (CRR) asynchronously replicates new objects to a destination bucket in a different region. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html",
})
QUESTIONS.append({
    "q": "Which S3 feature replicates existing objects (not just new ones) on demand?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Lifecycle", "Lifecycle transitions and expires objects."),
        ("S3 Batch Replication", "S3 Batch Replication replicates existing objects on demand."),
        ("S3 Inventory", "Inventory is a listing."),
        ("S3 Object Lock", "Object Lock is for immutability."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "S3 Batch Replication replicates existing objects that were not replicated by standard replication. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-batch-replication-batch.html",
})
QUESTIONS.append({
    "q": "Which SINGLE feature is REQUIRED to enable S3 CRR?",
    "type": "multiple-choice",
    "opts": [
        ("Versioning enabled on both source and destination buckets", "Versioning is required."),
        ("An IAM role that S3 assumes to replicate objects", "Replication role is required."),
        ("Public read on both buckets", "Public read is not required and is an antipattern for sensitive data."),
        ("The destination bucket in a different region for CRR", "CRR specifically requires a different region."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "CRR requires versioning, an IAM role, and a destination bucket in a different region. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html",
})
QUESTIONS.append({
    "q": "Which SINGLE storage class transition is valid for S3 CRR?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Standard in the source replicated to S3 Standard in the destination", "Standard-to-Standard is valid."),
        ("S3 Standard in the source replicated to S3 Standard-IA in the destination", "Standard-to-IA is valid for cost optimization."),
        ("S3 Glacier in the source replicated to S3 Standard", "Glacier-to-Standard is valid for restoring."),
        ("S3 One Zone-IA in the source replicated to S3 Glacier", "Storage class transitions in replication are supported."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "S3 replication supports changing storage class in the destination. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html",
})
QUESTIONS.append({
    "q": "Which S3 Multi-Region Access Point feature provides automatic failover to an alternate region when the primary region is unavailable?",
    "type": "multiple-choice",
    "opts": [
        ("Active-active replication", "Active-active replication provides automatic failover."),
        ("Manual failover only", "Multi-Region Access Points do not require manual failover."),
        ("Eventual consistency only", "Multi-Region Access Points provide active-active."),
        ("Health checks via Route 53", "Route 53 is not the underlying mechanism for MRAP failover."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "S3 Multi-Region Access Points provide active-active replication with automatic failover. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPoints.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a global endpoint for routing requests to the nearest healthy regional endpoint with health-check-based failover?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Global Accelerator", "Global Accelerator provides a global anycast endpoint with failover."),
        ("Amazon CloudFront only", "CloudFront is a CDN, not a global endpoint with failover."),
        ("Amazon Route 53 only", "Route 53 is DNS, not a global endpoint."),
        ("AWS Direct Connect", "DX is a private link."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "AWS Global Accelerator provides a global anycast endpoint that routes to the nearest healthy region. Reference: https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html",
})
QUESTIONS.append({
    "q": "Which SINGLE storage class transition is valid for S3 CRR?",
    "type": "multiple-choice",
    "opts": [
        ("Two or more regions with full deployment", "Active-active requires full deployment in each region."),
        ("Global database replication (Aurora Global Database, DynamoDB Global Tables)", "Global replication enables active-active."),
        ("Route 53 latency-based or geolocation routing", "DNS routing directs users to the nearest region."),
        ("Single region with backups", "Single region with backups is not active-active."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Active-active multi-region: full deployment in each region, global database, latency-based routing. Reference: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html",
})
QUESTIONS.append({
    "q": "Which Route 53 routing policy is BEST for active-passive failover between two regions?",
    "type": "multiple-choice",
    "opts": [
        ("Latency-based routing", "Latency routing is for active-active."),
        ("Failover routing", "Failover routing is designed for active-passive."),
        ("Weighted routing", "Weighted routing splits traffic; not for failover."),
        ("Geolocation routing", "Geolocation routes by user location."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Failover routing policy directs traffic to a primary and falls over to a secondary based on health checks. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides managed health checks for Route 53 failover routing, with health checkers in multiple global locations?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Route 53 health checks", "Route 53 health checks are global and managed."),
        ("AWS Config", "Config is for resource configuration."),
        ("AWS CloudTrail", "CloudTrail is for API audit."),
        ("Amazon CloudWatch", "CloudWatch is for metrics and logs."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Route 53 health checks are managed, global health checkers that drive failover routing. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html",
})
QUESTIONS.append({
    "q": "Which SINGLE service provides a global anycast endpoint for failover?",
    "type": "multiple-choice",
    "opts": [
        ("Aurora Global Database", "Aurora Global Database provides sub-second RPO across regions."),
        ("DynamoDB Global Tables", "DynamoDB Global Tables provide multi-region replication."),
        ("RDS read replicas cross-region", "Read replicas provide async replication; lag is seconds to minutes."),
        ("Manual SQL replication", "Manual SQL replication is error-prone and slow."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Aurora Global Database and DynamoDB Global Tables are the best sub-second RPO options. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html",
})
QUESTIONS.append({
    "q": "Which AWS service is a managed message QUEUE for decoupling producers and consumers, with standard and FIFO queue types?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon SNS", "SNS is a pub/sub notification service."),
        ("Amazon SQS", "SQS is a managed message queue with standard and FIFO."),
        ("Amazon EventBridge", "EventBridge is an event bus."),
        ("Amazon Kinesis", "Kinesis is a streaming data service."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Amazon SQS is the managed message queue with standard (best-effort ordering, at-least-once) and FIFO (exactly-once, ordered) types. Reference: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html",
})
QUESTIONS.append({
    "q": "Which AWS service is a managed pub/sub NOTIFICATION service that pushes messages to multiple subscribers?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon SQS", "SQS is a queue, not a pub/sub."),
        ("Amazon SNS", "SNS is the pub/sub notification service."),
        ("Amazon EventBridge", "EventBridge is an event bus with rules."),
        ("AWS Step Functions", "Step Functions orchestrates workflows."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Amazon SNS is a pub/sub notification service that pushes to multiple subscribers (HTTP, SQS, Lambda, email, SMS). Reference: https://docs.aws.amazon.com/sns/latest/dg/welcome.html",
})
QUESTIONS.append({
    "q": "Which service is a serverless event bus that connects applications using events from AWS services, SaaS apps, and custom sources?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon EventBridge", "EventBridge is the serverless event bus with SaaS integration."),
        ("Amazon SQS", "SQS is a queue."),
        ("Amazon SNS", "SNS is a notification service."),
        ("Amazon Kinesis Data Streams", "Kinesis is streaming."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Amazon EventBridge is a serverless event bus for application integration with rules, schedules, and SaaS events. Reference: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html",
})
QUESTIONS.append({
    "q": "Which SINGLE pattern is the BEST for fan-out to multiple downstream consumers?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon SNS topic subscribed by multiple SQS queues", "SNS fan-out to SQS is the canonical pattern."),
        ("Amazon SNS topic with Lambda subscribers", "Lambda can subscribe directly to an SNS topic."),
        ("Single SQS queue with no fan-out", "A single SQS queue is not fan-out."),
        ("Direct calls to many services in a tight loop", "Tight-loop calls couple services."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Fan-out pattern: SNS topic with multiple subscribers (SQS queues, Lambda, HTTP endpoints). Reference: https://docs.aws.amazon.com/sns/latest/dg/sns-common-scenarios.html",
})
QUESTIONS.append({
    "q": "Which SINGLE Step Functions state type runs branches concurrently?",
    "type": "multiple-choice",
    "opts": [
        ("Unlimited throughput", "Standard queues scale to nearly unlimited throughput."),
        ("At-least-once delivery", "Standard queues deliver each message at least once."),
        ("Best-effort ordering", "Standard queues do not guarantee order."),
        ("Exactly-once delivery", "Standard queues do not guarantee exactly-once; FIFO does."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "SQS Standard: unlimited throughput, at-least-once, best-effort ordering. FIFO adds exactly-once and ordering. Reference: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.html",
})
QUESTIONS.append({
    "q": "Which service captures real-time streaming data with shards, retention up to 365 days, and fan-out to multiple consumers?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Kinesis Data Streams", "Kinesis Data Streams is real-time streaming with shards and retention."),
        ("Amazon SQS", "SQS is a queue with at most 14-day retention."),
        ("Amazon SNS", "SNS is pub/sub notifications."),
        ("AWS Step Functions", "Step Functions is workflow orchestration."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Amazon Kinesis Data Streams captures real-time streaming data with shards and configurable retention. Reference: https://docs.aws.amazon.com/streams/latest/dev/introduction.html",
})
QUESTIONS.append({
    "q": "Which service is a fully managed workflow orchestrator for coordinating distributed components using state machines?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Step Functions", "Step Functions coordinates distributed components using state machines."),
        ("Amazon SQS", "SQS is a queue, not an orchestrator."),
        ("Amazon EventBridge", "EventBridge is an event bus with rules."),
        ("AWS Lambda", "Lambda is a single function execution."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "AWS Step Functions coordinates distributed components and microservices using visual workflows. Reference: https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html",
})
QUESTIONS.append({
    "q": "Which pattern BEST handles spikey, asynchronous workloads where order matters but exactly-once delivery is not required?",
    "type": "multiple-choice",
    "opts": [
        ("SQS Standard queue with Lambda consumers", "SQS Standard + Lambda scales to spikey async workloads."),
        ("Direct synchronous calls", "Sync calls do not absorb spikes."),
        ("S3 only", "S3 is storage, not a queue."),
        ("EC2 with cron", "Cron-based polling is inefficient."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "SQS Standard with Lambda is the canonical pattern for spikey async workloads. Reference: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html",
})
QUESTIONS.append({
    "q": "Which SINGLE reason is the BEST for using async messaging?",
    "type": "multiple-choice",
    "opts": [
        ("S3 event notifications to an SQS queue with a DLQ", "SQS + DLQ handles failures and retries."),
        ("S3 event notifications to SNS topic with multiple SQS subscribers", "Fan-out via SNS to multiple SQS queues."),
        ("S3 event notifications to EventBridge for advanced filtering", "EventBridge adds rules-based filtering."),
        ("Polling S3 every second from EC2", "Polling is inefficient and not the best pattern."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Use S3 event notifications with SQS, SNS fan-out, or EventBridge for decoupled, fault-tolerant processing. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html",
})
QUESTIONS.append({
    "q": "Which SINGLE combination of SQS and Lambda provides the BEST fault-tolerance?",
    "type": "multiple-choice",
    "opts": [
        ("SQS visibility timeout longer than Lambda timeout", "Visibility timeout must be longer than the Lambda timeout to prevent duplicate processing."),
        ("SQS dead-letter queue for failed messages", "DLQ captures messages that fail repeatedly."),
        ("Lambda reserved concurrency", "Reserved concurrency throttles Lambda invocations; useful but not fault-tolerance per se."),
        ("Lambda sync invocation with no DLQ", "Sync invocation without a DLQ loses failed messages."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "SQS + Lambda: visibility timeout > Lambda timeout, configure DLQ for failed messages. Reference: https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html",
})
QUESTIONS.append({
    "q": "Which SINGLE option is the BEST for SQS FIFO delivery?",
    "type": "multiple-choice",
    "opts": [
        ("Visibility timeout for in-flight messages", "Visibility timeout hides a message during processing."),
        ("Dead-letter queue for failed messages", "DLQ captures messages that fail repeatedly."),
        ("Long polling to reduce empty receives", "Long polling reduces API calls and cost."),
        ("Auto-scaling based on queue depth", "Use Lambda event source mapping to scale on queue depth."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "SQS supports visibility timeout, DLQ, long polling, and scaling via Lambda. Reference: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-short-and-long-polling.html",
})
QUESTIONS.append({
    "q": "Which service provides a serverless pub/sub pattern with message filtering at the subscription level?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon SNS with message filtering", "SNS supports subscription filter policies."),
        ("Amazon SQS", "SQS is a queue, not pub/sub with filtering."),
        ("Amazon Kinesis Data Streams", "Kinesis is streaming."),
        ("AWS Step Functions", "Step Functions is workflow orchestration."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Amazon SNS supports subscription filter policies to route only matching messages. Reference: https://docs.aws.amazon.com/sns/latest/dg/sns-message-filtering.html",
})
QUESTIONS.append({
    "q": "Which SINGLE Kinesis feature provides near-real-time sub-second latency?",
    "type": "multiple-choice",
    "opts": [
        ("Rules to filter and route events", "EventBridge rules filter and route events."),
        ("Schedules for cron-like triggers", "EventBridge Scheduler triggers on a schedule."),
        ("SaaS event integration (e.g., Zendesk, Datadog)", "EventBridge integrates with many SaaS apps."),
        ("Message ordering guarantees", "EventBridge does not guarantee order; use SQS FIFO or Kinesis."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "EventBridge supports rules, schedules, and SaaS integration but does not guarantee order. Reference: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides managed Apache Kafka with automatic scaling, patching, and integration with other AWS services?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Kinesis Data Streams", "Kinesis is a streaming service, not Kafka."),
        ("Amazon Managed Streaming for Apache Kafka (MSK)", "MSK is the managed Kafka service."),
        ("Amazon SQS", "SQS is a queue, not Kafka."),
        ("Amazon MQ", "Amazon MQ is for ActiveMQ/RabbitMQ, not Kafka."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Amazon MSK is the managed Apache Kafka service. Reference: https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html",
})
QUESTIONS.append({
    "q": "Which service is the BEST fit for a managed message broker that supports industry-standard protocols (AMQP, MQTT, STOMP) and migration from on-prem brokers?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon SQS", "SQS is AWS-native, not industry-standard protocol."),
        ("Amazon MQ", "Amazon MQ supports AMQP, MQTT, STOMP for migration."),
        ("Amazon MSK", "MSK is for Kafka, not these protocols."),
        ("Amazon SNS", "SNS is pub/sub, not a broker with these protocols."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Amazon MQ supports AMQP, MQTT, and STOMP for migration from on-prem brokers. Reference: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html",
})
QUESTIONS.append({
    "q": "Which Kinesis Data Streams feature allows you to CONSUME THE SAME STREAM by multiple applications, each tracking its own position?",
    "type": "multiple-choice",
    "opts": [
        ("Enhanced fan-out", "Enhanced fan-out provides dedicated throughput per consumer."),
        ("Multiple shards", "Shards are for parallel processing, not multiple consumer positions."),
        ("Kinesis Client Library (KCL)", "KCL tracks position per consumer."),
        ("Streams independently track position", "Each consumer tracks its own position via a checkpoint."),
    ],
    "correct": "4",
    "domain": RESILIENT,
    "overall": "Each Kinesis Data Streams consumer independently tracks its position via checkpointing, enabling multiple consumers. Reference: https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-app.html",
})
QUESTIONS.append({
    "q": "Which SINGLE Step Functions state type performs work?",
    "type": "multiple-choice",
    "opts": [
        ("Task", "Task performs work."),
        ("Choice", "Choice branches based on input."),
        ("Parallel", "Parallel runs branches concurrently."),
        ("Map", "Map iterates over input array."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Step Functions supports Task, Choice, Parallel, Map, and more state types. Reference: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-states.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed pub/sub messaging service for IoT devices, with support for MQTT, HTTP, and WebSockets?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon SNS", "SNS is general pub/sub, not optimized for IoT."),
        ("AWS IoT Core", "AWS IoT Core is the managed IoT messaging service."),
        ("Amazon MQ", "Amazon MQ supports AMQP, not IoT specifically."),
        ("Amazon SQS", "SQS is a queue."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "AWS IoT Core is the managed service for IoT messaging with MQTT, HTTP, and WebSockets. Reference: https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html",
})
QUESTIONS.append({
    "q": "Which SINGLE combination is the BEST pattern for fault-tolerant image processing?",
    "type": "multiple-choice",
    "opts": [
        ("S3 event notifications to SQS queue", "SQS decouples upload and processing."),
        ("SQS queue with Lambda consumer", "Lambda processes the message."),
        ("Direct synchronous processing in the upload request", "Synchronous processing is a coupling antipattern."),
        ("SNS topic with SQS subscribers for fan-out", "Fan-out pattern works for parallel processing."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Use S3 event notifications + SQS + Lambda, or SNS fan-out for asynchronous image processing. Reference: https://docs.aws.amazon.com/lambda/latest/dg/with-s3.html",
})
QUESTIONS.append({
    "q": "Which SQS feature provides a delay BEFORE a message is available for processing, useful for scheduling retries?",
    "type": "multiple-choice",
    "opts": [
        ("DelaySeconds", "DelaySeconds is a per-queue or per-message delay setting."),
        ("VisibilityTimeout", "VisibilityTimeout is for in-flight messages."),
        ("MessageRetentionPeriod", "MessageRetentionPeriod is the queue's retention setting."),
        ("ReceiveMessageWaitTimeSeconds", "ReceiveMessageWaitTimeSeconds is for long polling."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "DelaySeconds provides a delay before a message becomes available for processing. Reference: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-delay-queues.html",
})
QUESTIONS.append({
    "q": "Which SINGLE reason is the BEST for using async messaging?",
    "type": "multiple-choice",
    "opts": [
        ("Decouple service lifetimes", "Async messaging decouples producer and consumer."),
        ("Smooth out bursty traffic", "Queues buffer bursts."),
        ("Improve availability of the overall system", "Async removes sync dependencies."),
        ("Reduce code complexity in all cases", "Async can add complexity; it's not always simpler."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Async messaging decouples services, smooths bursts, and improves availability. Reference: https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/microservices-on-aws.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides FIFO message delivery with exactly-once processing for ordered, deduplicated messages?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon SQS Standard", "Standard does not guarantee order or exactly-once."),
        ("Amazon SQS FIFO", "FIFO provides ordering and exactly-once."),
        ("Amazon SNS", "SNS is pub/sub; FIFO topic is also available."),
        ("Amazon Kinesis Data Streams", "Kinesis provides ordering per partition key."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Amazon SQS FIFO provides FIFO ordering and exactly-once processing. Reference: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html",
})
QUESTIONS.append({
    "q": "Which SINGLE component is the AWS side of a Direct Connect connection?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Step Functions", "Step Functions coordinates multi-step workflows."),
        ("Amazon SQS for step queueing", "SQS provides reliable buffering between steps."),
        ("Lambda functions for individual steps", "Lambda implements each step."),
        ("Direct tight-loop calls between services", "Tight coupling is an antipattern."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Use Step Functions + SQS + Lambda for multi-step workflows. Reference: https://docs.aws.amazon.com/step-functions/latest/dg/concepts.html",
})
QUESTIONS.append({
    "q": "Which Kinesis Data Streams feature provides NEAR-REAL-TIME processing with sub-second latency, suitable for analytics?",
    "type": "multiple-choice",
    "opts": [
        ("Kinesis Data Streams", "Kinesis Data Streams provides sub-second real-time processing."),
        ("Kinesis Data Firehose", "Firehose is for batch delivery to S3/Redshift/OpenSearch."),
        ("SQS", "SQS is a queue, not a streaming service."),
        ("S3", "S3 is storage, not streaming."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Kinesis Data Streams provides sub-second latency real-time processing. Reference: https://docs.aws.amazon.com/streams/latest/dev/introduction.html",
})
QUESTIONS.append({
    "q": "Which SINGLE Kinesis Data Streams feature provides retention up to 365 days?",
    "type": "multiple-choice",
    "opts": [
        ("Shards for parallel processing", "Shards provide throughput and parallelism."),
        ("Retention up to 365 days", "Retention can be configured up to 365 days."),
        ("Multiple consumers per stream", "Multiple consumers can process the same stream."),
        ("Built-in message ordering across all messages", "Ordering is per partition key, not across all messages."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Kinesis Data Streams supports shards, 365-day retention, and multiple consumers. Ordering is per partition key. Reference: https://docs.aws.amazon.com/streams/latest/dev/introduction.html",
})
QUESTIONS.append({
    "q": "Which Route 53 routing policy splits traffic between two regions in a fixed ratio (e.g., 70/30) for canary or A/B testing?",
    "type": "multiple-choice",
    "opts": [
        ("Latency routing", "Latency routing picks lowest latency."),
        ("Weighted routing", "Weighted routing splits traffic by ratios."),
        ("Failover routing", "Failover is active-passive."),
        ("Geolocation routing", "Geolocation routes by user location."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Weighted routing policy routes traffic in ratios you specify; useful for canary or A/B. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html",
})
QUESTIONS.append({
    "q": "Which Route 53 routing policy routes based on the geographic location of the user (continent, country, US state)?",
    "type": "multiple-choice",
    "opts": [
        ("Geolocation routing", "Geolocation routes by user location."),
        ("Latency routing", "Latency routes by network latency."),
        ("Geoproximity routing", "Geoproximity uses bias to shift traffic."),
        ("Failover routing", "Failover is for active-passive."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Geolocation routing routes based on the user's continent, country, or US state. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geolocation.html",
})
QUESTIONS.append({
    "q": "Which Route 53 feature lets you use a percentage bias to shift traffic between regions, even to nearby regions, with traffic flow rules?",
    "type": "multiple-choice",
    "opts": [
        ("Geoproximity routing with traffic flow", "Geoproximity uses a bias to shift traffic."),
        ("Latency routing", "Latency routing is automatic based on network latency."),
        ("Weighted routing", "Weighted is for fixed ratios."),
        ("Multivalue answer routing", "Multivalue returns up to 8 healthy records."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Geoproximity routing uses a bias value to shift traffic toward or away from a region. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geoproximity.html",
})
QUESTIONS.append({
    "q": "Which Route 53 feature lets you return up to 8 healthy records in response to a single DNS query, for client-side load balancing?",
    "type": "multiple-choice",
    "opts": [
        ("Multivalue answer routing", "Multivalue returns up to 8 healthy records."),
        ("Weighted routing", "Weighted is for fixed ratios."),
        ("Failover routing", "Failover is for active-passive."),
        ("Latency routing", "Latency returns a single record."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Multivalue answer routing returns up to 8 healthy records, enabling client-side load balancing. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-multivalue.html",
})
QUESTIONS.append({
    "q": "Which service provides a logically isolated section of the AWS Cloud where you can launch resources in a defined virtual network?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon VPC", "Amazon VPC is the logically isolated virtual network."),
        ("AWS Direct Connect", "Direct Connect is a private network link."),
        ("Amazon Route 53", "Route 53 is a DNS service."),
        ("AWS Transit Gateway", "Transit Gateway connects VPCs and on-prem networks."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Amazon VPC provides a logically isolated section of the AWS Cloud for your resources. Reference: https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html",
})
QUESTIONS.append({
    "q": "Which VPC component connects a VPC to your on-premises network via an IPsec VPN tunnel over the public internet?",
    "type": "multiple-choice",
    "opts": [
        ("Internet gateway", "An internet gateway is for public internet access."),
        ("Virtual private gateway + customer gateway + VPN connection", "A VPN uses VGW on the AWS side and CGW on-prem."),
        ("AWS Direct Connect", "Direct Connect is a dedicated private fiber link."),
        ("NAT gateway", "NAT gateway is for outbound internet from private subnets."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Site-to-site VPN uses a Virtual Private Gateway on AWS and a Customer Gateway on-prem, with an IPsec tunnel over the internet. Reference: https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html",
})
QUESTIONS.append({
    "q": "Which VPC component is the AWS side of a Direct Connect connection, providing a private, dedicated link between your on-prem network and AWS?",
    "type": "multiple-choice",
    "opts": [
        ("Virtual private gateway", "VGW is for VPN; Direct Connect uses a different component."),
        ("Direct Connect gateway", "Direct Connect gateway is the AWS-side component for DX."),
        ("Customer gateway", "CGW is the on-prem side of a VPN."),
        ("Internet gateway", "IGW is for public access."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Direct Connect gateway is the AWS-side component of a Direct Connect connection. Reference: https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways.html",
})
QUESTIONS.append({
    "q": "Which service provides a NETWORK HUB that connects multiple VPCs and on-premises networks through a single gateway?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon VPC peering", "VPC peering is a 1:1 connection, not a hub."),
        ("AWS Transit Gateway", "Transit Gateway is a hub for VPCs and on-prem."),
        ("AWS PrivateLink", "PrivateLink is for service connectivity, not VPC peering."),
        ("Internet gateway", "IGW is for public access."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "AWS Transit Gateway is a network hub that connects VPCs and on-premises networks. Reference: https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html",
})
QUESTIONS.append({
    "q": "Which SINGLE benefit is the BEST description of AWS Transit Gateway?",
    "type": "multiple-choice",
    "opts": [
        ("Reduces the number of VPC peering connections", "TGW replaces many peering connections."),
        ("Centralized routing control", "TGW provides centralized route tables."),
        ("Connect to on-prem via VPN or Direct Connect", "TGW integrates with VPN and DX."),
        ("Replace Direct Connect entirely", "TGW does not replace DX; they complement."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "TGW reduces peering, centralizes routing, and integrates with VPN and DX. It does not replace DX. Reference: https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html",
})
QUESTIONS.append({
    "q": "Which SINGLE service is the BEST hub for a hybrid cloud?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Transit Gateway as the central hub", "TGW is the hub for VPCs and on-prem."),
        ("AWS Direct Connect for private connectivity", "DX provides dedicated private connectivity."),
        ("Site-to-Site VPN as backup", "VPN is a lower-cost backup to DX."),
        ("Multiple VPC peering connections", "Many peering connections are hard to manage; TGW is better."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Use TGW as hub, DX for primary, VPN as backup, and avoid many peering connections. Reference: https://docs.aws.amazon.com/vpc/latest/tgw/tgw-getting-started.html",
})
QUESTIONS.append({
    "q": "Which service provides a centralized, automated backup solution across AWS services (EBS, RDS, DynamoDB, EFS, FSx) with policy-based retention?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Backup", "AWS Backup is the centralized backup service across many AWS resources."),
        ("Amazon CloudWatch", "CloudWatch is monitoring."),
        ("AWS Systems Manager", "SSM is for ops items."),
        ("AWS Config", "Config tracks configuration."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "AWS Backup centralizes and automates backup across services with policies and retention. Reference: https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html",
})
QUESTIONS.append({
    "q": "Which SINGLE option is a valid RDS backup option?",
    "type": "multiple-choice",
    "opts": [
        ("Automated daily backups with point-in-time recovery", "Automated backups are enabled by default."),
        ("Manual DB snapshots", "Manual snapshots persist until explicitly deleted."),
        ("Cross-region snapshot copy", "You can copy snapshots to other regions for DR."),
        ("Continuous replication to S3", "RDS does not continuously replicate to S3; that's Aurora Backtrack for some Aurora engines."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "RDS supports automated backups, manual snapshots, and cross-region snapshot copy. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html",
})
QUESTIONS.append({
    "q": "Which Amazon CloudWatch feature provides a single dashboard with metrics from multiple AWS accounts and regions?",
    "type": "multiple-choice",
    "opts": [
        ("CloudWatch cross-account cross-region dashboards", "CloudWatch supports cross-account and cross-region dashboards."),
        ("AWS Organizations alone", "Organizations is for account management."),
        ("AWS Config alone", "Config is for configuration."),
        ("AWS Systems Manager alone", "SSM is for ops items."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "CloudWatch cross-account cross-region dashboards aggregate metrics into a single dashboard. Reference: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html",
})
QUESTIONS.append({
    "q": "Which AWS service aggregates logs from multiple accounts and regions for centralized analysis?",
    "type": "multiple-choice",
    "opts": [
        ("CloudWatch Logs with cross-account subscriptions", "CloudWatch Logs subscriptions deliver to a central account."),
        ("AWS Config", "Config is for resource configuration."),
        ("AWS CloudTrail alone", "CloudTrail is a log source, not a log aggregator."),
        ("AWS Trusted Advisor", "Trusted Advisor is for best-practice checks."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "CloudWatch Logs subscriptions can deliver logs to a central account for aggregation and analysis. Reference: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions.html",
})
QUESTIONS.append({
    "q": "Which service is the AWS-native implementation of the Well-Architected Framework's Reliability Pillar?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Well-Architected Tool", "The AWS Well-Architected Tool reviews workloads against the framework."),
        ("AWS Trusted Advisor", "Trusted Advisor provides best-practice checks."),
        ("AWS Config only", "Config is for configuration compliance."),
        ("AWS Service Catalog", "Service Catalog is for IT service governance."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "The AWS Well-Architected Tool helps you review workloads against the framework, including the Reliability Pillar. Reference: https://docs.aws.amazon.com/wellarchitected/latest/userguide/intro.html",
})
QUESTIONS.append({
    "q": "Which of the following are key design principles of the Reliability Pillar? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Automatically recover from failure", "Automated recovery is a reliability principle."),
        ("Test recovery procedures", "Regular recovery testing is essential."),
        ("Scale horizontally to improve availability", "Horizontal scaling is a reliability pattern."),
        ("Manage change via automation", "Automation reduces manual error."),
    ],
    "correct": "1,2,3,4",
    "domain": RESILIENT,
    "overall": "Reliability Pillar principles include automated recovery, testing, horizontal scaling, and change management via automation. Reference: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/reliability-pillar.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides infrastructure-as-code templates to define and provision AWS resources in a repeatable way?",
    "type": "multiple-choice",
    "opts": [
        ("AWS CloudFormation", "CloudFormation is the AWS-native IaC service."),
        ("AWS Systems Manager", "SSM is for ops items."),
        ("AWS Config", "Config tracks configuration."),
        ("AWS CodeDeploy", "CodeDeploy is for application deployments."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "AWS CloudFormation defines AWS resources in JSON/YAML templates for repeatable, version-controlled provisioning. Reference: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html",
})
QUESTIONS.append({
    "q": "Which service is a regional, low-latency, fully managed in-memory key-value store supporting Redis and Memcached?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon DynamoDB", "DynamoDB is a NoSQL database, not in-memory cache."),
        ("Amazon ElastiCache", "ElastiCache is the managed Redis and Memcached service."),
        ("Amazon MemoryDB", "MemoryDB is a Redis-compatible durable in-memory database."),
        ("AWS Cloud Map", "Cloud Map is a service discovery service."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Amazon ElastiCache is the managed in-memory key-value store supporting Redis and Memcached. Reference: https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html",
})
QUESTIONS.append({
    "q": "Which service complements ElastiCache by providing an in-memory cache specifically for DynamoDB to reduce read latency from milliseconds to microseconds?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon CloudFront", "CloudFront is a CDN, not a DynamoDB cache."),
        ("Amazon DynamoDB Accelerator (DAX)", "DAX is the in-memory cache for DynamoDB."),
        ("Amazon ElastiCache", "ElastiCache is general-purpose, not DynamoDB-specific."),
        ("AWS PrivateLink", "PrivateLink is for private connectivity."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "DynamoDB Accelerator (DAX) is the in-memory cache for DynamoDB, reducing read latency from ms to µs. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid ELB health check configurations? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Health check protocol (HTTP, HTTPS, TCP)", "Health checks support multiple protocols."),
        ("Health check path (e.g., /health)", "HTTP/HTTPS checks use a path."),
        ("Healthy and unhealthy thresholds", "Thresholds determine when an instance is marked healthy/unhealthy."),
        ("Health check interval and timeout", "Interval and timeout control check frequency and tolerance."),
    ],
    "correct": "1,2,3,4",
    "domain": RESILIENT,
    "overall": "ELB health checks support multiple protocols, paths, thresholds, and intervals. Reference: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html",
})
QUESTIONS.append({
    "q": "Which service provides a managed, cross-region, cross-account DNS firewall with domain whitelisting and threat intelligence?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Route 53 Resolver DNS Firewall", "Route 53 DNS Firewall is the managed DNS firewall."),
        ("AWS WAF", "WAF is for HTTP/HTTPS, not DNS."),
        ("AWS Network Firewall", "Network Firewall is for IP traffic, not DNS-specific."),
        ("AWS Shield", "Shield is for DDoS protection."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Route 53 Resolver DNS Firewall provides a managed DNS firewall with domain lists. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html",
})
QUESTIONS.append({
    "q": "Which service provides an automated, centralized way to manage DNS records for services running in AWS?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cloud Map", "Cloud Map is a managed service discovery for resources."),
        ("Amazon Route 53", "Route 53 is DNS-as-a-Service."),
        ("AWS App Mesh", "App Mesh is a service mesh."),
        ("AWS Transit Gateway", "Transit Gateway is a network hub."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "AWS Cloud Map is the managed service discovery service for dynamic resources. Reference: https://docs.aws.amazon.com/cloud-map/latest/dg/what-is-cloud-map.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed, scalable, time-series database optimized for monitoring and observability?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Timestream", "Timestream is the managed time-series database."),
        ("Amazon CloudWatch Logs", "CloudWatch Logs is a log service, not a time-series DB."),
        ("Amazon DynamoDB", "DynamoDB is a key-value NoSQL database."),
        ("Amazon Aurora", "Aurora is a relational database."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Amazon Timestream is the managed time-series database for monitoring and observability. Reference: https://docs.aws.amazon.com/timestream/latest/developerguide/what-is-timestream.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides managed Grafana dashboards for observability, with integration to CloudWatch, Prometheus, and other data sources?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Managed Grafana", "Amazon Managed Grafana is the managed Grafana service."),
        ("Amazon CloudWatch Dashboards", "CloudWatch Dashboards are a different format."),
        ("AWS X-Ray", "X-Ray is for distributed tracing."),
        ("Amazon QuickSight", "QuickSight is for business intelligence."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Amazon Managed Grafana is the managed Grafana service with integration to many data sources. Reference: https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides distributed tracing for analyzing and debugging microservices?",
    "type": "multiple-choice",
    "opts": [
        ("AWS X-Ray", "X-Ray is the AWS distributed tracing service."),
        ("Amazon CloudWatch", "CloudWatch is metrics and logs."),
        ("AWS Config", "Config is for configuration."),
        ("AWS CloudTrail", "CloudTrail is for API audit."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "AWS X-Ray provides distributed tracing for microservices analysis. Reference: https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides centralized backup across AWS services (EBS, RDS, DynamoDB, EFS) with policy-based retention?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Backup", "AWS Backup is the centralized backup service across many AWS resources."),
        ("Amazon CloudWatch", "CloudWatch is monitoring."),
        ("AWS Systems Manager", "SSM is for ops items."),
        ("AWS Config", "Config tracks configuration."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "AWS Backup centralizes and automates backup across services with policies and retention. Reference: https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid components of an AWS Backup plan? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Backup rule with schedule", "Backup rules define when backups run."),
        ("Backup vault for storage", "Backup vaults store backups."),
        ("Lifecycle policy for transitioning to cold storage", "Lifecycle moves backups to cold storage."),
        ("Cross-region copy", "AWS Backup supports cross-region copy for DR."),
    ],
    "correct": "1,2,3,4",
    "domain": RESILIENT,
    "overall": "AWS Backup plans include rules, vaults, lifecycle, and cross-region copy. Reference: https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html",
})
QUESTIONS.append({
    "q": "Which EBS snapshot feature allows you to copy snapshots to another region for DR?",
    "type": "multiple-choice",
    "opts": [
        ("EBS snapshot copy across regions", "EBS supports cross-region snapshot copy."),
        ("EBS snapshot export to S3", "Snapshot export is to S3, not to another region."),
        ("EBS encryption", "Encryption is unrelated to copy."),
        ("EBS Fast Snapshot Restore", "FSR is for fast restore, not cross-region."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "EBS snapshot copy across regions enables cross-region DR. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-copy-snapshot.html",
})
QUESTIONS.append({
    "q": "Which S3 replication option replicates objects within the same region?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Cross-Region Replication (CRR)", "CRR is cross-region."),
        ("S3 Same-Region Replication (SRR)", "SRR replicates within the same region."),
        ("S3 Batch Replication", "Batch Replication is for existing objects."),
        ("S3 Live Replication", "Not a real feature."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "S3 Same-Region Replication (SRR) replicates objects within the same region. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html",
})
QUESTIONS.append({
    "q": "Which combination of features provides the BEST data protection for S3 objects? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Versioning", "Versioning protects against accidental delete/overwrite."),
        ("Cross-region replication", "CRR provides cross-region durability."),
        ("Object Lock", "Object Lock provides immutability for WORM."),
        ("Public access", "Public access is an antipattern for sensitive data."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "Use Versioning + CRR + Object Lock for S3 data protection. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/data-protection.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid S3 storage classes for backup and archive with appropriate retrieval options? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("S3 Glacier Instant Retrieval", "Millisecond retrieval for archive."),
        ("S3 Glacier Flexible Retrieval", "Minutes-to-hours retrieval for archive."),
        ("S3 Glacier Deep Archive", "Hours retrieval for long-term archive."),
        ("S3 Standard only", "Standard is for frequent access, not archive."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "Glacier Instant Retrieval, Flexible Retrieval, and Deep Archive are the archive classes. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html",
})
QUESTIONS.append({
    "q": "Which S3 lifecycle configuration should be used to TRANSITION objects to a colder storage class after 90 days and DELETE them after 365 days?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Lifecycle policy with transition and expiration rules", "Lifecycle rules include transition and expiration."),
        ("S3 Replication", "Replication is for copying to another bucket."),
        ("S3 Inventory", "Inventory is a listing report."),
        ("S3 Object Lock", "Object Lock is for immutability."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "S3 Lifecycle rules transition objects to other storage classes and expire them. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid components of an EFS backup strategy? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS Backup with EFS support", "AWS Backup supports EFS."),
        ("EFS-to-EFS replication cross-region", "EFS replication provides cross-region durability."),
        ("EFS IA storage class for infrequent access", "EFS IA reduces cost for infrequent access."),
        ("EFS public access", "EFS is private; public access is not a thing."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "Use AWS Backup, EFS replication, and EFS IA for EFS backup strategy. Reference: https://docs.aws.amazon.com/efs/latest/ug/backup-and-restore.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides point-in-time recovery for DynamoDB tables, with continuous backups and 35-day retention?",
    "type": "multiple-choice",
    "opts": [
        ("DynamoDB on-demand backups", "On-demand backups are user-initiated, not continuous."),
        ("DynamoDB point-in-time recovery (PITR)", "PITR provides continuous backups with 35-day retention."),
        ("DynamoDB Streams", "Streams are change-data capture."),
        ("DynamoDB Global Tables", "Global Tables are for cross-region replication."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "DynamoDB PITR provides continuous backups with 35-day retention for point-in-time recovery. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.html",
})
QUESTIONS.append({
    "q": "Which Aurora feature provides in-place time-travel within a cluster, useful for recovering from accidental writes?",
    "type": "multiple-choice",
    "opts": [
        ("Aurora Backtrack", "Aurora Backtrack rewinds the cluster to a previous point in time."),
        ("Aurora Global Database", "Global Database is for cross-region replication."),
        ("Aurora read replica", "Read replicas scale reads."),
        ("Aurora Multi-Master", "Multi-Master is multi-writer within a region."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Aurora Backtrack rewinds the cluster to a previous point in time without restoring from a backup. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Backtrack.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid Aurora failover targets? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("An Aurora read replica in the same cluster", "Aurora fails over to a read replica in the cluster."),
        ("A new instance created automatically", "Aurora can create a new instance if no replica is available."),
        ("A different region's read replica", "Cross-region failover uses Global Database."),
        ("A separate standalone RDS instance", "Failover to a separate RDS instance is not Aurora's pattern."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "Aurora fails over to a read replica in the cluster or creates a new one; cross-region uses Global Database. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html",
})
QUESTIONS.append({
    "q": "Which RDS feature provides automatic failover for Aurora MySQL/PostgreSQL in under 30 seconds?",
    "type": "multiple-choice",
    "opts": [
        ("RDS Multi-AZ", "Multi-AZ is for RDS, not Aurora; Aurora has its own failover."),
        ("Aurora failover with read replicas", "Aurora failover with replicas is sub-30-second."),
        ("RDS Proxy", "RDS Proxy is a connection pooler."),
        ("RDS read replica", "Read replicas scale reads."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Aurora failover to a read replica is typically under 30 seconds. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid options for protecting EBS volumes from accidental deletion? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Enable EBS snapshots for backup", "Snapshots protect data."),
        ("Use termination protection on the EC2 instance", "Termination protection prevents EC2 termination."),
        ("Use EBS encryption", "Encryption protects data at rest, not deletion."),
        ("Disable EBS Delete on Termination", "DelOnTerm=false preserves the volume after EC2 termination."),
    ],
    "correct": "1,2,4",
    "domain": RESILIENT,
    "overall": "Use snapshots, EC2 termination protection, and disable Delete on Termination to protect EBS volumes. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-deleting-volume.html",
})
QUESTIONS.append({
    "q": "Which S3 Versioning feature provides the ability to recover a previous version of an object after it has been overwritten or deleted?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Lifecycle", "Lifecycle is for storage class and expiration."),
        ("S3 Versioning", "Versioning keeps multiple object versions."),
        ("S3 Object Lock", "Object Lock is for immutability."),
        ("S3 Replication", "Replication is for cross-bucket copy."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "S3 Versioning keeps multiple object versions, enabling recovery from overwrites or deletes. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid ways to protect against accidental deletion of an S3 bucket? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Enable MFA delete on the bucket", "MFA delete requires MFA to delete objects or the bucket."),
        ("Use a bucket policy with a Deny on s3:DeleteBucket", "Bucket policy with Deny prevents unauthorized deletion."),
        ("Use S3 Versioning with delete marker protection", "Versioning protects against overwrite; MFA delete protects against delete."),
        ("Share root user credentials with all developers", "Sharing root credentials is a critical security antipattern."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "Use MFA delete, bucket policy Deny, and Versioning to protect against accidental deletion. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid DynamoDB backup and recovery options? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("On-demand backups", "On-demand backups are user-initiated full backups."),
        ("Point-in-time recovery (PITR)", "PITR provides continuous backups with 35-day retention."),
        ("DynamoDB Streams for change-data capture", "Streams are for change-data capture, not backup."),
        ("AWS Backup with DynamoDB support", "AWS Backup supports DynamoDB."),
    ],
    "correct": "1,2,4",
    "domain": RESILIENT,
    "overall": "DynamoDB supports on-demand backups, PITR, and AWS Backup. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BackupAndRestore.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides CROSS-REGION replication for FSx for Windows File Server?",
    "type": "multiple-choice",
    "opts": [
        ("FSx Multi-AZ", "Multi-AZ is single-region."),
        ("FSx Single-AZ", "Single-AZ is single-region."),
        ("FSx DR using Windows DFS Replication or AWS DataSync", "DFS Replication or DataSync provides cross-region DR for FSx."),
        ("FSx does not support cross-region", "FSx supports cross-region via DFS Replication or DataSync."),
    ],
    "correct": "3",
    "domain": RESILIENT,
    "overall": "FSx for Windows File Server cross-region DR uses DFS Replication or AWS DataSync. Reference: https://docs.aws.amazon.com/fsx/latest/WindowsGuide/disaster-recovery.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid AWS DataSync use cases? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Migrate on-prem NFS to Amazon EFS", "DataSync supports NFS to EFS migration."),
        ("Replicate data between FSx file systems", "DataSync replicates between FSx systems."),
        ("Migrate S3 to on-prem storage", "DataSync supports S3 to on-prem and vice versa."),
        ("Stream real-time clickstream data", "DataSync is for batch data transfer, not real-time streaming."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "DataSync migrates on-prem storage to AWS and between AWS services. Reference: https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html",
})
QUESTIONS.append({
    "q": "Which service provides an automated, online data transfer service for moving large datasets (hundreds of TB) to AWS?",
    "type": "multiple-choice",
    "opts": [
        ("AWS DataSync", "DataSync is for online transfer of moderate volumes."),
        ("AWS Snowball", "Snowball is for offline transfer of large volumes."),
        ("AWS Transfer Family", "Transfer Family is for SFTP/FTPS/FTP file transfers."),
        ("AWS Storage Gateway", "Storage Gateway is for hybrid storage integration."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "AWS Snowball provides offline transfer for very large datasets. Reference: https://docs.aws.amazon.com/snowball/latest/developer-guide/what-is-snowball.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid AWS Storage Gateway types? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("File Gateway (NFS/SMB)", "File Gateway presents NFS/SMB backed by S3."),
        ("Volume Gateway (iSCSI)", "Volume Gateway provides iSCSI block storage backed by S3."),
        ("Tape Gateway (VTL)", "Tape Gateway presents a virtual tape library backed by S3 Glacier."),
        ("Object Gateway (S3-compatible)", "Storage Gateway does not have an Object Gateway type."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "Storage Gateway has File Gateway, Volume Gateway, and Tape Gateway types. Reference: https://docs.aws.amazon.com/storagegateway/latest/userguide/WhatIsStorageGateway.html",
})
QUESTIONS.append({
    "q": "In the Streamify scenario, Streamify needs to ingest 50,000+ concurrent live video streams and run real-time computer-vision analytics at 5 FPS per stream. Which combination of AWS services is the BEST fit? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon Kinesis Data Streams for ingestion", "Kinesis Data Streams ingests high-throughput streaming data."),
        ("Amazon EC2 GPU instances for inference", "GPU instances run CV inference at scale."),
        ("AWS Lambda alone for inference", "Lambda is not optimized for sustained GPU inference."),
        ("S3 Glacier for raw video storage", "Glacier has hours retrieval; not for hot video."),
    ],
    "correct": "1,2",
    "domain": RESILIENT,
    "overall": "Use Kinesis Data Streams for ingestion and GPU EC2 for inference. Lambda is not optimized for sustained GPU. Reference: https://docs.aws.amazon.com/streams/latest/dev/introduction.html",
})
QUESTIONS.append({
    "q": "In the Streamify scenario, Streamify wants to autoscale inference workers based on the depth of the queue to handle 50x spikes. Which combination of services is the BEST fit? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon SQS as the buffer between ingestion and inference", "SQS buffers and triggers auto-scaling."),
        ("Auto Scaling group with target tracking on SQS ApproximateNumberOfMessagesVisible", "ASG scales on queue depth."),
        ("Lambda with provisioned concurrency", "Lambda does not auto-scale on SQS depth the same way."),
        ("Manual scaling only", "Manual scaling does not handle 50x spikes."),
    ],
    "correct": "1,2",
    "domain": RESILIENT,
    "overall": "Use SQS + ASG target tracking on SQS depth to autoscale inference workers. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html",
})
QUESTIONS.append({
    "q": "In the Streamify scenario, Streamify wants to run the GPU inference cost-effectively for the highly spiky workload. Which EC2 pricing model is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("On-Demand", "On-Demand is the most expensive for sustained workloads."),
        ("Reserved Instances", "Reserved Instances require commitment; not ideal for spiky."),
        ("Spot Instances for inference workers", "Spot offers up to 90% discount; fault-tolerant for batch inference."),
        ("Dedicated Hosts", "Dedicated Hosts are most expensive."),
    ],
    "correct": "3",
    "domain": RESILIENT,
    "overall": "Spot Instances are ideal for fault-tolerant, cost-effective spiky workloads like inference. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html",
})
QUESTIONS.append({
    "q": "In the Streamify scenario, Streamify needs raw video to be replayed for re-processing up to 30 days after capture. Which S3 storage class is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Glacier Deep Archive", "Glacier Deep Archive has hours retrieval, too slow for 30-day replay."),
        ("S3 Standard", "Standard is fast but expensive for large volumes."),
        ("S3 Standard-IA with Lifecycle transition from Standard after 30 days", "Standard for the 30-day hot window; transition to IA after."),
        ("S3 One Zone-IA", "One Zone-IA is for data that can be lost; not appropriate."),
    ],
    "correct": "3",
    "domain": RESILIENT,
    "overall": "Use S3 Standard for the 30-day hot window and Lifecycle transition to Standard-IA after. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html",
})
QUESTIONS.append({
    "q": "In the Streamify scenario, Streamify wants aggregate metrics to be retained for 2 years for analytics. Which combination of S3 storage classes is the BEST fit? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("S3 Standard for the first 90 days", "Standard for hot analytics."),
        ("S3 Standard-IA after 90 days", "IA for occasional analytics queries."),
        ("S3 Glacier after 365 days", "Glacier for long-term archive."),
        ("S3 One Zone-IA", "One Zone-IA is for data that can be lost; not for 2-year metrics."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "Use a Lifecycle policy: Standard 0-90d, Standard-IA 90-365d, Glacier 365d+. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html",
})
QUESTIONS.append({
    "q": "In the Streamify scenario, Streamify wants the aggregate metrics to reach the sponsor dashboard within 10 seconds of the video frame. Which combination of services is the BEST fit? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon Kinesis Data Streams with sub-second latency", "Kinesis provides sub-second real-time processing."),
        ("AWS Lambda to compute and push metrics", "Lambda runs the aggregation and pushes to the dashboard."),
        ("S3 Glacier for the metrics store", "Glacier is too slow for 10-second latency."),
        ("Amazon Aurora for the metrics store", "Aurora is fast but not the lowest-latency option for 10s."),
    ],
    "correct": "1,2",
    "domain": RESILIENT,
    "overall": "Use Kinesis + Lambda for sub-10-second metrics pipeline. Reference: https://docs.aws.amazon.com/streams/latest/dev/introduction.html",
})
QUESTIONS.append({
    "q": "In the Streamify scenario, Streamify wants to use S3 Intelligent-Tiering for the raw video bucket to automatically optimize storage costs. Which is TRUE about Intelligent-Tiering?",
    "type": "multiple-choice",
    "opts": [
        ("There are no retrieval charges", "Intelligent-Tiering has no retrieval charges, only monitoring fees."),
        ("It moves objects between access tiers based on usage", "Intelligent-Tiering automatically moves objects."),
        ("It is the lowest-cost storage class", "Glacier Deep Archive is the lowest cost; Intelligent-Tiering optimizes across tiers."),
        ("It does not support S3 Lifecycle", "Intelligent-Tiering can be combined with Lifecycle policies."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "S3 Intelligent-Tiering has no retrieval charges, only per-object monitoring fees. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html",
})
QUESTIONS.append({
    "q": "In the Streamify scenario, Streamify wants to use CloudFront to deliver the dashboard to global brand sponsors with low latency. Which feature of CloudFront reduces origin load?",
    "type": "multiple-choice",
    "opts": [
        ("CloudFront Origin Shield", "Origin Shield adds an extra caching layer."),
        ("CloudFront signed URLs", "Signed URLs are for private content, not caching."),
        ("CloudFront Lambda@Edge", "Lambda@Edge is for code at the edge."),
        ("CloudFront OAI", "OAI restricts S3 origin access."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "CloudFront Origin Shield is an additional caching layer that reduces origin load. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html",
})
QUESTIONS.append({
    "q": "In the Streamify scenario, Streamify wants to replicate raw video to a second region for DR. Which S3 feature is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Cross-Region Replication", "CRR is the standard for cross-region DR."),
        ("S3 Same-Region Replication", "SRR is same-region, not DR."),
        ("S3 Batch Operations", "Batch is for one-time operations."),
        ("S3 Object Lock", "Object Lock is for immutability."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "S3 Cross-Region Replication (CRR) replicates objects to a destination bucket in a different region for DR. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html",
})
QUESTIONS.append({
    "q": "In the Streamify scenario, Streamify wants to ingest video from on-premises data centers to AWS. Which AWS service provides an online, automated data transfer for large volumes?",
    "type": "multiple-choice",
    "opts": [
        ("AWS DataSync", "DataSync is for online automated data transfer."),
        ("AWS Snowball", "Snowball is for offline physical transfer."),
        ("S3 only", "S3 is the destination, not the transfer mechanism."),
        ("AWS Direct Connect only", "DX is a private link, not a transfer service."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "AWS DataSync provides online, automated data transfer for large volumes. Reference: https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html",
})
QUESTIONS.append({
    "q": "In the Streamify scenario, Streamify wants to use Route 53 latency-based routing to direct brand sponsors to the lowest-latency dashboard endpoint. Which is TRUE about latency-based routing?",
    "type": "multiple-choice",
    "opts": [
        ("It uses a single region for all users", "Latency routing is for multi-region."),
        ("It measures latency over time and routes to the lowest-latency region", "Latency routing is based on measured latency."),
        ("It always prefers the primary region", "Latency routing is not failover-based."),
        ("It only works for HTTP", "Latency routing works for any health-checked endpoint."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "Route 53 latency-based routing measures latency over time and routes to the lowest-latency region. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html",
})
QUESTIONS.append({
    "q": "In the Streamify scenario, Streamify wants to monitor pipeline health, including ingestion rate, queue depth, and inference latency. Which combination of services is the BEST fit? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon CloudWatch metrics for pipeline components", "CloudWatch collects metrics for pipeline components."),
        ("CloudWatch alarms for thresholds", "CloudWatch alarms notify on threshold breaches."),
        ("AWS X-Ray for distributed tracing", "X-Ray traces requests across services."),
        ("AWS Config for metrics", "Config tracks configuration, not metrics."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "Use CloudWatch metrics, alarms, and X-Ray for pipeline monitoring. Reference: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html",
})
QUESTIONS.append({
    "q": "In the Streamify scenario, Streamify wants to use AWS Backup to protect the DynamoDB tables that store the aggregate metrics. Which is the BEST feature for point-in-time recovery of DynamoDB?",
    "type": "multiple-choice",
    "opts": [
        ("DynamoDB on-demand backups only", "On-demand backups are not continuous."),
        ("DynamoDB point-in-time recovery (PITR)", "PITR provides continuous backup with 35-day retention."),
        ("DynamoDB Streams", "Streams are for change-data capture."),
        ("AWS Backup for DynamoDB only", "AWS Backup supports DynamoDB but PITR is more granular."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "DynamoDB PITR provides continuous backup with 35-day retention for point-in-time recovery. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.html",
})
QUESTIONS.append({
    "q": "In the Streamify scenario, Streamify wants to use Step Functions to orchestrate the inference workflow. Which is TRUE about Step Functions?",
    "type": "multiple-choice",
    "opts": [
        ("It coordinates distributed components with visual workflows", "Step Functions coordinates with state machines."),
        ("It is a queueing service", "Step Functions is a workflow orchestrator, not a queue."),
        ("It only works with Lambda", "Step Functions can coordinate many AWS services."),
        ("It is for batch only", "Step Functions can be used for real-time workflows too."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Step Functions coordinates distributed components and microservices using visual workflows. Reference: https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html",
})
QUESTIONS.append({
    "q": "In the Streamify scenario, Streamify wants to use EventBridge to trigger the inference pipeline when new video chunks arrive. Which is TRUE about EventBridge?",
    "type": "multiple-choice",
    "opts": [
        ("It is a queue with FIFO support", "EventBridge is an event bus, not a queue."),
        ("It is a serverless event bus with rules and SaaS integration", "EventBridge is a serverless event bus."),
        ("It guarantees message ordering", "EventBridge does not guarantee ordering; use SQS FIFO."),
        ("It replaces CloudWatch Events", "EventBridge supersedes CloudWatch Events; they are the same service."),
    ],
    "correct": "4",
    "domain": RESILIENT,
    "overall": "EventBridge is the evolution of CloudWatch Events. They are the same service. Reference: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html",
})
QUESTIONS.append({
    "q": "In the Streamify scenario, Streamify wants to use Global Accelerator to provide a global anycast endpoint for the dashboard. Which is TRUE about Global Accelerator?",
    "type": "multiple-choice",
    "opts": [
        ("It is a CDN", "Global Accelerator is not a CDN; CloudFront is."),
        ("It provides static anycast IPs and instant regional failover", "Global Accelerator is a global anycast endpoint with failover."),
        ("It is for HTTP only", "Global Accelerator supports TCP and UDP, not just HTTP."),
        ("It requires Direct Connect", "Global Accelerator does not require DX."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "AWS Global Accelerator provides static anycast IPs with instant regional failover. Reference: https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html",
})
QUESTIONS.append({
    "q": "In the Streamify scenario, Streamify wants to monitor the end-to-end pipeline health and detect anomalies in the inference latency. Which AWS service provides ML-based anomaly detection on metrics?",
    "type": "multiple-choice",
    "opts": [
        ("CloudWatch Anomaly Detection", "CloudWatch Anomaly Detection uses ML to detect anomalies."),
        ("CloudTrail Insights", "CloudTrail Insights is for API call anomalies."),
        ("AWS Config", "Config is for configuration."),
        ("AWS Trusted Advisor", "Trusted Advisor is for best-practice checks."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "CloudWatch Anomaly Detection uses ML to detect anomalies in metrics. Reference: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html",
})
QUESTIONS.append({
    "q": "In the Streamify scenario, Streamify wants to use AWS WAF to protect the dashboard from web exploits. Which combination of WAF features is the BEST fit? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS managed rule groups for OWASP Top 10", "Managed rule groups cover OWASP Top 10."),
        ("Rate-based rules to throttle abusive clients", "Rate-based rules limit requests per IP."),
        ("Disable logging to improve performance", "Disabling logging is a security antipattern."),
        ("Allow all traffic by default", "Allow all is a security antipattern."),
    ],
    "correct": "1,2",
    "domain": RESILIENT,
    "overall": "Use managed rule groups and rate-based rules for WAF. Disabling logging and allow-all are antipatterns. Reference: https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html",
})
QUESTIONS.append({
    "q": "In the Streamify scenario, Streamify wants to use AWS FIS to inject faults into the inference pipeline and test resilience. Which is TRUE about AWS FIS?",
    "type": "multiple-choice",
    "opts": [
        ("It is for security testing only", "FIS is for chaos engineering, not security testing."),
        ("It injects controlled faults to test resilience", "FIS injects controlled faults for resilience testing."),
        ("It replaces CloudWatch", "FIS complements CloudWatch."),
        ("It is a paid service", "FIS is a paid service."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "AWS FIS injects controlled faults for chaos engineering and resilience testing. Reference: https://docs.aws.amazon.com/fis/latest/userguide/what-is.html",
})
QUESTIONS.append({
    "q": "In the Streamify scenario, Streamify wants to use S3 Multi-Region Access Points for the raw video bucket to provide automatic failover. Which is TRUE about Multi-Region Access Points?",
    "type": "multiple-choice",
    "opts": [
        ("They are for compute, not storage", "Multi-Region Access Points are for S3."),
        ("They provide a global endpoint with automatic failover across regions", "Multi-Region Access Points provide a global endpoint with failover."),
        ("They require manual failover", "Multi-Region Access Points provide automatic failover."),
        ("They replace CloudFront", "Multi-Region Access Points and CloudFront complement each other."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "S3 Multi-Region Access Points provide a global endpoint with automatic failover across regions. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPoints.html",
})
QUESTIONS.append({
    "q": "Which ASG feature provides rolling updates to a new instance configuration with minimum healthy instances during the update?",
    "type": "multiple-choice",
    "opts": [
        ("Instance refresh", "Instance refresh replaces instances with the latest template."),
        ("Health check replacement", "Health check replacement is for unhealthy instances."),
        ("Termination protection", "Termination protection prevents termination."),
        ("Lifecycle hooks", "Lifecycle hooks pause actions during state changes."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "ASG instance refresh replaces instances with the latest launch template in a rolling manner. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-refresh.html",
})
QUESTIONS.append({
    "q": "Which RDS Multi-AZ deployment option uses TWO standby replicas in different AZs for higher availability?",
    "type": "multiple-choice",
    "opts": [
        ("Multi-AZ (single standby)", "Multi-AZ has one standby in another AZ."),
        ("Multi-AZ DB cluster (two standbys)", "Multi-AZ DB cluster has two standbys in different AZs for higher HA."),
        ("Read replicas", "Read replicas are async, not Multi-AZ."),
        ("Aurora only", "Aurora has its own 6-way replication; RDS Multi-AZ cluster is separate."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "RDS Multi-AZ DB cluster has two standbys in different AZs for higher availability. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html",
})
QUESTIONS.append({
    "q": "Which ALB feature distributes traffic across multiple target groups based on the URL path?",
    "type": "multiple-choice",
    "opts": [
        ("Listener rules", "Listener rules route based on path, host, headers."),
        ("Target groups", "Target groups are collections of targets."),
        ("Health checks", "Health checks determine target health."),
        ("Sticky sessions", "Sticky sessions bind user to instance."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "ALB listener rules route traffic based on path, host, headers, and other conditions. Reference: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-update-rules.html",
})
QUESTIONS.append({
    "q": "Which NLB feature preserves the client source IP for the backend without requiring X-Forwarded-For?",
    "type": "multiple-choice",
    "opts": [
        ("NLB preserves client IP by default", "NLB preserves the client IP by default at L4."),
        ("X-Forwarded-For header", "NLB does not use XFF; that's ALB."),
        ("Sticky sessions", "Sticky sessions are for session affinity, not source IP."),
        ("TLS termination", "TLS termination is unrelated to source IP."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "NLB preserves the client source IP by default at L4, unlike ALB which uses XFF. Reference: https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html",
})
QUESTIONS.append({
    "q": "Which ASG termination policy protects instances marked as protected from scale-in termination?",
    "type": "multiple-choice",
    "opts": [
        ("Instance scale-in protection", "Instance scale-in protection prevents ASG from terminating the instance during scale-in."),
        ("Termination protection", "Termination protection is a separate EC2 API to prevent accidental termination."),
        ("Lifecycle hooks", "Lifecycle hooks pause actions during state changes."),
        ("Health check grace period", "Grace period is for health check timing."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "ASG instance scale-in protection prevents ASG from terminating protected instances during scale-in. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html#instance-protection",
})
QUESTIONS.append({
    "q": "Which ALB feature limits the number of requests per target to prevent any single target from being overwhelmed?",
    "type": "multiple-choice",
    "opts": [
        ("Target group request threshold", "ALB can be configured with target group request thresholds."),
        ("Health checks", "Health checks are for target health."),
        ("Sticky sessions", "Sticky sessions are for session affinity."),
        ("Cross-zone load balancing", "Cross-zone is for traffic distribution."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "ALB and NLB support per-target request limits to protect individual targets. Reference: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html",
})
QUESTIONS.append({
    "q": "Which RDS feature enables connection pooling and failover with sub-second latency, reducing database connection overhead?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon RDS Proxy", "RDS Proxy is a managed connection pooler with failover."),
        ("RDS Multi-AZ", "Multi-AZ is for HA, not connection pooling."),
        ("RDS read replicas", "Read replicas are for read scaling."),
        ("RDS Storage Auto Scaling", "Storage Auto Scaling is for storage."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Amazon RDS Proxy is a managed connection pooler with sub-second failover. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html",
})
QUESTIONS.append({
    "q": "Which Aurora feature allows you to scale the cluster's read capacity by adding read replicas, with sub-second replication lag?",
    "type": "multiple-choice",
    "opts": [
        ("Aurora read replicas", "Aurora supports up to 15 read replicas with sub-second lag."),
        ("Aurora Global Database", "Global Database is for cross-region replication."),
        ("Aurora Multi-Master", "Multi-Master is for multi-writer within a region."),
        ("Aurora Backtrack", "Backtrack is for in-place time-travel."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Aurora read replicas scale read capacity with sub-second lag. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-replicas.html",
})
QUESTIONS.append({
    "q": "Which combination is the BEST pattern for serving a global API with low latency and high availability? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS Global Accelerator", "Global Accelerator provides anycast IPs with regional failover."),
        ("Amazon API Gateway with multi-region endpoints", "API Gateway multi-region provides API failover."),
        ("Single-AZ EC2 behind ALB", "Single-AZ is an HA antipattern."),
        ("Static S3 website only", "S3 static website is not a global API pattern."),
    ],
    "correct": "1,2",
    "domain": RESILIENT,
    "overall": "Use Global Accelerator + API Gateway multi-region for a global, low-latency, highly available API. Reference: https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed, highly available message broker for traditional protocols (MQTT, AMQP, STOMP) for migration from on-prem?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon MQ", "Amazon MQ supports AMQP, MQTT, STOMP for migration."),
        ("Amazon SQS", "SQS is AWS-native, not these protocols."),
        ("Amazon SNS", "SNS is pub/sub."),
        ("Amazon MSK", "MSK is for Kafka."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Amazon MQ supports AMQP, MQTT, and STOMP for migration from on-prem brokers. Reference: https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html",
})
QUESTIONS.append({
    "q": "Which combination of services provides the BEST multi-region active-active architecture for a global web application? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon CloudFront for global content delivery", "CloudFront caches content at edge."),
        ("AWS Global Accelerator for global anycast IPs", "Global Accelerator provides anycast with failover."),
        ("DynamoDB Global Tables for global data", "Global Tables provide multi-region replication."),
        ("Single-region EC2 only", "Single-region is not multi-region."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "CloudFront + Global Accelerator + DynamoDB Global Tables is the global active-active pattern. Reference: https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/aws-fault-isolation-boundaries.pdf",
})
QUESTIONS.append({
    "q": "Which feature of AWS Global Accelerator provides health-check-based failover to a healthy regional endpoint?",
    "type": "multiple-choice",
    "opts": [
        ("Endpoint health checks", "Global Accelerator uses endpoint health checks for failover."),
        ("Cross-region replication", "Replication is for data, not traffic."),
        ("Direct Connect", "DX is a private link."),
        ("Route 53 only", "Route 53 is DNS, not Global Accelerator's mechanism."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Global Accelerator uses endpoint health checks to detect unhealthy endpoints and route traffic to healthy ones. Reference: https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid strategies for cross-region database replication for DR? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Aurora Global Database", "Aurora Global Database for sub-second RPO."),
        ("DynamoDB Global Tables", "DynamoDB Global Tables for multi-region."),
        ("RDS read replicas cross-region", "RDS read replicas for cross-region async."),
        ("Manual SQL exports to S3", "Manual SQL exports are slow and error-prone."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "Aurora Global Database, DynamoDB Global Tables, and cross-region RDS read replicas are the standard cross-region DR options. Reference: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides DNS-based failover with health checks for active-passive DR?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Route 53", "Route 53 supports DNS failover with health checks."),
        ("Amazon CloudFront", "CloudFront is a CDN, not a DNS failover service."),
        ("AWS Global Accelerator", "Global Accelerator uses anycast IPs, not DNS."),
        ("Amazon API Gateway", "API Gateway is for APIs."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Amazon Route 53 with failover routing provides DNS-based failover with health checks. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html",
})
QUESTIONS.append({
    "q": "Which combination of services provides automatic, sub-second RTO failover for a multi-region web application? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS Global Accelerator", "Global Accelerator provides sub-second regional failover."),
        ("Amazon CloudFront origin failover", "CloudFront origin failover provides automatic origin failover."),
        ("Route 53 failover routing", "Route 53 failover is DNS-based and may take longer."),
        ("Single-region EC2 only", "Single-region is not multi-region."),
    ],
    "correct": "1,2",
    "domain": RESILIENT,
    "overall": "Global Accelerator and CloudFront origin failover provide sub-second failover. Route 53 is DNS-based. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high-availability.html",
})
QUESTIONS.append({
    "q": "Which combination of services provides the BEST DR posture for a regulated workload with RPO 5 minutes and RTO 1 hour? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Aurora Global Database with sub-second lag", "Aurora Global Database provides RPO < 5 min."),
        ("Cross-region read replicas for RDS", "RDS read replicas provide cross-region async replication."),
        ("AWS Backup with cross-region copy", "AWS Backup cross-region copy provides RPO via backup."),
        ("Manual snapshot copy only", "Manual snapshot is too slow for 5-minute RPO."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "Aurora Global Database, RDS read replicas, and AWS Backup cross-region copy provide DR posture. Reference: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides cross-region replication for S3 with 15-minute SLA on replication, designed for compliance and DR?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Cross-Region Replication", "S3 CRR provides cross-region async replication."),
        ("S3 Same-Region Replication", "SRR is same-region, not cross-region."),
        ("S3 Batch Replication", "Batch Replication is for existing objects."),
        ("S3 Object Lock", "Object Lock is for immutability."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "S3 Cross-Region Replication provides async replication across regions for DR. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html",
})
QUESTIONS.append({
    "q": "Which Route 53 health check feature provides global, distributed health checking from multiple AWS regions?",
    "type": "multiple-choice",
    "opts": [
        ("Route 53 health checkers in multiple global locations", "Route 53 health checkers are globally distributed."),
        ("Single-AZ health checks", "Route 53 does not have single-AZ checks."),
        ("CloudWatch health checks", "CloudWatch is for metrics, not health checks."),
        ("EC2 health checks only", "EC2 is not the health checker."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Route 53 health checkers are globally distributed for high availability. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid S3 cross-region replication (CRR) options? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Replica in a single destination region", "CRR can replicate to a single destination region."),
        ("Multiple destinations via S3 Multi-Region Access Points", "Multi-Region Access Points can span multiple regions."),
        ("Cross-account destination", "CRR can replicate to a different account."),
        ("Same-region destination only", "CRR is cross-region, not same-region; that's SRR."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "CRR can replicate to a single region, multiple regions via MRAP, and cross-account. Same-region is SRR. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed, private connection from on-premises to AWS for consistent, low-latency, high-bandwidth connectivity?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Direct Connect", "Direct Connect is a private dedicated link."),
        ("AWS Site-to-Site VPN", "VPN is over the internet, not dedicated."),
        ("Internet gateway", "An internet gateway is for public access."),
        ("Transit Gateway", "Transit Gateway is a hub, not a private link."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "AWS Direct Connect provides a private, dedicated link with consistent, low-latency, high-bandwidth connectivity. Reference: https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html",
})
QUESTIONS.append({
    "q": "Which combination of SQS and Lambda provides the BEST pattern for processing a high-volume queue with no message loss? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("SQS visibility timeout longer than Lambda timeout", "Visibility timeout prevents duplicate processing."),
        ("SQS dead-letter queue for failed messages", "DLQ captures failed messages."),
        ("Lambda reserved concurrency to throttle", "Reserved concurrency throttles to prevent overload."),
        ("Sync invocation with no DLQ", "Sync invocation without DLQ loses failed messages."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "Use proper visibility timeout, DLQ, and reserved concurrency for reliable SQS + Lambda processing. Reference: https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid SNS subscription types? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon SQS", "SQS is a common SNS subscriber."),
        ("AWS Lambda", "Lambda is a common SNS subscriber."),
        ("HTTP/HTTPS endpoints", "HTTP/HTTPS endpoints can be SNS subscribers."),
        ("DynamoDB tables directly", "DynamoDB tables are not direct SNS subscribers; use Lambda."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "SNS supports SQS, Lambda, HTTP/HTTPS, email, SMS, and mobile push as subscribers. Reference: https://docs.aws.amazon.com/sns/latest/dg/sns-basic-subscribe.html",
})
QUESTIONS.append({
    "q": "Which EventBridge feature allows you to filter events based on content before routing to a target?",
    "type": "multiple-choice",
    "opts": [
        ("EventBridge rules with event patterns", "Event patterns filter events based on content."),
        ("EventBridge Schedule", "Schedule is for time-based triggers."),
        ("EventBridge Archive", "Archive is for replaying past events."),
        ("EventBridge Schema Registry", "Schema Registry is for documenting event schemas."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "EventBridge rules with event patterns filter events based on content before routing. Reference: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html",
})
QUESTIONS.append({
    "q": "Which SQS message attribute can be used to route messages to different Lambda functions based on content?",
    "type": "multiple-choice",
    "opts": [
        ("SQS message attributes (custom key-value)", "Custom message attributes can drive routing decisions."),
        ("SQS body only", "Body content is not a routing attribute by itself."),
        ("SQS MessageId", "MessageId is unique, not for routing."),
        ("SQS ReceiptHandle", "ReceiptHandle is for message deletion, not routing."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "SQS message attributes are custom key-value pairs that can drive routing decisions. Reference: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.html",
})
QUESTIONS.append({
    "q": "Which combination of services provides the BEST pattern for processing S3 events in multiple Lambda functions in parallel? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("S3 event notifications to SNS topic", "SNS fan-out to multiple subscribers."),
        ("Multiple SQS queues subscribed to the SNS topic", "Each SQS queue triggers a different Lambda."),
        ("Single Lambda with no fan-out", "Single Lambda is not parallel fan-out."),
        ("Direct S3 to multiple Lambda", "S3 event notifications go to one target; use SNS for fan-out."),
    ],
    "correct": "1,2",
    "domain": RESILIENT,
    "overall": "Use S3 event notifications to SNS topic with multiple SQS subscribers for parallel Lambda processing. Reference: https://docs.aws.amazon.com/sns/latest/dg/sns-common-scenarios.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed, serverless pub/sub pattern with FIFO ordering via SNS FIFO topics?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon SNS FIFO topics", "SNS FIFO topics provide FIFO ordering and deduplication."),
        ("Amazon SNS standard topics", "Standard SNS does not guarantee order."),
        ("Amazon SQS FIFO", "SQS FIFO is a queue, not a topic."),
        ("Amazon EventBridge", "EventBridge does not guarantee order."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Amazon SNS FIFO topics provide FIFO ordering and deduplication for pub/sub. Reference: https://docs.aws.amazon.com/sns/latest/dg/sns-fifo-topics.html",
})
QUESTIONS.append({
    "q": "Which SQS feature is used to delay the visibility of a message after it is sent, useful for scheduled tasks?",
    "type": "multiple-choice",
    "opts": [
        ("DelaySeconds (queue or message)", "DelaySeconds delays message visibility."),
        ("VisibilityTimeout", "VisibilityTimeout is for in-flight messages."),
        ("MessageRetentionPeriod", "MessageRetentionPeriod is the queue's retention."),
        ("ReceiveMessageWaitTimeSeconds", "ReceiveMessageWaitTimeSeconds is for long polling."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "DelaySeconds can be set on a queue or per-message to delay message visibility. Reference: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-delay-queues.html",
})
QUESTIONS.append({
    "q": "Which Step Functions feature lets you invoke a state machine on a schedule or in response to events?",
    "type": "multiple-choice",
    "opts": [
        ("EventBridge integration", "EventBridge triggers state machines on schedule or events."),
        ("Step Functions only triggers manually", "Step Functions can be triggered by EventBridge."),
        ("SQS only", "SQS does not directly trigger Step Functions."),
        ("Direct API only", "Step Functions has an API but EventBridge is the standard pattern."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "EventBridge can trigger Step Functions on a schedule or in response to events. Reference: https://docs.aws.amazon.com/step-functions/latest/dg/concepts-events.html",
})
QUESTIONS.append({
    "q": "Which combination of services provides the BEST pattern for an event-driven serverless application? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon EventBridge for event routing", "EventBridge routes events from many sources."),
        ("AWS Lambda for compute", "Lambda runs the code."),
        ("Amazon SQS for buffering", "SQS buffers traffic for spikey workloads."),
        ("EC2 instances only", "EC2 is not serverless."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "Use EventBridge + Lambda + SQS for an event-driven serverless application. Reference: https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed message broker for Apache Kafka, with automatic scaling and patching?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon MSK", "Amazon MSK is the managed Kafka service."),
        ("Amazon SQS", "SQS is a queue, not Kafka."),
        ("Amazon SNS", "SNS is pub/sub."),
        ("Amazon MQ", "Amazon MQ is for ActiveMQ/RabbitMQ."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Amazon MSK provides managed Apache Kafka with automatic scaling and patching. Reference: https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html",
})
QUESTIONS.append({
    "q": "Which Route 53 routing policy is BEST for directing users to the closest region in terms of network latency?",
    "type": "multiple-choice",
    "opts": [
        ("Latency-based routing", "Latency routing picks the lowest-latency region."),
        ("Geolocation routing", "Geolocation routes by user location."),
        ("Failover routing", "Failover is active-passive."),
        ("Weighted routing", "Weighted is for fixed ratios."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Route 53 latency-based routing directs users to the region with the lowest measured network latency. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html",
})
QUESTIONS.append({
    "q": "Which combination of services provides DNS-based failover for a multi-region application? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon Route 53 with failover routing", "Route 53 failover routing switches on health check failure."),
        ("Route 53 health checks", "Health checks drive failover."),
        ("EC2 alone without DNS", "EC2 alone is not DNS failover."),
        ("Internet gateway", "An internet gateway is for routing, not failover."),
    ],
    "correct": "1,2",
    "domain": RESILIENT,
    "overall": "Use Route 53 failover routing with health checks for DNS-based failover. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-failover.html",
})
QUESTIONS.append({
    "q": "Which Route 53 feature provides a domain registration service for your custom domain names?",
    "type": "multiple-choice",
    "opts": [
        ("Route 53 domain registration", "Route 53 provides domain registration."),
        ("Route 53 health checks", "Health checks are for health monitoring."),
        ("Route 53 traffic flow", "Traffic flow is for visual policy."),
        ("Route 53 resolver", "Resolver is for hybrid DNS."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Route 53 provides domain registration alongside DNS and health checking. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar.html",
})
QUESTIONS.append({
    "q": "Which Route 53 feature provides a visual editor for complex routing policies with multiple records?",
    "type": "multiple-choice",
    "opts": [
        ("Route 53 traffic flow", "Traffic flow provides a visual policy editor."),
        ("Route 53 health checks", "Health checks are for monitoring."),
        ("Route 53 domain registration", "Domain registration is for buying domains."),
        ("Route 53 resolver", "Resolver is for hybrid DNS."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Route 53 traffic flow provides a visual editor for complex routing policies. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/traffic-flow.html",
})
QUESTIONS.append({
    "q": "Which service provides DNS resolution between on-premises networks and AWS VPCs, supporting conditional forwarding rules?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Route 53 Resolver", "Route 53 Resolver provides hybrid DNS."),
        ("Amazon CloudFront", "CloudFront is a CDN."),
        ("AWS Transit Gateway", "Transit Gateway is a network hub."),
        ("Amazon VPC DNS only", "VPC DNS is local, not hybrid."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Amazon Route 53 Resolver provides DNS resolution between on-prem and AWS VPCs with conditional forwarding. Reference: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html",
})
QUESTIONS.append({
    "q": "Which combination of services provides the BEST pattern for multi-VPC connectivity in a single region without VPC peering? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS Transit Gateway", "Transit Gateway is the central hub for multi-VPC."),
        ("VPC peering", "VPC peering is for 1:1 connections."),
        ("AWS PrivateLink", "PrivateLink is for service connectivity."),
        ("Multiple VPC peering connections", "Many peering connections are hard to manage; TGW is better."),
    ],
    "correct": "1,3",
    "domain": RESILIENT,
    "overall": "Use Transit Gateway as a hub, or PrivateLink for service-specific connectivity. Many peering connections are an antipattern. Reference: https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html",
})
QUESTIONS.append({
    "q": "Which feature of AWS Direct Connect provides redundant connections from different Direct Connect locations for high availability?",
    "type": "multiple-choice",
    "opts": [
        ("Direct Connect gateway with redundant connections", "Use multiple DX connections in different locations for HA."),
        ("Single DX connection", "A single DX connection is a single point of failure."),
        ("Internet gateway", "An internet gateway is not for DX."),
        ("AWS VPN only", "VPN is over the internet, not a DX feature."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Use a Direct Connect gateway with redundant DX connections in different locations for HA. Reference: https://docs.aws.amazon.com/directconnect/latest/UserGuide/disaster-recovery-resiliency.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed IP address prefix for AWS resources, simplifying IP management across VPCs and on-prem?",
    "type": "multiple-choice",
    "opts": [
        ("AWS IPAM (IP Address Manager)", "IPAM is the managed IP address manager."),
        ("Amazon VPC CIDR only", "VPC CIDR is local, not managed."),
        ("AWS Transit Gateway", "Transit Gateway is a network hub."),
        ("Route 53", "Route 53 is DNS."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "AWS IPAM is the managed IP address manager for planning and tracking IP allocations. Reference: https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html",
})
QUESTIONS.append({
    "q": "Which feature of CloudFront provides automatic failover to a secondary origin when the primary is unhealthy?",
    "type": "multiple-choice",
    "opts": [
        ("CloudFront origin failover with origin groups", "Origin groups provide automatic failover between origins."),
        ("CloudFront cache behaviors", "Cache behaviors are for path-based routing."),
        ("CloudFront Lambda@Edge", "Lambda@Edge is for code at the edge."),
        ("CloudFront signed URLs", "Signed URLs are for private content."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "CloudFront origin groups with primary and secondary origins provide automatic failover. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/high-availability.html",
})
QUESTIONS.append({
    "q": "Which combination of services provides the BEST pattern for a global, low-latency, highly available web application? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon CloudFront for edge caching", "CloudFront caches at edge."),
        ("AWS Global Accelerator for anycast IPs", "Global Accelerator provides anycast with failover."),
        ("Multi-region backend with Route 53", "Multi-region backend with DNS routing."),
        ("Single-region EC2 only", "Single-region is not global."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "Use CloudFront + Global Accelerator + multi-region backend for a global app. Reference: https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides automated recovery actions in response to CloudWatch alarms, used for self-healing infrastructure?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon CloudWatch alarms with actions", "CloudWatch alarms can trigger automated actions."),
        ("AWS Config only", "Config is for configuration compliance."),
        ("AWS Trusted Advisor", "Trusted Advisor is for best-practice checks."),
        ("AWS Systems Manager only", "SSM can run commands but is not the primary alarm-action service."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "CloudWatch alarms can trigger automated actions like EC2 reboot, SNS notification, or Lambda. Reference: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid components of a DR runbook? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Step-by-step recovery procedures", "A runbook documents recovery steps."),
        ("Roles and responsibilities", "RACI matrix for who does what."),
        ("Validation steps after recovery", "Validation ensures recovery is complete."),
        ("Skip RTO/RPO targets", "RTO/RPO targets are fundamental to DR."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "A DR runbook includes procedures, roles, and validation steps. RTO/RPO targets are essential. Reference: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed, self-service portal for compliance reports and agreements?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Artifact", "Artifact is the self-service portal for compliance reports."),
        ("AWS Audit Manager", "Audit Manager is for automated evidence collection."),
        ("AWS Security Hub", "Security Hub is for findings."),
        ("AWS Config", "Config is for resource configuration."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "AWS Artifact is the self-service portal for AWS compliance reports and BAA. Reference: https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html",
})
QUESTIONS.append({
    "q": "Which combination of services provides the BEST pattern for centralized log aggregation across multiple accounts? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("CloudTrail organization trail to central S3", "Org trail aggregates API logs."),
        ("CloudWatch Logs subscriptions to central account", "Subscriptions aggregate application logs."),
        ("S3 with Object Lock for immutability", "Object Lock protects logs from tampering."),
        ("Local logs in each account", "Local logs do not provide centralized aggregation."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "Use org trail + CloudWatch subscriptions + S3 Object Lock for centralized immutable logs. Reference: https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed, scalable Prometheus-compatible monitoring service for containers?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Managed Service for Prometheus", "AMP is the managed Prometheus service."),
        ("Amazon CloudWatch only", "CloudWatch is metrics but not Prometheus-compatible."),
        ("Amazon Managed Grafana", "Managed Grafana is for visualization, not metrics."),
        ("AWS X-Ray", "X-Ray is for distributed tracing."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Amazon Managed Service for Prometheus (AMP) provides managed Prometheus-compatible monitoring. Reference: https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed, scalable Loki-compatible log aggregation service for containers?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon CloudWatch Logs", "CloudWatch Logs is AWS-native, not Loki-compatible."),
        ("Amazon Managed Grafana", "Managed Grafana is for visualization."),
        ("Self-managed Loki on EC2", "Self-managed Loki is not a managed service."),
        ("All of the above are valid", "CloudWatch is the AWS-native option; no managed Loki service from AWS as of 2026."),
    ],
    "correct": "4",
    "domain": RESILIENT,
    "overall": "AWS does not have a managed Loki service; CloudWatch is the AWS-native log aggregation. Reference: https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/What-is-CloudWatch-Logs.html",
})
QUESTIONS.append({
    "q": "Which combination of services provides automated, runbook-driven remediation in response to AWS Config rule changes? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS Config rules", "Config rules detect non-compliance."),
        ("AWS Systems Manager Automation runbooks", "Automation runbooks perform remediation."),
        ("EventBridge to trigger runbooks", "EventBridge drives remediation from Config events."),
        ("Manual remediation only", "Manual remediation is slow and error-prone."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "Config + SSM Automation + EventBridge is the standard auto-remediation pattern. Reference: https://docs.aws.amazon.com/config/latest/developerguide/remediation.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a managed workflow for orchestrating hybrid cloud DR?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Systems Manager Automation", "SSM Automation runbooks orchestrate hybrid DR."),
        ("AWS Step Functions", "Step Functions can also orchestrate DR."),
        ("AWS CloudFormation", "CloudFormation is for infrastructure, not DR orchestration."),
        ("AWS Config", "Config is for configuration compliance."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "AWS Systems Manager Automation runbooks orchestrate hybrid DR with cross-platform actions. Reference: https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html",
})
QUESTIONS.append({
    "q": "Which service provides a managed way to run Chaos engineering experiments on AWS?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Fault Injection Service (FIS)", "FIS is the managed chaos engineering service."),
        ("AWS Config", "Config is for configuration."),
        ("AWS Systems Manager", "SSM is for ops items."),
        ("AWS CloudWatch", "CloudWatch is for metrics and logs."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "AWS Fault Injection Service (FIS) provides managed chaos engineering experiments. Reference: https://docs.aws.amazon.com/fis/latest/userguide/what-is.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid FIS experiment types? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("EC2 instance stop or reboot", "FIS can stop or reboot EC2 instances."),
        ("RDS failover", "FIS can trigger RDS failover."),
        ("Network packet loss or latency", "FIS can inject network faults."),
        ("EBS snapshot creation", "FIS does not directly create EBS snapshots."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "FIS can stop/reboot EC2, trigger RDS failover, and inject network faults. Reference: https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html",
})
QUESTIONS.append({
    "q": "Which combination of services provides the BEST pattern for protecting EBS volumes from accidental deletion? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Disable Delete on Termination", "DeleteOnTermination=false preserves the volume."),
        ("Enable EC2 termination protection", "Termination protection prevents EC2 termination."),
        ("Use AWS Backup with retention", "AWS Backup provides policy-based backup."),
        ("Disable EBS encryption", "Disabling encryption is unrelated to deletion protection."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "Disable Delete on Termination, enable termination protection, and use AWS Backup for retention. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-deleting-volume.html",
})
QUESTIONS.append({
    "q": "Which S3 feature provides cross-region replication with automatic encryption using a customer managed KMS key in the destination?",
    "type": "multiple-choice",
    "opts": [
        ("S3 CRR with replica KMS key", "CRR supports replica-side KMS encryption."),
        ("S3 SRR only", "SRR is same-region, not cross-region."),
        ("S3 Object Lock", "Object Lock is for immutability."),
        ("S3 Batch Replication", "Batch is for existing objects."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "S3 CRR supports replica-side KMS encryption with a customer managed key in the destination. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid S3 replication time controls (S3 RTC)? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("15-minute replication SLA", "S3 RTC provides a 15-minute SLA."),
        ("CloudWatch metrics for replication", "S3 RTC publishes CloudWatch metrics."),
        ("Replication event notifications", "S3 RTC supports event notifications."),
        ("Real-time synchronous replication", "S3 replication is async, not real-time."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "S3 RTC provides 15-minute SLA, CloudWatch metrics, and event notifications. Replication is async. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-time-control.html",
})
QUESTIONS.append({
    "q": "Which service provides automated, policy-based snapshot management for EBS volumes across the account?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Data Lifecycle Manager (DLM)", "DLM automates EBS snapshot lifecycle."),
        ("AWS Backup", "AWS Backup also supports EBS but DLM is dedicated to EBS."),
        ("CloudWatch Events", "CloudWatch Events is for event rules, not snapshot management."),
        ("AWS Systems Manager", "SSM is for ops items."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Amazon Data Lifecycle Manager (DLM) automates EBS snapshot creation, retention, and deletion. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html",
})
QUESTIONS.append({
    "q": "Which combination of services provides the BEST pattern for cross-region EBS snapshot DR? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("EBS snapshot copy to destination region", "EBS supports cross-region snapshot copy."),
        ("AWS Backup with cross-region copy", "AWS Backup cross-region copy provides policy-based DR."),
        ("Direct EBS volume replication", "EBS does not support direct volume replication across regions."),
        ("Manual copy only", "Manual copy is not a best practice for DR."),
    ],
    "correct": "1,2",
    "domain": RESILIENT,
    "overall": "Use EBS snapshot copy or AWS Backup cross-region copy for EBS DR. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-copy-snapshot.html",
})
QUESTIONS.append({
    "q": "Which RDS feature provides automated, point-in-time recovery across multiple AWS accounts for centralized DR?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Backup with cross-account copy", "AWS Backup supports cross-account copy for RDS."),
        ("RDS Multi-AZ only", "Multi-AZ is single-region."),
        ("Read replicas cross-account", "Read replicas can be cross-account, but for DR AWS Backup is more comprehensive."),
        ("Manual snapshot share", "Manual snapshot share is for read-only, not full DR."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "AWS Backup with cross-account copy provides centralized RDS DR. Reference: https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-feature-cvo.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid S3 Versioning-related features? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("MFA delete", "MFA delete requires MFA to delete."),
        ("Lifecycle expiration of old versions", "Lifecycle can expire noncurrent versions."),
        ("Cross-region replication of all versions", "Replication can include all versions or current only."),
        ("Automatic deletion of all versions", "S3 does not auto-delete; you set Lifecycle rules."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "S3 Versioning supports MFA delete, lifecycle expiration of old versions, and replication of versions. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html",
})
QUESTIONS.append({
    "q": "Which S3 Object Lock mode provides the STRONGEST protection against deletion, even by the root user, for compliance use cases?",
    "type": "multiple-choice",
    "opts": [
        ("Governance mode", "Governance allows special users to bypass retention."),
        ("Compliance mode", "Compliance mode prevents deletion by anyone, even root."),
        ("Legal hold", "Legal hold is independent of retention."),
        ("Standard mode", "Standard mode is not an Object Lock mode."),
    ],
    "correct": "2",
    "domain": RESILIENT,
    "overall": "S3 Object Lock Compliance mode is the strongest: no user, including root, can delete or overwrite the object until the retention period ends. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html",
})
QUESTIONS.append({
    "q": "Which service provides automated, point-in-time recovery for EFS file systems with hourly snapshots?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon EFS automatic backups", "EFS supports automatic backups via AWS Backup."),
        ("EFS does not support backups", "EFS supports backups via AWS Backup."),
        ("Manual snapshots only", "AWS Backup automates EFS snapshots."),
        ("S3 snapshots", "S3 is not for EFS."),
    ],
    "correct": "1",
    "domain": RESILIENT,
    "overall": "Amazon EFS supports automatic backups via AWS Backup for point-in-time recovery. Reference: https://docs.aws.amazon.com/efs/latest/ug/backup-and-restore.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid AWS Backup features? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Cross-region copy", "AWS Backup supports cross-region copy."),
        ("Cross-account copy", "AWS Backup supports cross-account copy."),
        ("Compliance monitoring with audit reports", "AWS Backup provides audit reports."),
        ("Real-time replication of all data", "AWS Backup is for scheduled backups, not real-time replication."),
    ],
    "correct": "1,2,3",
    "domain": RESILIENT,
    "overall": "AWS Backup supports cross-region/cross-account copy and compliance monitoring. Real-time replication is not a backup feature. Reference: https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html",
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
    assert counts[RESILIENT] >= 150, f"Resilient={counts[RESILIENT]} (expected >= 150 for D2 deep dive)"
    assert multi == 40, f"Multi-select={multi}"

    out = "/home/user/Cert/course/AWS-SAA-C03-03-practice-sets/set-3/practice-set-3.csv"
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
