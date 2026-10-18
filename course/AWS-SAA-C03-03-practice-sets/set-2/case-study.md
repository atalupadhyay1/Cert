# Set 2 Case Study — **HealthFirst's HIPAA-Compliant Patient Portal**

> **How to use this case study:** Read the scenario below before starting the
> set. Several questions in the set reference this scenario directly. You can
> come back to this README as often as needed during the set.

## Background

**HealthFirst** is a US-based healthcare provider that runs a patient portal
web application used by 1.5 million patients to book appointments, view
lab results, message their providers, and pay bills. The current
architecture is:

- A single **EC2-based** Java Spring Boot application running in `us-east-1`.
- An **RDS PostgreSQL** Multi-AZ database (`db.r5.xlarge`) storing PHI.
- A **classic load balancer** in front of the app.
- An **SFTP server** for nightly batch uploads of lab results from partner
  labs.
- A separate **on-premises data center** in New Jersey that runs the
  billing system and is connected to AWS via **Direct Connect**.

The architecture has several problems:

- **HIPAA compliance gaps** — PHI is not consistently encrypted at rest,
  access logs are not centralized, and the on-premises-to-AWS link has no
  encryption.
- **Patient complaints about slow lab results** — results take 4-12 hours
  to appear in the portal.
- **A recent ransomware attack** on a peer healthcare provider prompted
  HealthFirst to harden their backups and disaster recovery posture.
- **A failed PCI audit** for the patient billing integration.

## Key facts

- **Compliance frameworks in scope:** HIPAA (mandatory), SOC 2 Type II,
  PCI DSS (for billing), state-level healthcare data regulations.
- **Data:** Protected Health Information (PHI) including diagnoses, lab
  results, medications, and demographic data.
- **RPO target:** 15 minutes.
- **RTO target:** 1 hour.
- **Users:** 1.5M patients, peak usage 7-9 AM and 7-9 PM local time.
- **Latency budget:** patient must see a lab result within 60 seconds of
  release by the lab.
- **Audit requirement:** ALL access to PHI must be logged and retained
  for 7 years.

## Your task

You are the lead AWS Solutions Architect. Design a HIPAA-eligible, highly
resilient, secure architecture for the patient portal. Pay particular
attention to:

1. Encryption at rest and in transit for ALL PHI.
2. Centralized audit logging with 7-year retention.
3. DR strategy that meets RPO 15 min / RTO 1 hour.
4. Network segmentation and least-privilege access.

## Case-study questions

In the practice set, look for questions that begin with the phrase
**"In the HealthFirst scenario..."** — these are the case-study questions.
The remaining questions in the set are standalone questions unrelated to
this scenario.
