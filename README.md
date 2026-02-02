# Unified Military Analytics and Comparison Dashboard - DV

A comprehensive, fully interactive dashboard suite for analyzing global military power in 2025. This project scrapes, processes, and visualizes military metrics from 140+ countries using Python-based data pipelines and advanced visualization tools.

## 📋 Project Overview

This dashboard suite enables users to:
- **Quick Stats**: View global rankings, trends, and military highlights
- **Nation Overview**: Analyze detailed country military capabilities
- **Compare Powers**: Side-by-side comparison of any two countries
- **Coalition Builder**: Simulate alliance strength and combined assets

## 🎯 Key Features

✅ Data scraped from GlobalFirepower.com (140+ countries)  
✅ 50+ defense and economic indicators  
✅ 5+ calculated KPIs (Power Index, Assets per Capita, etc.)  
✅ Multi-platform support (Tableau, Streamlit, Dash, Power BI)  
✅ Cross-linked dashboards with dynamic filters  
✅ GitHub-ready structure with full documentation

## 📂 Project Structure

```
├── Milestone_1_Data_Collection/
│   ├── Module_1_Scraping/           # Web scraping scripts
│   └── Module_2_Data_Cleaning/      # Data cleaning & validation
│
├── Milestone_2_KPI_Engineering/
│   ├── Module_3_KPI_Engineering/    # KPI calculation scripts
│   └── Module_4_Dashboard_Planning/  # Dashboard wireframes & prototypes
│
├── Milestone_3_Dashboard_Development/
│   ├── Module_5_Quick_Stats_Nation_Overview/  # Dashboard modules 1-2
│   └── Module_6_Compare_Coalition/            # Dashboard modules 3-4
│
├── Milestone_4_Final_Delivery/
│   ├── Module_7_Testing/            # QA & testing results
│   └── Module_8_Documentation/      # Final documentation
│
├── data/                            # Centralized data storage
├── dashboards/                      # Final dashboard artifacts
├── scripts/                         # Utility scripts & helpers
└── docs/                           # Project documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pandas, numpy, requests, BeautifulSoup4
- Tableau Public/Desktop (optional) or Streamlit/Dash

### Installation
```bash
# Clone repository
git clone <repo-url>
cd Unified-Military-Analytics-and-Comparison-Dashboard-DV

# Install dependencies
pip install -r requirements.txt

# Run data pipeline
python scripts/scrapers/scrape_military_metrics.py
python scripts/cleaners/clean_data.py
python scripts/kpi_generators/generate_kpis.py
```

### Running Dashboards
```bash
# Streamlit
streamlit run dashboards/streamlit/main_app.py

# Dash
python dashboards/dash/app.py
```

## 📊 Milestones & Deliverables

| Milestone | Focus | Status |
|-----------|-------|--------|
| **M1** | Scraping & Cleaning | [Status] |
| **M2** | KPI Engineering | [Status] |
| **M3** | Dashboard Development | [Status] |
| **M4** | Testing & Delivery | [Status] |

## 📈 Data & KPIs

**Data Coverage**: 140+ countries, 50+ indicators  
**Key Metrics**: Budget, Personnel, Aircraft, Tanks, Navy, etc.

**Calculated KPIs**:
- Power Index Rank Gap
- Assets per Capita
- Defense Budget-to-GDP Ratio
- Military Strength Index
- Coalition Aggregation Metrics

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| **Scraping** | Python, requests, BeautifulSoup |
| **Processing** | pandas, numpy |
| **Visualization** | Tableau, Streamlit, Dash, Power BI |
| **Integration** | Parameters, filters, dynamic navigation |
| **Documentation** | Markdown, GitHub |

## 📖 Documentation

- [Installation Guide](Milestone_4_Final_Delivery/Module_8_Documentation/INSTALLATION.md)
- [Usage Guide](Milestone_4_Final_Delivery/Module_8_Documentation/USAGE_GUIDE.md)
- [KPI Reference](Milestone_4_Final_Delivery/Module_8_Documentation/KPI_REFERENCE.md)
- [Architecture](docs/architecture/)

## ✅ Quality Assurance

- ≥95% URL success rate from source list
- <2% missing/null values in cleaned data
- All KPIs validated and documented
- End-to-end dashboard testing completed

## 📝 File Organization Guide

- **Module Folders**: Each module contains its own scripts, data, and documentation
- **data/**: Centralized data storage (raw, processed, final, metadata)
- **dashboards/**: Final deployment-ready dashboard artifacts
- **scripts/**: Shared utility functions and scripts
- **docs/**: Architecture, API references, and supplementary documentation

## 🤝 Contributing

[Add contribution guidelines here]

## 📄 License

[Add license information here]

## 👨‍💻 Authors & Contact

[Add team information here]

---

**Last Updated**: February 2026  
**Status**: In Development
