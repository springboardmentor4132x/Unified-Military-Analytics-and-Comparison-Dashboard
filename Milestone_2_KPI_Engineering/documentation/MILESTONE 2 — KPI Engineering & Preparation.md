# MILESTONE 2 — KPI Engineering & Preparation

## Overview
Milestone 2 focuses on **calculating KPIs** from cleaned data and **preparing datasets** in multiple formats for dashboard visualization. This milestone contains **Module 3: KPI Engineering**.

## Timeline
**Duration**: 2-3 hours  
**Target Completion**: End of Week 1

## Module Structure

### Module 3: KPI Feature Engineering
- **Location**: `Milestone_2_KPI_Engineering/Module_3_KPI_Engineering/`
- **Objective**: Calculate 5 strategic KPIs and add metadata enrichment
- **Deliverables**: 
  - `military_final_wide.csv` (Excel format - 1 row per country)
  - `military_final_long.csv` (CSV format - optimized for Tableau)
  - `military_final.xlsx` (Excel workbook with calculations)
- **Time Estimate**: 2-3 hours

**Key Tasks**:
1. Load cleaned data from Milestone 1
2. Calculate 5 KPIs
3. Add region and alliance metadata
4. Create wide and long formats
5. Validate calculations
6. Export to Excel and CSV

## 5 Strategic KPIs

| KPI | Formula | Purpose |
|-----|---------|---------|
| **Power Index Rank Gap** | Rank - 1 | Measures deviation from top rank |
| **Assets per Capita** | Total Assets / Population | Equipment density per person |
| **Budget-to-GDP Ratio** | Defense Budget / GDP × 100 | Military spending as % of GDP |
| **Personnel Density** | Active Military / (Population / 1000) | Soldiers per 1000 population |
| **Equipment Density** | Equipment Count / (Land Area / 1000 km²) | Equipment per 1000 km² |

## Metadata Enrichment

### Regional Classification (5 Regions)
- **Asia**: 40+ countries
- **Europe**: 50+ countries
- **Americas**: 35+ countries
- **Africa**: 55+ countries
- **Oceania**: 10+ countries

### Alliance Classification
- **NATO**: 32+ members
- **BRICS**: 5 members
- **ASEAN**: 10 members
- **EU**: 27 members
- **SCO**: 8+ members

## Success Criteria

✅ **KPI Calculation**:
- All 5 KPIs calculated for ≥140 countries
- No calculation errors or NaN values
- All formulas validated with spot-checks
- Statistical summaries generated

✅ **Data Formats**:
- Wide format: 1 row per country, all KPIs in columns
- Long format: 1 row per country-KPI combination (optimal for Tableau)
- Excel workbook: Clean, formatted, ready for analysis

✅ **Metadata**:
- All countries assigned to regions
- Alliance memberships properly flagged
- Continent classifications accurate
- Lookup tables complete

## File Structure

```
Milestone_2_KPI_Engineering/
├── documentation/
│   └── MILESTONE 2 — KPI Engineering & Preparation.md
├── Module_3_KPI_Engineering/
│   ├── data/
│   │   └── processed/
│   │       ├── military_final_wide.csv
│   │       ├── military_final_long.csv
│   │       └── military_final.xlsx
│   ├── notebooks/
│   │   └── kpi_notebook.ipynb
│   ├── generate_kpis.py
│   ├── kpi_definitions.json
│   └── README.md
└── README.md
```

## Dependencies
- Python 3.8+
- pandas
- numpy
- openpyxl (Excel output)

## Getting Started

1. Copy cleaned data to `data/` folder:
   ```
   military_cleaned.csv → Module_3_KPI_Engineering/data/
   ```

2. Configure KPI settings (optional):
   ```bash
   # Edit kpi_definitions.json if needed
   ```

3. Execute KPI generation:
   ```bash
   python generate_kpis.py
   ```

4. Validate outputs:
   ```bash
   # Check data/processed/ folder for:
   # - military_final_wide.csv (140+ rows, 56+ columns)
   # - military_final_long.csv (700+ rows, 4 columns)
   # - military_final.xlsx (formatted Excel)
   ```

## Output Files

| File | Format | Rows | Columns | Purpose |
|------|--------|------|---------|---------|
| military_final_wide.csv | CSV | 140+ | 56+ | Analysis-ready, one country per row |
| military_final_long.csv | CSV | 700+ | 4 | Tableau-optimized, one KPI per row |
| military_final.xlsx | XLSX | 140+ | 56+ | Formatted Excel with calculations |

## Key Features

✅ **5 Calculated KPIs** for strategic analysis  
✅ **Regional Classification** (5 regions, all 140+ countries)  
✅ **Alliance Metadata** (NATO, BRICS, ASEAN, EU, SCO)  
✅ **Dual Formats** (wide for analysis, long for visualization)  
✅ **Data Validation** (error checking, spot-validation)  
✅ **Statistical Reports** (summaries, distributions)  

## Next Steps

Once Milestone 2 is complete:
→ Move to **Milestone 3: Dashboard Development**
→ Build 4 interactive dashboards
→ Integrate data with Tableau/Power BI

---

**Generated**: February 2, 2026  
**Status**: Ready for Implementation
