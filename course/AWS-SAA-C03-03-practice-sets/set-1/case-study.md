# Set 1 Case Study — **RetailCo's Multi-Region Web Platform**

> **How to use this case study:** Read the scenario below before starting the
> set. Several questions in the set (the "case study questions") reference this
> scenario directly. You can come back to this README as often as needed during
> the set.

## Background

**RetailCo** is a global online retailer headquartered in the United States, with
peak traffic during the holiday season (November-December). Their current
architecture is a single-region deployment in `us-east-1` running a 3-tier web
application on EC2 instances behind an ALB, with an RDS MySQL Multi-AZ
database, a Redis ElastiCache cluster, and S3 for product images and static
assets. The site has been suffering from:

- **Holiday season outages** when traffic spikes 10x.
- **Slow page loads** for international users in Europe and Asia.
- **Compliance concerns** because customer PII (name, address, payment last 4)
  is stored unencrypted at rest in the application database.
- **A small data breach** in Q1 2026 that prompted an audit.

The CTO has asked you, the new AWS Solutions Architect, to redesign the
platform to be more resilient, more secure, and more performant globally,
while **not** increasing the annual AWS spend by more than 15%.

## Key facts

- **Traffic pattern:** 10x peak during November-December; steady baseline the
  rest of the year.
- **Users:** 70% North America, 20% Europe, 10% Asia-Pacific.
- **Data residency requirement:** EU customer PII must remain in the EU;
  US customer PII must remain in the US. The company is fine with
  cross-region replication for DR, but PII must not be stored or processed
  in a non-compliant region.
- **Existing application:** Monolithic Java EE app running on EC2 m5.large
  instances (8 instances, 2 in each of 4 AZs).
- **Database:** RDS MySQL Multi-AZ db.r5.2xlarge, 1 TB General Purpose SSD.
- **Cache:** ElastiCache Redis r5.large, 2 nodes.
- **Storage:** 50 TB of product images in S3 Standard, 10 TB of static
  assets (JS, CSS, fonts).
- **Compliance frameworks in scope:** PCI DSS (because they store payment
  last 4), GDPR (because of EU customers), SOC 2.

## Your task

The CTO has approved a budget increase of up to 15% year-over-year and wants
your architecture proposal. You are NOT expected to write code; you ARE
expected to choose the right AWS services, design the right network
topology, and explain the cost / security / performance trade-offs.

## Case-study questions

In the practice set, look for questions that begin with the phrase
**"In the RetailCo scenario..."** — these are the case-study questions. The
remaining questions in the set are standalone questions unrelated to this
scenario.
