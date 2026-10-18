# Set 3 Case Study — **Streamify's Real-Time Video Analytics Pipeline**

> **How to use this case study:** Read the scenario below before starting the
> set. Several questions in the set reference this scenario directly. You can
> come back to this README as often as needed during the set.

## Background

**Streamify** is a media analytics startup that ingests **video streams**
from 50,000+ live events per day (concerts, sports, conferences) and runs
real-time computer-vision analytics on each stream to:

- Detect brand logos and count impressions per second.
- Identify crowd sentiment (positive / neutral / negative).
- Generate highlight clips in real time.
- Push 10-second aggregate metrics to a dashboard used by brand sponsors.

The current architecture uses on-premises GPU servers and is unable to
scale to meet peak demand. Streamify is migrating to AWS.

## Key facts

- **Ingestion rate:** 50,000 concurrent live streams at peak, 200,000 hours
  of video per day.
- **Per-frame analysis:** a computer-vision model runs at 5 FPS per stream
  (so 250,000 inferences per second at peak).
- **Latency budget:** aggregate metrics must reach the sponsor dashboard
  within 10 seconds of the video frame.
- **Storage:** raw video is retained 30 days for re-processing; aggregate
  metrics are retained 2 years for analytics.
- **Data volume:** ~5 PB of video per month.
- **Cost constraint:** the migration must not increase the unit cost per
  analyzed video minute by more than 20%.
- **Workload pattern:** highly spiky — concert events cause 50x spikes in
  specific regions.

## Your task

Design the data ingestion, processing, storage, and analytics pipeline
that scales to peak load, meets the 10-second latency budget, controls
cost, and can replay historical video for re-processing. Pay particular
attention to:

1. The compute layer for real-time inference.
2. The buffer between ingestion and processing.
3. The storage tier for raw video vs. aggregate metrics.
4. The autoscaling strategy that handles 50x spikes cost-effectively.

## Case-study questions

In the practice set, look for questions that begin with the phrase
**"In the Streamify scenario..."** — these are the case-study questions.
The remaining questions in the set are standalone questions unrelated to
this scenario.
