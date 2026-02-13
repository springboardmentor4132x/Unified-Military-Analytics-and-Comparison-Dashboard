# QA Checklist - Power BI Dashboard

## Dashboard Testing Checklist

### Quick Stats Dashboard
- Top 10 Power Index chart displays correctly
- Region slicer filters all visuals
- Continent slicer filters all visuals
- Alliance slicer filters all visuals
- KPI cards show correct totals
- Navigation button works

### Nation Overview Dashboard
- Country dropdown shows all countries
- Selecting country updates all cards
- KPI cards display correct values
- Charts update with country selection
- Navigation buttons work

### Compare Powers Dashboard
-  Country 1 slicer works independently
-  Country 2 slicer works independently
-  Multi-select slicer filters charts
-  Bar charts show correct comparison
-  Values match source data
-  Navigation buttons work

### Coalition Builder Dashboard
- Multi-select slicer allows multiple countries
- Combined totals calculate correctly (SUM)
- Donut chart shows correct contribution %
- Coalition vs USA comparison charts work
- Navigation buttons work

---

## Data Accuracy Checks

### Spot Check Countries (Verify 5+ countries)
| Country | Field | Expected | Actual | Pass? |
|---------|-------|----------|--------|-------|
| USA | Power Rank | 1 | | |
| China | Power Rank | 2 | | |
| Russia | Power Rank | 3 | | |
| India | Power Rank | 4 | | |
| UK | Power Rank | 5 | | |

### KPI Verification
-  Power Index Rank Gap = (Rank - 1)
- [ ] Assets per Capita formula correct
-  Budget-to-GDP Ratio calculated properly
-  Alliance flags assigned correc 
# visual/Layout Checks
-  All titles readable and spelled correctly
-  No overlapping visuals
-  Consistent colors across dashboards
-  Font sizes appropriate
-  Dashboard fits screen without scroll 
# Navigation Checks
-  Quick Stats → Nation Overview works
-  Nation Overview → Compare Powers works
-  Compare Powers → Coalition Builder works
-  Coalition Builder → Quick Stats works

---

## Final Sign-Off
- Date: ___________
- Tested By: ___________
- All tests passed: [ ] Yes [ ] No
