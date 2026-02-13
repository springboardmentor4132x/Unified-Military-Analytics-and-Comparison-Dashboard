# Unified Military Analytics and Comparison Dashboard

A comprehensive Power BI analytics suite for analyzing global military power in 2025. Built using data scraped from GlobalFirepower.com covering 140+ countries and 50+ military/economic indicators.

## 🎯 Project Overview

This project develops a fully interactive dashboard suite for analyzing global military power in 2025. Using Python, military metrics are scraped from GlobalFirepower.com for 140+ countries via a pre-defined URL list (`links_for_military_data.txt`).

The platform unifies 50+ defense and economic indicators across four interconnected dashboards:

1. **Quick Stats** – Global overview of rankings, trends, and highlights
2. **Nation Overview** – Detailed analysis of individual country capabilities
3. **Compare Powers** – Side-by-side military and economic comparison
4. **Coalition Builder** – Interactive simulation of alliance strength and combined assets

---

## 📁 Project Structure (By Milestones)

```
unified-military-analytics/
│
├── Milestone_1_Data_Collection/
│   ├── scripts/
│   │   └── scrape_military_metrics.py   # Web scraping script
│   └── data/
│       ├── raw/                         # Raw HTML/scraped data
│       └── military_cleaned.csv         # Cleaned dataset
│
├── Milestone_2_KPI_Engineering/
│   ├── scripts/
│   │   └── generate_kpis.py             # KPI calculation script
│   ├── config/
│   │   ├── power_rankings.json          # Country power rankings (145 countries)
│   │   ├── regions.json                 # Region/continent mappings
│   │   └── alliances.json               # Alliance memberships (NATO, BRICS, etc.)
│   └── data/
│       ├── military_final.csv           # Final processed data with KPIs
│       ├── military_final.xlsx          # Excel format for Power BI
│       └── military_long_format.csv     # Long format for advanced charts
│
├── Milestone_3_Dashboard_Development/
│   ├── dashboard/
│   │   └── global_military_firepower_2025.pbix
│   └── notebooks/
│       └── data_exploration.ipynb
│
├── Milestone_4_Final_Delivery/
│   └── docs/
│       ├── qa_checklist.md              # Testing checklist
│       └── dashboard_usage_guide.md     # How to use the dashboards
│
├── README.md
├── links_for_military_data.txt          # Source URLs for scraping
└── DV_Unified Military Analytics and Comparison Dashboard (1).pdf
```

---

## 🕷️ Scraping Method

### Data Collection Pipeline

1. **URL Source:** All URLs are loaded from `links_for_military_data.txt` (50+ metric pages)
2. **Scraping Script:** `scrape_military_metrics.py` uses `requests` + `BeautifulSoup`
3. **Process:**
   - Fetches each ranking page from GlobalFirepower.com
   - Parses HTML to extract country name, rank, and metric value
   - Uses CSS selectors targeting `recordsetContainer`, `rankNumContainer`, `longFormName`, and `valueContainer`
   - Saves raw HTML to `data/raw/html_pages/` for debugging
   - Merges all metrics per country into a single wide-format row
   - Outputs `military_raw_data.csv`
4. **Rate Limiting:** Random delay (1-3 seconds) between requests to respect server
5. **Error Handling:** Failed URLs are logged and skipped; retries not needed (95%+ success rate)

### Data Cleaning
- Remove special characters (commas, %, +, $)
- Convert all metrics to numeric formats
- Standardize column names (e.g., `active_military_manpower`, `aircraft_total`)
- Handle missing/null values (< 2% after cleaning)
- Output: `military_cleaned.csv`

---

## 🔢 KPI Definitions

### Custom KPIs (Computed in `generate_kpis.py`)

| KPI | Formula | Description |
|-----|---------|-------------|
| **Power Index Rank Gap** | `Official GlobalFirepower Rank - 1` | Distance from the #1 ranked nation |
| **Assets per Capita** | `(Aircraft + Tanks + AFVs + Ships + Submarines) / Population × 100,000` | Military assets per 100K citizens |
| **Budget-to-GDP Ratio** | `Defense Budget / Purchasing Power Parity × 100` | Percentage of GDP spent on defense |
| **Personnel Ratio** | `Active Military / Total Population × 100` | Percentage of population in active service |
| **Air Power Score** | `aircraft_total × 10 + helicopters_total × 5` | Composite air capability index |
| **Naval Power Score** | `navy_ships × 5 + submarines × 50 + carriers × 500 + destroyers × 100 + frigates × 50` | Composite naval capability index |
| **Land Power Score** | `tanks × 10 + AFVs × 5 + artillery × 8` | Composite ground force index |

### Enrichment Fields

| Field | Source | Description |
|-------|--------|-------------|
| `region` | `config/regions.json` | Geographic region (e.g., South Asia, Western Europe) |
| `continent` | `config/regions.json` | Continent (e.g., Asia, Europe) |
| `alliance_nato` | `config/alliances.json` | NATO membership flag (0/1) |
| `alliance_brics` | `config/alliances.json` | BRICS membership flag (0/1) |
| `alliances` | Computed | Combined alliance string (e.g., "NATO, FIVE_EYES") |

---

## 📈 How to Open and Use the Dashboards

### Prerequisites
- **Power BI Desktop** (free download from [Microsoft](https://powerbi.microsoft.com/desktop/))
- Windows 10/11

### Opening the Dashboard
1. Navigate to `Milestone_3_Dashboard_Development/dashboard/`
2. Open `global_military_firepower_2025.pbix`
3. Click **Refresh** to load the latest data

### Dashboard 1: Quick Stats
- View **Top 10 military powers** by Power Index
- Use **Region/Continent/Alliance** slicers to filter data
- See global summary KPI cards

### Dashboard 2: Nation Overview
- Select any country from the **dropdown**
- View full military profile with KPI scores
- Analyze bar charts for all major categories

### Dashboard 3: Compare Powers
- Select **Country 1** (left slicer) and **Country 2** (right slicer)
- Use **multi-select slicer** to control bar charts
- Compare metrics: Aircraft, Tanks, Ships, Personnel, Budget

### Dashboard 4: Coalition Builder
- **Ctrl+click** to select multiple countries in the slicer
- View **combined totals** (personnel, aircraft, fleet, budget)
- See **donut chart** showing each country's contribution
- Compare coalition strength vs **USA** in bar charts

### Navigation
Use the navigation buttons at the bottom of each page:
- Quick Stats ↔ Nation Overview ↔ Compare Powers ↔ Coalition Builder

> For detailed instructions, see `Milestone_4_Final_Delivery/docs/dashboard_usage_guide.md`

---

## 📊 Milestone Summary

| Milestone | Description | Deliverables |
|-----------|-------------|--------------|
| **1** | Data Collection & Preparation | `scrape_military_metrics.py`, raw data, `military_cleaned.csv` |
| **2** | KPI Engineering & Power BI Prep | `generate_kpis.py`, config files, `military_final.csv/.xlsx` |
| **3** | Dashboard Development | 4 interconnected Power BI dashboards |
| **4** | Final Review & Delivery | QA checklist, documentation, GitHub release |

---

## 🛠 Tech Stack

| Area | Tools/Libraries |
|------|-----------------|
| Scraping | Python, BeautifulSoup, Requests |
| Processing | Pandas, NumPy |
| Visualization | Power BI Desktop |
| Integration | DAX Measures, Parameters, Filters, Navigation Buttons |
| Documentation | Markdown, GitHub |

---

## 📝 Data Sources

- [GlobalFirepower.com](https://www.globalfirepower.com) – Military rankings and statistics (2025 edition)

## 👥 Author

Vivek – Unified Military Analytics Project

## 📄 License

This project is for educational purposes only. Data sourced from GlobalFirepower.com.
