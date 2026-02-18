Project Overview
The Unified Defense Analytics & Comparison Dashboard is a data-driven project designed to collect, process, analyze, and visualize military strength metrics for 140+ countries.
The data is sourced from the Global Firepower website and transformed into an interactive analytical dashboard for country-level comparison.
Project Modules
Module 1: Data Collection (Web Scraping)
This module scrapes country-level military metrics using predefined URLs.
Files
scrape_defense_data.py – Main scraping script
military_links.txt – List of source URLs
military_raw_dataset.csv – Raw scraped dataset
▶️ How to Run
pip install -r requirements.txt
python scripts/scrape_defense_data.py
Output
Structured CSV file containing raw military metrics (no preprocessing applied).
Module 2: Data Cleaning & Preprocessing
This module cleans and standardizes the scraped dataset by:
Handling missing values
Formatting numeric fields
Removing inconsistencies
Standardizing column names
Files
Military_raw_data.py – Data cleaning script
Military_raw_dataset.csv – Input dataset
Military_cleaned_dataset.csv – Cleaned dataset
▶️How to Run
python scripts/clean_defense_data.py
Output
Cleaned and structured dataset ready for analysis.
Module 3: Data Analysis & Comparison
This module performs analytical computations such as:
Country ranking calculations
Category-wise strength comparison
Aggregated military metrics
Performance benchmarking
Files
Military_raw_data.py – Analysis script
Military_cleaned_dataset.csv – Input dataset
Military_processed_data.csv – Analytical output
▶️ How to Run
python scripts/analyze_defense_data.py
📤 Output
Comparative dataset with rankings and calculated insights.
 Module 4: Dashboard Visualization
This module builds an interactive dashboard to visualize country comparisons and insights.
Files
dashboard_app.py – Dashboard application
Military_processed_dataset.csv – Data source
▶️ How to Run
python dashboard_app.py
 Features
1. Country-wise comparison
2. Ranking visualization
3. Category-level military strength analysis
4.Interactive filters and selections
Technologies Used
Python
Pandas
Requests & BeautifulSoup
Data Visualization Libraries (Matplotlib / Plotly / Power BI integration if used)
Project Workflow
Scrape military data
Clean and preprocess dataset
Perform comparative analysis
Build interactive dashboard
