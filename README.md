# Marketing Campaign & ROI Analytics

End-to-end Data Analyst portfolio project for Kavali Harshavardhan using Excel, SQLite, Python and Power BI setup assets.

[Setup](#local-installation--setup-guide) · [Architecture](#architecture--system-design-diagram) · [Detailed guide](PROJECT_GUIDE.md) · [Repository standard](docs/REPOSITORY_STANDARD.md)

## Visuals

![Dashboard](<outputs/dashboard.png>)

Existing project visual; diagrams and illustrative graphics are not evidence of a deployed application.

## Live Link / Demo

Download and open [dashboard.html](outputs/dashboard.html) in a browser. This is a local synthetic-data dashboard, not a live marketing service.

## Key Features

- `data/`: raw, clean and quarantined campaign-day CSVs.
- `sql/analysis.sql`: channel ROI, campaign ranking, month-over-month trend, audience analysis.
- `src/analyze.py`: seeded generator and reproducible analysis.
- `notebooks/EDA.ipynb`: executed notebook with exploratory summaries.
- `outputs/`: SQLite database, SQL results, KPI summaries, dashboard PNG and interactive HTML.
- `excel/`: formatted, formula-based analysis workbook.
- `powerbi/`: DAX measures, Power Query import, theme, data dictionary and dashboard instructions.
- `docs/`: final report, publishing instructions, resume bullets and interview notes.

## Tech Stack

![Python](https://img.shields.io/badge/Python-334155?style=flat-square) ![Pandas](https://img.shields.io/badge/Pandas-334155?style=flat-square) ![NumPy](https://img.shields.io/badge/NumPy-334155?style=flat-square) ![SQL](https://img.shields.io/badge/SQL-334155?style=flat-square)

Dependency versions and optional packages are defined in the repository manifests.

## Architecture / System Design Diagram

Source layout and component inventory (asset not present in this checkout). A runtime architecture diagram remains a follow-up task.

## Local Installation & Setup Guide

```bash
git clone https://github.com/harshakavali81-collab/Marketing-Campaign-ROI-Analytics-project.git
cd Marketing-Campaign-ROI-Analytics-project
```

Python 3.10+ is recommended. From this folder:
```
python -m pip install -r requirements.txt
python src/analyze.py
```
The checked-in raw dataset is used on reruns. Delete it only if you want the seeded generator to recreate it. The pipeline cleans data, saves quarantine records, builds SQLite, executes SQL, reconciles Python/SQL, and regenerates charts, CSVs, HTML and the final report. Excel is a delivered snapshot with live formulas; source regeneration does not automatically refresh its source sheet. Replace clean sheet records to refresh it.

## Challenges & Solutions

**Repository organization:** this project uses `src/`. Keeping those paths stable avoids breaking imports, asset links and deployment commands while the documentation follows a shared format. Project-specific technical limitations and prior release evidence are retained in [Project guide](PROJECT_GUIDE.md).

## Future Improvements

- Capture a reproducible end-to-end demo with runtime versions and sample inputs.
- Expand regression checks for invalid inputs and documented edge cases.
- Record measured results, data provenance and deployment limitations alongside each release.

## Scope and supporting evidence

End-to-end Data Analyst portfolio project for Kavali Harshavardhan using Excel, SQLite, Python and Power BI setup assets.

**Synthetic data only.** This is a simulation, not a client engagement. No actual business growth or savings are claimed.

## Repository Structure

| Location | Purpose |
| --- | --- |
| `src/` | Source modules |
| `docs/` | Documentation |
| `data/` | Data and samples |
| `sql/` | SQL schema and analysis |
| `powerbi/` | Power BI build assets |
| `.github/` | Issue forms, PR template and automated checks |

[Complete file inventory and workflow](docs/REPOSITORY_STANDARD.md). Runtime entry points retain their existing paths.

## Workflow & Tracking

Use the [bug and feature forms](https://github.com/harshakavali81-collab/Marketing-Campaign-ROI-Analytics-project/issues/new/choose) to define work with acceptance criteria. Keep tasks in Todo → In progress → Review → Done, and link a pull request with `Closes #<number>`. See [the maintenance workflow](docs/REPOSITORY_STANDARD.md#workflow).

## License

See [LICENSE](LICENSE) for the existing terms.
