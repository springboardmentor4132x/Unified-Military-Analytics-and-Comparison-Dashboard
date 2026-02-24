# Unified Military Analytics and Comparison Dashboard (2025)

## Project Overview

This project develops a fully interactive military analytics dashboard suite for analyzing global military power in 2025.

Using Python-based data pipelines, defense metrics were scraped from GlobalFirepower.com for 140+ countries and transformed into structured KPIs. The final system enables cross-country comparison, coalition simulation, and dynamic dashboard interaction.

The platform integrates data engineering, KPI modeling, and dashboard development into a unified analytical ecosystem.

---

## Project Architecture

The system is built across four major stages:

1. Web Scraping  
2. Data Cleaning & Structuring  
3. KPI Engineering  
4. Dashboard Development & Integration  

---

## Milestone 1 – Data Collection & Preparation

### Module 1: Web Scraping

- Scraped 140+ country-level military indicators  
- Extracted aircraft, manpower, navy, budget, logistics, energy, and geography metrics  
- Stored structured raw output in CSV format  

**Script:** `scrape_military_metrics.py`  
**Output:** `military_raw_data.csv`

---

### Module 2: Data Cleaning

- Removed commas, %, special characters  
- Converted metrics to numeric types  
- Standardized column names  
- Handled missing values (< 2%)  

**Output:** `military_cleaned.csv`

---

## Milestone 2 – KPI Engineering

### Module 3: Feature Engineering

The following KPIs were computed using custom Python scripts:

- **Overall Power Index**
- **Power Index Rank Gap**
- **Assets per Capita**
- **Budget-to-GDP Ratio**
- **Debt Adjustment Factor**
- Alliance Flags (NATO, EU, BRICS)

KPIs were normalized for fair cross-country comparison.

**Script:** `generate_kpis.py`  
**Output:** `military_final.xlsx`

---

## Milestone 3 – Dashboard Development

Four fully integrated dashboards were built:

### 1. Quick Stats
- Top 10 countries by Overall Power Index
- Region / Continent / Alliance filters
- Dynamic KPI cards

### 2. Nation Overview
- Country profile selection
- Domain-wise capability breakdown
- Rank visualization

### 3. Compare Powers
- Side-by-side comparison of any 2 countries
- Military and economic metrics comparison
- KPI contrast view

### 4. Coalition Builder
- Multi-country aggregation
- Combined capability totals
- Alliance strength simulation

All dashboards are interconnected using filters, slicers, and navigation controls.

---

## Milestone 4 – Testing & Documentation

- Validated KPI accuracy
- Verified dashboard navigation
- Debugged visual interactions
- Packaged repository for GitHub release

---

## Tech Stack

**Scraping:** Python, requests, BeautifulSoup  
**Processing:** pandas, numpy  
**Visualization:** Power BI  
**Version Control:** GitHub  
**Documentation:** Markdown  

---

## Key Outcomes

- 140+ countries analyzed  
- 50+ defense & economic indicators unified  
- 5+ engineered KPIs  
- 4 integrated dashboards  
- Fully documented and deployable project  

---

## Contribution

- Designed KPI framework and normalization logic  
- Implemented data cleaning pipeline  
- Built comparison and coalition logic  
- Developed integrated dashboard ecosystem  
- Conducted final validation and presentation  

---

## Repository Structure
