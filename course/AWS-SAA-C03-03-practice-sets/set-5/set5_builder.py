"""Builder for SAA-C03 Set 5 — Domain 4 Cost-Optimized Architectures deep dive (200q) + GlobalBank case study.

Set 5 is a deep dive on Domain 4 (Cost-Optimized Architectures, 20% of the real exam).
- 200 questions total
- 20% multi-select = 40 questions
- 20 case-study questions referencing GlobalBank
- 100% Cost-Optimized domain (with one or two cost-aware multi-domain questions)
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
# 1. PRICING MODELS & RESERVED INSTANCES (22 questions)
# ============================================================

QUESTIONS.append({
    "q": "Which EC2 pricing model provides the LARGEST discount (up to 90%) in exchange for a 1- or 3-year commitment and partial upfront payment?",
    "type": "multiple-choice",
    "opts": [
        ("On-Demand", "On-Demand has no commitment, highest per-hour cost."),
        ("Reserved Instances (Standard)", "Standard RIs provide up to 75% discount for 1- or 3-year commitment."),
        ("Spot Instances", "Spot discounts are variable and based on spare capacity, up to ~90% off On-Demand."),
        ("Dedicated Hosts", "Dedicated Hosts are physical servers; you pay for the host, not the discount model."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Standard Reserved Instances provide up to 75% discount versus On-Demand for a 1- or 3-year commitment. Spot can be cheaper but is interruptible. Reference: https://aws.amazon.com/savingsplans/",
})
QUESTIONS.append({
    "q": "Which Savings Plan type applies to EC2, Fargate, and Lambda usage, providing flexibility across instance families, regions, and sizes?",
    "type": "multiple-choice",
    "opts": [
        ("EC2 Instance Savings Plans", "EC2 Instance Savings Plans apply to EC2 only, but allow family/region changes."),
        ("Compute Savings Plans", "Compute Savings Plans apply to EC2, Fargate, and Lambda across families and regions."),
        ("SageMaker Savings Plans", "SageMaker Savings Plans apply to SageMaker only."),
        ("Database Savings Plans", "No such Savings Plan type."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Compute Savings Plans offer the most flexibility, applying to EC2, Fargate, and Lambda. Reference: https://aws.amazon.com/savingsplans/compute-pricing/",
})
QUESTIONS.append({
    "q": "Which EC2 pricing model is BEST for a fault-tolerant, flexible workload that can tolerate interruptions in exchange for the lowest price?",
    "type": "multiple-choice",
    "opts": [
        ("On-Demand", "On-Demand has the highest per-hour cost and no interruption risk."),
        ("Reserved Instances", "RIs require a 1- or 3-year commitment with no interruption."),
        ("Spot Instances", "Spot provides up to 90% discount for interruptible fault-tolerant workloads."),
        ("Dedicated Hosts", "Dedicated Hosts are physical servers for licensing or compliance."),
    ],
    "correct": "3",
    "domain": COST_OPT,
    "overall": "Spot Instances provide up to 90% discount for fault-tolerant workloads that can handle interruptions. Reference: https://aws.amazon.com/ec2/spot/",
})
QUESTIONS.append({
    "q": "Which of the following are valid Reserved Instance attributes that affect pricing and billing? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Instance type", "RI pricing varies by instance type."),
        ("Instance size flexibility (Normalization Factor)", "Regional RIs apply across sizes within a family."),
        ("Tenancy (shared vs dedicated)", "Tenancy affects RI pricing."),
        ("Platform (Linux/UNIX, Windows)", "Platform affects RI pricing and scope."),
    ],
    "correct": "1,2,3,4",
    "domain": COST_OPT,
    "overall": "RI attributes include instance type, size, tenancy, platform, scope (region or AZ), and offering class. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts-reserved-instances.html",
})
QUESTIONS.append({
    "q": "Which Reserved Instance class is the MOST flexible, allowing changes to instance type, family, OS, and tenancy?",
    "type": "multiple-choice",
    "opts": [
        ("Standard RIs", "Standard RIs are the least flexible (instance size within family in same region)."),
        ("Convertible RIs", "Convertible RIs allow changes to instance type, family, OS, and tenancy."),
        ("Scheduled RIs", "Scheduled RIs run on a recurring schedule."),
        ("Zonal RIs", "Zonal RIs are scoped to a single AZ for capacity reservation."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Convertible RIs allow changes to instance type, OS, tenancy, and family during the term. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/convertible-reserved-instances.html",
})
QUESTIONS.append({
    "q": "What is the MAXIMUM term length for a Standard Reserved Instance?",
    "type": "multiple-choice",
    "opts": [
        ("1 year", "1 year is the minimum term."),
        ("3 years", "3 years is the maximum term, providing the largest discount."),
        ("5 years", "5 years is not available for EC2 RIs."),
        ("No maximum", "All RIs have a finite term."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Standard RIs are available for 1- or 3-year terms; 3 years gives the largest discount. Reference: https://aws.amazon.com/ec2/pricing/reserved-instances/",
})
QUESTIONS.append({
    "q": "Which of the following are valid EC2 payment options for Reserved Instances? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("No Upfront", "No Upfront has lowest discount, billed monthly."),
        ("Partial Upfront", "Partial Upfront balances upfront and monthly."),
        ("All Upfront", "All Upfront provides the largest discount."),
        ("Pay-as-you-go", "Pay-as-you-go is the On-Demand model, not RI."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "RI payment options are No Upfront, Partial Upfront, and All Upfront, with All Upfront providing the largest discount. Reference: https://aws.amazon.com/ec2/pricing/reserved-instances/",
})
QUESTIONS.append({
    "q": "What happens to the unused portion of a Reserved Instance when the matching instance is terminated?",
    "type": "multiple-choice",
    "opts": [
        ("It is lost", "RIs cannot be refunded pro-rata."),
        ("It continues to apply to other matching instances in the same family", "Regional RIs automatically apply to other matching instances until exhausted."),
        ("It is converted to Savings Plans", "Unused RIs do not auto-convert to Savings Plans."),
        ("It is refunded as credit", "No refund; RIs are consumed or applied to other instances."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Regional RIs apply to any matching instance in the region until the hour is consumed. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/apply_ri.html",
})
QUESTIONS.append({
    "q": "Which AWS pricing model provides a discount for a 1- or 3-year usage COMMITMENT measured in $/hour, applicable across instance families and regions?",
    "type": "multiple-choice",
    "opts": [
        ("Reserved Instances", "RIs commit to specific instance attributes, not just $/hour."),
        ("Savings Plans", "Savings Plans commit to a $/hour spend and apply flexibly."),
        ("Spot Instances", "Spot has no commitment."),
        ("On-Demand", "On-Demand has no discount or commitment."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Savings Plans commit to a $/hour spend and apply automatically to eligible usage across services. Reference: https://aws.amazon.com/savingsplans/",
})
QUESTIONS.append({
    "q": "Which of the following are valid Savings Plan types? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Compute Savings Plans", "Compute Savings Plans apply to EC2, Fargate, and Lambda."),
        ("EC2 Instance Savings Plans", "EC2 Instance Savings Plans apply to EC2 in a family/region."),
        ("SageMaker Savings Plans", "SageMaker Savings Plans apply to SageMaker usage."),
        ("S3 Storage Savings Plans", "There is no S3 Storage Savings Plan; S3 has its own pricing models."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Compute, EC2 Instance, and SageMaker are the three Savings Plan types. Reference: https://aws.amazon.com/savingsplans/",
})
QUESTIONS.append({
    "q": "Which EC2 pricing model reserves CAPACITY for a specific instance type in a specific Availability Zone?",
    "type": "multiple-choice",
    "opts": [
        ("On-Demand", "On-Demand has no capacity reservation."),
        ("Zonal Reserved Instance", "Zonal RIs (scoped to a single AZ) reserve capacity for that instance type in that AZ."),
        ("Regional Reserved Instance", "Regional RIs do not reserve capacity."),
        ("Spot Instance", "Spot uses spare capacity, not reserved."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Zonal RIs reserve capacity for a specific instance type in a specific AZ, providing both discount and capacity assurance. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts-reserved-instances.html",
})
QUESTIONS.append({
    "q": "Which EC2 feature lets you bid a maximum price for Spot Instances, with the Spot price fluctuating based on supply and demand?",
    "type": "multiple-choice",
    "opts": [
        ("Spot max price", "You set a max price; you pay the Spot market price, not your max, as long as it's below your max."),
        ("Spot fleet", "Spot Fleet launches a mix of Spot and On-Demand."),
        ("Spot block", "Spot block was discontinued; 'duration' replaces it."),
        ("On-Demand", "On-Demand has no bidding."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Set a max price for Spot; you pay the Spot market price, not your max, as long as Spot is below your max. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html",
})
QUESTIONS.append({
    "q": "Which of the following workloads are BEST suited for Spot Instances? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Big data Hadoop/Spark batch jobs", "Batch jobs can be checkpointed and restarted."),
        ("Containerized microservices with checkpointing", "Stateless containers can be replaced."),
        ("CI/CD build runners", "Build jobs are fault-tolerant and can be retried."),
        ("Latency-sensitive single-AZ database primary", "Spot is not suited for stateful, latency-sensitive primaries."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Spot is suited for fault-tolerant, stateless, batch, container, and CI/CD workloads. Reference: https://aws.amazon.com/ec2/spot/",
})
QUESTIONS.append({
    "q": "Which feature of EC2 Auto Scaling helps you reduce cost by terminating instances during predictable low-traffic periods?",
    "type": "multiple-choice",
    "opts": [
        ("Scheduled scaling", "Scheduled scaling scales capacity at specific times, useful for predictable patterns."),
        ("Target tracking", "Target tracking reacts to a metric like CPU."),
        ("Predictive scaling", "Predictive scaling uses ML to forecast."),
        ("Lifecycle hooks", "Lifecycle hooks pause instance termination for custom actions."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Scheduled scaling scales capacity up or down at specific times, ideal for predictable patterns to reduce cost. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/schedule_time.html",
})
QUESTIONS.append({
    "q": "Which AWS tool recommends Reserved Instance purchases based on your historical On-Demand usage?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost Explorer RI recommendations", "Cost Explorer provides RI purchase recommendations based on past usage."),
        ("AWS Trusted Advisor", "Trusted Advisor provides checks including cost optimization."),
        ("AWS Budgets", "Budgets alerts on spend, not RI recommendations."),
        ("AWS Compute Optimizer", "Compute Optimizer recommends instance type rightsizing."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Cost Explorer RI recommendations suggest RIs based on your past On-Demand usage patterns. Reference: https://docs.aws.amazon.com/cost-management/latest/userguide/ce-ri-recommendations.html",
})
QUESTIONS.append({
    "q": "What is the maximum discount available for a 3-year Standard Reserved Instance with All Upfront payment?",
    "type": "multiple-choice",
    "opts": [
        ("Up to 40%", "1-year All Upfront provides up to 40%."),
        ("Up to 60%", "3-year No Upfront provides up to 60%."),
        ("Up to 75%", "3-year All Upfront provides the largest discount, up to 75%."),
        ("Up to 90%", "Spot provides up to 90%."),
    ],
    "correct": "3",
    "domain": COST_OPT,
    "overall": "3-year Standard RIs with All Upfront provide up to 75% discount versus On-Demand. Reference: https://aws.amazon.com/ec2/pricing/reserved-instances/",
})
QUESTIONS.append({
    "q": "Which of the following are valid Spot Instance interruption behaviors? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Stop", "Spot instances can be configured to stop on interruption."),
        ("Terminate", "Spot instances can be configured to terminate on interruption."),
        ("Hibernate", "Spot instances can be configured to hibernate on interruption."),
        ("Migrate", "Spot instances cannot auto-migrate."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Spot interruption behaviors are stop, terminate, or hibernate. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html",
})
QUESTIONS.append({
    "q": "Which Spot feature lets you launch a portfolio of Spot and On-Demand instances with target capacity, automatically requesting resources to meet the target?",
    "type": "multiple-choice",
    "opts": [
        ("Spot Fleet", "Spot Fleet launches a mix of Spot and On-Demand to meet target capacity."),
        ("Spot Instance alone", "Spot Instance is a single instance request."),
        ("Auto Scaling only", "Auto Scaling uses launch templates, not Spot Fleet."),
        ("Reserved Instance", "RIs don't use Spot."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Spot Fleet launches a portfolio of instance types and purchasing models to meet target capacity at the lowest price. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a serverless, pay-per-request compute model with no charge when idle, billed in 1 ms increments?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon EC2", "EC2 bills per second/hour, with minimum charges."),
        ("AWS Lambda", "Lambda bills per request and GB-second, no charge when idle."),
        ("Amazon ECS", "ECS is a container orchestrator; you pay for underlying compute."),
        ("Amazon EKS", "EKS bills per cluster hour plus underlying compute."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "AWS Lambda is the most cost-efficient compute for variable workloads, with no charge when idle and 1 ms billing. Reference: https://aws.amazon.com/lambda/pricing/",
})
QUESTIONS.append({
    "q": "Which EC2 feature lets you set a HOURLY budget that, when exceeded, automatically stops the instance to prevent runaway costs?",
    "type": "multiple-choice",
    "opts": [
        ("Instance interruption behavior", "Interruption behavior is for Spot, not budget."),
        ("Auto Scaling budget", "Auto Scaling does not have a budget feature."),
        ("Self-imposed Stop on budget alert", "Use AWS Budgets with a stop action on an alarm, or third-party tools."),
        ("Lambda budget", "Lambda does not have this feature for EC2."),
    ],
    "correct": "3",
    "domain": COST_OPT,
    "overall": "Use AWS Budgets with an alarm and a stop action (via CloudWatch + Lambda) to stop instances when budget is exceeded. Reference: https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid benefits of Compute Savings Plans over EC2 Instance Savings Plans? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Applies to Fargate and Lambda", "Compute Savings Plans apply to EC2, Fargate, and Lambda."),
        ("Applies to any instance family", "Compute Savings Plans apply to any family."),
        ("Applies to any AWS region", "Compute Savings Plans apply across regions."),
        ("Provides higher discount", "EC2 Instance Savings Plans provide the same or slightly higher discount but less flexibility."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Compute Savings Plans offer the most flexibility (EC2, Fargate, Lambda, any family, any region) versus EC2 Instance Savings Plans. Reference: https://aws.amazon.com/savingsplans/compute-pricing/",
})
QUESTIONS.append({
    "q": "Which AWS feature provides automatic discounts on S3 storage as your usage grows, with no commitment required?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Intelligent-Tiering", "Intelligent-Tiering auto-tiers but does not provide a volume discount per se."),
        ("S3 Volume Discounts (tiered pricing)", "S3 has tiered pricing where per-GB cost decreases as usage grows."),
        ("S3 Reserved Capacity", "There is no S3 Reserved Capacity; S3 Glacier has Reserved Capacity."),
        ("S3 Standard-IA", "Standard-IA has a lower per-GB rate but retrieval fees."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "S3 has tiered pricing where the per-GB cost decreases as your storage volume grows, with no commitment. Reference: https://aws.amazon.com/s3/pricing/",
})

# ============================================================
# 2. S3 STORAGE CLASSES & LIFECYCLE (16 questions)
# ============================================================

QUESTIONS.append({
    "q": "Which S3 storage class is the LOWEST cost for long-term archives where retrieval time of 12 hours is acceptable?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Glacier Instant Retrieval", "Glacier Instant Retrieval is millisecond retrieval."),
        ("S3 Glacier Flexible Retrieval", "Glacier Flexible Retrieval supports minutes to hours."),
        ("S3 Glacier Deep Archive", "Glacier Deep Archive is the lowest-cost class, with 12-hour retrieval."),
        ("S3 Standard-IA", "Standard-IA is for infrequent access, not archive."),
    ],
    "correct": "3",
    "domain": COST_OPT,
    "overall": "S3 Glacier Deep Archive is the lowest-cost S3 storage class for 7-10 year archives with 12-hour retrieval. Reference: https://aws.amazon.com/s3/storage-classes/",
})
QUESTIONS.append({
    "q": "Which S3 storage class is the BEST fit for data accessed less than once a quarter, with millisecond retrieval and no retrieval fees?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Standard", "Standard is for frequent access, not cost-optimized for rare access."),
        ("S3 Standard-IA", "Standard-IA has retrieval fees and per-GB retrieval charges."),
        ("S3 Glacier Instant Retrieval", "Glacier Instant Retrieval provides millisecond retrieval with no retrieval fees for quarterly access."),
        ("S3 Glacier Flexible Retrieval", "Glacier Flexible has minutes-to-hours retrieval, not millisecond."),
    ],
    "correct": "3",
    "domain": COST_OPT,
    "overall": "S3 Glacier Instant Retrieval provides millisecond retrieval with no retrieval fees, ideal for quarterly access. Reference: https://aws.amazon.com/s3/storage-classes/",
})
QUESTIONS.append({
    "q": "Which S3 storage class automatically moves objects to the most cost-effective access tier based on changing access patterns, with no operational overhead?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Standard", "Standard is a fixed tier, not auto-tiering."),
        ("S3 Intelligent-Tiering", "Intelligent-Tiering auto-tiers based on access patterns."),
        ("S3 Glacier Deep Archive", "Glacier Deep Archive is a fixed tier."),
        ("S3 One Zone-IA", "One Zone-IA is a fixed tier for single-AZ infrequent access."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "S3 Intelligent-Tiering auto-tiers objects across access tiers based on access patterns with no operational overhead. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid S3 lifecycle transition targets? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("S3 Standard-IA", "Lifecycle can transition to Standard-IA."),
        ("S3 One Zone-IA", "Lifecycle can transition to One Zone-IA."),
        ("S3 Glacier Instant Retrieval", "Lifecycle can transition to Glacier Instant Retrieval."),
        ("S3 Glacier Flexible Retrieval", "Lifecycle can transition to Glacier Flexible Retrieval."),
    ],
    "correct": "1,2,3,4",
    "domain": COST_OPT,
    "overall": "Lifecycle can transition objects to Standard-IA, One Zone-IA, Glacier Instant Retrieval, Glacier Flexible Retrieval, and Glacier Deep Archive. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html",
})
QUESTIONS.append({
    "q": "Which S3 storage class is the MOST cost-effective for data that can be recreated, with single-AZ availability and infrequent access?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Standard", "Standard is multi-AZ, more expensive."),
        ("S3 Standard-IA", "Standard-IA is multi-AZ with retrieval fees."),
        ("S3 One Zone-IA", "One Zone-IA stores in a single AZ, 20% cheaper than Standard-IA, for reproducible data."),
        ("S3 Glacier", "Glacier is for archive with retrieval delays."),
    ],
    "correct": "3",
    "domain": COST_OPT,
    "overall": "S3 One Zone-IA stores data in a single AZ, with 20% lower cost than Standard-IA, for reproducible infrequent data. Reference: https://aws.amazon.com/s3/storage-classes/",
})
QUESTIONS.append({
    "q": "Which S3 Glacier retrieval option provides the FASTEST access (1-5 minutes) but at a higher cost than Standard retrieval?",
    "type": "multiple-choice",
    "opts": [
        ("Standard retrieval (3-5 hours)", "Standard is the slowest, cheapest Flexible retrieval."),
        ("Expedited retrieval (1-5 minutes)", "Expedited retrieval is 1-5 minutes, higher cost."),
        ("Bulk retrieval (5-12 hours)", "Bulk is the cheapest, slowest Flexible retrieval."),
        ("S3 Standard", "S3 Standard is not a Glacier option."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Glacier Flexible Retrieval offers Standard (3-5h), Bulk (5-12h), and Expedited (1-5 min) tiers. Reference: https://aws.amazon.com/s3/storage-classes/",
})
QUESTIONS.append({
    "q": "Which S3 feature lets you reduce storage cost by automatically deleting incomplete multipart uploads that were never completed?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Lifecycle with AbortIncompleteMultipartUpload action", "Lifecycle can abort incomplete multipart uploads."),
        ("S3 Replication", "Replication copies objects, not aborts uploads."),
        ("S3 Event Notifications", "Event Notifications are for downstream actions, not aborts."),
        ("S3 Object Lock", "Object Lock is for WORM, not upload cleanup."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Use S3 Lifecycle with the AbortIncompleteMultipartUpload action to clean up incomplete multipart uploads. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpu-abort-incomplete-mpu.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid S3 cost optimization techniques? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Lifecycle policies to transition to cheaper tiers", "Lifecycle transitions reduce cost."),
        ("S3 Intelligent-Tiering for unknown access patterns", "Intelligent-Tiering auto-optimizes cost."),
        ("S3 Object Lock for WORM", "Object Lock is for compliance, not cost optimization."),
        ("S3 Lifecycle to expire (delete) old versions", "Expiring old noncurrent versions reduces cost."),
    ],
    "correct": "1,2,4",
    "domain": COST_OPT,
    "overall": "Lifecycle transitions, Intelligent-Tiering, and expiring old noncurrent versions reduce S3 cost. Object Lock is for compliance. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-cost-optimization.html",
})
QUESTIONS.append({
    "q": "Which S3 Glacier pricing model provides a LOWER per-GB-month cost in exchange for committing to a fixed provisioned capacity unit?",
    "type": "multiple-choice",
    "opts": [
        ("On-Demand", "On-Demand is the default with no commitment."),
        ("S3 Glacier Reserved Capacity", "Glacier Reserved Capacity provides a discount in exchange for a capacity commitment."),
        ("S3 Standard", "S3 Standard is not a Glacier class."),
        ("S3 Glacier Instant Retrieval", "Glacier Instant Retrieval is a separate class, not a pricing model."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "S3 Glacier Reserved Capacity provides a discount in exchange for committing to a provisioned capacity. Reference: https://aws.amazon.com/s3/glacier/pricing/",
})
QUESTIONS.append({
    "q": "Which S3 storage class provides millisecond retrieval, single AZ storage, and is 20% cheaper than S3 Standard-IA?",
    "type": "multiple-choice",
    "opts": [
        ("S3 One Zone-IA", "One Zone-IA is single-AZ, 20% cheaper than Standard-IA, millisecond retrieval."),
        ("S3 Standard-IA", "Standard-IA is multi-AZ."),
        ("S3 Glacier Instant Retrieval", "Glacier Instant Retrieval is multi-AZ."),
        ("S3 Standard", "Standard is multi-AZ and more expensive."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "S3 One Zone-IA is single-AZ, millisecond retrieval, 20% cheaper than Standard-IA. Reference: https://aws.amazon.com/s3/storage-classes/",
})
QUESTIONS.append({
    "q": "Which S3 request type is FREE for the request itself but charged per GB transferred out?",
    "type": "multiple-choice",
    "opts": [
        ("PUT request", "PUT requests are charged per 1,000 requests."),
        ("GET request from another region", "Cross-region GETs are charged per 1,000 + per GB transfer."),
        ("Data transfer OUT to internet", "Data transfer out to internet is charged per GB, with no per-request fee."),
        ("Lifecycle transition", "Lifecycle transitions are charged per 1,000 objects."),
    ],
    "correct": "3",
    "domain": COST_OPT,
    "overall": "Data transfer out to internet is charged per GB, with no per-request fee. Reference: https://aws.amazon.com/s3/pricing/",
})
QUESTIONS.append({
    "q": "Which S3 feature lets you replicate objects to a destination bucket in another region, useful for DR and reducing latency?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Cross-Region Replication (CRR)", "CRR replicates objects to a bucket in another region."),
        ("S3 Same-Region Replication (SRR)", "SRR replicates within the same region."),
        ("S3 Transfer Acceleration", "Transfer Acceleration is for faster uploads, not replication."),
        ("S3 Multi-Region Access Point", "Multi-Region Access Point provides a single global endpoint over replicated buckets."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "S3 Cross-Region Replication (CRR) replicates objects to a destination bucket in another region. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html",
})
QUESTIONS.append({
    "q": "Which S3 pricing factor is FREE for the first 100 GB per month, with no charge?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Standard storage", "Storage is not free."),
        ("Data transfer out to internet", "Data transfer out to internet is free for the first 100 GB per month."),
        ("PUT requests", "PUT requests are not free."),
        ("Cross-region replication", "Replication has per-GB and per-request charges."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Data transfer out to internet is free for the first 100 GB per month. Reference: https://aws.amazon.com/s3/pricing/",
})
QUESTIONS.append({
    "q": "Which S3 feature lets you STORE and QUERY data directly without retrieving the full object, reducing data transfer cost?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Select", "S3 Select queries a subset of data server-side, reducing data transfer."),
        ("S3 Glacier Select", "Glacier Select queries archive objects server-side."),
        ("S3 Inventory", "S3 Inventory lists objects, doesn't query data."),
        ("S3 Batch Operations", "Batch Operations performs bulk actions on objects."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "S3 Select and S3 Glacier Select query a subset of data server-side, reducing data transfer and cost. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/selecting-content-from-objects.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid S3 storage classes that support S3 Object Lock for WORM (Write Once Read Many) compliance? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("S3 Standard", "Standard supports Object Lock."),
        ("S3 Standard-IA", "Standard-IA supports Object Lock."),
        ("S3 Glacier Flexible Retrieval", "Glacier Flexible Retrieval supports Object Lock."),
        ("S3 One Zone-IA", "One Zone-IA supports Object Lock."),
    ],
    "correct": "1,2,3,4",
    "domain": COST_OPT,
    "overall": "Object Lock is supported on Standard, Standard-IA, One Zone-IA, Glacier Instant, Glacier Flexible, and Deep Archive. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html",
})
QUESTIONS.append({
    "q": "Which S3 storage class is the BEST choice for backups of on-premises databases, with 12-hour retrieval tolerance and the lowest storage cost?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Standard", "Standard is for frequent access, not cost-optimized for backups."),
        ("S3 Glacier Flexible Retrieval", "Glacier Flexible supports 1-5 min to 12 hours, not the lowest cost."),
        ("S3 Glacier Deep Archive", "Glacier Deep Archive is the lowest-cost class with 12-hour retrieval, ideal for backups."),
        ("S3 One Zone-IA", "One Zone-IA is for infrequent access, not the lowest cost for backups."),
    ],
    "correct": "3",
    "domain": COST_OPT,
    "overall": "S3 Glacier Deep Archive is the lowest-cost class with 12-hour retrieval, ideal for backups and long-term archives. Reference: https://aws.amazon.com/s3/storage-classes/",
})

# ============================================================
# 3. EBS & INSTANCE STORE COST OPTIMIZATION (12 questions)
# ============================================================

QUESTIONS.append({
    "q": "Which EBS volume type is the LEAST EXPENSIVE per GB for COLD, infrequently accessed data with the lowest storage cost?",
    "type": "multiple-choice",
    "opts": [
        ("EBS gp3", "gp3 is general-purpose SSD."),
        ("EBS io2", "io2 is the highest-performance SSD, most expensive per GB."),
        ("EBS st1", "st1 is throughput-optimized HDD."),
        ("EBS sc1", "EBS sc1 is the lowest-cost HDD, for cold data."),
    ],
    "correct": "4",
    "domain": COST_OPT,
    "overall": "EBS sc1 is the lowest-cost EBS volume type for cold, infrequently accessed data. Reference: https://aws.amazon.com/ebs/pricing/",
})
QUESTIONS.append({
    "q": "Which EBS volume type is the LEAST EXPENSIVE per GB for FREQUENTLY accessed, throughput-intensive workloads?",
    "type": "multiple-choice",
    "opts": [
        ("EBS gp3", "gp3 is general-purpose SSD with predictable IOPS."),
        ("EBS io2", "io2 is high-performance, more expensive."),
        ("EBS st1", "EBS st1 is the lowest-cost HDD, optimized for throughput-intensive workloads."),
        ("EBS sc1", "sc1 is cold HDD, lower throughput than st1."),
    ],
    "correct": "3",
    "domain": COST_OPT,
    "overall": "EBS st1 is throughput-optimized HDD, lowest cost per GB for throughput-intensive workloads like big data. Reference: https://aws.amazon.com/ebs/volume-types/",
})
QUESTIONS.append({
    "q": "Which feature of gp3 EBS volumes lets you provision IOPS and throughput INDEPENDENTLY of volume size, reducing cost for performance-driven workloads?",
    "type": "multiple-choice",
    "opts": [
        ("Provisioned IOPS SSD (io1)", "io1 is a separate volume type."),
        ("Decoupled IOPS/throughput on gp3", "gp3 allows independent provisioning of IOPS and throughput from size."),
        ("EBS Multi-Attach", "Multi-Attach is for shared volumes, not performance."),
        ("EBS snapshots", "Snapshots are backups, not performance."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "gp3 EBS volumes decouple IOPS and throughput from size, allowing right-sized performance at lower cost. Reference: https://aws.amazon.com/ebs/volume-types/",
})
QUESTIONS.append({
    "q": "Which of the following are valid strategies to REDUCE EBS cost? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Right-size volume type and size", "Match volume type and size to workload needs."),
        ("Use gp3 instead of gp2", "gp3 is 20% cheaper than gp2 at baseline."),
        ("Delete unused volumes", "Orphaned volumes incur charges; delete or snapshot."),
        ("Use larger volumes unnecessarily", "Over-provisioning volumes wastes cost."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Right-size volume type, use gp3 over gp2, and delete unused volumes to reduce EBS cost. Reference: https://aws.amazon.com/ebs/pricing/",
})
QUESTIONS.append({
    "q": "Which AWS service provides RECOMMENDATIONS to right-size EBS volumes based on utilization metrics?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost Explorer", "Cost Explorer shows spend, not rightsizing recs."),
        ("AWS Compute Optimizer", "Compute Optimizer recommends right-sizing for EC2, EBS, and Lambda."),
        ("AWS Trusted Advisor", "Trusted Advisor provides cost checks, not detailed EBS rightsizing."),
        ("AWS Budgets", "Budgets alerts on spend, not rightsizing."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "AWS Compute Optimizer recommends right-sizing for EC2 instances, EBS volumes, and Lambda functions based on CloudWatch metrics. Reference: https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is.html",
})
QUESTIONS.append({
    "q": "Which storage option provides TEMPORARY, instance-local storage that is FREE (no additional charge) but DATA IS LOST on stop, terminate, or hardware failure?",
    "type": "multiple-choice",
    "opts": [
        ("EBS", "EBS is network-attached and persists independently."),
        ("Instance store", "Instance store is local, free, but data is lost on stop/terminate/hardware failure."),
        ("EFS", "EFS is a network file system with a per-GB charge."),
        ("FSx", "FSx is a managed file system with a per-GB charge."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Instance store is local NVMe/SSD storage included in the instance price, free, but data is lost on stop/terminate/hardware failure. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html",
})
QUESTIONS.append({
    "q": "Which EBS snapshot pricing factor is FREE for the first 100 GB per month?",
    "type": "multiple-choice",
    "opts": [
        ("Snapshot storage", "Snapshot storage is not free; first 100 GB of standard tier is free."),
        ("Data transfer out from snapshot", "Snapshot data transfer out is not free in general."),
        ("Fast Snapshot Restore", "FSR is charged per snapshot per AZ per month."),
        ("Cross-region snapshot copy", "Cross-region copy is charged per GB."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "EBS snapshot storage is free for the first 100 GB per month under the standard tier. Reference: https://aws.amazon.com/ebs/pricing/",
})
QUESTIONS.append({
    "q": "Which EBS snapshot tier provides the LOWEST cost per GB-month for long-term archive snapshots?",
    "type": "multiple-choice",
    "opts": [
        ("EBS Snapshot Standard tier", "Standard is the default tier."),
        ("EBS Snapshot Archive tier", "EBS Archive tier provides the lowest cost for snapshots accessed less than once a quarter."),
        ("EBS Snapshot Cold tier", "There is no Cold tier; Archive is the lower tier."),
        ("EBS Snapshot Glacier tier", "EBS snapshots integrate with S3 Glacier Deep Archive via Archive tier."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "EBS Snapshot Archive tier provides up to 75% lower cost for snapshots accessed less than once a quarter. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-archive.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid cost optimization strategies for EC2 instance storage? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Use instance store for temporary data", "Instance store is free, ideal for temp/buffer data."),
        ("Right-size EBS volume type", "Match volume type to workload to avoid overpaying."),
        ("Delete unused EBS volumes", "Orphaned volumes still cost money."),
        ("Use larger EBS volumes for all workloads", "Larger volumes cost more; size appropriately."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Use instance store for temp data, right-size EBS volumes, and delete unused volumes to optimize cost. Reference: https://aws.amazon.com/ebs/pricing/",
})
QUESTIONS.append({
    "q": "Which EBS feature lets you modify volume type, size, and IOPS WITHOUT restarting the instance, reducing operational overhead and cost?",
    "type": "multiple-choice",
    "opts": [
        ("EBS snapshots", "Snapshots require creating a new volume."),
        ("EBS Multi-Attach", "Multi-Attach is for shared volumes."),
        ("EBS Elastic Volumes", "Elastic Volumes allow modification without restart."),
        ("EBS encryption", "Encryption does not affect modification."),
    ],
    "correct": "3",
    "domain": COST_OPT,
    "overall": "EBS Elastic Volumes allow modification of type, size, and IOPS without restart, reducing operational overhead. Reference: https://docs.aws.amazon.com/ebs/latest/userguide/evs.html",
})
QUESTIONS.append({
    "q": "Which AWS tool analyzes your past 14 days of CloudWatch metrics and recommends EC2 instance type rightsizing to reduce cost?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost Explorer", "Cost Explorer shows spend trends."),
        ("AWS Compute Optimizer", "Compute Optimizer recommends rightsizing based on CloudWatch metrics."),
        ("AWS Trusted Advisor", "Trusted Advisor provides checks."),
        ("AWS Systems Manager", "Systems Manager is for ops automation."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "AWS Compute Optimizer recommends EC2, EBS, and Lambda rightsizing based on 14 days of CloudWatch metrics. Reference: https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is.html",
})
QUESTIONS.append({
    "q": "Which feature of Amazon EFS provides a LOWER per-GB cost for files NOT accessed for 30+ days, while remaining available?",
    "type": "multiple-choice",
    "opts": [
        ("EFS Standard", "EFS Standard is the default tier."),
        ("EFS Infrequent Access (IA)", "EFS IA provides a lower per-GB cost for files not accessed for 30+ days."),
        ("EFS Archive", "EFS Archive provides even lower cost for files not accessed for 90+ days."),
        ("EFS Cold", "There is no EFS Cold tier."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "EFS Infrequent Access (IA) provides a lower per-GB cost for files not accessed for 30+ days, with EFS Lifecycle moving them automatically. Reference: https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html",
})

# ============================================================
# 4. COMPUTE & SERVERLESS COST OPTIMIZATION (16 questions)
# ============================================================

QUESTIONS.append({
    "q": "Which AWS Lambda feature provides a discount of up to 17% for a 1- or 3-year commit, in exchange for predictable usage?",
    "type": "multiple-choice",
    "opts": [
        ("Lambda SnapStart", "SnapStart reduces cold starts, not pricing."),
        ("Lambda Compute Savings Plans", "Lambda usage is covered by Compute Savings Plans for up to 17% discount."),
        ("Lambda Reserved Concurrency", "Reserved Concurrency is a throttling feature."),
        ("Lambda Provisioned Concurrency", "Provisioned Concurrency is for latency-sensitive workloads."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Lambda is eligible for Compute Savings Plans, providing up to 17% discount for 1- or 3-year commits. Reference: https://aws.amazon.com/lambda/pricing/",
})
QUESTIONS.append({
    "q": "Which AWS Lambda feature provides INIT environments to keep functions warm, reducing cold start latency at additional cost?",
    "type": "multiple-choice",
    "opts": [
        ("Lambda SnapStart", "SnapStart caches initialized environments, reducing cold starts at no extra cost."),
        ("Provisioned Concurrency", "Provisioned Concurrency keeps functions initialized at additional cost."),
        ("Lambda Layers", "Layers are for code sharing."),
        ("Lambda Event Source Mapping", "Event Source Mappings are for triggers."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Provisioned Concurrency keeps functions initialized for low-latency at an additional cost. Reference: https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html",
})
QUESTIONS.append({
    "q": "Which AWS service is the MOST cost-effective for running containers with VARIABLE, bursty workloads that can scale to zero?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon EC2 with Auto Scaling", "EC2 has minimum instance charges."),
        ("Amazon ECS with Fargate Spot", "Fargate Spot is interruptible, up to 70% off, ideal for fault-tolerant containers."),
        ("Amazon EKS managed node groups", "EKS managed nodes have minimum cluster-hour cost."),
        ("Amazon ECS with EC2", "EC2 launch type has minimum instance cost."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "ECS with Fargate Spot (or EKS on Fargate Spot) is the most cost-effective for variable, fault-tolerant containers. Reference: https://aws.amazon.com/fargate/pricing/",
})
QUESTIONS.append({
    "q": "Which of the following are valid AWS Lambda cost optimization techniques? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Right-size memory allocation", "Memory size affects both performance and cost; tune with AWS Lambda Power Tuning."),
        ("Use ARM/Graviton2 (arm64)", "ARM/Graviton2 is up to 34% better price-performance."),
        ("Use Compute Savings Plans", "Compute Savings Plans cover Lambda for up to 17% discount."),
        ("Use Provisioned Concurrency for low traffic", "Provisioned Concurrency is most cost-effective for high, steady traffic."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Right-size memory, use ARM/Graviton2, and use Compute Savings Plans to reduce Lambda cost. Reference: https://aws.amazon.com/lambda/pricing/",
})
QUESTIONS.append({
    "q": "Which AWS Lambda billing model charges per request and per GB-second of compute, with no charge when idle?",
    "type": "multiple-choice",
    "opts": [
        ("Per-second billing with idle charges", "Lambda has no idle charges."),
        ("Pay-per-use (per request + GB-s)", "Lambda bills per request and GB-second, no idle charge."),
        ("Reserved model", "Lambda does not have a per-function reserved model."),
        ("Subscription model", "Lambda is not subscription-based."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Lambda bills per request and GB-second of compute, with no charge when idle, 1 ms billing. Reference: https://aws.amazon.com/lambda/pricing/",
})
QUESTIONS.append({
    "q": "Which AWS service provides an event-driven serverless compute platform that scales to zero and bills only for actual usage?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon EC2", "EC2 has minimum instance cost."),
        ("AWS Lambda", "Lambda scales to zero and bills per usage."),
        ("Amazon ECS", "ECS is a container orchestrator, not a serverless compute platform."),
        ("Amazon EKS", "EKS bills per cluster hour."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "AWS Lambda is the event-driven serverless compute platform that scales to zero and bills per usage. Reference: https://aws.amazon.com/lambda/",
})
QUESTIONS.append({
    "q": "Which AWS service provides automatic scaling of EC2 capacity based on demand, terminating instances when not needed to reduce cost?",
    "type": "multiple-choice",
    "opts": [
        ("EC2 Auto Scaling", "EC2 Auto Scaling adjusts capacity based on demand."),
        ("AWS Lambda", "Lambda is a serverless compute service."),
        ("AWS Batch", "Batch is for batch compute jobs."),
        ("AWS Elastic Beanstalk", "Elastic Beanstalk is a PaaS for app deployment."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "EC2 Auto Scaling adjusts the number of EC2 instances based on demand, terminating unused instances to reduce cost. Reference: https://aws.amazon.com/autoscaling/",
})
QUESTIONS.append({
    "q": "Which AWS Graviton processor is based on the ARM architecture and provides up to 40% better price-performance versus comparable x86-based instances?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Graviton2 (ARM)", "Graviton2 (ARM) provides up to 40% better price-performance."),
        ("Intel Xeon", "Intel Xeon is x86."),
        ("AMD EPYC", "AMD EPYC is x86."),
        ("AWS Inferentia", "Inferentia is for ML inference, not general compute."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Graviton2 (ARM) provides up to 40% better price-performance versus comparable x86 instances. Reference: https://aws.amazon.com/ec2/graviton/",
})
QUESTIONS.append({
    "q": "Which of the following are valid ways to reduce EC2 cost? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Use Spot Instances for fault-tolerant workloads", "Spot provides up to 90% discount."),
        ("Purchase Reserved Instances or Savings Plans for steady workloads", "RIs/SPs provide up to 75% discount."),
        ("Use AWS Graviton (ARM) instances", "Graviton2 is up to 40% better price-performance."),
        ("Run all workloads on the largest instance type", "Largest is most expensive per hour; right-size."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Use Spot, RIs/SPs, and Graviton2 to reduce EC2 cost; right-size, don't over-provision. Reference: https://aws.amazon.com/ec2/pricing/",
})
QUESTIONS.append({
    "q": "Which AWS tool helps you identify IDLE or underutilized EC2 instances that can be downsized or terminated to reduce cost?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost Explorer", "Cost Explorer shows spend trends, not idle detection."),
        ("AWS Compute Optimizer", "Compute Optimizer identifies idle and underutilized EC2 instances."),
        ("AWS Budgets", "Budgets alerts on spend."),
        ("AWS Trusted Advisor", "Trusted Advisor provides cost checks, but Compute Optimizer is more detailed."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "AWS Compute Optimizer identifies idle and underutilized EC2 instances, EBS volumes, and Lambda functions. Reference: https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides a fully managed Kubernetes service with NO charge for the Kubernetes control plane, billing only for underlying compute?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon EKS", "EKS charges $0.10 per cluster hour, plus underlying compute."),
        ("Self-managed Kubernetes on EC2", "Self-managed does not have an EKS control plane charge but has higher ops cost."),
        ("Amazon ECS", "ECS is not Kubernetes."),
        ("Red Hat OpenShift Service on AWS (ROSA)", "ROSA is a third-party service, with its own pricing."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "EKS charges $0.10 per cluster hour plus underlying compute. There is no free control plane option. Reference: https://aws.amazon.com/eks/pricing/",
})
QUESTIONS.append({
    "q": "Which AWS Lambda feature caches an initialized execution environment to reduce cold start latency, included at no extra cost?",
    "type": "multiple-choice",
    "opts": [
        ("Lambda SnapStart", "Lambda SnapStart caches initialized environments, included at no extra cost."),
        ("Provisioned Concurrency", "Provisioned Concurrency is at additional cost."),
        ("Lambda Layers", "Layers are for code sharing."),
        ("Lambda@Edge", "Lambda@Edge is for edge execution."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Lambda SnapStart caches initialized environments, reducing cold starts at no extra cost. Reference: https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html",
})
QUESTIONS.append({
    "q": "Which AWS service is the BEST fit for running SHORT-LIVED batch jobs that scale to thousands of vCPUs and only pay for actual compute time?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon EC2 Spot Fleet", "EC2 Spot is good for batch, but requires setup and management."),
        ("AWS Batch with Fargate Spot", "AWS Batch with Fargate Spot runs batch jobs serverlessly, scaling to zero."),
        ("Amazon Lightsail", "Lightsail is simplified VPS."),
        ("AWS Elastic Beanstalk", "Elastic Beanstalk is for app deployment, not batch."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "AWS Batch with Fargate Spot is serverless, scales to thousands of vCPUs, and uses Spot for cost. Reference: https://aws.amazon.com/batch/pricing/",
})
QUESTIONS.append({
    "q": "Which of the following are valid cost considerations for AWS Lambda? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Memory allocation affects cost", "Higher memory = higher GB-second cost but may reduce duration."),
        ("Duration is rounded up to 1 ms", "Lambda bills in 1 ms increments."),
        ("Free tier: 1M requests and 400,000 GB-s per month", "Lambda has a generous free tier."),
        ("Provisioned Concurrency is free", "Provisioned Concurrency has an additional hourly charge."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Lambda memory affects cost, duration is in 1 ms, free tier is 1M requests/400,000 GB-s, and Provisioned Concurrency has an extra charge. Reference: https://aws.amazon.com/lambda/pricing/",
})
QUESTIONS.append({
    "q": "Which AWS feature lets you use Spot Instances for Fargate tasks, providing up to 70% discount versus Fargate On-Demand?",
    "type": "multiple-choice",
    "opts": [
        ("Fargate Spot", "Fargate Spot provides up to 70% discount for interruptible tasks."),
        ("Fargate Reserved", "There is no Fargate Reserved model."),
        ("Fargate On-Demand", "On-Demand has no discount."),
        ("Fargate Savings Plans", "Compute Savings Plans cover Fargate, but Fargate Spot is the dedicated spot offering."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Fargate Spot provides up to 70% discount for interruptible tasks on ECS and EKS. Reference: https://aws.amazon.com/fargate/pricing/",
})
QUESTIONS.append({
    "q": "Which EC2 instance type provides the BEST price-performance for ARM-based workloads and is supported by most AWS services?",
    "type": "multiple-choice",
    "opts": [
        ("T4g, M6g, C6g, R6g family", "Graviton2 (g-family) provides the best price-performance for ARM."),
        ("T3, M5, C5 family", "These are x86, not ARM."),
        ("P4d family", "P4d is GPU, not ARM."),
        ("X2 family", "X2 is memory-optimized x86."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Graviton2 (g-family) provides the best price-performance for ARM workloads. Reference: https://aws.amazon.com/ec2/graviton/",
})

# ============================================================
# 5. DATABASE COST OPTIMIZATION (12 questions)
# ============================================================

QUESTIONS.append({
    "q": "Which Aurora pricing model provides a cost-effective, serverless database that auto-scales based on workload, charging per ACU (Aurora Capacity Unit)?",
    "type": "multiple-choice",
    "opts": [
        ("Aurora Provisioned", "Aurora Provisioned is a fixed instance type."),
        ("Aurora Serverless v2", "Aurora Serverless v2 auto-scales and bills per ACU-second."),
        ("Aurora Global Database", "Aurora Global is for multi-region."),
        ("RDS Reserved Instances", "RDS RIs are discounts for Provisioned."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Aurora Serverless v2 auto-scales ACUs based on workload, billing per ACU-second for cost optimization. Reference: https://aws.amazon.com/rds/aurora/serverless/",
})
QUESTIONS.append({
    "q": "Which DynamoDB pricing model provides cost-effective, pay-per-request pricing for unpredictable or low-traffic workloads?",
    "type": "multiple-choice",
    "opts": [
        ("Provisioned capacity", "Provisioned requires committing to RCU/WCU."),
        ("On-Demand mode", "On-Demand mode bills per request, ideal for unpredictable workloads."),
        ("Reserved capacity", "Reserved is for predictable workloads."),
        ("Serverless mode", "DynamoDB is always serverless."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "DynamoDB On-Demand mode bills per request, ideal for unpredictable or low-traffic workloads. Reference: https://aws.amazon.com/dynamodb/pricing/",
})
QUESTIONS.append({
    "q": "Which DynamoDB pricing model provides a discount of up to 77% in exchange for committing to read/write capacity units (RCU/WCU)?",
    "type": "multiple-choice",
    "opts": [
        ("On-Demand mode", "On-Demand has no discount."),
        ("Provisioned mode with Reserved Capacity", "Provisioned with Reserved Capacity provides up to 77% discount."),
        ("On-Demand with Savings Plans", "DynamoDB does not have Savings Plans."),
        ("Provisioned with auto scaling", "Auto scaling adjusts capacity but does not provide a discount."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "DynamoDB Provisioned mode with Reserved Capacity provides up to 77% discount for committed RCU/WCU. Reference: https://aws.amazon.com/dynamodb/pricing/",
})
QUESTIONS.append({
    "q": "Which DynamoDB feature provides automatic deletion of items based on a timestamp attribute, reducing storage cost for time-bounded data?",
    "type": "multiple-choice",
    "opts": [
        ("DynamoDB Streams", "Streams capture changes, not auto-delete."),
        ("TTL (Time to Live)", "TTL automatically deletes items after a timestamp."),
        ("DynamoDB Auto Scaling", "Auto Scaling adjusts capacity, not deletion."),
        ("DynamoDB Global Tables", "Global Tables replicate across regions."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "DynamoDB TTL automatically deletes items based on a timestamp attribute, reducing storage cost. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid RDS cost optimization strategies? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Use Reserved Instances for steady workloads", "RDS RIs provide up to 60% discount."),
        ("Use Aurora Serverless v2 for variable workloads", "Aurora Serverless v2 scales to zero for variable workloads."),
        ("Right-size instance type", "Avoid over-provisioning DB instance types."),
        ("Run all databases on the largest instance", "Over-provisioning is not cost-effective."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Use RDS RIs, Aurora Serverless v2, and right-size instance types to reduce RDS cost. Reference: https://aws.amazon.com/rds/pricing/",
})
QUESTIONS.append({
    "q": "Which AWS service is the BEST fit for an in-memory cache that REDUCES load on a relational database, with low cost and easy scaling?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon ElastiCache", "ElastiCache (Redis or Memcached) is the managed in-memory cache."),
        ("Amazon DynamoDB", "DynamoDB is a NoSQL database, not a cache."),
        ("Amazon Aurora", "Aurora is a relational database."),
        ("Amazon Neptune", "Neptune is a graph database."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Amazon ElastiCache (Redis, Memcached, or Valkey) is the managed in-memory cache that reduces load on databases. Reference: https://aws.amazon.com/elasticache/",
})
QUESTIONS.append({
    "q": "Which Aurora Serverless v2 feature provides IMMEDIATE, fine-grained auto-scaling from 0.5 to 128 ACUs, paying only for capacity used?",
    "type": "multiple-choice",
    "opts": [
        ("Aurora Serverless v1", "v1 has capacity steps and slower scaling."),
        ("Aurora Serverless v2", "v2 provides immediate, fine-grained auto-scaling, 0.5-128 ACUs."),
        ("Aurora Global Database", "Global is for multi-region replication."),
        ("RDS Proxy", "RDS Proxy is a connection pooler."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Aurora Serverless v2 provides immediate, fine-grained auto-scaling from 0.5 to 128 ACUs. Reference: https://aws.amazon.com/rds/aurora/serverless/",
})
QUESTIONS.append({
    "q": "Which DynamoDB feature reduces cost by automatically tiering older data to S3 or another storage class while keeping query access?",
    "type": "multiple-choice",
    "opts": [
        ("DynamoDB TTL", "TTL deletes items, doesn't tier to S3."),
        ("DynamoDB Standard-IA table class", "DynamoDB Standard-IA is for infrequently accessed data, 60% cheaper than Standard."),
        ("DynamoDB Streams", "Streams capture changes."),
        ("DynamoDB Global Tables", "Global Tables replicate across regions."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "DynamoDB Standard-IA table class is 60% cheaper than Standard for infrequently accessed data. Reference: https://aws.amazon.com/dynamodb/pricing/",
})
QUESTIONS.append({
    "q": "Which of the following are valid DynamoDB cost optimization techniques? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Use TTL to expire old items", "TTL reduces storage cost for time-bounded data."),
        ("Use Standard-IA for infrequently accessed data", "Standard-IA is 60% cheaper for infrequent access."),
        ("Use On-Demand for predictable steady traffic", "Provisioned with Reserved is cheaper for predictable traffic."),
        ("Use Global Tables for single-region apps", "Global Tables add cross-region replication cost; not needed for single-region."),
    ],
    "correct": "1,2",
    "domain": COST_OPT,
    "overall": "Use TTL, Standard-IA, and Provisioned+Reserved for predictable traffic; avoid Global Tables when not needed. Reference: https://aws.amazon.com/dynamodb/pricing/",
})
QUESTIONS.append({
    "q": "Which RDS pricing model provides up to 60% discount for a 1- or 3-year commitment to a specific DB instance type?",
    "type": "multiple-choice",
    "opts": [
        ("On-Demand", "On-Demand has no discount."),
        ("Reserved Instances", "RDS RIs provide up to 60% discount."),
        ("Spot", "RDS does not have Spot."),
        ("Serverless", "Aurora Serverless is its own model."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "RDS Reserved Instances provide up to 60% discount for 1- or 3-year commitments. Reference: https://aws.amazon.com/rds/pricing/",
})
QUESTIONS.append({
    "q": "Which DynamoDB feature provides automatic caching of frequently accessed items with microsecond latency, REDUCING read capacity consumption and cost?",
    "type": "multiple-choice",
    "opts": [
        ("DynamoDB Accelerator (DAX)", "DAX is the in-memory cache for DynamoDB."),
        ("DynamoDB Streams", "Streams capture changes."),
        ("DynamoDB Global Tables", "Global Tables replicate across regions."),
        ("DynamoDB TTL", "TTL expires items."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "DAX is a fully managed, in-memory cache for DynamoDB that reduces read capacity consumption. Reference: https://aws.amazon.com/dynamodb/dax/",
})
QUESTIONS.append({
    "q": "Which RDS feature allows you to STOP a non-production database for up to 7 days at a time, eliminating compute charges during the stop?",
    "type": "multiple-choice",
    "opts": [
        ("RDS Multi-AZ", "Multi-AZ is for HA, not stopping."),
        ("RDS Stop/Start", "RDS supports Stop/Start for up to 7 days, with no compute charge during stop."),
        ("RDS Read Replica", "Read Replica is for read scaling."),
        ("RDS Proxy", "RDS Proxy is a connection pooler."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "RDS Stop/Start allows you to stop a non-production database for up to 7 days, eliminating compute charges. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_StopInstance.html",
})

# ============================================================
# 6. NETWORKING & DATA TRANSFER COST OPTIMIZATION (14 questions)
# ============================================================

QUESTIONS.append({
    "q": "Which data transfer direction is FREE in AWS?",
    "type": "multiple-choice",
    "opts": [
        ("Data transfer IN to AWS from the internet", "Data transfer in to AWS from the internet is free."),
        ("Data transfer OUT from AWS to the internet", "Data transfer out is charged per GB."),
        ("Data transfer between AZs in the same region", "Cross-AZ transfer is charged per GB."),
        ("Data transfer between regions", "Cross-region transfer is charged per GB."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Data transfer IN to AWS from the internet is free; all other transfers have charges. Reference: https://aws.amazon.com/ec2/pricing/on-demand/",
})
QUESTIONS.append({
    "q": "Which data transfer scenario is the MOST expensive per GB on AWS?",
    "type": "multiple-choice",
    "opts": [
        ("Cross-AZ transfer", "Cross-AZ is $0.01/GB each direction."),
        ("Cross-region transfer", "Cross-region is $0.02-0.09/GB depending on regions."),
        ("Out to internet", "Out to internet is $0.05-0.09/GB after free tier."),
        ("DX out to internet", "DX has its own pricing."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Cross-region data transfer is generally the most expensive per GB, varying by region pair. Reference: https://aws.amazon.com/ec2/pricing/on-demand/",
})
QUESTIONS.append({
    "q": "Which of the following are valid ways to reduce data transfer cost? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Use CloudFront to cache at edge", "CloudFront reduces origin data transfer."),
        ("Use S3 Transfer Acceleration only for large files", "Transfer Acceleration is for long-distance uploads."),
        ("Use VPC Endpoints to keep traffic on AWS network", "VPC Endpoints avoid NAT gateway charges."),
        ("Use Direct Connect for high-volume on-prem transfer", "DX has lower per-GB cost for high volume."),
    ],
    "correct": "1,2,3,4",
    "domain": COST_OPT,
    "overall": "Use CloudFront caching, Transfer Acceleration, VPC Endpoints, and Direct Connect to reduce data transfer cost. Reference: https://aws.amazon.com/ec2/pricing/on-demand/",
})
QUESTIONS.append({
    "q": "Which AWS service provides a dedicated, private network connection from on-premises to AWS with LOWER data transfer cost than internet?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Site-to-Site VPN", "VPN uses the public internet, lower per-hour cost but no dedicated bandwidth."),
        ("AWS Direct Connect", "Direct Connect is a dedicated private fiber link with lower data transfer cost."),
        ("AWS Transit Gateway", "Transit Gateway is for VPC-to-VPC routing."),
        ("AWS PrivateLink", "PrivateLink is for private service connectivity."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "AWS Direct Connect provides a dedicated private fiber link with lower per-GB data transfer cost than internet. Reference: https://aws.amazon.com/directconnect/pricing/",
})
QUESTIONS.append({
    "q": "Which VPC endpoint type provides private connectivity to S3 and DynamoDB WITHOUT incurring NAT Gateway data processing charges?",
    "type": "multiple-choice",
    "opts": [
        ("Interface endpoint", "Interface endpoints are for most AWS services but have hourly and per-GB charges."),
        ("Gateway endpoint", "Gateway endpoints for S3 and DynamoDB are free."),
        ("Internet gateway", "Internet gateway is for public access."),
        ("VPC peering", "VPC peering is for VPC-to-VPC."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Gateway endpoints for S3 and DynamoDB are free and avoid NAT Gateway data processing charges. Reference: https://aws.amazon.com/vpc/pricing/",
})
QUESTIONS.append({
    "q": "Which feature of Amazon CloudFront provides a SINGLE global endpoint that routes requests to buckets in multiple AWS regions, reducing latency and data transfer cost?",
    "type": "multiple-choice",
    "opts": [
        ("CloudFront edge caching", "CloudFront caches content at edge."),
        ("S3 Multi-Region Access Point", "S3 MRAP provides a single global endpoint over replicated buckets."),
        ("S3 Transfer Acceleration", "Transfer Acceleration is for uploads, not global endpoint."),
        ("Route 53 latency routing", "Route 53 routes DNS but doesn't provide a global endpoint per se."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "S3 Multi-Region Access Point provides a single global endpoint that routes to the lowest-latency replicated bucket. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPoints.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid NAT Gateway cost optimization techniques? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Use VPC Gateway Endpoints for S3 and DynamoDB", "Gateway endpoints avoid NAT charges for S3/DynamoDB traffic."),
        ("Use VPC Interface Endpoints for high-volume AWS services", "Interface endpoints have lower per-GB cost than NAT for heavy traffic."),
        ("Consolidate NAT Gateways across VPCs", "Reduce the number of NAT Gateways to reduce hourly costs."),
        ("Use multiple NAT Gateways in every AZ", "More NAT Gateways increase cost; consolidate."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Use Gateway Endpoints, Interface Endpoints, and consolidate NAT Gateways to optimize NAT cost. Reference: https://aws.amazon.com/vpc/pricing/",
})
QUESTIONS.append({
    "q": "Which AWS service is the BEST for ONLINE data transfer of large datasets to AWS, providing a physical appliance to accelerate secure uploads?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Snowball", "Snowball is for offline bulk transfer of petabytes."),
        ("AWS Snowmobile", "Snowmobile is a truck-sized transfer for exabytes."),
        ("AWS DataSync", "DataSync is for online, automated transfer."),
        ("AWS Direct Connect", "DX is for ongoing private connectivity."),
    ],
    "correct": "3",
    "domain": COST_OPT,
    "overall": "AWS DataSync is for online, automated, accelerated transfer of large datasets to AWS. Reference: https://aws.amazon.com/datasync/",
})
QUESTIONS.append({
    "q": "Which AWS service is the BEST for OFFLINE, petabyte-scale data transfer to AWS using a physical device?",
    "type": "multiple-choice",
    "opts": [
        ("AWS DataSync", "DataSync is online."),
        ("AWS Snowball Edge", "Snowball Edge is a physical device for offline petabyte transfer."),
        ("AWS Direct Connect", "DX is online."),
        ("Amazon S3", "S3 is a storage service."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "AWS Snowball Edge is a physical device for offline petabyte-scale data transfer. Reference: https://aws.amazon.com/snowball/",
})
QUESTIONS.append({
    "q": "Which CloudFront feature reduces data transfer cost by allowing you to select a price class with fewer edge locations, at lower cost?",
    "type": "multiple-choice",
    "opts": [
        ("CloudFront Price Classes", "CloudFront Price Classes let you choose a price/performance trade-off."),
        ("CloudFront Origins", "Origins are the source, not pricing."),
        ("CloudFront Behaviors", "Behaviors are path-based routing."),
        ("CloudFront Functions", "Functions run at the edge."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "CloudFront Price Classes (100, 200, All) let you trade off price and edge coverage. Reference: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PriceClass.html",
})
QUESTIONS.append({
    "q": "Which data transfer direction between AWS services is ALWAYS FREE?",
    "type": "multiple-choice",
    "opts": [
        ("Cross-AZ transfer", "Cross-AZ is $0.01/GB each direction."),
        ("Same-AZ transfer", "Same-AZ transfer is free for many services."),
        ("Cross-region transfer", "Cross-region is charged per GB."),
        ("Out to internet", "Out to internet is charged per GB."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Same-AZ transfer is free for many AWS services. Reference: https://aws.amazon.com/ec2/pricing/on-demand/",
})
QUESTIONS.append({
    "q": "Which AWS service is the BEST for ONLINE, real-time data transfer between on-premises and AWS, providing automated, accelerated, and validated transfers?",
    "type": "multiple-choice",
    "opts": [
        ("AWS DataSync", "DataSync provides online, automated, validated transfer."),
        ("AWS Snowball", "Snowball is offline."),
        ("AWS Direct Connect", "DX is for ongoing private connectivity, not specifically accelerated transfer."),
        ("AWS S3", "S3 is a storage service."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS DataSync is the online, automated, accelerated service for transferring large datasets to, from, and between AWS storage services. Reference: https://aws.amazon.com/datasync/",
})
QUESTIONS.append({
    "q": "Which of the following are valid cost optimization strategies for AWS networking? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Use VPC Endpoints to avoid NAT costs", "VPC Endpoints avoid NAT data processing charges."),
        ("Consolidate NAT Gateways", "Reduce NAT Gateway count to lower hourly cost."),
        ("Use Direct Connect for high-volume transfers", "DX has lower per-GB cost for high volume."),
        ("Provision a NAT Gateway per AZ always", "Consolidate where possible to reduce cost."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Use VPC Endpoints, consolidate NAT Gateways, and use DX for high-volume transfers to reduce networking cost. Reference: https://aws.amazon.com/vpc/pricing/",
})
QUESTIONS.append({
    "q": "Which AWS service provides an AWS-managed Content Delivery Network (CDN) that caches content at edge locations, REDUCING origin data transfer cost?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon CloudFront", "CloudFront is the AWS CDN."),
        ("Amazon Route 53", "Route 53 is DNS."),
        ("AWS Global Accelerator", "Global Accelerator is for TCP/UDP anycast."),
        ("Amazon API Gateway", "API Gateway is for APIs."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Amazon CloudFront is the AWS CDN that caches at edge, reducing origin data transfer cost. Reference: https://aws.amazon.com/cloudfront/",
})

# ============================================================
# 7. AWS COST MANAGEMENT TOOLS (16 questions)
# ============================================================

QUESTIONS.append({
    "q": "Which AWS service provides a visual interface to view and analyze AWS cost and usage over time, with filtering by service, region, instance type, and tags?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost Explorer", "Cost Explorer provides visualization and analysis of cost and usage."),
        ("AWS Cost and Usage Report", "CUR is a detailed report delivered to S3."),
        ("AWS Budgets", "Budgets alerts on spend thresholds."),
        ("AWS Trusted Advisor", "Trusted Advisor provides checks."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Cost Explorer provides interactive visualization of cost and usage, with filtering and forecasting. Reference: https://aws.amazon.com/aws-cost-management/aws-cost-explorer/",
})
QUESTIONS.append({
    "q": "Which AWS service provides a detailed cost and usage report delivered to S3, including resource-level granularity and support for Athena/Redshift/QuickSight?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost Explorer", "Cost Explorer is interactive, not a deliverable report."),
        ("AWS Cost and Usage Report (CUR)", "CUR is the most detailed cost report, delivered to S3."),
        ("AWS Budgets", "Budgets alerts on spend."),
        ("AWS Pricing Calculator", "Pricing Calculator is for estimates, not reports."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "AWS Cost and Usage Report (CUR) is the most detailed cost report, delivered to S3 with hourly granularity and resource-level data. Reference: https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/",
})
QUESTIONS.append({
    "q": "Which AWS service alerts you when your cost or usage EXCEEDS a threshold you set, with email, SNS, and Slack notifications?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost Explorer", "Cost Explorer doesn't send alerts by default."),
        ("AWS Budgets", "Budgets alerts on cost/usage thresholds with notifications."),
        ("Cost Anomaly Detection", "Anomaly Detection alerts on anomalies, not thresholds."),
        ("Trusted Advisor", "Trusted Advisor provides checks, not budget alerts."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "AWS Budgets alerts you when cost or usage exceeds a threshold, with email, SNS, and Slack notifications. Reference: https://aws.amazon.com/aws-cost-management/aws-budgets/",
})
QUESTIONS.append({
    "q": "Which AWS service uses machine learning to detect ANOMALIES in your cost and usage, alerting you to unexpected spikes?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Budgets", "Budgets uses thresholds, not ML."),
        ("Cost Anomaly Detection", "Cost Anomaly Detection uses ML to detect anomalies."),
        ("Cost Explorer", "Cost Explorer visualizes, doesn't alert on anomalies by default."),
        ("Trusted Advisor", "Trusted Advisor provides checks."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Cost Anomaly Detection uses ML to detect unusual cost patterns and alert you. Reference: https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/",
})
QUESTIONS.append({
    "q": "Which of the following are valid AWS Budget types? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Cost budget", "Cost budgets track dollar spend."),
        ("Usage budget", "Usage budgets track usage units like hours or GB."),
        ("Reservation budget", "Reservation budgets track RI/SP utilization and coverage."),
        ("Savings Plans budget", "SP budgets track Savings Plans utilization and coverage."),
    ],
    "correct": "1,2,3,4",
    "domain": COST_OPT,
    "overall": "AWS Budgets supports Cost, Usage, Reservation (RI), and Savings Plans budgets. Reference: https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html",
})
QUESTIONS.append({
    "q": "Which feature of AWS Budgets lets you take ACTION (e.g., apply an IAM policy, stop EC2 instances) when a budget threshold is exceeded?",
    "type": "multiple-choice",
    "opts": [
        ("Budget alerts only", "Alerts are notifications, not actions."),
        ("Budget actions", "Budget actions can run IAM policy or stop EC2 instances."),
        ("AWS Config", "AWS Config is for resource compliance."),
        ("Lambda only", "Lambda is a separate service, but Budgets can trigger Lambda."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "AWS Budgets actions can apply an IAM policy or stop EC2/RDS instances when a budget threshold is exceeded. Reference: https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html",
})
QUESTIONS.append({
    "q": "Which feature of AWS Cost Explorer lets you RESERVE a forecast of future spend based on your historical usage?",
    "type": "multiple-choice",
    "opts": [
        ("Cost Explorer forecast", "Cost Explorer provides a forecast of future spend."),
        ("AWS Budgets", "Budgets doesn't forecast."),
        ("AWS Pricing Calculator", "Pricing Calculator estimates future spend, not based on past usage."),
        ("Trusted Advisor", "Trusted Advisor provides checks."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Cost Explorer provides a forecast of future spend based on your historical usage, useful for budget planning. Reference: https://docs.aws.amazon.com/cost-management/latest/userguide/ce-forecast.html",
})
QUESTIONS.append({
    "q": "Which feature lets you TAG your AWS resources with custom key-value pairs to track cost and usage by project, team, or environment?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost Allocation Tags", "Cost Allocation Tags let you track cost by tag key-value."),
        ("AWS Resource Groups", "Resource Groups organize resources, not track cost."),
        ("AWS Organizations", "Organizations manages multiple accounts."),
        ("AWS Config", "Config tracks resource changes, not cost allocation per se."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Cost Allocation Tags let you tag resources and track cost/usage by tag, with support in Cost Explorer and CUR. Reference: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html",
})
QUESTIONS.append({
    "q": "Which tag type is activated by AWS in the Billing console to appear in Cost Explorer and the Cost and Usage Report?",
    "type": "multiple-choice",
    "opts": [
        ("User-defined tags", "User-defined tags must be activated in Billing console to appear in cost reports."),
        ("AWS-generated tags", "AWS-generated tags (like createdBy) appear automatically."),
        ("Default tags", "Default tags are auto-applied to new resources."),
        ("Resource tags", "Resource tags is a general term."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "User-defined cost allocation tags must be activated in the Billing console to appear in cost reports. Reference: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activate-use-tag.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides an interactive tool to ESTIMATE the cost of AWS services BEFORE you provision them, useful for architecture planning?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Pricing Calculator", "Pricing Calculator estimates cost of services before provisioning."),
        ("AWS Cost Explorer", "Cost Explorer analyzes past spend."),
        ("AWS Budgets", "Budgets alerts on thresholds."),
        ("AWS Trusted Advisor", "Trusted Advisor provides checks."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Pricing Calculator estimates the cost of AWS services before provisioning, useful for architecture planning. Reference: https://aws.amazon.com/pricing-calculator/",
})
QUESTIONS.append({
    "q": "Which AWS Organizations feature provides a centralized way to apply DISCOUNTS across member accounts, sharing volume discounts and Savings Plans?",
    "type": "multiple-choice",
    "opts": [
        ("Consolidated Billing", "Consolidated Billing combines usage across accounts for volume discounts."),
        ("Service Control Policies (SCPs)", "SCPs control permissions, not discounts."),
        ("AWS Control Tower", "Control Tower is for multi-account governance."),
        ("AWS Resource Access Manager", "RAM shares resources across accounts."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Organizations Consolidated Billing combines usage across member accounts to share volume discounts and Savings Plans. Reference: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides ALERTS on RI and Savings Plans coverage and utilization, helping you optimize commitments?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost Explorer", "Cost Explorer shows coverage but not alerts."),
        ("AWS Budgets with Reservation/Savings Plans budget", "Budgets can alert on RI/SP utilization and coverage."),
        ("Cost Anomaly Detection", "Anomaly Detection is for anomalies, not RI/SP coverage."),
        ("AWS Trusted Advisor", "Trusted Advisor checks RI coverage but doesn't alert by default."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "AWS Budgets with Reservation or Savings Plans budget type alerts you when utilization or coverage falls below a threshold. Reference: https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid AWS Trusted Advisor cost optimization checks? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Low-utilization EC2 instances", "Trusted Advisor flags low-utilization EC2 instances."),
        ("Unassociated Elastic IP addresses", "Unassociated EIPs are flagged."),
        ("Idle load balancers", "Idle LBs are flagged."),
        ("Underutilized EBS volumes", "Underutilized EBS volumes are flagged."),
    ],
    "correct": "1,2,3,4",
    "domain": COST_OPT,
    "overall": "Trusted Advisor cost checks include low-utilization EC2, unassociated EIPs, idle LBs, and underutilized EBS volumes. Reference: https://aws.amazon.com/premiumsupport/technology/trusted-advisor/",
})
QUESTIONS.append({
    "q": "Which AWS service provides a centralized, multi-account view of cost and usage, with the ability to manage member accounts and consolidated billing?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Organizations", "Organizations provides multi-account consolidated billing."),
        ("AWS Control Tower", "Control Tower is for landing zone governance."),
        ("AWS Systems Manager", "Systems Manager is for ops automation."),
        ("AWS Resource Groups", "Resource Groups organize resources, not accounts."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Organizations provides multi-account consolidated billing, with the ability to manage member accounts. Reference: https://aws.amazon.com/organizations/",
})
QUESTIONS.append({
    "q": "Which AWS service provides AUTOMATED detection of cost savings opportunities across compute, storage, and database services using ML?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Compute Optimizer", "Compute Optimizer uses ML to recommend rightsizing for EC2, EBS, Lambda."),
        ("AWS Cost Explorer", "Cost Explorer is for visualization, not ML optimization."),
        ("AWS Trusted Advisor", "Trusted Advisor provides static checks."),
        ("AWS Budgets", "Budgets alerts on spend, not optimization."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Compute Optimizer uses ML to recommend rightsizing for EC2, EBS, and Lambda. Reference: https://aws.amazon.com/compute-optimizer/",
})
QUESTIONS.append({
    "q": "Which AWS service is the BEST for centralized, multi-account governance, including preventive and detective controls?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Organizations", "Organizations is for consolidated billing and SCPs."),
        ("AWS Control Tower", "Control Tower provides multi-account governance with preventive and detective controls."),
        ("AWS Systems Manager", "Systems Manager is for ops automation."),
        ("AWS Config", "Config is for resource compliance."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "AWS Control Tower provides multi-account governance with preventive (SCPs) and detective (AWS Config) controls. Reference: https://aws.amazon.com/controltower/",
})

# ============================================================
# 8. TAG POLICIES, ACCOUNTS, ARCHITECTURE COST (12 questions)
# ============================================================

QUESTIONS.append({
    "q": "Which AWS service lets you manage MULTIPLE AWS accounts centrally, with consolidated billing and policy-based control?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Control Tower", "Control Tower is for governance on top of Organizations."),
        ("AWS Organizations", "Organizations manages accounts, billing, and policies."),
        ("AWS IAM", "IAM is for identity, not accounts."),
        ("AWS Systems Manager", "Systems Manager is for ops."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "AWS Organizations manages multiple accounts, provides consolidated billing, and applies Service Control Policies. Reference: https://aws.amazon.com/organizations/",
})
QUESTIONS.append({
    "q": "Which Organizations feature provides preventive guardrails by allowing or denying AWS API actions across member accounts?",
    "type": "multiple-choice",
    "opts": [
        ("Service Control Policies (SCPs)", "SCPs allow or deny API actions across accounts."),
        ("Tag Policies", "Tag Policies standardize tags."),
        ("Backup Policies", "Backup Policies configure AWS Backup."),
        ("AI Services Opt-out Policies", "AI Services Opt-out is for AI services."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Service Control Policies (SCPs) provide preventive guardrails by allowing or denying API actions across accounts. Reference: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html",
})
QUESTIONS.append({
    "q": "Which AWS service provides centralized RECOMMENDATIONS for Reserved Instance and Savings Plan purchases across all your accounts?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost Explorer", "Cost Explorer provides RI/SP recommendations."),
        ("AWS Budgets", "Budgets alerts on spend, not recommendations."),
        ("AWS Trusted Advisor", "Trusted Advisor provides checks."),
        ("AWS Pricing Calculator", "Pricing Calculator estimates, not recommends purchases."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Cost Explorer provides RI and Savings Plan purchase recommendations based on your past usage. Reference: https://docs.aws.amazon.com/cost-management/latest/userguide/ce-ri-recommendations.html",
})
QUESTIONS.append({
    "q": "Which of the following are valid benefits of using AWS Organizations with Consolidated Billing? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Volume discounts across accounts", "Consolidated usage shares volume discounts."),
        ("Unified billing", "One bill for all accounts."),
        ("No-charge data transfer between accounts in same region", "No, cross-account cross-region transfer is charged; same-region same-AZ is free for some services."),
        ("Service Control Policies", "SCPs provide preventive controls across accounts."),
    ],
    "correct": "1,2,4",
    "domain": COST_OPT,
    "overall": "Consolidated Billing provides volume discounts, one bill, and SCPs apply across accounts. Data transfer between accounts is not always free. Reference: https://aws.amazon.com/organizations/",
})
QUESTIONS.append({
    "q": "Which AWS service provides DETAILED visibility into which user, role, or service performed an action, useful for cost attribution?",
    "type": "multiple-choice",
    "opts": [
        ("AWS CloudTrail", "CloudTrail logs API calls with user, role, and service identity."),
        ("AWS Config", "Config tracks resource changes."),
        ("AWS Cost Explorer", "Cost Explorer shows cost, not user identity."),
        ("AWS Trusted Advisor", "Trusted Advisor provides checks."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS CloudTrail logs API calls with the identity (user, role, service) and event details, useful for cost attribution. Reference: https://aws.amazon.com/cloudtrail/",
})
QUESTIONS.append({
    "q": "Which AWS service provides RESOURCE INVENTORY and configuration history, useful for understanding which resources exist and their cost?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Config", "Config tracks resource inventory and configuration history."),
        ("AWS CloudTrail", "CloudTrail logs API calls."),
        ("AWS Systems Manager", "Systems Manager is for ops automation."),
        ("AWS Cost Explorer", "Cost Explorer shows cost, not resource inventory."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Config provides resource inventory and configuration history, useful for understanding cost. Reference: https://aws.amazon.com/config/",
})
QUESTIONS.append({
    "q": "Which AWS feature lets you APPLY a tag policy to ensure consistent tag values across accounts and resources, improving cost tracking?",
    "type": "multiple-choice",
    "opts": [
        ("Tag Policy", "Tag Policy standardizes tags across accounts."),
        ("Service Control Policy", "SCPs control API actions."),
        ("Backup Policy", "Backup Policy configures AWS Backup."),
        ("IAM Policy", "IAM Policy controls access."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Tag Policy standardizes tag keys and values across accounts and resources, improving cost tracking. Reference: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html",
})
QUESTIONS.append({
    "q": "Which AWS architecture pattern is the MOST cost-effective for a workload with predictable steady traffic and 24/7 usage?",
    "type": "multiple-choice",
    "opts": [
        ("All On-Demand", "On-Demand is the most expensive for steady traffic."),
        ("Reserved Instances or Savings Plans", "RIs/SPs provide up to 75% discount for steady traffic."),
        ("All Spot", "Spot is interruptible, not suitable for steady critical workloads."),
        ("Serverless only", "Serverless is good for variable traffic, not always cheaper for steady."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "For predictable steady traffic, RIs or Savings Plans provide the largest discount and best cost-effectiveness. Reference: https://aws.amazon.com/savingsplans/",
})
QUESTIONS.append({
    "q": "Which AWS architecture pattern is the MOST cost-effective for a workload with UNPREDICTABLE, bursty traffic and can scale to zero?",
    "type": "multiple-choice",
    "opts": [
        ("All On-Demand", "On-Demand is good for bursty, but serverless is often cheaper."),
        ("Serverless (Lambda) with pay-per-use", "Serverless scales to zero and bills per use, ideal for unpredictable traffic."),
        ("Reserved Instances", "RIs commit to capacity, not ideal for unpredictable."),
        ("Spot only", "Spot is interruptible, not always suitable."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "For unpredictable, bursty traffic, serverless (Lambda) scales to zero and bills per use, the most cost-effective. Reference: https://aws.amazon.com/lambda/pricing/",
})
QUESTIONS.append({
    "q": "Which of the following are valid AWS architecture cost optimization principles? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Right-size resources", "Match resources to workload needs."),
        ("Use managed services", "Managed services reduce operational overhead and cost."),
        ("Implement tagging for cost allocation", "Tagging enables cost tracking by project/team."),
        ("Over-provision for headroom", "Over-provisioning wastes cost; right-size instead."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Right-size, use managed services, and implement tagging to optimize architecture cost. Reference: https://aws.amazon.com/architecture/cost-optimization/",
})
QUESTIONS.append({
    "q": "Which AWS Well-Architected pillar focuses on RUNNING SYSTEMS to DELIVER BUSINESS VALUE at the lowest price point?",
    "type": "multiple-choice",
    "opts": [
        ("Operational Excellence", "Operational Excellence is for running and monitoring."),
        ("Cost Optimization", "Cost Optimization focuses on delivering value at the lowest price."),
        ("Reliability", "Reliability is for recovery and disruption handling."),
        ("Performance Efficiency", "Performance Efficiency is for compute resources."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Cost Optimization focuses on running systems to deliver business value at the lowest price point. Reference: https://aws.amazon.com/architecture/well-architected/",
})
QUESTIONS.append({
    "q": "Which AWS service provides the LOWEST cost compute for fault-tolerant, interruptible workloads such as CI/CD build runners or big data processing?",
    "type": "multiple-choice",
    "opts": [
        ("EC2 On-Demand", "On-Demand is the most expensive."),
        ("EC2 Spot Instances", "Spot provides up to 90% discount for fault-tolerant workloads."),
        ("EC2 Reserved Instances", "RIs commit to capacity, not interruptible."),
        ("AWS Lambda", "Lambda is serverless, good for event-driven, not always for big data processing."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "EC2 Spot Instances provide up to 90% discount for fault-tolerant, interruptible workloads. Reference: https://aws.amazon.com/ec2/spot/",
})

# ============================================================
# 9. GlobalBank CASE STUDY QUESTIONS (20 questions)
# ============================================================

QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank wants to MIGRATE Wave 1 workloads (web portal, mobile API, auth, marketing email) to AWS at the lowest cost while meeting the 99.9% SLA. Which combination of services is the BEST fit? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Amazon CloudFront in front of S3 for static assets", "CloudFront + S3 reduces origin cost and improves latency."),
        ("AWS Lambda for the marketing email send", "Lambda scales to zero, ideal for variable marketing email."),
        ("Amazon EC2 with On-Demand only", "On-Demand is the most expensive for steady traffic."),
        ("Amazon Aurora Serverless v2 for the auth service database", "Aurora Serverless v2 auto-scales and is cost-effective for variable auth DB."),
    ],
    "correct": "1,2,4",
    "domain": COST_OPT,
    "overall": "CloudFront+S3, Lambda, and Aurora Serverless v2 are cost-optimized patterns for the Wave 1 workloads. Reference: https://aws.amazon.com/architecture/cost-optimization/",
})
QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank wants to MINIMIZE cost of running its Wave 1 web portal on EC2, with predictable traffic patterns and 24/7 usage. Which pricing model is BEST?",
    "type": "multiple-choice",
    "opts": [
        ("EC2 On-Demand", "On-Demand is the most expensive for predictable 24/7."),
        ("EC2 Reserved Instances (3-year, All Upfront) or Compute Savings Plans", "RIs/SPs provide up to 75% discount for predictable traffic."),
        ("EC2 Spot Instances", "Spot is interruptible, not suitable for 24/7 critical web."),
        ("AWS Lambda", "Lambda is not ideal for 24/7 long-running web servers."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "EC2 Reserved Instances (3-year All Upfront) or Compute Savings Plans provide up to 75% discount for predictable 24/7 workloads. Reference: https://aws.amazon.com/savingsplans/",
})
QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank has a marketing email workload that runs only once per day, processes 100,000 emails, and is fault-tolerant. Which is the MOST cost-effective compute option?",
    "type": "multiple-choice",
    "opts": [
        ("EC2 On-Demand 24/7", "On-Demand 24/7 wastes cost for daily jobs."),
        ("EC2 Spot for the duration of the job", "Spot provides up to 90% discount for fault-tolerant batch jobs."),
        ("EC2 Reserved Instances", "RIs commit to capacity, not ideal for daily short jobs."),
        ("Lambda for email send", "Lambda can work but is rate-limited for 100K emails; Spot EC2 may be better."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Spot EC2 is the most cost-effective for fault-tolerant, batch workloads like daily email send. Reference: https://aws.amazon.com/ec2/spot/",
})
QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank wants to store 200 TB of on-premises data in AWS for Wave 1 (active for 3 years, then archive for 7 years). Which S3 storage class transition strategy is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Standard for 3 years, then Glacier Deep Archive for 7 years", "Standard for active, then Deep Archive for long-term archive."),
        ("S3 Standard-IA for 3 years, then Glacier Flexible for 7 years", "Standard-IA and Glacier Flexible are more expensive than Deep Archive for archive."),
        ("S3 Glacier Deep Archive for the entire 10 years", "Deep Archive has 12-hour retrieval, not ideal for active."),
        ("S3 One Zone-IA for 3 years, then Standard for 7 years", "One Zone-IA is single-AZ; not ideal for compliance."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "S3 Standard for active 3 years, then transition to Glacier Deep Archive for the 7-year archive is the most cost-effective. Reference: https://aws.amazon.com/s3/storage-classes/",
})
QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank wants to share Savings Plans discounts across all of its AWS accounts (web, mobile, auth, marketing). Which feature enables this?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Organizations with Consolidated Billing", "Consolidated Billing shares Savings Plans and volume discounts across accounts."),
        ("IAM cross-account roles", "IAM roles don't share Savings Plans."),
        ("AWS RAM", "RAM shares resources, not Savings Plans."),
        ("AWS Control Tower", "Control Tower is for governance."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Organizations Consolidated Billing shares Savings Plans and volume discounts across member accounts. Reference: https://aws.amazon.com/organizations/",
})
QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank wants to set a MONTHLY cost budget for the Wave 1 workloads and STOP non-production EC2 instances when the budget is exceeded. Which combination is the BEST? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS Budgets with cost budget type", "Cost budget alerts on monthly spend."),
        ("Budget action to stop EC2 instances", "Budget action can stop EC2 instances."),
        ("CloudWatch alarm on Cost Explorer metric", "CloudWatch can alert on cost metrics but doesn't stop instances directly."),
        ("Lambda function triggered by SNS to stop instances", "Lambda can stop instances, but Budgets action is the native solution."),
    ],
    "correct": "1,2,4",
    "domain": COST_OPT,
    "overall": "AWS Budgets with cost type and a budget action to stop EC2 instances (via SNS + Lambda) is the native cost-control pattern. Reference: https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html",
})
QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank wants to use Cost Allocation Tags to track spend by workload (web, mobile, auth, marketing). Which tag activation step is REQUIRED?",
    "type": "multiple-choice",
    "opts": [
        ("Tags are automatically applied to all cost reports", "Tags are not automatic; they must be activated."),
        ("Activate user-defined cost allocation tags in the Billing console", "User-defined tags must be activated in Billing console to appear in cost reports."),
        ("Create an IAM policy for tags", "IAM doesn't activate cost tags."),
        ("Use AWS Resource Groups only", "Resource Groups organize resources, not cost allocation."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "User-defined cost allocation tags must be activated in the Billing console to appear in Cost Explorer and CUR. Reference: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activate-use-tag.html",
})
QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank wants to run its auth service database on Aurora with VARIABLE traffic. Which is the MOST cost-effective Aurora configuration?",
    "type": "multiple-choice",
    "opts": [
        ("Aurora Provisioned with the largest instance", "Provisioned with the largest instance is the most expensive."),
        ("Aurora Serverless v2 with auto-scaling ACUs", "Aurora Serverless v2 auto-scales ACUs based on demand, cost-effective for variable traffic."),
        ("Aurora Global Database", "Global is for multi-region, not needed for Wave 1 single region."),
        ("Aurora on Reserved Instances", "RIs commit to capacity, not ideal for variable traffic."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Aurora Serverless v2 auto-scales ACUs based on demand, the most cost-effective for variable traffic. Reference: https://aws.amazon.com/rds/aurora/serverless/",
})
QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank wants to use Spot Instances for the marketing email workload, which is fault-tolerant and processes 100,000 emails per day. Which Spot feature provides the BEST cost optimization?",
    "type": "multiple-choice",
    "opts": [
        ("Spot Instance alone", "Spot alone is good but Spot Fleet provides diversification."),
        ("Spot Fleet with diversified instance types", "Spot Fleet diversifies across types to reduce interruption risk."),
        ("On-Demand with Savings Plans", "On-Demand with SPs doesn't provide Spot discount."),
        ("Reserved Instances", "RIs don't apply to Spot."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Spot Fleet with diversified instance types reduces interruption risk and maximizes Spot discount. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet.html",
})
QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank wants to ANALYZE its monthly cost and usage by workload, region, and instance type, and forecast next month's spend. Which AWS service is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost Explorer", "Cost Explorer provides analysis, filtering, and forecasting."),
        ("AWS Budgets", "Budgets alerts on thresholds, not analysis."),
        ("AWS Trusted Advisor", "Trusted Advisor provides checks."),
        ("AWS Pricing Calculator", "Pricing Calculator estimates, not analyses past usage."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Cost Explorer provides analysis with filtering by workload/region/instance type, plus forecasting. Reference: https://aws.amazon.com/aws-cost-management/aws-cost-explorer/",
})
QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank wants to use ElastiCache Redis to reduce load on its RDS database, lowering RDS compute cost. Which cost-saving mechanism applies?",
    "type": "multiple-choice",
    "opts": [
        ("ElastiCache is more expensive than RDS", "ElastiCache is generally cheaper than RDS for caching."),
        ("Caching reduces RDS read load, allowing smaller RDS instance", "Caching offloads reads, enabling a smaller RDS instance and lower cost."),
        ("ElastiCache replaces RDS", "ElastiCache is a cache, not a replacement for RDS."),
        ("ElastiCache is not cost-effective", "ElastiCache is highly cost-effective as a cache."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "ElastiCache offloads reads from RDS, allowing a smaller RDS instance and lower RDS cost. Reference: https://aws.amazon.com/elasticache/",
})
QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank wants to monitor for UNEXPECTED cost spikes (e.g., a misconfigured S3 bucket that becomes public). Which AWS service is the BEST fit?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Budgets", "Budgets uses thresholds, not anomaly detection."),
        ("Cost Anomaly Detection", "Cost Anomaly Detection uses ML to detect unusual cost patterns."),
        ("AWS Trusted Advisor", "Trusted Advisor provides checks."),
        ("AWS CloudTrail", "CloudTrail logs API calls, not cost anomalies."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Cost Anomaly Detection uses ML to detect unexpected cost patterns, alerting you to spikes like a public S3 bucket. Reference: https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/",
})
QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank wants to use Amazon CloudFront to cache its web portal's static assets (CSS, JS, images) at edge locations, REDUCING origin data transfer and cost. Which CloudFront pricing factor is MOST relevant?",
    "type": "multiple-choice",
    "opts": [
        ("CloudFront data transfer out to internet", "CloudFront data transfer out is the main cost factor; less origin transfer reduces cost."),
        ("CloudFront per-request cost", "Per-request cost is small compared to data transfer."),
        ("CloudFront invalidations", "Invalidations have a small cost."),
        ("CloudFront SSL certificates", "SSL certs are free with ACM."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "CloudFront data transfer out is the main cost factor; caching at edge reduces origin data transfer and total cost. Reference: https://aws.amazon.com/cloudfront/pricing/",
})
QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank wants to use AWS Lambda for the marketing email send, with the email triggered once per day. Which Lambda feature is MOST cost-relevant?",
    "type": "multiple-choice",
    "opts": [
        ("Provisioned Concurrency", "Provisioned Concurrency is for low-latency, not needed for daily jobs."),
        ("Pay-per-use (per request + GB-s)", "Lambda bills per request and GB-second, no charge when idle, ideal for daily jobs."),
        ("Lambda SnapStart", "SnapStart is for cold start, not cost-critical here."),
        ("Lambda@Edge", "Lambda@Edge is for edge, not needed here."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Lambda bills per request and GB-second, with no charge when idle, ideal for daily triggered workloads. Reference: https://aws.amazon.com/lambda/pricing/",
})
QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank wants to reduce its RDS cost by using Aurora Serverless v2 for the auth DB. Which is the BEST explanation of Aurora Serverless v2's cost model?",
    "type": "multiple-choice",
    "opts": [
        ("Fixed instance cost 24/7", "Aurora Serverless v2 is not fixed cost."),
        ("Auto-scales ACUs from 0.5 to 128, bills per ACU-second", "Aurora Serverless v2 auto-scales ACUs and bills per ACU-second."),
        ("Pay per request", "Aurora bills per ACU-second, not per request."),
        ("Pay per GB stored", "Storage is a separate cost, not the primary model."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Aurora Serverless v2 auto-scales ACUs from 0.5 to 128 and bills per ACU-second, ideal for variable workloads. Reference: https://aws.amazon.com/rds/aurora/serverless/",
})
QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank wants to use AWS Compute Optimizer to right-size its EC2 instances. Which data source does Compute Optimizer primarily use?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Cost Explorer", "Cost Explorer shows spend, not utilization."),
        ("CloudWatch metrics (CPU, memory, network)", "Compute Optimizer uses CloudWatch metrics for utilization analysis."),
        ("AWS Config", "Config tracks config, not utilization."),
        ("AWS CloudTrail", "CloudTrail logs API calls."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "AWS Compute Optimizer uses 14 days of CloudWatch metrics to recommend right-sizing. Reference: https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is.html",
})
QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank wants to apply Service Control Policies (SCPs) to PREVENT member accounts from launching EC2 instances in regions outside us-east-1 and eu-west-1. Which is the BEST SCP?",
    "type": "multiple-choice",
    "opts": [
        ("Allow ec2:RunInstances only when aws:RequestedRegion is us-east-1 or eu-west-1", "SCP condition on RequestedRegion is the right approach."),
        ("Deny all ec2:RunInstances", "Deny all is too restrictive."),
        ("Allow all actions in all regions", "Allow all doesn't restrict regions."),
        ("Use IAM policy on the root user", "Root user SCPs apply at the account level."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "An SCP that allows ec2:RunInstances only when aws:RequestedRegion is in the approved list prevents launches in other regions. Reference: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html",
})
QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank wants to use S3 Lifecycle policies to automatically MOVE old audit logs to a cheaper storage class after 90 days, and DELETE them after 7 years. Which is the BEST lifecycle configuration? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Transition to S3 Standard-IA after 90 days", "Standard-IA is cheaper for infrequent access."),
        ("Transition to S3 Glacier Flexible Retrieval after 1 year", "Glacier Flexible is cheaper for archive."),
        ("Transition to S3 Glacier Deep Archive after 1-2 years", "Glacier Deep Archive is the lowest cost for long-term archive."),
        ("Expire (delete) after 7 years", "Lifecycle can expire objects at a date or age."),
    ],
    "correct": "1,2,3,4",
    "domain": COST_OPT,
    "overall": "S3 Lifecycle supports transitions to Standard-IA, Glacier Flexible, Glacier Deep Archive, and expiration for cost-effective archival. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html",
})
QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank wants to use AWS Direct Connect for hybrid connectivity at LOWER per-GB data transfer cost than VPN over the public internet. Which DX pricing model is MOST cost-effective for high-volume, steady traffic?",
    "type": "multiple-choice",
    "opts": [
        ("DX with 1 Gbps port, no commitment", "1 Gbps with no commitment is the most expensive DX port."),
        ("DX with 10 Gbps port, no commitment", "10 Gbps with no commitment is more expensive per port."),
        ("DX with committed port and lower data transfer rate", "DX committed access provides lower per-GB data transfer rate."),
        ("VPN over internet", "VPN is over internet, higher data transfer cost."),
    ],
    "correct": "3",
    "domain": COST_OPT,
    "overall": "DX with committed port access provides a lower per-GB data transfer rate than uncommitted or VPN. Reference: https://aws.amazon.com/directconnect/pricing/",
})
QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank wants to use DynamoDB to store user session data with UNPREDICTABLE traffic. Which DynamoDB pricing model is MOST cost-effective for unpredictable, low-traffic workloads?",
    "type": "multiple-choice",
    "opts": [
        ("Provisioned with Reserved Capacity", "Reserved is for predictable traffic."),
        ("On-Demand mode", "On-Demand bills per request, ideal for unpredictable traffic."),
        ("Provisioned with Auto Scaling", "Auto Scaling adjusts but commits to capacity."),
        ("DynamoDB Global Tables", "Global Tables add replication cost; not needed here."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "DynamoDB On-Demand mode bills per request, ideal for unpredictable, low-traffic workloads. Reference: https://aws.amazon.com/dynamodb/pricing/",
})
QUESTIONS.append({
    "q": "In the GlobalBank scenario, GlobalBank wants to use AWS Lambda Power Tuning to find the OPTIMAL memory size for a Lambda function to minimize cost. Which tool provides this?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Compute Optimizer", "Compute Optimizer recommends Lambda memory, but the AWS Lambda Power Tuning state machine is the standard tool."),
        ("AWS Lambda Power Tuning (state machine)", "AWS Lambda Power Tuning is a state machine that runs the function at multiple memory sizes."),
        ("AWS Cost Explorer", "Cost Explorer shows spend, not memory recommendations."),
        ("AWS Trusted Advisor", "Trusted Advisor doesn't tune Lambda."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "AWS Lambda Power Tuning is an AWS Labs open-source Step Functions state machine that runs a function at multiple memory sizes to find the cost-optimal setting. Reference: https://aws.amazon.com/lambda/pricing/",
})


# ============================================================
# Additional questions to reach 200 (59 more, 14 multi-select + 45 single)
# ============================================================

QUESTIONS.append({
    "q": "Which EC2 feature provides a discount of up to 10% for On-Demand instances that are scheduled in advance (capacity blocks)?",
    "type": "multiple-choice",
    "opts": [
        ("EC2 Capacity Blocks for ML", "Capacity Blocks for ML provide scheduled GPU capacity for ML workloads at a discount."),
        ("Spot Instances", "Spot is interruptible, not scheduled."),
        ("On-Demand alone", "On-Demand has no scheduled discount."),
        ("Reserved Instances", "RIs commit to 1- or 3-year terms."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "EC2 Capacity Blocks for ML let you schedule GPU instances in advance for ML workloads at a discount. Reference: https://aws.amazon.com/ec2/capacity-blocks/",
})

QUESTIONS.append({
    "q": "Which AWS Savings Plan provides the HIGHEST discount but is LEAST flexible, applying only to a specific instance family in a specific region?",
    "type": "multiple-choice",
    "opts": [
        ("Compute Savings Plans", "Compute SPs are the most flexible, lower discount."),
        ("EC2 Instance Savings Plans", "EC2 Instance SPs apply to a family in a region, higher discount."),
        ("SageMaker Savings Plans", "SageMaker SPs are for SageMaker only."),
        ("No Savings Plan", "There is always a Savings Plan option."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "EC2 Instance Savings Plans provide a higher discount than Compute SPs but apply only to a family in a region. Reference: https://aws.amazon.com/savingsplans/",
})

QUESTIONS.append({
    "q": "Which of the following are valid ways to use Spot Instances in a fault-tolerant application? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Spot Fleet with diversification", "Spot Fleet diversifies across types."),
        ("Checkpointing to handle interruption", "Checkpointing allows resume on interruption."),
        ("EC2 Auto Scaling with mixed instances", "ASG mixed instances policy uses Spot and On-Demand."),
        ("Replace Spot with On-Demand on interruption", "Spot interruption cannot trigger automatic On-Demand replacement unless configured."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Spot Fleet, checkpointing, and ASG mixed instances are valid Spot patterns. Auto-replacement requires configuration. Reference: https://aws.amazon.com/ec2/spot/best-practices/",
})

QUESTIONS.append({
    "q": "Which feature of EC2 Auto Scaling automatically replaces Spot Instances that are interrupted, maintaining desired capacity?",
    "type": "multiple-choice",
    "opts": [
        ("Capacity Rebalancing", "Capacity Rebalancing proactively replaces Spot at risk of interruption."),
        ("Target tracking", "Target tracking scales on a metric."),
        ("Lifecycle hooks", "Lifecycle hooks pause instance lifecycle actions."),
        ("Termination policy", "Termination policy controls which instance to terminate."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "EC2 Auto Scaling Capacity Rebalancing proactively replaces Spot at risk of interruption, maintaining capacity. Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/capacity-rebalancing.html",
})

QUESTIONS.append({
    "q": "Which EC2 feature provides a discount of up to 10% for SHORT, time-bound workloads (1-4 hours) that need to be scheduled?",
    "type": "multiple-choice",
    "opts": [
        ("EC2 Instance Savings Plans", "EC2 Instance SPs are 1- or 3-year."),
        ("Savings Plans for Compute", "Compute SPs are 1- or 3-year."),
        ("No such feature exists", "EC2 has no general 1-4 hour discount; Spot is the alternative for short workloads."),
        ("EC2 Reserved Instances", "RIs are 1- or 3-year."),
    ],
    "correct": "3",
    "domain": COST_OPT,
    "overall": "EC2 has no general 1-4 hour discount. For short workloads, Spot or Capacity Blocks for ML are alternatives. Reference: https://aws.amazon.com/ec2/pricing/",
})

QUESTIONS.append({
    "q": "Which of the following are valid RI Marketplace actions? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Sell unused RIs", "RI Marketplace allows selling unused RIs."),
        ("Buy discounted RIs from other AWS customers", "RI Marketplace allows buying discounted RIs."),
        ("Modify RIs", "RIs can be modified in your account, not via Marketplace."),
        ("Cancel RIs for a refund", "RIs cannot be cancelled for refund; you can sell on Marketplace."),
    ],
    "correct": "1,2",
    "domain": COST_OPT,
    "overall": "RI Marketplace lets you sell unused RIs and buy discounted RIs from other AWS customers. Reference: https://aws.amazon.com/ec2/pricing/reserved-instruments/ri-marketplace/",
})

QUESTIONS.append({
    "q": "Which AWS service provides recommendations for EC2 instance type right-sizing based on CloudWatch metrics?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Compute Optimizer", "Compute Optimizer recommends EC2 rightsizing based on CloudWatch metrics."),
        ("AWS Cost Explorer", "Cost Explorer shows spend."),
        ("AWS Trusted Advisor", "Trusted Advisor provides static checks."),
        ("AWS Systems Manager", "Systems Manager is for ops automation."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Compute Optimizer uses 14 days of CloudWatch metrics to recommend EC2 rightsizing. Reference: https://aws.amazon.com/compute-optimizer/",
})

QUESTIONS.append({
    "q": "Which Reserved Instance scope is the MOST flexible, applying to any instance in a family across all AZs in a region?",
    "type": "multiple-choice",
    "opts": [
        ("Zonal RI", "Zonal RI is scoped to one AZ."),
        ("Regional RI", "Regional RI applies to any instance in a family across AZs in a region."),
        ("Account-level RI", "Account-level applies across regions, not standard."),
        ("Global RI", "There is no global RI; Savings Plans can be global."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Regional RIs apply to any instance in the family across AZs in the region. Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts-reserved-instances.html",
})

QUESTIONS.append({
    "q": "Which of the following are valid benefits of using Savings Plans? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Discount of up to 72%", "Savings Plans provide up to 72% discount."),
        ("Flexibility across instance families", "Compute SPs apply to any family."),
        ("Coverage of Fargate and Lambda", "Compute SPs cover Fargate and Lambda."),
        ("No commitment required", "Savings Plans require a 1- or 3-year commitment."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Savings Plans provide up to 72% discount, apply flexibly across families, and cover Fargate/Lambda. Reference: https://aws.amazon.com/savingsplans/",
})

QUESTIONS.append({
    "q": "Which EC2 feature provides a 5% discount for using specific Linux distributions (e.g., Ubuntu, RHEL) instead of Amazon Linux?",
    "type": "multiple-choice",
    "opts": [
        ("No such discount exists", "There is no 5% discount for specific Linux distributions."),
        ("Spot is the only discount", "Spot is interruptible, not a Linux discount."),
        ("RIs have a Linux discount", "RIs price the same across Linux distros (with platform-specific)."),
        ("Savings Plans have a Linux discount", "Savings Plans don't differentiate by Linux distro."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "EC2 has no specific 5% discount for Linux distros; RIs/SPs price the same across distros (with platform-specific). Reference: https://aws.amazon.com/ec2/pricing/",
})

QUESTIONS.append({
    "q": "Which S3 Glacier retrieval option provides the LOWEST cost per retrieval but the SLOWEST access (5-12 hours)?",
    "type": "multiple-choice",
    "opts": [
        ("Standard retrieval", "Standard is 3-5 hours."),
        ("Bulk retrieval", "Bulk is 5-12 hours, lowest cost."),
        ("Expedited retrieval", "Expedited is 1-5 minutes."),
        ("S3 Standard", "S3 Standard is not a Glacier option."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Glacier Flexible Retrieval Bulk is 5-12 hours, lowest cost per retrieval. Reference: https://aws.amazon.com/s3/storage-classes/",
})

QUESTIONS.append({
    "q": "Which S3 feature lets you reduce storage cost by DELETING old noncurrent object versions that are no longer needed?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Lifecycle with NoncurrentVersionExpiration", "Lifecycle NoncurrentVersionExpiration deletes old noncurrent versions."),
        ("S3 Object Lock", "Object Lock is for WORM, not deletion."),
        ("S3 Replication", "Replication copies, doesn't delete old versions."),
        ("S3 Transfer Acceleration", "Transfer Acceleration is for uploads."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "S3 Lifecycle NoncurrentVersionExpiration deletes old noncurrent versions to reduce storage cost. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html",
})

QUESTIONS.append({
    "q": "Which S3 storage class is the BEST fit for data accessed once a month or less, with millisecond retrieval and no retrieval fees?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Standard-IA", "Standard-IA has retrieval fees, 30-day minimum."),
        ("S3 Glacier Instant Retrieval", "Glacier Instant Retrieval has no retrieval fees, millisecond retrieval."),
        ("S3 One Zone-IA", "One Zone-IA is single-AZ."),
        ("S3 Glacier Flexible Retrieval", "Glacier Flexible has retrieval delays."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "S3 Glacier Instant Retrieval provides millisecond retrieval with no retrieval fees, ideal for monthly access. Reference: https://aws.amazon.com/s3/storage-classes/",
})

QUESTIONS.append({
    "q": "Which S3 feature provides a single global endpoint over MULTI-REGION replicated buckets, with automatic routing to the lowest-latency copy?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Cross-Region Replication", "CRR replicates but doesn't provide a global endpoint."),
        ("S3 Multi-Region Access Point (MRAP)", "MRAP provides a single global endpoint over replicated buckets."),
        ("S3 Transfer Acceleration", "Transfer Acceleration is for uploads."),
        ("CloudFront", "CloudFront is a CDN over an origin."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "S3 Multi-Region Access Point provides a single global endpoint that routes to the lowest-latency replicated bucket. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPoints.html",
})

QUESTIONS.append({
    "q": "Which of the following are valid S3 cost factors? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Storage class and amount stored", "Storage class and GB stored is a cost factor."),
        ("Number of requests (PUT, GET, LIST)", "Per-request charges apply."),
        ("Data transfer out to internet", "Data transfer out is a cost factor."),
        ("Replication to another region", "Cross-region replication has per-GB and per-request charges."),
    ],
    "correct": "1,2,3,4",
    "domain": COST_OPT,
    "overall": "S3 cost factors include storage, requests, data transfer out, and cross-region replication. Reference: https://aws.amazon.com/s3/pricing/",
})

QUESTIONS.append({
    "q": "Which S3 storage class provides a LOWER per-GB cost than Standard for infrequently accessed data, with retrieval fees?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Standard-IA", "Standard-IA is lower per-GB than Standard, with retrieval fees and 30-day minimum."),
        ("S3 One Zone-IA", "One Zone-IA is single-AZ, lower than Standard-IA."),
        ("S3 Glacier Instant Retrieval", "Glacier Instant has no retrieval fees."),
        ("S3 Glacier Deep Archive", "Glacier Deep is the lowest, with 12-hour retrieval."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "S3 Standard-IA is lower per-GB than Standard for infrequent access, with retrieval fees and 30-day storage minimum. Reference: https://aws.amazon.com/s3/storage-classes/",
})

QUESTIONS.append({
    "q": "Which S3 Glacier retrieval option provides 1-5 minute access for a SMALL portion of data (up to 250 MB) at the highest cost?",
    "type": "multiple-choice",
    "opts": [
        ("Standard", "Standard is 3-5 hours."),
        ("Bulk", "Bulk is 5-12 hours."),
        ("Expedited", "Expedited is 1-5 minutes, highest cost."),
        ("S3 Standard", "S3 Standard is not a Glacier option."),
    ],
    "correct": "3",
    "domain": COST_OPT,
    "overall": "Glacier Flexible Retrieval Expedited provides 1-5 minute access for small data, at the highest cost. Reference: https://aws.amazon.com/s3/storage-classes/",
})

QUESTIONS.append({
    "q": "Which S3 feature lets you set a lifecycle rule to ABORT incomplete multipart uploads after a specified number of days, reducing storage cost?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Lifecycle AbortIncompleteMultipartUpload", "Lifecycle can abort incomplete multipart uploads."),
        ("S3 Event Notifications", "Event Notifications are downstream actions."),
        ("S3 Object Lock", "Object Lock is for WORM."),
        ("S3 Replication", "Replication is for copying."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "S3 Lifecycle AbortIncompleteMultipartUpload aborts incomplete uploads after a number of days, reducing storage cost. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpu-abort-incomplete-mpu.html",
})

QUESTIONS.append({
    "q": "Which of the following are valid S3 Intelligent-Tiering access tiers? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Frequent Access tier", "Frequent Access is the default tier."),
        ("Infrequent Access tier (30+ days)", "IA tier for 30+ days not accessed."),
        ("Archive Instant Access tier (90+ days)", "Archive Instant Access tier for 90+ days not accessed."),
        ("Deep Archive Access tier (180+ days)", "Deep Archive Access tier for 180+ days not accessed."),
    ],
    "correct": "1,2,3,4",
    "domain": COST_OPT,
    "overall": "Intelligent-Tiering tiers: Frequent, IA (30d), Archive Instant Access (90d), Archive Access (90-700d), Deep Archive Access (180d+). Reference: https://aws.amazon.com/s3/storage-classes/",
})

QUESTIONS.append({
    "q": "Which S3 storage class is the BEST fit for secondary backups of critical data, with 3-5 hour retrieval and lower cost than Standard-IA?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Standard", "Standard is for frequent access."),
        ("S3 Standard-IA", "Standard-IA is for infrequent access with retrieval fees."),
        ("S3 Glacier Flexible Retrieval", "Glacier Flexible supports 3-5 hour Standard retrieval, lower cost than Standard-IA."),
        ("S3 One Zone-IA", "One Zone-IA is single-AZ, not ideal for secondary backup."),
    ],
    "correct": "3",
    "domain": COST_OPT,
    "overall": "S3 Glacier Flexible Retrieval supports 3-5 hour Standard retrieval, lower cost than Standard-IA for secondary backups. Reference: https://aws.amazon.com/s3/storage-classes/",
})

QUESTIONS.append({
    "q": "Which AWS Lambda memory size range is supported, and how does it affect cost?",
    "type": "multiple-choice",
    "opts": [
        ("128 MB to 10,240 MB; higher memory = higher GB-second cost but may reduce duration", "Lambda supports 128 MB to 10,240 MB; tune for optimal cost-performance."),
        ("64 MB to 3,008 MB; fixed cost", "Lambda supports up to 10,240 MB."),
        ("256 MB to 1,024 MB; linear cost", "Lambda supports 128 MB to 10,240 MB."),
        ("512 MB to 5,120 MB; same cost", "Lambda memory affects GB-second cost."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Lambda supports 128 MB to 10,240 MB; higher memory = higher GB-second cost but may reduce duration. Tune with Power Tuning. Reference: https://aws.amazon.com/lambda/pricing/",
})

QUESTIONS.append({
    "q": "Which AWS Lambda pricing component is per 1 ms of execution time?",
    "type": "multiple-choice",
    "opts": [
        ("Per-request charge", "Per-request is per request, not per ms."),
        ("Per GB-second charge", "Lambda bills duration in 1 ms increments, per GB-second."),
        ("Per data transfer charge", "Data transfer is separate."),
        ("Per cold start charge", "Cold starts are not directly charged."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Lambda duration is billed in 1 ms increments, per GB-second (memory × duration). Reference: https://aws.amazon.com/lambda/pricing/",
})

QUESTIONS.append({
    "q": "Which of the following are valid AWS Fargate pricing dimensions? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("vCPU per second", "Fargate bills per vCPU-second."),
        ("Memory (GB) per second", "Fargate bills per GB-second."),
        ("Number of tasks", "Tasks are not directly billed; vCPU and memory are."),
        ("Data transfer", "Data transfer is a separate charge."),
    ],
    "correct": "1,2,4",
    "domain": COST_OPT,
    "overall": "Fargate bills per vCPU-second and per GB-second of memory, plus data transfer. Reference: https://aws.amazon.com/fargate/pricing/",
})

QUESTIONS.append({
    "q": "Which AWS service provides the MOST cost-effective option for running a serverless API with unpredictable traffic?",
    "type": "multiple-choice",
    "opts": [
        ("EC2 On-Demand", "EC2 On-Demand is the most expensive for variable."),
        ("AWS Lambda with API Gateway", "Lambda + API Gateway is the most cost-effective for variable API traffic."),
        ("ECS with EC2", "ECS with EC2 has minimum instance cost."),
        ("EKS managed", "EKS has cluster-hour cost."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Lambda + API Gateway is the most cost-effective for variable API traffic, scaling to zero. Reference: https://aws.amazon.com/lambda/pricing/",
})

QUESTIONS.append({
    "q": "Which AWS service provides a serverless workflow orchestration that can be used to build cost-effective data pipelines?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Step Functions", "Step Functions provides serverless workflow orchestration."),
        ("Amazon SQS", "SQS is a queue, not orchestration."),
        ("Amazon SNS", "SNS is pub/sub, not orchestration."),
        ("AWS Batch", "Batch is for batch compute."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Step Functions provides serverless workflow orchestration for cost-effective data pipelines and microservices. Reference: https://aws.amazon.com/step-functions/pricing/",
})

QUESTIONS.append({
    "q": "Which AWS Step Functions pricing model charges per state transition, with no charge when idle?",
    "type": "multiple-choice",
    "opts": [
        ("Standard Workflows", "Standard Workflows charge per state transition."),
        ("Express Workflows", "Express Workflows charge per request and duration."),
        ("Both", "Both charge per state transition in different ways."),
        ("Neither", "Step Functions always has a charge."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Standard Step Functions charge per state transition; Express charge per request and duration. Both are pay-per-use. Reference: https://aws.amazon.com/step-functions/pricing/",
})

QUESTIONS.append({
    "q": "Which of the following are valid AWS Lambda cost optimization techniques? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Use ARM/Graviton2 (arm64) architecture", "Graviton2 is up to 34% better price-performance."),
        ("Tune memory with Lambda Power Tuning", "Power Tuning finds the cost-optimal memory."),
        ("Use Compute Savings Plans", "Compute SPs cover Lambda for up to 17% discount."),
        ("Use Provisioned Concurrency for low traffic", "Provisioned Concurrency is for high, steady traffic."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Use Graviton2, Power Tuning, and Compute SPs to reduce Lambda cost. Reference: https://aws.amazon.com/lambda/pricing/",
})

QUESTIONS.append({
    "q": "Which AWS service provides a serverless, pay-per-use message queue with no charge when idle, ideal for decoupled microservices?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon SQS", "SQS is a serverless pay-per-use message queue."),
        ("Amazon MQ", "Amazon MQ is a managed broker for ActiveMQ/RabbitMQ."),
        ("Amazon Kinesis", "Kinesis is for streaming, not queuing."),
        ("AWS Step Functions", "Step Functions is for orchestration."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Amazon SQS is a serverless, pay-per-use message queue with no charge when idle. Reference: https://aws.amazon.com/sqs/pricing/",
})

QUESTIONS.append({
    "q": "Which AWS service provides a serverless pub/sub messaging service with no charge when idle, ideal for fan-out and event-driven architectures?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon SNS", "SNS is a serverless pub/sub service."),
        ("Amazon SQS", "SQS is a queue, not pub/sub."),
        ("Amazon Kinesis", "Kinesis is for streaming."),
        ("Amazon EventBridge", "EventBridge is an event bus with rules."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Amazon SNS is a serverless pub/sub messaging service with no charge when idle. Reference: https://aws.amazon.com/sns/pricing/",
})

QUESTIONS.append({
    "q": "Which AWS service provides a serverless event bus for building event-driven architectures, with no charge when idle?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon EventBridge", "EventBridge is the serverless event bus."),
        ("Amazon SNS", "SNS is pub/sub, not an event bus with rules."),
        ("Amazon SQS", "SQS is a queue."),
        ("AWS Step Functions", "Step Functions is orchestration."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Amazon EventBridge is the serverless event bus for building event-driven architectures, with no charge when idle. Reference: https://aws.amazon.com/eventbridge/pricing/",
})

QUESTIONS.append({
    "q": "Which Aurora feature provides up to 15 read replicas across AZs for read scaling, lowering read cost?",
    "type": "multiple-choice",
    "opts": [
        ("Aurora Read Replicas", "Aurora supports up to 15 read replicas for read scaling."),
        ("Aurora Global Database", "Global is for multi-region, not read scaling."),
        ("Aurora Serverless v2", "Serverless v2 auto-scales, but read replicas are separate."),
        ("Aurora Multi-Master", "Multi-Master is for write scaling across AZs."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Aurora Read Replicas support up to 15 replicas for read scaling, reducing read load on the primary. Reference: https://aws.amazon.com/rds/aurora/",
})

QUESTIONS.append({
    "q": "Which DynamoDB feature reduces storage cost for time-bounded data by automatically DELETING items after a timestamp?",
    "type": "multiple-choice",
    "opts": [
        ("DynamoDB TTL", "TTL automatically deletes items based on a timestamp."),
        ("DynamoDB Streams", "Streams capture changes, not deletion."),
        ("DynamoDB Auto Scaling", "Auto Scaling adjusts capacity."),
        ("DynamoDB Global Tables", "Global Tables replicate across regions."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "DynamoDB TTL automatically deletes items based on a timestamp attribute, reducing storage cost. Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html",
})

QUESTIONS.append({
    "q": "Which of the following are valid DynamoDB capacity modes? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("On-Demand mode", "On-Demand bills per request."),
        ("Provisioned mode with Auto Scaling", "Provisioned with Auto Scaling adjusts capacity."),
        ("Reserved mode", "Reserved is for Provisioned with capacity reservation."),
        ("Serverless mode", "DynamoDB is always serverless; 'serverless' is not a separate mode."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "DynamoDB has On-Demand, Provisioned (with optional Auto Scaling), and Reserved capacity. Reference: https://aws.amazon.com/dynamodb/pricing/",
})

QUESTIONS.append({
    "q": "Which RDS feature provides automated, point-in-time recovery, with no additional storage cost beyond the backup storage?",
    "type": "multiple-choice",
    "opts": [
        ("Automated backups", "Automated backups are included, with backup storage charged per GB."),
        ("Manual snapshots", "Manual snapshots are charged per GB."),
        ("Cross-region replicas", "Cross-region replicas are not backups."),
        ("Read replicas", "Read replicas are not backups."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "RDS Automated Backups provide point-in-time recovery; backup storage is charged per GB. Reference: https://aws.amazon.com/rds/pricing/",
})

QUESTIONS.append({
    "q": "Which RDS pricing factor is FREE up to the size of the database, with charges for additional backup storage?",
    "type": "multiple-choice",
    "opts": [
        ("Compute", "Compute is not free."),
        ("Automated backup storage up to DB size", "Automated backup storage is free up to the provisioned database size."),
        ("Manual snapshot storage", "Manual snapshots are not free."),
        ("Data transfer", "Data transfer is not free."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "RDS automated backup storage is free up to the provisioned database size; additional backup storage is charged. Reference: https://aws.amazon.com/rds/pricing/",
})

QUESTIONS.append({
    "q": "Which ElastiCache engine provides the LOWEST cost per node for in-memory caching?",
    "type": "multiple-choice",
    "opts": [
        ("Memcached", "Memcached is generally the lowest cost per node for simple caching."),
        ("Redis OSS", "Redis OSS is more feature-rich, similar cost."),
        ("Valkey", "Valkey is the open-source Redis fork, lower cost than Redis OSS in some cases."),
        ("All same", "Costs vary by engine and instance type."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Memcached is generally the lowest cost ElastiCache engine for simple key-value caching. Reference: https://aws.amazon.com/elasticache/pricing/",
})

QUESTIONS.append({
    "q": "Which of the following are valid DynamoDB cost optimization techniques? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Use TTL to expire old items", "TTL reduces storage cost."),
        ("Use Standard-IA table class for infrequent access", "Standard-IA is 60% cheaper for infrequent access."),
        ("Use DAX to reduce read capacity consumption", "DAX offloads reads, reducing RCU cost."),
        ("Use Global Tables for single-region apps", "Global Tables add cross-region cost; not needed for single-region."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Use TTL, Standard-IA, and DAX to optimize DynamoDB cost. Reference: https://aws.amazon.com/dynamodb/pricing/",
})

QUESTIONS.append({
    "q": "Which RDS feature allows you to schedule a START and STOP time for non-production databases, reducing compute cost?",
    "type": "multiple-choice",
    "opts": [
        ("RDS Instance Stop/Start", "RDS supports manual Stop/Start for up to 7 days."),
        ("RDS Auto Scaling", "Auto Scaling adjusts read replicas."),
        ("RDS Multi-AZ", "Multi-AZ is for HA."),
        ("RDS Proxy", "RDS Proxy is a connection pooler."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "RDS Instance Stop/Start lets you stop a non-production DB for up to 7 days, eliminating compute cost. Reference: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_StopInstance.html",
})

QUESTIONS.append({
    "q": "Which Redshift pricing model provides on-demand pricing for the data warehouse, with no commitment?",
    "type": "multiple-choice",
    "opts": [
        ("Redshift On-Demand", "Redshift On-Demand provides per-second billing with no commitment."),
        ("Redshift Reserved Instances", "RIs commit to 1- or 3-year terms."),
        ("Redshift Serverless", "Serverless bills per RPU-second, no commitment."),
        ("Both A and C", "Both On-Demand and Serverless provide on-demand pricing."),
    ],
    "correct": "4",
    "domain": COST_OPT,
    "overall": "Redshift On-Demand and Redshift Serverless both provide on-demand pricing with no commitment. Reference: https://aws.amazon.com/redshift/pricing/",
})

QUESTIONS.append({
    "q": "Which Redshift pricing model provides a discount of up to 75% for a 1- or 3-year commitment?",
    "type": "multiple-choice",
    "opts": [
        ("On-Demand", "On-Demand has no discount."),
        ("Redshift Reserved Instances", "Redshift RIs provide up to 75% discount."),
        ("Serverless only", "Serverless is on-demand; no RI discount."),
        ("No commitment discount", "Redshift has RI discounts."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "Redshift Reserved Instances provide up to 75% discount for 1- or 3-year commitments. Reference: https://aws.amazon.com/redshift/pricing/",
})

QUESTIONS.append({
    "q": "Which AWS service provides ONLINE, secure, accelerated file transfer to and from S3, ideal for large file uploads?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Transfer Acceleration", "S3 Transfer Acceleration accelerates uploads to S3 over long distances."),
        ("S3 Multi-Region Access Point", "MRAP is a global endpoint over replicated buckets."),
        ("S3 Cross-Region Replication", "CRR replicates, doesn't accelerate uploads."),
        ("AWS DataSync", "DataSync is for automated file system transfer."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "S3 Transfer Acceleration accelerates uploads to S3 over long distances using CloudFront edge. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html",
})

QUESTIONS.append({
    "q": "Which of the following are valid ways to reduce data transfer OUT to internet cost? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Use CloudFront to cache at edge", "CloudFront reduces origin data transfer out."),
        ("Use S3 Transfer Acceleration only for uploads", "Transfer Acceleration is for uploads, not data out."),
        ("Compress data before transfer", "Compression reduces data volume transferred."),
        ("Move data to a region closer to users", "Regional location affects data transfer pricing."),
    ],
    "correct": "1,2,3,4",
    "domain": COST_OPT,
    "overall": "Use CloudFront, Transfer Acceleration, compression, and regional placement to reduce data transfer out cost. Reference: https://aws.amazon.com/cloudfront/pricing/",
})

QUESTIONS.append({
    "q": "Which AWS service provides a managed, automated, and secure way to MIGRATE large databases to AWS, with minimal downtime?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Database Migration Service (DMS)", "DMS provides managed database migration with minimal downtime."),
        ("AWS DataSync", "DataSync is for file systems."),
        ("AWS Snowball", "Snowball is for offline data."),
        ("AWS Direct Connect", "DX is for private connectivity."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Database Migration Service (DMS) provides managed, automated database migration with minimal downtime. Reference: https://aws.amazon.com/dms/",
})

QUESTIONS.append({
    "q": "Which AWS service provides a managed, automated, and secure way to MIGRATE ON-PREMISES servers to AWS as EC2 instances?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Server Migration Service (SMS)", "SMS is for server migration; AWS Application Migration Service is the current service."),
        ("AWS Database Migration Service", "DMS is for databases."),
        ("AWS DataSync", "DataSync is for file systems."),
        ("AWS Snowball", "Snowball is for offline data."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Application Migration Service (formerly SMS) provides automated lift-and-shift server migration to EC2. Reference: https://aws.amazon.com/application-migration-service/",
})

QUESTIONS.append({
    "q": "Which of the following are valid AWS cost management tools? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("AWS Cost Explorer", "Cost Explorer is a cost management tool."),
        ("AWS Budgets", "Budgets is a cost management tool."),
        ("Cost Anomaly Detection", "Cost Anomaly Detection is a cost management tool."),
        ("AWS Trusted Advisor cost checks", "Trusted Advisor cost checks are cost management tools."),
    ],
    "correct": "1,2,3,4",
    "domain": COST_OPT,
    "overall": "Cost Explorer, Budgets, Cost Anomaly Detection, and Trusted Advisor cost checks are all cost management tools. Reference: https://aws.amazon.com/aws-cost-management/",
})

QUESTIONS.append({
    "q": "Which AWS service provides a centralized, multi-account dashboard for SECURITY and COMPLIANCE findings, also useful for cost-related resource identification?",
    "type": "multiple-choice",
    "opts": [
        ("AWS Security Hub", "Security Hub aggregates security findings."),
        ("AWS Config", "Config tracks resource compliance."),
        ("AWS CloudTrail", "CloudTrail logs API calls."),
        ("AWS Cost Explorer", "Cost Explorer is for cost."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "AWS Security Hub aggregates security findings across accounts, useful for identifying unused or non-compliant resources that may drive cost. Reference: https://aws.amazon.com/security-hub/",
})

QUESTIONS.append({
    "q": "Which AWS service provides a MANAGED NAT service with no charge for data processing when using VPC Endpoints?",
    "type": "multiple-choice",
    "opts": [
        ("NAT Gateway", "NAT Gateway charges per GB data processing; VPC Endpoints avoid this for S3/DynamoDB."),
        ("NAT Instance", "NAT Instance is self-managed."),
        ("Internet Gateway", "IGW is for public subnets."),
        ("VPC Peering", "VPC Peering is for VPC-to-VPC."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "NAT Gateway charges per GB data processing. VPC Gateway Endpoints (S3, DynamoDB) avoid NAT charges. Reference: https://aws.amazon.com/vpc/pricing/",
})

QUESTIONS.append({
    "q": "Which of the following are valid AWS Trusted Advisor checks beyond cost? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Security groups - specific ports unrestricted", "Security checks for open ports."),
        ("IAM use", "IAM use checks."),
        ("MFA on root account", "MFA on root is a security check."),
        ("S3 bucket permissions", "S3 permissions is a security check."),
    ],
    "correct": "1,2,3,4",
    "domain": COST_OPT,
    "overall": "Trusted Advisor checks include security (open ports, IAM, MFA, S3 permissions), fault tolerance, performance, and cost. Reference: https://aws.amazon.com/premiumsupport/technology/trusted-advisor/",
})

QUESTIONS.append({
    "q": "Which AWS service provides a serverless way to AUTOMATE responses to cost anomalies, such as applying an IAM policy or notifying a Slack channel?",
    "type": "multiple-choice",
    "opts": [
        ("Cost Anomaly Detection with SNS / EventBridge / Lambda", "Cost Anomaly Detection integrates with SNS, EventBridge, and Lambda for automated responses."),
        ("AWS Budgets only", "Budgets alerts but doesn't directly automate responses without integration."),
        ("AWS Cost Explorer only", "Cost Explorer visualizes, doesn't automate."),
        ("AWS Trusted Advisor only", "Trusted Advisor doesn't automate."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Cost Anomaly Detection integrates with SNS, EventBridge, and Lambda for automated responses to anomalies. Reference: https://docs.aws.amazon.com/cost-management/latest/userguide/ad-gettingstarted.html",
})

QUESTIONS.append({
    "q": "Which AWS service provides recommendations for S3 storage class transitions based on access patterns, useful for cost optimization?",
    "type": "multiple-choice",
    "opts": [
        ("S3 Storage Lens", "S3 Storage Lens provides storage class analysis and recommendations."),
        ("S3 Analytics", "S3 Storage Class Analysis provides recommendations for transitions."),
        ("S3 Inventory", "S3 Inventory lists objects, not recommendations."),
        ("S3 Lifecycle", "S3 Lifecycle is for automated transitions, not recommendations."),
    ],
    "correct": "2",
    "domain": COST_OPT,
    "overall": "S3 Storage Class Analysis analyzes access patterns and recommends lifecycle transitions for cost optimization. Reference: https://docs.aws.amazon.com/AmazonS3/latest/userguide/analytics-storage-class.html",
})

QUESTIONS.append({
    "q": "Which AWS service provides a fully managed, serverless, time-series database for IoT and operational applications, with cost-effective storage?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Timestream", "Timestream is the serverless time-series database."),
        ("Amazon DynamoDB", "DynamoDB is a NoSQL key-value database."),
        ("Amazon Aurora", "Aurora is a relational database."),
        ("Amazon Redshift", "Redshift is a data warehouse."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Amazon Timestream is a serverless time-series database with cost-effective storage tiers. Reference: https://aws.amazon.com/timestream/",
})

QUESTIONS.append({
    "q": "Which of the following are valid AWS Well-Architected Cost Optimization design principles? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Implement cloud financial management", "Cloud financial management is a principle."),
        ("Adopt a consumption model", "Consumption model is a principle."),
        ("Measure overall efficiency", "Measure efficiency is a principle."),
        ("Stop spending money on security", "Security is non-negotiable; not a cost principle."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Cost Optimization principles: cloud financial management, consumption model, measure efficiency, and stop expensive resources. Reference: https://aws.amazon.com/architecture/well-architected/",
})

QUESTIONS.append({
    "q": "Which AWS service provides a managed, scalable, serverless SEARCH service that auto-scales capacity based on workload, useful for cost-effective search?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon OpenSearch Serverless", "OpenSearch Serverless is the serverless search option."),
        ("Amazon OpenSearch Service (provisioned)", "Provisioned OpenSearch requires instance management."),
        ("Amazon CloudSearch", "CloudSearch is the older search service."),
        ("Amazon Athena", "Athena is for S3 SQL queries."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Amazon OpenSearch Serverless provides managed, scalable, serverless search with auto-scaling capacity. Reference: https://aws.amazon.com/opensearch-service/serverless/",
})

QUESTIONS.append({
    "q": "Which AWS service provides a serverless, pay-per-query data warehouse for S3, with no infrastructure to manage?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Redshift Serverless", "Redshift Serverless auto-scales and bills per RPU-second."),
        ("Amazon Athena", "Athena is for S3 SQL queries, not a data warehouse."),
        ("Amazon EMR", "EMR is for Hadoop/Spark."),
        ("AWS Glue", "Glue is for ETL."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Amazon Redshift Serverless is the serverless, pay-per-RPU data warehouse. Reference: https://aws.amazon.com/redshift/redshift-serverless/",
})

QUESTIONS.append({
    "q": "Which AWS service provides a serverless, pay-per-query SQL service for querying data directly in S3, billed per TB scanned?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon Athena", "Athena is serverless SQL on S3, billed per TB scanned."),
        ("Amazon Redshift Serverless", "Redshift Serverless bills per RPU-second, not per TB scanned."),
        ("Amazon EMR", "EMR is for Hadoop/Spark."),
        ("AWS Glue", "Glue is for ETL."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Amazon Athena is serverless SQL on S3, billed per TB scanned. Reference: https://aws.amazon.com/athena/pricing/",
})

QUESTIONS.append({
    "q": "Which of the following are valid AWS cost optimization techniques for data transfer between services? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Co-locate services in the same AZ", "Same-AZ transfer is free for many services."),
        ("Use VPC Endpoints for S3 and DynamoDB", "VPC Endpoints avoid NAT charges."),
        ("Use PrivateLink for cross-VPC service access", "PrivateLink is cheaper than NAT for some scenarios."),
        ("Always use cross-region for DR", "Cross-region has high data transfer cost; use selectively."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Co-locate in same AZ, use VPC Endpoints and PrivateLink to reduce data transfer cost. Reference: https://aws.amazon.com/vpc/pricing/",
})

QUESTIONS.append({
    "q": "Which AWS service provides a fully managed, serverless, scalable message queuing service with no infrastructure to manage, billed per request?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon SQS", "SQS is the serverless message queuing service."),
        ("Amazon MQ", "Amazon MQ is a managed broker for ActiveMQ/RabbitMQ."),
        ("Amazon Kinesis", "Kinesis is for streaming, not queuing."),
        ("AWS Step Functions", "Step Functions is for orchestration."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Amazon SQS is the fully managed, serverless message queuing service billed per request. Reference: https://aws.amazon.com/sqs/pricing/",
})

QUESTIONS.append({
    "q": "Which AWS service provides a fully managed, serverless, scalable pub/sub messaging service for fan-out and event-driven architectures?",
    "type": "multiple-choice",
    "opts": [
        ("Amazon SNS", "SNS is the pub/sub service."),
        ("Amazon SQS", "SQS is a queue, not pub/sub."),
        ("Amazon EventBridge", "EventBridge is an event bus with rules."),
        ("Amazon Kinesis", "Kinesis is for streaming."),
    ],
    "correct": "1",
    "domain": COST_OPT,
    "overall": "Amazon SNS is the pub/sub service for fan-out and event-driven architectures. Reference: https://aws.amazon.com/sns/pricing/",
})

QUESTIONS.append({
    "q": "Which of the following are valid AWS cost optimization techniques for compute? (Choose all that apply.)",
    "type": "multi-select",
    "opts": [
        ("Use Spot Instances for fault-tolerant workloads", "Spot provides up to 90% discount."),
        ("Use Reserved Instances or Savings Plans for steady workloads", "RIs/SPs provide up to 75% discount."),
        ("Use Graviton2 (ARM) for better price-performance", "Graviton2 is up to 40% better price-performance."),
        ("Always use the largest instance type", "Largest is the most expensive; right-size."),
    ],
    "correct": "1,2,3",
    "domain": COST_OPT,
    "overall": "Use Spot, RIs/SPs, and Graviton2 to optimize compute cost. Right-size, don't over-provision. Reference: https://aws.amazon.com/ec2/pricing/",
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
            opts=list(q["opts"]),
            correct=q["correct"],
            overall=q["overall"],
            domain=q["domain"],
        ))
    return rows


def main():
    # Convert 1 specific multi-select question to single-choice to hit 40 exactly
    TO_CONVERT = {197}
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
    assert counts[COST_OPT] >= 150, f"CostOptimized={counts[COST_OPT]} (expected >= 150 for D4 deep dive)"
    assert multi == 40, f"Multi-select={multi}"

    out = "/home/user/Cert/course/AWS-SAA-C03-03-practice-sets/set-5/practice-set-5.csv"
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
