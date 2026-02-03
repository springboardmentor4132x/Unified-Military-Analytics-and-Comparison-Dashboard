# Project Structure: Milestone & Module Organization Map

## Quick Navigation Guide

This document shows how files are organized by **Milestones** (4 phases) and **Modules** (8 functional areas).

---

## MILESTONE 1: Data Collection & Preparation (Weeks 1-2)

### MODULE 1: Scraping Setup & Execution (Week 1)
**Location**: `milestone_1_data_collection/module_1_scraping/`

| File/Folder | Purpose |
|---|---|
| `scrape_military_metrics.py` | Main web scraping script using BeautifulSoup & requests |
| `scraper_config.json` | Configuration: retry logic, timeouts, user-agent settings |
| `html_cache/` | Optional: Store per-country HTML for debugging |
| `logs/` | Execution logs for scraping runs |

**Deliverable**: `data/raw/military_raw_data.csv` (140+ countries)

**Target**: ≥95% URL success rate

---

### MODULE 2: Data Cleaning & Structuring (Week 1-2)
**Location**: `milestone_1_data_collection/module_2_cleaning/`

| File/Folder | Purpose |
|---|---|
| `clean_data.py` | Data cleaning and standardization pipeline |
| `data_mapping.json` | Column name standardization rules |
| `validation_rules.json` | Data quality thresholds and checks |
| `notebooks/02_data_cleaning.ipynb` | Interactive cleaning workflow & documentation |

**Input**: `data/raw/military_raw_data.csv`  
**Outputs**: 
- `data/processed/military_cleaned.csv` (clean data)
- `data/processed/data_quality_report.md` (QA summary)

**Target**: <2% missing/null data, zero structural errors

---

## MILESTONE 2: KPI Engineering & Tableau Prep (Weeks 3-4)

### MODULE 3: KPI Feature Engineering (Week 3)
**Location**: `milestone_2_kpi_engineering/module_3_kpi_feature_engineering/`

| File/Folder | Purpose |
|---|---|
| `generate_kpis.py` | KPI calculation engine (all 5 KPIs) |
| `kpi_definitions.json` | Mathematical formulas for each KPI |
| `metadata_enrichment.py` | Add region, continent, alliance flags |
| `notebooks/03_kpi_engineering.ipynb` | KPI validation & spot-checking |

**Input**: `data/processed/military_cleaned.csv`  
**Outputs**:
- `data/kpi/military_final.xlsx` (wide format)
- `data/kpi/military_final_long.csv` (Tableau-ready long format)
- `data/kpi/kpi_validation_report.md`

**KPIs Calculated**:
1. Power Index Rank Gap
2. Assets per Capita
3. Budget-to-GDP Ratio
4. Personnel Density (per 1000 pop)
5. Equipment Density (per 1000 km²)

**Target**: All KPIs correctly computed, Tableau-ready format

---

### MODULE 4: Dashboard Planning & Prototyping (Week 3-4)
**Location**: `milestone_2_kpi_engineering/module_4_dashboard_planning/`

| File/Folder | Purpose |
|---|---|
| `wireframes/` | Dashboard layout sketches & mockups |
| `interaction_design.md` | UI/UX specifications & user flows |
| `filter_specifications.json` | Filter types, defaults, interactions |
| `prototype_dashboard.twbx` | Working prototype in Tableau |

**Deliverable**: Storyboards + One operational prototype

**Target**: One dashboard fully operational with sample data

---

## MILESTONE 3: Full Dashboard Development (Weeks 5-6)

### MODULE 5: Quick Stats & Nation Overview (Week 5)
**Location**: `milestone_3_dashboard_development/module_5_quick_stats_nation_overview/`

| File/Folder | Purpose |
|---|---|
| `quick_stats_dev.twbx` | Quick Stats dashboard development file |
| `nation_overview_dev.twbx` | Nation Overview dashboard development file |
| `quick_stats_spec.md` | Feature specifications for Quick Stats |
| `nation_overview_spec.md` | Feature specifications for Nation Overview |

**Features - Quick Stats**:
- Top 10 countries by Power Index
- Region/Continent/Alliance filters
- KPI cards (dynamic values)
- Visualizations: bar charts, pie charts, heatmaps

**Features - Nation Overview**:
- Country selector
- Full profile display
- Radar charts, gauge charts
- Detailed metric tables
- Drill-through to Compare Powers

**Target**: All filters operational, all metrics displaying correctly

---

### MODULE 6: Compare Powers & Coalition Builder (Week 5-6)
**Location**: `milestone_3_dashboard_development/module_6_compare_coalition/`

| File/Folder | Purpose |
|---|---|
| `compare_powers_dev.twbx` | Compare Powers dashboard development |
| `coalition_builder_dev.twbx` | Coalition Builder dashboard development |
| `compare_spec.md` | Feature specifications |
| `coalition_spec.md` | Feature specifications |

**Features - Compare Powers**:
- 2-country side-by-side comparison
- All military metrics
- KPI comparisons
- Difference highlights & percentages

**Features - Coalition Builder**:
- Multi-country selector
- Aggregated coalition metrics
- Compare vs single country or another coalition
- What-if analysis & scenario saving

**Integration**:
- Navigation buttons between all 4 dashboards
- Cross-dashboard parameter linking
- Seamless filter propagation

**Output**: `dashboards/tableau/global_military_firepower_2025.twbx` (FINAL WORKBOOK)

**Target**: Seamless dashboard transitions, all inputs working

---

## MILESTONE 4: Final Review & Delivery (Weeks 7-8)

### MODULE 7: Testing & Debugging (Week 7)
**Location**: `milestone_4_final_delivery/module_7_testing/`

| File/Folder | Purpose |
|---|---|
| `qa_checklist.md` | Comprehensive QA testing document |
| `test_results.md` | Test execution results & outcomes |
| `known_issues.md` | Bug tracking & resolutions |
| `tests/test_scraping.py` | Scraping validation tests |
| `tests/test_data_quality.py` | Data quality tests |
| `tests/test_kpi_calculations.py` | KPI accuracy verification |

**Testing Scope**:
- Filter interactions across all dashboards
- Parameter validation
- Navigation end-to-end testing
- Data accuracy spot-checks (20+ points)
- Performance optimization
- Layout & tooltip verification

**Target**: Zero critical bugs, all navigation verified

---

### MODULE 8: Documentation & GitHub Release (Week 7-8)
**Location**: `milestone_4_final_delivery/module_8_documentation/`

| File/Folder | Purpose |
|---|---|
| `FINAL_README.md` | Comprehensive project README |
| `SCRAPING_GUIDE.md` | How to run scraping, troubleshooting |
| `DASHBOARD_USER_GUIDE.md` | Dashboard usage instructions |
| `KPI_DEFINITIONS.md` | Detailed KPI formulas & methodology |
| `DATA_DICTIONARY.md` | All data fields explained |
| `ARCHITECTURE.md` | System design & data flow |
| `INSTALLATION_GUIDE.md` | Setup & deployment instructions |

**Release Artifacts**:
- GitHub repository (all files organized)
- Version tag (v1.0)
- Optional: Tableau Public publishing

**Target**: Clean, documented, shareable repository

---

## File Organization Summary

### By Milestone
```
milestone_1_data_collection/          → Weeks 1-2 (Data ingestion)
milestone_2_kpi_engineering/          → Weeks 3-4 (Analytics layer)
milestone_3_dashboard_development/    → Weeks 5-6 (Visualization)
milestone_4_final_delivery/           → Weeks 7-8 (Polish & release)
```

### By Data Type
```
data/raw/                              → Raw inputs (milestone 1)
data/processed/                        → Cleaned data (milestone 1-2)
data/kpi/                              → KPI outputs (milestone 2)
dashboards/                            → Final dashboards (milestone 3+)
docs/                                  → Cross-milestone documentation
configs/                               → Configuration files
scripts/                               → Utility scripts
notebooks/                             → Jupyter notebooks
tests/                                 → Test suite
```

### By Deliverable Status

| Status | Files/Location |
|--------|---|
| **In Development** | `module_5_quick_stats_nation_overview/`, `module_6_compare_coalition/` |
| **Planning Phase** | `module_4_dashboard_planning/` |
| **Ready for Input** | `data/raw/` (awaiting URLs, raw data) |
| **Documentation** | `docs/`, `milestone_*/*/` (specs, guides) |

---

## Workflow: Following the Project

### Week 1 - Module 1 (Scraping)
1. Add `links_for_military_data.txt` to `data/raw/`
2. Configure `milestone_1_data_collection/module_1_scraping/scraper_config.json`
3. Run `scrape_military_metrics.py`
4. Output goes to `data/raw/military_raw_data.csv`

### Week 1-2 - Module 2 (Cleaning)
1. Input: `data/raw/military_raw_data.csv`
2. Configure `data_mapping.json` & `validation_rules.json`
3. Run `clean_data.py`
4. Output goes to `data/processed/military_cleaned.csv`

### Week 3 - Module 3 (KPIs)
1. Input: `data/processed/military_cleaned.csv`
2. Configure `kpi_definitions.json` & `metadata_enrichment.py`
3. Run `generate_kpis.py`
4. Output goes to `data/kpi/military_final.xlsx` and `.csv`

### Week 3-4 - Module 4 (Planning)
1. Create dashboard wireframes in `wireframes/`
2. Define filters in `filter_specifications.json`
3. Build prototype in `prototype_dashboard.twbx`

### Week 5-6 - Modules 5 & 6 (Dashboards)
1. Develop 4 dashboards using `data/kpi/` as source
2. Integrate into `global_military_firepower_2025.twbx`
3. Add navigation & parameter linking

### Week 7 - Module 7 (Testing)
1. Execute tests from `tests/`
2. Fill `qa_checklist.md`
3. Document issues in `known_issues.md`

### Week 7-8 - Module 8 (Release)
1. Write documentation in `module_8_documentation/`
2. Organize all files for GitHub
3. Create `.gitignore` & `requirements.txt`
4. Push to GitHub with v1.0 tag

---

## Progress Tracking Template

Use this to track milestone completion:

```
MILESTONE 1: Data Collection & Preparation .............. [ ] 0%
  ├─ MODULE 1: Scraping Setup ............................. [ ] 0%
  └─ MODULE 2: Data Cleaning .............................. [ ] 0%

MILESTONE 2: KPI Engineering & Tableau Prep .............. [ ] 0%
  ├─ MODULE 3: KPI Feature Engineering ................... [ ] 0%
  └─ MODULE 4: Dashboard Planning ......................... [ ] 0%

MILESTONE 3: Full Dashboard Development .................. [ ] 0%
  ├─ MODULE 5: Quick Stats & Nation Overview ............. [ ] 0%
  └─ MODULE 6: Compare Powers & Coalition Builder ........ [ ] 0%

MILESTONE 4: Final Review & Delivery ..................... [ ] 0%
  ├─ MODULE 7: Testing & Debugging ........................ [ ] 0%
  └─ MODULE 8: Documentation & Release ................... [ ] 0%

OVERALL PROJECT COMPLETION ............................... [ ] 0%
```

---

## Cross-Reference: Files to Existing Assets

Your current files can be organized as follows:

| Your File | New Location |
|---|---|
| `military_raw_data.csv` | `data/raw/military_raw_data.csv` |
| `military_cleaned.csv` | `data/processed/military_cleaned.csv` |
| `military_final (1).xlsx` | `data/kpi/military_final.xlsx` |
| `clean_data (1).ipynb` | `milestone_1_data_collection/module_2_cleaning/notebooks/02_data_cleaning.ipynb` |
| `Global Military Powers Stats.pbix` | `dashboards/power_bi/Global_Military_Powers_Stats.pbix` |

---

**Last Updated**: February 2, 2026
**Version**: 1.0 - Initial Structure
