# MILESTONE 1 — Data Collection & Initial Cleaning

## Overview
Milestone 1 focuses on **scraping military data** from GlobalFirepower.com and **cleaning the raw data** to prepare for KPI engineering. This milestone consists of two modules: **Module 1 (Scraping)** and **Module 2 (Data Cleaning)**.

## Timeline
**Duration**: 3-6 hours  
**Target Completion**: End of Week 1

## Module Structure

### Module 1: Scraping
- **Location**: `Milestone_1_Data_Collection/Module_1_Scraping/`
- **Objective**: Extract military metrics from GlobalFirepower.com for 140+ countries
- **Deliverable**: `military_raw_data.csv`
- **Time Estimate**: 2-4 hours

**Key Tasks**:
1. Configure scraper settings in `scraper_config.json`
2. Execute `scrape_military_metrics.py`
3. Validate data completeness (≥95% success rate)
4. Review scraping logs

### Module 2: Data Cleaning
- **Location**: `Milestone_1_Data_Collection/Module_2_Data_Cleaning/`
- **Objective**: Standardize column names, remove special characters, handle missing values
- **Deliverable**: `military_cleaned.csv`
- **Time Estimate**: 1-2 hours

**Key Tasks**:
1. Load raw data from Module 1
2. Execute cleaning pipeline with `clean_data.py`
3. Validate data quality (<2% missing)
4. Generate cleaning report

## Success Criteria

✅ **Module 1 (Scraping)**:
- At least 140 countries scraped
- At least 50 indicators collected per country
- Success rate ≥95%
- All metrics properly formatted
- Scraping log available

✅ **Module 2 (Cleaning)**:
- All column names standardized (snake_case)
- All special characters removed
- Numeric fields properly converted
- Missing values handled (<2%)
- Cleaning report generated

## File Structure

```
Milestone_1_Data_Collection/
├── documentation/
│   └── MILESTONE 1 — Data Collection & Initial Cleaning.md
├── Module_1_Scraping/
│   ├── data/
│   │   └── raw/
│   │       └── military_raw_data.csv
│   ├── notebooks/
│   │   └── scrape_notebook.ipynb
│   ├── scrape_military_metrics.py
│   ├── scraper_config.json
│   └── README.md
├── Module_2_Data_Cleaning/
│   ├── data/
│   │   ├── raw/
│   │   │   └── military_raw_data.csv
│   │   └── processed/
│   │       └── military_cleaned.csv
│   ├── notebooks/
│   │   ├── cleaning_notebook.ipynb
│   │   └── clean_data_notebook.ipynb
│   ├── scripts/
│   ├── clean_data.py
│   ├── data_mapping.json
│   └── README.md
└── README.md
```

## Dependencies
- Python 3.8+
- pandas
- numpy
- BeautifulSoup4
- requests
- openpyxl (optional)

## Getting Started

1. Navigate to `Milestone_1_Data_Collection/Module_1_Scraping/`
2. Follow instructions in `README.md`
3. Configure `scraper_config.json`
4. Run `scrape_military_metrics.py`
5. Move to `Milestone_2_Data_Collection/Module_2_Data_Cleaning/`
6. Follow cleaning instructions
7. Run `clean_data.py`

## Output Files

| File | Location | Size | Format |
|------|----------|------|--------|
| `military_raw_data.csv` | `Module_1_Scraping/data/raw/` | 140+ rows | CSV |
| `military_cleaned.csv` | `Module_2_Data_Cleaning/data/processed/` | 140+ rows | CSV |
| Scraping Log | `Module_1_Scraping/` | Log file | TXT |
| Cleaning Report | `Module_2_Data_Cleaning/` | Report file | MD |

## Next Steps

Once Milestone 1 is complete:
→ Move to **Milestone 2: KPI Engineering**
→ Execute KPI calculations
→ Prepare data for dashboard development

---

**Generated**: February 2, 2026  
**Status**: Ready for Implementation
