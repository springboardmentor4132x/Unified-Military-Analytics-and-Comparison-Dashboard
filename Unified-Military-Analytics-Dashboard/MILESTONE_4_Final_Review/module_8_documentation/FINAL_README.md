# Unified Military Analytics and Comparison Dashboard – 2025

##  Project Overview

This project develops a structured analytics framework for analyzing global military power in 2025. The system collects military data through web scraping, performs KPI engineering, and visualizes insights using interactive Power BI dashboards.

The platform enables:

- Global military ranking analysis
- Country-level capability assessment
- Side-by-side country comparison
- Coalition strength simulation
- KPI-driven analytical insights
- Interactive filtering and dynamic exploration


##  Data Collection (Web Scraping)

Military data was collected from:

- GlobalFirepower.com

### Scraping Methodology

- Python was used for web scraping.
- `requests` library was used to fetch HTML pages.
- `BeautifulSoup` was used to parse military metric blocks.
- Extracted metrics included manpower, aircraft, tanks, naval assets, defense budget, and GDP.
- Data was structured and exported into Excel format for further processing.

This ensured automated and scalable data acquisition.


## 🛠 Tech Stack

### Data Collection
- Python
- requests
- BeautifulSoup

### Data Processing
- pandas
- Microsoft Excel

### KPI Engineering
- Derived metric calculations in Excel

### Visualization
- Microsoft Power BI Desktop (.pbix)

### Documentation & Version Control
- GitHub


##  Key Performance Indicators (KPIs)

The following KPIs were engineered:

### 1. Power Index Rank Gap
Difference between ranking positions for comparative analysis.

### 2. Assets per Capita
Total military assets divided by population to normalize strength.

### 3. Defense Budget-to-GDP Ratio
Percentage of GDP allocated to defense spending.

### 4. Coalition Aggregated Strength
Sum of manpower, air power, naval strength, and land systems for selected countries.

All KPIs were validated before dashboard integration.

---

##  Project Milestones

### Milestone 1 – Data Collection & Preparation
- Implemented Python-based web scraping
- Extracted and structured 140+ country metrics
- Cleaned and standardized dataset

### Milestone 2 – KPI Engineering
- Computed analytical KPIs
- Prepared final dataset for visualization

### Milestone 3 – Dashboard Development
Developed interactive dashboards:
- Quick Stats
- Nation Overview
- Compare Powers
- Coalition Builder

Implemented dynamic slicers and comparative visuals.

### Milestone 4 – Testing & Documentation
- Validated KPI calculations
- Tested dashboard interactions
- Fixed formatting and aggregation issues
- Structured GitHub repository for final release

---

##  How to Use

1. Navigate to:
   Unified-Military-Analytics-Dashboard\MILESTONE_3_Dashboard_Development

2. Open using Microsoft Power BI Desktop.

3. Use slicers to explore country comparisons and coalition simulations.


##  Final Status

✔ Web scraping implemented  
✔ Dataset structured and validated  
✔ KPIs engineered and verified  
✔ Dashboards fully functional  
✔ Documentation completed  
✔ Ready for academic evaluation and portfolio presentation  

---

##  Author

Developed as part of the Unified Military Analytics and Comparison Dashboard initiative (2025).
