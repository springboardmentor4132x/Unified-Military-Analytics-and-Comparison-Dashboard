# Quick Stats – Dashboard Specification

## Overview

The Quick Stats dashboard provides a high-level summary of global military power metrics.  
It is designed to give users an immediate snapshot of overall rankings, spending, and asset distribution across countries and regions.

This page acts as the entry point for the full dashboard suite.

---

## Objectives

- Provide a global overview of military power distribution
- Identify top-ranked countries
- Compare defense spending across regions
- Enable region and alliance-based filtering
- Support high-level exploratory analysis

---

## Key KPIs Displayed

1. **Total Countries**
   - Count of all countries included in the dataset.

2. **Average Power Index**
   - Mean value of overall power index across all countries.

3. **Top Country**
   - Country with the best (minimum) overall power rank.

4. **Total Military Manpower**
   - Aggregated active military personnel across selected filters.

5. **Total Defense Budget**
   - Sum of defense budgets (USD) for selected countries.

---

## Filters and Slicers

The following interactive filters are available:

- **Continent**
- **Region**
- **NATO Membership (is_nato)**

These filters dynamically update all KPIs and visualizations on the page.

---

## Visualizations Included

### 1. Overall Power Index by Country
- Horizontal bar chart
- Displays power index comparison
- Sorted by ranking

### 2. Average Assets per Capita by Region
- Pie chart
- Shows distribution of military assets relative to population
- Region-based grouping

### 3. Defense Budget Table
- Tabular representation of:
  - Country
  - Overall Rank
  - Defense Budget (USD)
- Supports sorting


## Data Source

- Input dataset: `military_final.xlsx`
- KPI-engineered dataset from Milestone 2

---

## Technical Notes

- All KPIs are dynamic and filter-responsive.
- Calculations are based on validated KPI definitions.
- Measures are implemented using DAX in Power BI.
- No hardcoded values are used.

---

## Purpose in Dashboard Suite

Quick Stats serves as:

- Executive summary page
- High-level comparison view
- Entry dashboard for deeper analysis modules
