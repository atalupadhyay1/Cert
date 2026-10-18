# Set 4 Case Study — **StartupFast's Cost-Optimized SaaS Platform**

> **How to use this case study:** Read the scenario below before starting the
> set. Several questions in the set reference this scenario directly. You can
> come back to this README as often as needed during the set.

## Background

**StartupFast** is a Series B SaaS company that provides a B2B workflow
automation product. The platform runs on AWS and has 200 paying customers,
most of them small and mid-sized businesses. After the recent Series B
raise, the CFO has asked the engineering team to **cut AWS spend by 40%
over the next 6 months** without impacting customer-facing availability
(target: 99.9%).

The current architecture is over-provisioned:

- EC2 instances are 50% larger than needed (no right-sizing).
- RDS instances are running 24/7 even though traffic is heavily skewed to
  business hours in US time zones.
- All data is in S3 Standard, including a 200 TB archive that is rarely
  accessed.
- NAT gateways are over-provisioned across 3 AZs.
- The team has been buying On-Demand instances for everything, even
  steady-state workloads.

## Key facts

- **Workload pattern:** business hours, US time zone, with weekend drop.
- **Compute baseline:** 40 m5.2xlarge EC2 instances running 24/7.
- **Database:** 3 x db.r5.4xlarge RDS for PostgreSQL Multi-AZ.
- **S3:** 500 TB total, of which 200 TB is in Standard and never accessed
  after 30 days.
- **Egress:** 8 TB/month outbound to customers.
- **Reserved Instance coverage:** 0%.
- **Savings Plan coverage:** 0%.
- **Availability target:** 99.9% (43 minutes of downtime per month).

## Your task

You are the AWS Solutions Architect. Propose specific, measurable
cost-optimization changes that will cut the monthly AWS bill by 40% over
6 months without violating the 99.9% availability target. Quantify the
expected savings for each change.

## Case-study questions

In the practice set, look for questions that begin with the phrase
**"In the StartupFast scenario..."** — these are the case-study questions.
The remaining questions in the set are standalone questions unrelated to
this scenario.
