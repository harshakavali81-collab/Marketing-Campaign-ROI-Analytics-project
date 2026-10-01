# Marketing Campaign & ROI Analytics — Final Report

Prepared for Kavali Harshavardhan. Portfolio simulation, not a real client engagement.

## Scope and definitions
2025 campaign-day data, 10 campaigns across 5 channels; currency INR. All data is generated with seed 42. Each acquisition is an attributed first purchase, not necessarily a globally unique customer. Revenue is simulated last-click attribution within a 7-day window; no multi-touch or causal inference is possible. Contribution profit before marketing equals revenue less simulated variable product/fulfilment costs (55% margin). Spend is total simulated campaign marketing cost. Net contribution is contribution profit minus spend; it excludes corporate overhead, tax and fixed costs.

## Data quality
3,670 raw rows; 20 exact duplicates removed; 15 invalid rows quarantined; 3,635 analyzed rows. Channel labels normalized. Missing spend is excluded rather than assumed to be zero. Exclusions affect totals and could bias rankings in real data.

## Results
Total spend: INR 17,946,461.73. Attributed revenue: INR 157,487,468.50. Net contribution: INR 68,671,646.55. Overall ROAS: 8.78x. Profit-based ROI: 382.6%. CPA: INR 222.84.

Highest observed ROI: Email (2104.5%); lowest: Display (21.1%). These patterns partly reflect the generator's channel assumptions, so they demonstrate analysis methods rather than real channel superiority.

## Recommendations
1. Test a small, capped budget increase for Email; track marginal CPA and contribution, audience saturation and unsubscribe rates.
2. Audit Display targeting, creatives and landing pages before reducing budget; check assisted conversions and brand objectives.
3. Run a randomized holdout or geographic experiment before claiming incremental lift. Last-click ROAS cannot establish causality.
4. Reconcile attributed revenue with orders and refunds; replace assumed margin with actual product-level costs before financial decisions.

## Validation
SQL and Python channel spend, revenue and ROI reconcile to numerical tolerance. Daily records pass nonnegative values, funnel ordering and unique business-key checks. Overall ratios use sums, never average campaign ratios. Undefined ratios are null, not zero.

## Limitations
No customer-level retention, CLV or cross-channel deduplication. No actual incrementality, seasonality proof or optimization guarantee. Retention is an audience label only. Quarantined data must be investigated before production use.
