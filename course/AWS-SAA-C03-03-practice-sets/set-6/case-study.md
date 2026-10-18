# Set 6 Case Study — **GameDay's Serverless Live Sports Platform**

> **How to use this case study:** Read the scenario below before starting the
> set. Several questions in the set reference this scenario directly. You can
> come back to this README as often as needed during the set.

## Background

**GameDay** is a sports media startup that live-streams amateur and
semi-professional games to a global audience. The platform was originally
built on EC2 + ALB, but the engineering team has decided to migrate to a
fully **serverless** architecture on AWS to eliminate idle capacity cost
and improve global latency.

The platform serves:

- **Live game streams** (HLS, 2-5 Mbps per viewer).
- **Real-time chat** (WebSocket, ~50 messages per second per game).
- **Live scores and stats** updated every 5 seconds.
- **Video on demand** replays (kept for 90 days).
- **A mobile app** for iOS and Android.

## Key facts

- **Peak concurrency:** 500,000 simultaneous viewers during a major
  tournament, 20,000 average.
- **Latency budget:** live chat delivery < 500 ms p99; live score
  updates < 5 s p99; stream start time < 3 s p95.
- **Cost constraint:** variable cost scales linearly with usage, no
  idle capacity at 3 AM.
- **Tech stack:** React + TypeScript frontend, iOS / Android native
  apps, no backend preference as long as it is serverless.
- **Data volume:** 5 PB of video on demand at peak; 200 TB of chat
  history; 50 GB of score / stats.
- **Authentication:** Google, Apple, email magic link.

## Your task

Design the full serverless architecture. Pay particular attention to:

1. The live-stream origin and CDN strategy.
2. The real-time chat backbone (WebSocket API).
3. The live score / stats data path.
4. The video on demand storage and delivery tier.
5. The cost optimization (e.g. CloudFront price classes, S3
   Intelligent-Tiering, Lambda vs Fargate for batch).

## Case-study questions

In the practice set, look for questions that begin with the phrase
**"In the GameDay scenario..."** — these are the case-study questions.
The remaining questions in the set are standalone questions unrelated to
this scenario.

## Scoped extensions and architecture notes

The 20 referenced questions are included in the set's 200-question total. Each question's additional constraints take precedence for that question only:

- A live-video path can use MediaLive for encoding, MediaPackage for packaging/origin, and CloudFront for distribution. The service selection alone does not guarantee the latency objectives; test end to end and request required quotas before the tournament.
- Google and Apple use Cognito social federation; email magic links need a custom authentication challenge flow.
- A regional pilot targets North America and Europe when evaluating CloudFront Price Class 100. This is not the worldwide production audience.
- The HTTP score-summary endpoint permits one-second cached responses. It is separate from WebSocket push delivery.
- VOD file-based transcoding can exceed Lambda's execution limit and uses MediaConvert jobs; Lambda may orchestrate them.
- VOD retention is 90 days. In versioned buckets, cleanup must include noncurrent versions; archiving is not equivalent to deletion.
- The account-administration REST API is separate from the WebSocket chat API. WAF stage association in that question applies to the REST API.
- The Global Accelerator question evaluates an alternative custom WebSocket service behind NLBs, not direct integration with the API Gateway WebSocket service. That alternative is not the fully serverless baseline.
- Player session heartbeats measure active playback sessions. CDN request counts are not unique concurrent-viewer counts.
- The optional commentary-summary feature uses Lambda, Bedrock, and retrieval from OpenSearch Serverless. It is an extension, not a prerequisite for streaming or chat.

Provisioned or session-based media services, stored data, and persistent connections can still incur charges. The zero-idle-compute objective refers to eligible application compute paths, not a promise of a zero total AWS bill.
