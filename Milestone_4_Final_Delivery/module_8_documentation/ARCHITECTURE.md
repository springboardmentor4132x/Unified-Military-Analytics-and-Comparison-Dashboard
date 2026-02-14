# Architecture Documentation

## System Overview

The Unified Military Analytics Dashboard is built on a modular, 4-milestone architecture that processes, analyzes, and visualizes military data across 140+ countries.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│ MILESTONE 1: DATA COLLECTION & CLEANING                    │
├─────────────────────────────────────────────────────────────┤
│  Module 1: Web Scraper          Module 2: Data Cleaner     │
│  • BeautifulSoup parser         • Column standardization    │
│  • Retry logic (3 attempts)     • Special char removal      │
│  • 140+ countries               • Numeric conversion        │
│  • 50+ indicators               • Missing value handling    │
│                                                             │
│  Input: GlobalFirepower.com     Input: military_raw_data    │
│  Output: military_raw_data.csv  Output: military_cleaned.csv│
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ MILESTONE 2: KPI ENGINEERING                               │
├─────────────────────────────────────────────────────────────┤
│  Module 3: KPI Generator                                    │
│  • 5 Strategic KPIs calculated                             │
│  • Regional metadata (5 regions)                           │
│  • Alliance metadata (NATO, BRICS, etc)                    │
│  • Wide format (analysis)                                  │
│  • Long format (Tableau)                                   │
│                                                             │
│  Input: military_cleaned.csv                               │
│  Output: military_final.xlsx, military_final_long.csv      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ MILESTONE 3: DASHBOARD DEVELOPMENT                          │
├─────────────────────────────────────────────────────────────┤
│  Module 5: Quick Stats & Nation    Module 6: Compare &     │
│  • Dashboard 1: Overview            Coalition              │
│  • Dashboard 2: Country Profile     • Dashboard 3: Compare │
│  • Streamlit/Dash apps              • Dashboard 4: Coalition│
│                                     • Tableau workbooks     │
│                                                             │
│  Input: military_final files        Input: military_final   │
│  Output: Interactive dashboards     Output: Dashboards      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ MILESTONE 4: FINAL DELIVERY                                │
├─────────────────────────────────────────────────────────────┤
│  Module 7: Testing                 Module 8: Documentation │
│  • Unit tests                       • User guides           │
│  • Integration tests                • Developer docs        │
│  • QA validation                    • GitHub release        │
│                                                             │
│  Output: QA Report                 Output: v1.0 Release    │
└─────────────────────────────────────────────────────────────┘
```

## Technology Stack

### Data Processing
- **Python 3.8+**: Core language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **BeautifulSoup4**: Web scraping
- **Requests**: HTTP client

### Visualization
- **Tableau**: Primary dashboard platform
- **Power BI**: Alternative visualization
- **Streamlit**: Python web framework
- **Plotly**: Interactive charts
- **Dash**: Web application framework

### Infrastructure
- **Git**: Version control
- **Jupyter**: Interactive notebooks
- **Python venv**: Environment isolation
- **Windows/Linux/macOS**: Cross-platform support

## Data Flow

```
GlobalFirepower.com
        ↓
    Scraper (Module 1)
        ↓
military_raw_data.csv (raw)
        ↓
    Cleaner (Module 2)
        ↓
military_cleaned.csv (standardized)
        ↓
    KPI Generator (Module 3)
        ↓
military_final.xlsx (wide format)
military_final_long.csv (long format)
        ↓
Dashboards (Module 5 & 6)
        ↓
Interactive Visualizations
```

## Module Interactions

### Module 1 (Scraper)
- **Inputs**: Configuration (scraper_config.json), URL list
- **Processes**: Web scraping, retry logic, error handling
- **Outputs**: military_raw_data.csv
- **Dependencies**: BeautifulSoup, Requests, Pandas

### Module 2 (Cleaner)
- **Inputs**: military_raw_data.csv, data_mapping.json
- **Processes**: Standardization, special char removal, type conversion
- **Outputs**: military_cleaned.csv
- **Dependencies**: Pandas, NumPy

### Module 3 (KPI Generator)
- **Inputs**: military_cleaned.csv, kpi_definitions.json
- **Processes**: KPI calculation, metadata enrichment
- **Outputs**: military_final.xlsx, military_final_long.csv
- **Dependencies**: Pandas, NumPy, openpyxl

### Modules 5 & 6 (Dashboards)
- **Inputs**: military_final files
- **Processes**: Visualization, user interaction, filtering
- **Outputs**: Interactive dashboards
- **Dependencies**: Plotly, Streamlit/Dash/Tableau

## Key Design Patterns

### 1. Configuration-Driven
- External JSON configs (scraper_config.json, data_mapping.json, kpi_definitions.json)
- Easy customization without code changes

### 2. Modular Pipeline
- Each module independent and reusable
- Clear input/output contracts
- Error handling at each step

### 3. Logging & Monitoring
- Comprehensive logging throughout pipeline
- Scraping_log.txt, cleaning_log.txt, kpi_log.txt
- Test reports and QA documentation

### 4. Data Validation
- Quality checks at each stage
- Validation reports generated
- Success metrics tracked

## Scalability Considerations

### For Larger Datasets
- Partition data by region
- Implement batch processing
- Use database backends (PostgreSQL, MongoDB)

### For Real-Time Updates
- Schedule scraper jobs (Cron, Airflow)
- Implement incremental updates
- Cache results (Redis)

### For Multi-User Access
- Deploy to cloud (AWS, Azure, GCP)
- Add authentication (OAuth 2.0)
- Implement role-based access control

## Security Best Practices

1. **Data Protection**
   - No sensitive data in configs
   - Use environment variables for secrets
   - Implement data encryption

2. **Code Security**
   - Regular dependency updates
   - Security linting (Bandit, Safety)
   - Code review process

3. **Infrastructure**
   - HTTPS for all communications
   - Firewall rules
   - Regular backups

## Performance Metrics

- **Scraper**: ~2-4 hours for 140+ countries
- **Cleaner**: ~30 minutes for data standardization
- **KPI Generator**: ~15-20 minutes for calculations
- **Dashboard Load Time**: <3 seconds
- **Filter Response**: <500ms
- **Data Refresh**: <5 seconds

## Error Handling Strategy

```python
try:
    # Execute operation
    result = operation()
except SpecificError:
    # Handle specific error
    log_error()
    recovery_action()
except Exception:
    # Fallback handler
    log_error()
    exit_gracefully()
finally:
    # Cleanup
    cleanup_resources()
```

## Version Control

- **Repository**: GitHub
- **Branches**: main, develop, feature/*
- **Tags**: v1.0, v1.1, etc.
- **Releases**: GitHub Releases with notes

---

**Last Updated**: February 2, 2026  
**Version**: 1.0  
**Status**: Production Ready
