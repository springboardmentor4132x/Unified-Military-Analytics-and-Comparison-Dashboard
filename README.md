# Unified-Military-Analytics-and-Comparison-Dashboard
# Unified Military Analytics Dashboard

## Module 1: Data Scraping 

This module scrapes country-level military metrics for 140+ countries
from GlobalFirepower using a predefined list of URLs.

### Files
- scrape_military_metrics.py – main scraping script
- links_for_military_data.txt – source URLs
- military_raw_data.csv – raw scraped dataset

### How to Run
pip install -r requirements.txt
python scripts/scrape_military_metrics.py

### Output
Raw structured CSV containing all scraped metrics without cleaning.
