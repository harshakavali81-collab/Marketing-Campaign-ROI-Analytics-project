# Data dictionary

Grain: one row per calendar date and campaign ID. All values are synthetic; currency INR.

| Column | Meaning |
|---|---|
| date | Campaign reporting date, YYYY-MM-DD |
| campaign_id | Channel plus audience campaign identifier |
| channel | Search, Social, Email, Display, Affiliate |
| audience | Prospecting or Retention segment label |
| spend | Total simulated marketing cost |
| impressions | Ad/email impressions |
| clicks | Attributed clicks, no greater than impressions |
| acquisitions | Attributed first-purchase conversions; no cross-channel unique customer identity |
| revenue | Simulated attributed revenue, 7-day last-click convention |
| contribution_profit | Revenue less variable product/fulfilment costs, before marketing; assumed 55% margin |
| month | Clean-data YYYY-MM grouping field |

Generator: numpy RNG seed 42; channel CTR, conversion rate and CPC assumptions differ. Q4 simulated order values are multiplied by 1.12. Raw anomalies are deliberately introduced to demonstrate cleaning. Do not infer actual industry benchmarks from these assumptions.
