# Build the Power BI report

Native `.pbix` creation requires Power BI Desktop. These assets are supplied for that final step and have not been executed in Power BI here.

1. Import `data/clean_campaigns.csv` using Text/CSV. Name the table `Campaigns`. Alternatively use `import.pq` in a blank query and set its path.
2. Check date is Date; spend/revenue/contribution_profit are Decimal Number; impression/click/acquisition counts are Whole Number; other fields are Text. The single fact table is at date/campaign grain; no relationships are required for this report.
3. Create each measure in `measures.dax` separately. Format currency measures as INR, rate measures as percentages, and ROAS as `0.00"x"`.
4. Import `theme.json` via the report theme controls.
5. Create Overview page: cards for spend, revenue, net contribution, CPA, ROAS, ROI; line chart with month on X and revenue/spend on Y; clustered bar chart with channel and ROI; slicers for month, channel, audience.
6. Create Campaigns page: table with campaign_id, spend, acquisitions, CPA, ROAS, ROI; bar chart with channel and net contribution; scatter chart with CPA on X, ROI on Y, spend as size and campaign_id as detail.
7. Create Findings page: add text from `docs/FINAL_REPORT.md`, including synthetic-data disclosure, assumptions and proposed holdout test.
8. Add visible titles with units and a synthetic-data banner on every page. Ensure slicers interact with all intended visuals.
9. With all filters cleared, reconcile cards to `outputs/overall.csv`: spend 17,946,461.73; revenue 157,487,468.50; ROI 382.6473%; ROAS 8.7754x.
10. Filter Email and reconcile with `outputs/channel_summary.csv`. Save as `Marketing_ROI_Analytics.pbix` and add it to your repository if desired.

No customer table exists. Do not use DISTINCTCOUNT(acquisitions) or label acquisition totals as unique customers. Blank ratios should remain blank. The month field is YYYY-MM and sorts chronologically.
