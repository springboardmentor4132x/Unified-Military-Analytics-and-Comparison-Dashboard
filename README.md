# Unified-Military-Analytics-and-Comparison-Dashboard
# Unified Military Analytics Dashboard

## Module 1: Data Scraping 

This module scrapes country-level military metrics for 140+ countries
from GlobalFirepower using a predefined list of URLs.

### Files
- scrape_military_metrics.py – main scraping script
- links_for_military_data.txt – source URLs
- military_raw_data.csv – raw scraped dataset

### Folder Structure

```
Unified-Military-Analytics-and-Comparison-Dashboard-DV/
│
│
├───milestone_1
│   ├───Module_1
│   │   ├───data
│   │   │       aircraft-total-fighters_scrape_military_metrics.csv
│   │   │       links_for_military_data.txt
│   │   │       military_raw_data.csv
│   │   │       power_index_raw.csv
│   │   │
│   │   ├───documentation
│   │   │       Module 1.pdf
│   │   │
│   │   ├───notebooks
│   │   │       scrape_military_metrics.ipynb
│   │   │
│   │   └───scripts
│   │           scrape_military_metrics.py
│   │
│   └───Module_2
│       ├───data
│       │       aircraft-total-fighters_scrape_military_metrics.csv
│       │       military_cleaned.csv
│       │       military_raw_data.csv
│       │       power_index_raw.csv
│       │
│       ├───documentation
│       │       Module 2.pdf
│       │
│       ├───notebooks
│       │       clean_data.ipynb
│       │
│       └───scripts
│               clean_data.py
│
├───milestone_2
│   ├───Module_3
│   │   ├───data
│   │   │       military_final.xlsx
│   │   │
│   │   ├───documentation
│   │   │       Module 3.pdf
│   │   │
│   │   ├───notebooks
│   │   │       generate_kpis.ipynb
│   │   │
│   │   └───scripts
│   │           generate_kpis.py
│   │
│   └───Module_4
│       │   Dashboard application prototype.pdf
│       │   dashboard layouts.pdf
│       │
│       ├───dashboards
│       │       Unified Military Analytics and Comparison Dashboard-DV.pbix
│       │
│       └───documentation
│               Module 4.pdf
│
├───milestone_3
│   │   Unified Military Analytics and Comparison Dashboard-DV.pdf
│   │
│   ├───Module_5
│   │   ├───dashboards
│   │   │       Unified Military Analytics and Comparison Dashboard-DV.pbix
│   │   │
│   │   └───documentation
│   │           Module 5.pdf
│   │
│   └───Module_6
│       ├───dashboards
│       │       global_military_firepower_2025.pbix
│       │
│       └───documentation
│               Module 6.pdf
│
└───milestone_4
    ├───Module_7
    │   │   QA Checklist.pdf
    │   │
    │   └───documentation
    │           Module 7.pdf
    │
    └───Module_8
        └───documentation
                Final Documentation.pdf
```


### How to Run
pip install -r requirements.txt
python scripts/scrape_military_metrics.py

### Output
Raw structured CSV containing all scraped metrics without cleaning.
