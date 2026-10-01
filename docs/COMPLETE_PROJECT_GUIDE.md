# Marketing Campaign & ROI Analytics - Complete Project Guide

Prepared for Kavali Harshavardhan. This is a reproducible portfolio simulation using synthetic data, not a real client engagement. The project demonstrates Excel, SQL, Python and business reporting. Native Power BI setup assets are provided; a completed .pbix is not included.

## 1. Business problem and scope

Marketing managers need to compare spend, engagement, acquisition efficiency and profit contribution. The central question is: which campaigns and channels produce the strongest observed returns, and what budget experiments should the business test? A high revenue channel can still have poor profitability when acquisition costs or product costs are high.

The project covers 2025, ten campaigns and five channels: Search, Social, Email, Display and Affiliate. Each campaign has a Prospecting or Retention audience label. All currency is INR. Retention is a segment label; no customer history or actual retention-rate measurement exists.

The reporting grain is one date and campaign ID per row. Acquisitions are attributed first purchases rather than globally deduplicated customers. The synthetic revenue convention represents seven-day last-click attribution. This is an assumption, not a reconstructed clickstream attribution calculation.

## 2. Workflow and architecture

Define objectives, generate or collect data, preserve the raw source, clean and quarantine invalid rows, load SQLite, run SQL and Python analysis, calculate aggregated KPIs, compare campaigns, build reporting assets, document recommendations, validate, and publish to GitHub.

See WORKFLOW_AND_STRUCTURE.md for Mermaid diagrams, and diagrams/ for standalone PNG and SVG illustrations. The same diagrams are included in the PDF guide.

The workflow has two output branches. Clean data feeds SQLite and SQL results; it also feeds Python summaries, charts and the offline HTML dashboard. The Excel workbook contains a clean-data snapshot and live formulas. Power BI imports the clean CSV separately and uses DAX measures. Regenerating the Python analysis does not automatically refresh Excel or Power BI.

## 3. Data generation and fields

src/analyze.py generates data only when data/raw_campaigns.csv is absent. NumPy's random generator uses seed 42. The script varies impressions, clicks, acquisition counts, cost per click and order value by channel. Q4 simulated order values have a 1.12 multiplier. The channel assumptions deliberately create different performance patterns; they are not industry benchmarks.

Fields: date, campaign_id, channel, audience, spend, impressions, clicks, acquisitions, revenue and contribution_profit. Cleaning adds month in YYYY-MM format. contribution_profit means revenue minus variable product and fulfilment costs before marketing, using an assumed 55% margin. Net contribution subtracts marketing spend; corporate overhead, taxes and other fixed costs are excluded.

The raw dataset includes intentional problems: twenty repeated records, inconsistent channel labels, missing spend and negative impressions. The purpose is to demonstrate quality checks and explain their business consequences.

## 4. Data cleaning explained

Step 1: Read the raw CSV and remove exact duplicate rows. Retain the source file so cleaning remains auditable.

Step 2: Convert dates with invalid dates coerced to missing. Strip channel whitespace and standardize title case. Convert measurement columns to numeric values.

Step 3: Require all numeric fields to be present and nonnegative. Validate channel membership and a valid date. Require clicks no greater than impressions, acquisitions no greater than clicks, and contribution profit no greater than revenue.

Step 4: Save rejected records to quarantined_rows.csv. Missing spend must not be replaced with zero because that can inflate ROI and ROAS. In real data, investigate and repair rejected records rather than permanently accepting exclusions.

Step 5: Assert unique date/campaign keys on accepted records. Add the month field and export clean_campaigns.csv. Record counts and the rejection rule in cleaning_log.json.

Result: 3,670 raw rows, 20 duplicates removed, 15 quarantined rows and 3,635 accepted rows. Exclusions can bias results and should be disclosed.

One important extension for real data is campaign-to-channel consistency. A label can be a valid channel name but still be wrong for its campaign. The current pipeline validates channel membership, not a reference mapping; add a campaign dimension and mapping check before production use.

## 5. SQL analysis explained

The clean data is stored in outputs/marketing.sqlite, table campaign_daily. The script uses pandas.to_sql with replace mode so reruns recreate the analysis table from current inputs.

Query 1 groups by channel and sums spend, revenue and contribution profit. It calculates net contribution, ROAS, ROI and CPA, ordered by ROI. NULLIF protects against zero denominators.

Query 2 groups by campaign_id, calculates CTR, conversion rate, CPA and ROI, and uses DENSE_RANK to rank campaigns by ROI. Tied ROI values receive the same rank without gaps.

Query 3 groups by month, uses LAG to obtain the previous month's revenue, and calculates revenue growth. January has no preceding month, so its growth is undefined.

Query 4 compares channel and audience combinations. Audience labels can help explain performance mix, but they do not establish whether a campaign caused purchases.

Run python src/analyze.py to execute all four queries and produce sql_result_1.csv through sql_result_4.csv. Open the SQLite file in a SQLite viewer or VS Code extension to inspect the table and rerun individual queries.

## 6. Python EDA and pipeline explained

Pandas reads, cleans and aggregates records. NumPy supplies reproducible random data and numerical reconciliation. Matplotlib creates a four-panel dashboard PNG. SQLite stores data and executes the SQL analysis. The Python standard library provides paths and JSON serialization.

generate() builds the synthetic raw dataset. summarize() calculates totals for either the entire dataset or a grouping field and then derives ratios from those totals. run() orchestrates cleaning, database loading, queries, verification, charts, report generation and the browser dashboard.

The notebook shows sample records, summary statistics, quality checks, channel comparisons and monthly revenue changes. Its saved outputs are illustrative analysis evidence. If you change the dataset, rerun the Python script and then all notebook cells so displayed outputs match current inputs.

The offline dashboard embeds the clean records in HTML; it does not call a web server or external analytics API. Filtering by month or channel recalculates totals in JavaScript. The dashboard is a local deliverable, not a deployed public website.

## 7. KPI definitions and examples

CTR = clicks / impressions. It answers what fraction of impressions resulted in clicks. CPC = spend / clicks. It answers the average cost of a click.

Conversion rate = acquisitions / clicks. CPA = spend / acquisitions. These describe click-to-purchase performance and marketing acquisition cost. CPA is not customer lifetime acquisition cost when cross-channel identity is missing.

ROAS = attributed revenue / marketing spend. ROI = (contribution profit before marketing - marketing spend) / marketing spend. A ROAS of 3.0x means INR 3 of revenue for each INR 1 spent. A 65% ROI means INR 0.65 net contribution per INR 1 spent under the cost assumptions.

Example: spend INR 10,000; revenue INR 30,000; contribution before marketing INR 16,500; acquisitions 50; impressions 100,000; clicks 2,000. ROAS is 3.0x, net contribution INR 6,500, ROI 65%, CPA INR 200, CTR 2%, CPC INR 5 and conversion rate 2.5%. These illustrative values are separate from the dataset totals.

Always aggregate numerators and denominators before calculating rates. For two campaigns with spend 100 and 900 and returns 200 and 900, overall ROAS is 1,100/1,000 = 1.1x, not the simple mean of 2.0x and 1.0x. Zero-denominator ratios remain null rather than being presented as zero.

## 8. Excel workbook explained

excel/Marketing_ROI_Analysis.xlsx includes Campaign analysis and Clean data. The source sheet contains accepted records. The analysis sheet uses SUMIF to aggregate by channel and calculates derived metrics from summed values. The TOTAL row sums totals and recalculates portfolio ratios.

Use the workbook to trace a headline result to source records. Edit a source cost to observe changes in the scorecard and linked chart. When replacing data, keep the source field order and extend formula ranges for a different row count. The delivered workbook is not linked to the CSV file for automatic refresh.

excel/build_workbook.mjs is the original authoring source and depends on @oai/artifact-tool in the Codex runtime. It is not required to run the Python pipeline. Open the delivered workbook directly in Excel for ordinary use.

## 9. Power BI report explained

Use powerbi/BUILD_GUIDE.md. Import clean_campaigns.csv, name the table Campaigns, assign dates and numeric types, then create each DAX measure separately from measures.dax. import.pq supplies a Power Query import template; update its FilePath. theme.json supplies the visual palette.

Overview page: cards for spend, revenue, contribution, CPA, ROAS and ROI; monthly trend; channel ROI; month/channel/audience slicers. Campaigns page: ranking table, channel contribution comparison and campaign efficiency scatterplot. Findings page: recommendations and limitations.

All measures use SUM and DIVIDE so slicers recalculate weighted totals correctly. Do not average a row-level ROI column. Format monetary amounts as INR, rates as percentages, and ROAS as a multiple. Confirm slicers affect each intended visual.

Native Power BI Desktop has not been used in this environment. The assets are setup instructions, not a tested .pbix. After creating the report, reconcile unfiltered totals with overall.csv and filtered channel totals with channel_summary.csv before saving.

## 10. Findings and recommendations

Total spend is INR 17,946,461.73; revenue INR 157,487,468.50; contribution before marketing INR 86,618,108.28; net contribution INR 68,671,646.55. ROAS is 8.7754x, ROI 382.6473%, and CPA INR 222.84.

Email has the highest observed channel ROI in the simulation and Display the lowest. The ranking reflects assumptions built into the generator and is not evidence of real-market channel superiority. Channel grouping also needs a campaign reference mapping before real operational use.

Propose a capped incremental budget test for the efficient channel, audit low-efficiency creatives and targeting, reconcile attributed revenue with refunds and orders, and replace the assumed margin with actual costs. Assess saturation and assisted conversions. Validate causal lift with a randomized holdout or suitable geographic experiment before claiming improvement.

## 11. Validation and practical limits

The pipeline asserts unique date/campaign keys and valid funnel ordering. SQL and Python channel spend, revenue and ROI reconcile using numerical tolerance. Quarantined records and count logs support data-quality review.

Reconciliation between two implementations proves calculation consistency, not correctness of the source or attribution assumptions. Membership validation cannot detect a wrong but valid channel label. No cross-channel customer identity, customer lifetime value, real retention history, causal uplift or production monitoring is implemented.

Suggested production improvements: campaign dimension mapping, order/refund reconciliation, margin by product, repeat customer deduplication, explicit attribution-window logic, date completeness checks, pipeline logging and holdout experiment analysis.

## 12. Run in VS Code on Windows

Install Python and open the extracted marketing-roi folder in VS Code. In its terminal, run python -m venv .venv, then .venv\Scripts\activate. Install dependencies with python -m pip install -r requirements.txt. Run python src/analyze.py. The final printed summary should report SQL/Python reconciliation passed and 3,635 accepted rows for the supplied data.

Open outputs/dashboard.html directly in a browser. Open the Excel workbook in Excel. Open notebooks/EDA.ipynb using the VS Code Python/Jupyter extensions, select your Python environment, and run cells from top to bottom.

If python is not recognized on Windows, try py instead. If an import is missing, confirm the selected notebook environment matches the terminal environment. If file paths fail, open the extracted project folder rather than working inside the ZIP. The script uses paths relative to its source file and can be launched from another directory.

## 13. GitHub, file structure and downloads

The repository is https://github.com/harshakavali81-collab/Marketing-Campaign-ROI-Analytics-project. Clone it or download a ZIP using GitHub's Code menu. The downloadable bundle supplied in chat includes the PDFs, Excel file, all datasets, source code, notebook, reporting outputs and diagram assets.

Read README.md first. docs contains guides and reports; data contains source and quality outputs; src contains the analysis and HTML template; sql contains SQL queries; notebooks contains EDA; excel contains the workbook; powerbi contains import and report setup assets; outputs contains results and dashboards; diagrams contains structure diagrams and their sources.

docs/FILE_MANIFEST.json records each packaged file's path, size and SHA-256 digest. The manifest excludes itself and archive files to avoid circular digests. These digests help detect accidental file changes after download.

## 14. Interview presentation and resume use

Explain the business question, demonstrate filtering, trace one KPI to its formula and source, show the cleaning log, compare SQL and Python, and finish with the limitations and proposed test. A strong answer distinguishes observed attribution from causal impact and revenue efficiency from profit efficiency.

Resume example: Analyzed 3,635 synthetic marketing campaign-day records using Python and SQL, calculating CTR, CPA, ROAS and profit-based ROI across five channels. Built an Excel scorecard and offline dashboard with documented quality exclusions and business recommendations.

Only add a completed Power BI report to your resume after building and reviewing it. Do not claim actual cost savings, client experience, production deployment or independent authorship of code you have not understood. This project supports interview discussion through traceable work; it cannot guarantee selection.
