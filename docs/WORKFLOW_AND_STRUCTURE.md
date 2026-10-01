# Workflow, architecture and project structure

## Data processing and reporting

```mermaid
flowchart TD
 A[Raw campaign CSV] --> B[Clean and validate]
 B -->|Invalid rows| Q[Quarantine CSV]
 B -->|Accepted rows| C[Clean campaign CSV]
 C --> D[SQLite and SQL]
 C --> E[Python summaries]
 D --> V[Reconcile results]
 E --> V
 E --> H[Charts and HTML dashboard]
 C --> X[Excel source and formulas]
 C --> P[Power BI import and DAX]
 V --> R[Report and recommendations]
 H --> R
 X --> R
 P -->|Desktop build required| R
```

## KPI calculation dependencies

```mermaid
flowchart TD
 R[Revenue] --> C[Contribution before marketing]
 M[Assumed margin 55 percent] --> C
 C --> N[Net contribution]
 S[Marketing spend] --> N
 N --> I[ROI]
 S --> I
 R --> A[ROAS]
 S --> A
 S --> P[CPA]
 Q[Acquisitions] --> P
```

## Folder structure and responsibilities

```mermaid
flowchart TD
 ROOT[marketing-roi] --> DATA[Data and SQL]
 ROOT --> CODE[Source and notebooks]
 ROOT --> REPORT[Reporting assets]
 ROOT --> DOCS[Docs and diagrams]
 DATA --> RAW[data: raw, clean, quarantine]
 DATA --> SQL[sql: analysis queries]
 CODE --> SRC[src: pipeline and template]
 CODE --> NB[notebooks: EDA]
 REPORT --> EX[excel: workbook]
 REPORT --> BI[powerbi: import, DAX, theme]
 REPORT --> OUT[outputs: database and dashboards]
 DOCS --> GUIDE[docs: PDF and Markdown guides]
 DOCS --> DIAG[diagrams: SVG, PNG and sources]
```

The Excel workbook uses an embedded clean-data snapshot. Python refresh does not automatically update Excel. Power BI assets require a native Desktop report build. The HTML dashboard works offline with embedded data.
