# Compare Powers – Dashboard Specification

## Overview

The Compare Powers dashboard enables side-by-side comparison of multiple countries based on military strength, defense spending, manpower, and operational efficiency.

This module supports multi-country selection and comparative analytics.

---

## Objective

- Compare two or more countries simultaneously
- Analyze domain-level strengths
- Evaluate defense budget differences
- Compare manpower and asset capacity
- Assess relative military efficiency

---

## Country Selection

A multi-select country slicer allows users to:

- Select multiple countries
- Dynamically compare selected nations
- Update all visuals based on selection

All visuals are filter-responsive.

---

## Key Visualizations

### 1. Overall Rank Comparison
- Bar chart
- Displays overall military rank for selected countries

### 2. Defense Budget Comparison (USD)
- Bar chart
- Compares total defense budgets

### 3. Military Manpower Comparison
- Bar chart
- Displays total manpower for selected countries

### 4. Air, Land, and Naval Dependency
- Stacked bar chart
- Shows domain dependency distribution:
  - Air
  - Land
  - Naval

### 5. Domain-Wise Power Strength Comparison
- Clustered bar chart
- Compares:
  - Air assets
  - Land assets
  - Naval fleet strength

### 6. Military Vehicles Comparison
- Visual comparison of:
  - Total military aircraft
  - Tanks
  - Armored vehicles

### 7. Budget per Soldier
- Derived efficiency metric
- Defense budget divided by total personnel

### 8. Military Power Efficiency
- Comparative index reflecting
  - Spending relative to power rank
  - Personnel relative to assets

---

## Data Source

- Input dataset: `military_final.xlsx`
- KPI-enhanced dataset from Milestone 2

---

## Technical Notes

- All comparisons are driven by DAX measures.
- Supports multi-country filtering.
- Visual structure ensures proportional comparison.
- No hardcoded country logic.

---

## Role in Dashboard Suite

The Compare Powers module serves as:

- Strategic comparison tool
- Defense budget benchmarking view
- Multi-country analytical module
