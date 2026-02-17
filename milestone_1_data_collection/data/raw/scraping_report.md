# Scraping Report – Global Military Data Collection (2025)

## Overview

This document summarizes the automated scraping process used to collect global military data from GlobalFirepower.com.

The goal was to extract country-wise military, economic, and infrastructure metrics and consolidate them into a structured raw dataset for further cleaning and analysis.

---

## Data Source

Primary Source:
https://www.globalfirepower.com

Metric pages scraped include:

- Total population
- Military manpower
- Active and reserve personnel
- Aircraft inventory
- Armor and artillery
- Naval fleet strength
- Defense budget
- Economic indicators
- Infrastructure metrics
- Energy resources

Total metric pages configured: 50+  
Total countries covered: 140+

---

## Tools Used

- Python
- requests
- BeautifulSoup (bs4)
- pandas
- time
- random

---

## Scraping Process

1. Load metric URLs and corresponding metric names from the configuration file.
2. Send HTTP requests using a browser-like User-Agent header.
3. Parse HTML content using BeautifulSoup.
4. Extract:
   - Country name
   - Associated metric value
5. Store results in dictionary format:
   country → { metric_name : value }
6. Convert collected data into a pandas DataFrame.
7. Export the dataset to CSV format.

---

## Stability Measures

- Added User-Agent header to simulate browser requests.
- Introduced a random delay (1.5–3 seconds) between requests.
- Implemented basic error handling for failed HTTP responses.

---

## Output

Generated file:military_raw_data.csv

Dataset characteristics:

- ~140+ country entries
- 50+ military and economic indicators
- Values stored in original scraped format (including commas, %, currency symbols)

---

## Status

Scraping completed successfully.  
Raw dataset ready for cleaning and transformation.


