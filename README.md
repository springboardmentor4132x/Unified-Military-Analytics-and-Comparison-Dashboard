# Unified Military Analytics and Comparison Dashboard
 
**Data Source:** [GlobalFirepower.com](https://www.globalfirepower.com)  
**Coverage:** 140+ countries, 50+ defense and economic indicators, 2025 data  
**Final Dashboard:** `global_military_firepower_2025.pbix` (Power BI)

---

## Project Overview

This project builds a fully interactive analytics dashboard suite for analyzing global military power in 2025. Military metrics are scraped from GlobalFirepower.com using a pre-defined URL list, processed through Python-based data pipelines, and visualized across four interconnected dashboard modules.

| Dashboard Module | Description |
|-----------------|-------------|
| Quick Stats | Global rankings, top-10 by Power Index, trends and highlights |
| Nation Overview | Full country profile with bar/radar charts and tooltips |
| Compare Powers | Side-by-side comparison of any 2 countries across all metrics |
| Coalition Builder | Multi-country selector showing aggregated coalition strength |

Key KPIs computed: Power Index Rank Gap, Assets per Capita, Defense Budget-to-GDP Ratio

---

## Repository Structure

```
Unified-Military-Analytics-and-Comparison-Dashboard/
│
├── milestone_1_data_collection/              # Weeks 1-2: Scraping & Cleaning
│   │
│   ├── Documentaiton_module_1_and_2/
│   │   └── Module_1_and_2 documentation.pdf
│   │
│   ├── module_1_scraping/                    # Module 1: Scraping Setup & Execution
│   │   ├── datasets/
│   │   │   └── military_raw_data.csv         # Raw output: 140+ countries, 50+ metrics
│   │   └── scripts/
│   │       ├── scrape_military_metrics.py    # Main scraping script (requests + BeautifulSoup)
│   │       └── links for military data.txt   # Source URLs for all 140+ country pages
│   │
│   └── module_2_cleaning/                    # Module 2: Data Cleaning & Structuring
│       ├── dataset/
│       │   └── military_cleaned.csv          # Cleaned dataset (<2% nulls, numeric formats)
│       └── scripts/
│           └── clean_data.ipynb              # Cleaning notebook (pandas/numpy)
│
├── milestone_2_kpi_engineering/              # Weeks 3-4: KPI Engineering & Prototyping
│   │
│   ├── Module 3 and 4 documentation/
│   │   └── Module_3_and_4_documentation.pdf
│   │
│   ├── module_3_kpi_feature_engineering/     # Module 3: KPI Feature Engineering
│   │   ├── datasets/
│   │   │   └── military_final.xlsx           # Final enriched dataset with all KPIs
│   │   ├── generate_kpis.py                  # (root-level copy)
│   │   └── scripts/
│   │       └── generate_kpis.py              # Computes KPIs, adds region/alliance metadata
│   │
│   └── module4/                              # Module 4: Dashboard Planning & Prototype
│       └── dashboard/
│           ├── Module4_Draft_Layout.pdf      # Wireframes for all 4 dashboard pages
│           └── module_4_quick_dashboard.pbix # Early Power BI prototype (Quick Stats)
│
├── milestone_3_dashboard_development/        # Weeks 5-6: Full Dashboard Build
│   │
│   ├── Module 5 and 6 Documentation/
│   │   └── Unified_Military_Analytics_Module_5_6_Documentation.pdf
│   │
│   ├── module_5_quick_stats_nation_overview/ # Module 5: Quick Stats + Nation Overview
│   │   ├── Module_5_Dashboards.pbix          # Power BI file for tabs 1 & 2
│   │   ├── quick_stats_spec.md               # Spec: filters, KPI cards, top-10 charts
│   │   └── nation_overview_spec.md           # Spec: country selector, radar/bar charts
│   │
│   └── module_6_compare_coalition/           # Module 6: Compare Powers + Coalition Builder
│       ├── Module6 Dashboard.pbix            # Power BI file for tabs 3 & 4
│       ├── compare_spec.md                   # Spec: 2-country side-by-side comparison
│       └── coalition_builder.md              # Spec: multi-country selector & aggregation
│
└── milestone_4_final_delivery/               # Weeks 7-8: Testing, Docs & Release
    │
    ├── Milestone 4 documentation/
    │   ├── Milestone_4_Final_Review_and_Delivery_Report.pdf
    │   └── global_military_firepower_2025.pbix   # Final dashboard (copy)
    │
    ├── Module 7 and 8 Dashboard/
    │   └── global_military_firepower_2025.pbix   # Final dashboard (copy)
    │
    └── global_military_firepower_2025.pbix        # FINAL DELIVERABLE
```

---

## How to Run

**Step 1 - Scrape the data**

```bash
python milestone_1_data_collection/module_1_scraping/scripts/scrape_military_metrics.py
```

This reads country URLs from `links for military data.txt`, scrapes each page using `requests` and `BeautifulSoup`, and saves the result to `military_raw_data.csv`.

**Step 2 - Clean the data**

Open and run all cells in:

```
milestone_1_data_collection/module_2_cleaning/scripts/clean_data.ipynb
```

This removes special characters (`%`, `+`, commas), converts all metrics to numeric types, and standardizes column names like `total_aircraft` and `active_personnel`. Output is `military_cleaned.csv`.

**Step 3 - Generate KPIs**

```bash
python milestone_2_kpi_engineering/module_3_kpi_feature_engineering/scripts/generate_kpis.py
```

This computes Power Index Rank Gap, Assets per Capita, and Budget-to-GDP Ratio, then enriches the data with region, continent, and alliance metadata (e.g., NATO flags). Output is `military_final.xlsx`.

**Step 4 - Open the dashboard**

Open the file below in Power BI Desktop:

```
milestone_4_final_delivery/global_military_firepower_2025.pbix
```

---

## KPI Definitions

| KPI | Formula | Purpose |
|-----|---------|---------|
| Power Index Rank Gap | Country Rank - Global Average Rank | Measures relative standing vs. the world |
| Assets per Capita | Total Military Assets / Population | Normalizes military size by population |
| Budget-to-GDP Ratio | Defense Budget / GDP x 100 | Reflects military spending as a share of economy |

---

## Tech Stack

| Area | Tools |
|------|-------|
| Scraping | Python, requests, BeautifulSoup |
| Data Processing | pandas, numpy |
| Data Visualization | Power BI |
| Documentation | Markdown, PDF |
| Hosting | GitHub |

---

## Evaluation Targets

| Milestone | What is measured | Target |
|-----------|-----------------|--------|
| 1 - Scraping | URL success rate | 95% or more of provided URLs |
| 1 - Cleaning | Missing/null values | Less than 2% after cleaning |
| 2 - KPI Engineering | KPIs computed correctly | 5 or more KPIs validated |
| 3 - Dashboard | All tabs built and linked | Full integration, navigation working |
| 4 - Delivery | Final packaging and usability | No bugs, clean GitHub repo |

---

## Key Files Quick Reference

| File | Location | Purpose |
|------|----------|---------|
| `links for military data.txt` | `module_1_scraping/scripts/` | Source URLs for scraping |
| `scrape_military_metrics.py` | `module_1_scraping/scripts/` | Web scraper |
| `clean_data.ipynb` | `module_2_cleaning/scripts/` | Data cleaning pipeline |
| `military_raw_data.csv` | `module_1_scraping/datasets/` | Raw scraped data |
| `military_cleaned.csv` | `module_2_cleaning/dataset/` | Cleaned data |
| `generate_kpis.py` | `module_3_kpi_feature_engineering/scripts/` | KPI computation |
| `military_final.xlsx` | `module_3_kpi_feature_engineering/datasets/` | Final dataset for dashboard |
| `global_military_firepower_2025.pbix` | `milestone_4_final_delivery/` | Final dashboard |
