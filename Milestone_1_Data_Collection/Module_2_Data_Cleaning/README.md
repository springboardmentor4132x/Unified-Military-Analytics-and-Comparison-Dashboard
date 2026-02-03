# Module 2: Data Cleaning

## Overview
This module cleans and standardizes raw scraped data from Module 1, preparing it for KPI engineering through:
- Column name standardization
- Special character removal
- Numeric conversion
- Missing value handling
- Duplicate removal

## Files

- **clean_data.py**: Main cleaning script
- **data_mapping.json**: Mapping and cleaning rules
- **notebooks/cleaning_notebook.ipynb**: Interactive cleaning walkthrough
- **notebooks/clean_data_notebook.ipynb**: Alternative cleaning approach
- **scripts/**: Support scripts directory
- **data/raw/military_raw_data.csv**: Input (from Module 1)
- **data/processed/military_cleaned.csv**: Output

## Quick Start

1. **Copy Data**:
   ```bash
   # Copy military_raw_data.csv from Module 1 to data/raw/
   ```

2. **Configure** (if needed):
   ```json
   // Edit data_mapping.json to customize cleaning rules
   ```

3. **Run**:
   ```bash
   python clean_data.py
   ```

4. **Validate**:
   - Check `data/processed/military_cleaned.csv` exists
   - Review cleaning report (markdown)
   - Verify data quality (<2% missing)

## Success Metrics

✅ All column names standardized (snake_case)  
✅ All special characters removed (%, $, +, etc.)  
✅ Numeric fields properly converted  
✅ Missing values handled appropriately  
✅ Data quality: <2% missing  
✅ Duplicates removed (based on country)  

## Output

**File**: `data/processed/military_cleaned.csv`  
**Format**: CSV with 140+ rows, 50+ columns  
**Quality**: <2% missing values  
**Report**: `military_cleaned_cleaning_report.md`

## Cleaning Rules

- **Commas**: Removed from all fields
- **Percent signs**: Removed from numeric fields
- **Dollar signs**: Removed from currency fields
- **Plus/minus**: Handled based on context
- **Missing values**: Filled with mean/median or set to 0

## Troubleshooting

**Issue**: Too many missing values after cleaning
- Solution: Review data_mapping.json null handling strategy

**Issue**: Numeric conversion failing
- Solution: Check data_mapping.json numeric columns list

**Issue**: Column names not matching
- Solution: Update column mapping in data_mapping.json

---

**Next**: Move to Milestone 2 (KPI Engineering)
