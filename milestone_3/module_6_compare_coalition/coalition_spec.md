# Coalition Builder – Dashboard Specification

## Overview

The Coalition Builder dashboard simulates combined military strength by aggregating metrics across multiple selected countries.

This module enables what-if analysis of alliances and coalition strength.

---

## Objective

- Evaluate combined manpower and assets
- Estimate aggregated defense spending
- Analyze coalition domain strength
- Simulate alliance-based military comparison

---

## Country Selection

Users can:

- Select multiple countries
- Build a coalition
- View aggregated metrics instantly

All KPIs dynamically update based on selected coalition members.

---

## Key KPIs Displayed

1. **Coalition Total Manpower**
   - Sum of manpower across selected countries

2. **Coalition Total Assets**
   - Sum of military equipment and vehicles

3. **Coalition Defense Budget**
   - Combined defense spending

4. **Coalition Average Budget per Country**
   - Average defense spending across coalition members

5. **Coalition Air Support Ratio**
   - Aircraft relative to manpower

6. **Coalition Naval Projection Ratio**
   - Naval fleet relative to total military assets

---

## Visualizations Included

### 1. Coalition Domain Contribution (%)
- Donut chart
- Shows proportion of:
  - Air power
  - Land power
  - Naval strength

### 2. Military Asset Distribution by Category
- Pie chart
- Displays:
  - Aircraft
  - Tanks
  - Armored vehicles
  - Naval fleet

### 3. Manpower by Country
- Bar chart
- Displays manpower contribution of each coalition member

### 4. Defense Air Power Distribution
- Comparative visual showing air capability distribution

---

## Data Source

- Input dataset: `military_final.xlsx`
- KPI-engineered dataset from Milestone 2

---

## Technical Notes

- Coalition metrics are computed using aggregation measures.
- All KPIs are dynamically recalculated per selection.
- Designed for scenario-based analysis.

---

## Role in Dashboard Suite

The Coalition Builder serves as:

- Alliance simulation tool
- Strategic defense planning view
- Multi-country aggregation module
