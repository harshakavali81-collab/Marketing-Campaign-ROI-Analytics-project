# Repository standard

## Layout

This repository keeps its working source paths. A shared portfolio structure does not require moving a React application, Python package, BI workbook or Verilog project into identical runtime directories.

| Area | Convention |
| --- | --- |
| Landing page | `README.md`: purpose, visuals, demo, features, stack, architecture, setup, tradeoffs and roadmap |
| Detailed reference | `PROJECT_GUIDE.md`: retained project-specific explanation and historical release notes |
| Documentation | `docs/`: design, inventory, reproduction and evidence |
| Work intake | `.github/ISSUE_TEMPLATE/`: bug and feature forms |
| Review | `.github/PULL_REQUEST_TEMPLATE.md`: linked issue, behavior and validation |
| Automation | `.github/workflows/portfolio-docs.yml`: README section and local-link checks |
| Source and tests | Existing project-specific paths listed below; no empty source/test placeholders |

## Workflow

1. Open an issue describing the user problem and measurable acceptance criteria.
2. Add it to a GitHub Project with Todo, In progress, Review and Done states when a board is configured.
3. Use a focused branch and meaningful commits, such as `docs: correct local setup paths` or `fix(api): reject malformed input`.
4. Run the project's documented checks and `python scripts/check_portfolio_docs.py`.
5. Open a pull request with actual validation results and `Closes #<issue-number>`.
6. Merge after review; record release evidence and update the issue/board.

Board creation, profile pins, repository social previews and milestone settings require account-level configuration. This file does not claim those settings have been applied.

## Validation scope

The documentation check validates the landing-page headings and local link targets only. It does not execute models, certify test coverage, inspect Git history for secrets, verify external websites, or prove production readiness. Existing application workflows remain the source of runtime CI evidence.

Keep credentials in local environment variables. A gitignore rule does not remove secrets already tracked or committed. Use only permitted sample data in public demos.

## Inventory at standardization

The following are the pre-existing public project files. New standardization files are described above. Historical guides may mention external bundles that are not part of this list.

- [`LICENSE`](<../LICENSE>)
- [`README.md`](<../README.md>)
- [`data`](<../data>)
- [`data/clean_campaigns.csv`](<../data/clean_campaigns.csv>)
- [`data/quarantined_rows.csv`](<../data/quarantined_rows.csv>)
- [`data/raw_campaigns.csv`](<../data/raw_campaigns.csv>)
- [`diagrams`](<../diagrams>)
- [`diagrams/kpi_dependencies.png`](<../diagrams/kpi_dependencies.png>)
- [`diagrams/kpi_dependencies.svg`](<../diagrams/kpi_dependencies.svg>)
- [`diagrams/project_structure.png`](<../diagrams/project_structure.png>)
- [`diagrams/project_structure.svg`](<../diagrams/project_structure.svg>)
- [`diagrams/workflow.png`](<../diagrams/workflow.png>)
- [`diagrams/workflow.svg`](<../diagrams/workflow.svg>)
- [`docs`](<../docs>)
- [`docs/COMPLETE_PROJECT_GUIDE.md`](<../docs/COMPLETE_PROJECT_GUIDE.md>)
- [`docs/DATA_DICTIONARY.md`](<../docs/DATA_DICTIONARY.md>)
- [`docs/FILE_MANIFEST.json`](<../docs/FILE_MANIFEST.json>)
- [`docs/FINAL_REPORT.md`](<../docs/FINAL_REPORT.md>)
- [`docs/GITHUB_SETUP.md`](<../docs/GITHUB_SETUP.md>)
- [`docs/Marketing_Campaign_ROI_Project_Report.pdf`](<../docs/Marketing_Campaign_ROI_Project_Report.pdf>)
- [`docs/Marketing_ROI_Complete_Guide.pdf`](<../docs/Marketing_ROI_Complete_Guide.pdf>)
- [`docs/RESUME_AND_INTERVIEW.md`](<../docs/RESUME_AND_INTERVIEW.md>)
- [`docs/WORKFLOW_AND_STRUCTURE.md`](<../docs/WORKFLOW_AND_STRUCTURE.md>)
- [`docs/build_documentation.py`](<../docs/build_documentation.py>)
- [`excel`](<../excel>)
- [`excel/Marketing_ROI_Analysis.xlsx`](<../excel/Marketing_ROI_Analysis.xlsx>)
- [`excel/build_workbook.mjs`](<../excel/build_workbook.mjs>)
- [`notebooks`](<../notebooks>)
- [`notebooks/EDA.ipynb`](<../notebooks/EDA.ipynb>)
- [`outputs`](<../outputs>)
- [`outputs/campaign_summary.csv`](<../outputs/campaign_summary.csv>)
- [`outputs/channel_summary.csv`](<../outputs/channel_summary.csv>)
- [`outputs/cleaning_log.json`](<../outputs/cleaning_log.json>)
- [`outputs/dashboard.html`](<../outputs/dashboard.html>)
- [`outputs/dashboard.png`](<../outputs/dashboard.png>)
- [`outputs/marketing.sqlite`](<../outputs/marketing.sqlite>)
- [`outputs/monthly_summary.csv`](<../outputs/monthly_summary.csv>)
- [`outputs/overall.csv`](<../outputs/overall.csv>)
- [`outputs/sql_result_1.csv`](<../outputs/sql_result_1.csv>)
- [`outputs/sql_result_2.csv`](<../outputs/sql_result_2.csv>)
- [`outputs/sql_result_3.csv`](<../outputs/sql_result_3.csv>)
- [`outputs/sql_result_4.csv`](<../outputs/sql_result_4.csv>)
- [`powerbi`](<../powerbi>)
- [`powerbi/BUILD_GUIDE.md`](<../powerbi/BUILD_GUIDE.md>)
- [`powerbi/import.pq`](<../powerbi/import.pq>)
- [`powerbi/measures.dax`](<../powerbi/measures.dax>)
- [`powerbi/theme.json`](<../powerbi/theme.json>)
- [`requirements.txt`](<../requirements.txt>)
- [`sql`](<../sql>)
- [`sql/analysis.sql`](<../sql/analysis.sql>)
- [`src`](<../src>)
- [`src/analyze.py`](<../src/analyze.py>)
- [`src/dashboard_template.html`](<../src/dashboard_template.html>)
