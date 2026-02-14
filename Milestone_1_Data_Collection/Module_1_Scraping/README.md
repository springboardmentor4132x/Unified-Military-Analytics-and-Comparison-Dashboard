# Module 1: Web Scraping

## Overview
This module extracts military metrics from **GlobalFirepower.com** for 140+ countries using automated web scraping with BeautifulSoup and requests.

## Files

- **scrape_military_metrics.py**: Main scraping script
- **scraper_config.json**: Configuration for scraper behavior
- **notebooks/scrape_notebook.ipynb**: Interactive scraping walkthrough
- **data/raw/military_raw_data.csv**: Output (140+ countries, 50+ indicators)

## Quick Start

1. **Configure**:
   ```json
   // Edit scraper_config.json
   {
     "base_url": "https://www.globalfirepower.com",
     "timeout": 30,
     "retry_attempts": 3,
     "retry_delay": 5
   }
   ```

2. **Run**:
   ```bash
   python scrape_military_metrics.py
   ```

3. **Validate**:
   - Check `data/raw/military_raw_data.csv` exists
   - Verify row count ≥ 140
   - Verify column count ≥ 50

## Success Metrics

✅ At least 140 countries  
✅ At least 50 indicators per country  
✅ Success rate ≥95%  
✅ All rows valid (no null countries)

## Troubleshooting

**Issue**: Connection timeout
- Solution: Increase `timeout` in scraper_config.json

**Issue**: Low success rate
- Solution: Increase `retry_attempts` or `retry_delay`

**Issue**: Missing columns
- Solution: Update CSS selectors in scraper_config.json

## Output

**File**: `data/raw/military_raw_data.csv`  
**Format**: CSV with 140+ rows, 50+ columns  
**Size**: ~5-10 MB

---

**Next**: Move to Module 2 (Data Cleaning)
