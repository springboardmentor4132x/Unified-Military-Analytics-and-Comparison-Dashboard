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

Unified-Military-Analytics-and-Comparison-Dashboard-DV/
│
│
├── Milestone_1/
│   └── Module_1/
│       │
|       ├── data/
│       │   └── military_raw_data.csv
│       |   └── links_for_military_data.txt
│       │
│       ├── documentation
│       │   └── Module 1.pdf
│       │
│       ├── notebooks/
│       │   └── scrape_military_metrics.ipynb
│       │
│       └── scripts/
│           └── scrape_military_metrics.py   
│      
│   
├── Milestone_2/
├── Milestone_3/
├── Milestone_4/
├──.gitignore
├── README.md
└── requirements.txt



### How to Run
pip install -r requirements.txt
python scripts/scrape_military_metrics.py

### Output
Raw structured CSV containing all scraped metrics without cleaning.
