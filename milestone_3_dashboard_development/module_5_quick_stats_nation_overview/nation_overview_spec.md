# Nation Overview – Dashboard Specification

## Overview

The Nation Overview dashboard provides a detailed country-level military analysis.

It allows users to select a specific country and examine its manpower, assets, defense spending, and domain-level military strength in a structured visual format.

This page is designed for in-depth single-country analysis.

---

## Objective

- Provide detailed military insights for an individual country
- Break down manpower composition
- Visualize land, air, and naval strength
- Compare defense spending against economic capacity
- Show asset distribution across military domains

---

## Country Selection

A country selection slicer ("Find Country") allows users to:

- Select a single country
- Dynamically update all KPIs and charts
- Analyze country-specific metrics

All visuals on the page are filter-responsive.

---

## Key KPIs Displayed

1. **Overall Rank**
   - Minimum overall military rank of selected country

2. **Total Military Manpower**
   - Total personnel including:
     - Active
     - Reserve
     - Paramilitary

3. **Defense Budget (USD)**
   - Total defense spending

4. **Total Military Assets**
   - Combined military asset count

---

## Visualizations Included

### 1. Manpower Composition
- Donut chart
- Shows distribution of:
  - Active personnel
  - Reserve personnel
  - Paramilitary forces

### 2. Land Power Composition
- Bar chart
- Displays:
  - Tanks
  - Armored vehicles
  - Artillery units

### 3. Air Power Composition
- Bar chart
- Displays:
  - Fighter aircraft
  - Attack aircraft
  - Helicopters

### 4. Naval Fleet Composition
- Bar chart
- Displays:
  - Total naval fleet
  - Submarines
  - Destroyers
  - Frigates

### 5. Economy vs Defense Spending
- Comparative visualization
- Shows:
  - Purchasing power parity (economic indicator)
  - Defense budget

### 6. Domain Contribution to Military Power
- Horizontal comparison chart
- Shows proportional contribution of:
  - Manpower
  - Air power
  - Land power
  - Naval strength

### 7. Military Assets Breakdown
- Category-wise asset visualization
- Summarizes major equipment totals

---

## Data Source

- Input dataset: `military_final.xlsx`
- KPI-engineered dataset from Milestone 2

---

## Technical Notes

- All metrics are calculated using DAX measures.
- Visuals are dynamically updated based on country selection.
- No hardcoded country-specific logic is used.
- Data model supports single-country filtering.

---

## Role in Dashboard Suite

The Nation Overview page serves as:

- A detailed analytical view
- A drill-down module after Quick Stats
- A country-level intelligence summary page
