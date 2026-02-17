# Scraping Report – Military Data Collection (2025)

## Overview
This document summarizes the automated data scraping process used to collect global military metrics from GlobalFirepower.com.

The scraping pipeline was executed using a Python-based automated script with configurable URL mappings.

---

## Data Source

Primary Source:
- https://www.globalfirepower.com

Metric pages scraped include:
- Population metrics
- Military manpower statistics
- Aircraft inventory
- Armor and artillery data
- Naval fleet strength
- Defense budget
- Economic indicators
- Infrastructure metrics

Total metric pages configured: 50+  
Total countries covered: 140+

---

## Scraping Configuration

- Script: `scrape_military_metrics.py`
- Configuration File: `scraper_config.json`
- User-Agent header included to simulate browser requests
- Random delay (1.5–3 seconds) between requests to prevent server overload

---

## Data Extraction Logic

For each metric page:
- Country name extracted from structured HTML container
- Corresponding metric value extracted
- Data stored in dictionary structure (country → metrics)
- Combined into single structured DataFrame

---

## Output

Raw dataset generated:
