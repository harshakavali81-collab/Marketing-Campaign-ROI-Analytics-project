# Resume and interview notes

Use these only after reviewing and understanding the work. This is a portfolio simulation, not employment experience.

## Resume bullets
- Analyzed 3,635 synthetic campaign-day records using Python and SQL, calculating CTR, CPA, ROAS and profit-based ROI across five marketing channels.
- Built a formula-based Excel scorecard and interactive dashboard; reconciled SQL/Python totals and documented data-quality exclusions and budget-testing recommendations.

After completing the native Power BI report, you may add: Created a Power BI report with DAX measures and channel/month filters to compare marketing efficiency.

## 60-second explanation
I worked on a simulated marketing analytics project to compare campaign profitability. I cleaned duplicated and invalid records, analyzed the clean data in SQLite and Python, and calculated metrics from aggregated totals. I separated ROAS, which measures revenue against spend, from ROI, which uses contribution profit. I built an Excel scorecard and browser dashboard. Email had the highest ROI in the generated dataset, but that reflects the simulation assumptions. I recommended a capped experiment and attribution checks before making real budget changes.

## Questions to prepare
1. Why quarantine missing spend? Zero imputation would overstate returns.
2. Why not average campaign ROI? It weights small campaigns the same as large ones; ratio of total profit to total spend gives the portfolio ROI.
3. Why can high ROAS still be unprofitable? Product and fulfilment costs can absorb revenue.
4. Does attribution prove lift? No; incremental impact needs a control group or experiment.
5. What would improve the project? Actual order/refund data, product margins, customer deduplication, attribution comparison and experiments.
6. How was accuracy checked? SQL/Python reconciliation, unique date/campaign keys and nonnegative funnel consistency checks.
