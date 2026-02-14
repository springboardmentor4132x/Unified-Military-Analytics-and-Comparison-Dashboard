# 📋 QUICK FILE REFERENCE - WHAT TO RUN WHERE

## 🚀 Start Here (5 Minutes)

1. **Open**: `QUICK_REFERENCE_CARD.md` ← You are here
2. **Read**: `README.md` (project overview)
3. **Review**: `CLEAN_STRUCTURE.md` (file locations)

---

## 📂 Where to Find What

### **Need to Scrape Data?**
```
📁 Milestone_1_Data_Collection/Module_1_Scraping/
├── 🐍 scrape_military_metrics.py          ← RUN THIS
├── ⚙️  scraper_config.json                ← CONFIGURE THIS
├── 📖 README.md                          ← READ THIS FIRST
└── 📔 notebooks/scrape_notebook.ipynb     ← INTERACTIVE DEMO
```
**Steps**:
1. Read `README.md` in this folder
2. Edit `scraper_config.json` if needed
3. Run: `python scrape_military_metrics.py`
4. Output: `data/raw/military_raw_data.csv`

---

### **Need to Clean Data?**
```
📁 Milestone_1_Data_Collection/Module_2_Data_Cleaning/
├── 🐍 clean_data.py                      ← RUN THIS
├── ⚙️  data_mapping.json                 ← CONFIGURE THIS
├── 📖 README.md                          ← READ THIS FIRST
├── 📔 notebooks/cleaning_notebook.ipynb   ← INTERACTIVE DEMO
└── 🔧 scripts/data_validator.py          ← VALIDATION UTILITY
```
**Steps**:
1. Read `README.md` in this folder
2. Ensure `data/raw/military_raw_data.csv` exists
3. Run: `python clean_data.py`
4. Output: `data/processed/military_cleaned.csv`

---

### **Need to Calculate KPIs?**
```
📁 Milestone_2_KPI_Engineering/Module_3_KPI_Engineering/
├── 🐍 generate_kpis.py                   ← RUN THIS
├── ⚙️  kpi_definitions.json              ← CONFIGURE THIS
├── 📖 README.md                          ← READ THIS FIRST
└── 📔 notebooks/kpi_notebook.ipynb        ← INTERACTIVE DEMO
```
**Steps**:
1. Read `README.md` in this folder
2. Ensure cleaned data exists
3. Run: `python generate_kpis.py`
4. Output: `data/processed/military_final*` files

---

### **Need to View Dashboards?**
```
📁 Milestone_3_Dashboard_Development/

Module_5_Quick_Stats_Nation_Overview/
├── 🎨 dashboards/streamlit/app.py        ← RUN THIS (Streamlit)
└── 📔 notebooks/

Module_6_Compare_Coalition/
├── 🎨 dashboards/app.py                  ← RUN THIS (Dash)
```
**Steps**:
1. **Streamlit**: `streamlit run Module_5_Quick_Stats_Nation_Overview/dashboards/streamlit/app.py`
2. **Dash**: `python Module_6_Compare_Coalition/dashboards/app.py`

---

### **Need to Run Tests?**
```
📁 Milestone_4_Final_Delivery/Module_7_Testing/
├── 🧪 test_suite.py                      ← RUN THIS
└── 📖 README.md
```
**Steps**:
1. Run: `python test_suite.py`
2. Output: Test report in console

---

### **Need Documentation?**
```
📁 Milestone_4_Final_Delivery/Module_8_Documentation/
├── 📚 ARCHITECTURE.md          ← System design
├── 📚 DATA_DICTIONARY.md       ← Field definitions
├── 📚 DASHBOARD_USER_GUIDE.md  ← How to use
└── 📚 DEVELOPER_GUIDE.md       ← Extension guide
```

---

## ⏱️ Typical Execution Flow

```
1. Setup (30 min)
   └─ python -m venv venv
   └─ pip install -r requirements.txt

2. Scrape (2-4 hrs)
   └─ cd Milestone_1_Data_Collection/Module_1_Scraping/
   └─ python scrape_military_metrics.py

3. Clean (1-2 hrs)
   └─ cd ../Module_2_Data_Cleaning/
   └─ python clean_data.py

4. KPI (2-3 hrs)
   └─ cd ../../Milestone_2_KPI_Engineering/Module_3_KPI_Engineering/
   └─ python generate_kpis.py

5. Dashboard (12-16 hrs)
   └─ Streamlit: streamlit run Module_5_Quick_Stats.../streamlit/app.py
   └─ Dash: python Module_6_Compare.../app.py

6. Test (3-4 hrs)
   └─ cd Milestone_4_Final_Delivery/Module_7_Testing/
   └─ python test_suite.py

Total: 24-35 hours / 2-3 weeks
```

---

## 📊 Key Files to Know

| File | Purpose | When to Use |
|------|---------|-----------|
| `scrape_military_metrics.py` | Web scraper | Phase 2 |
| `clean_data.py` | Data cleaner | Phase 3 |
| `generate_kpis.py` | KPI generator | Phase 4 |
| `streamlit app.py` | Dashboard 1 | Phase 5-6 |
| `dash app.py` | Dashboard 2 | Phase 7 |
| `test_suite.py` | Tests | Phase 8 |
| `SETUP_GUIDE.md` | Installation | Phase 1 |
| `COMPLETE_BUILD_GUIDELINES.md` | Full roadmap | Anytime |

---

## 🎯 Expected Outputs

### After Scraping
```
data/raw/military_raw_data.csv (140+ countries, 50+ indicators)
scraping_log.txt (execution log)
```

### After Cleaning
```
data/processed/military_cleaned.csv (<2% missing)
military_cleaned_cleaning_report.md (quality report)
cleaning_log.txt (execution log)
```

### After KPI
```
data/processed/military_final.xlsx (Excel)
data/processed/military_final_wide.csv (analysis)
data/processed/military_final_long.csv (Tableau)
kpi_validation_report.md (validation)
```

### After Dashboard
```
Quick Stats Dashboard (http://localhost:8501)
Nation Overview (interactive)
Compare Powers (http://localhost:8050)
Coalition Builder (interactive)
```

### After Testing
```
test_results.txt (all tests)
qa_report.md (detailed report)
```

---

## ✅ Checklist Before Starting

- [ ] Read QUICK_REFERENCE_CARD.md (this file)
- [ ] Read SETUP_GUIDE.md
- [ ] Create Python virtual environment
- [ ] Install dependencies (pandas, requests, beautifulsoup4, plotly, streamlit, dash)
- [ ] Verify folder structure matches Milestone format
- [ ] Check that config files exist
- [ ] Verify Python 3.8+ installed
- [ ] Ensure internet connection (for scraping)

---

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| Python not found | Install Python 3.8+ and add to PATH |
| Missing dependencies | Run: `pip install -r requirements.txt` |
| Module not found | Check working directory |
| Port already in use | Change port in app.py |
| Data file not found | Verify phase completed before running next |
| Network timeout | Increase timeout in config file |
| Dashboard won't load | Check browser console for errors |

---

## 📞 Quick Help

- **Need overview?** → `README.md`
- **Need setup?** → `SETUP_GUIDE.md`
- **Need roadmap?** → `COMPLETE_BUILD_GUIDELINES.md`
- **Need file list?** → `CLEAN_STRUCTURE.md`
- **Need architecture?** → `ARCHITECTURE.md`
- **Need to start?** → `FILES_POPULATED.md`

---

## 🎉 You're All Set!

**Everything is organized, configured, and ready to run.**

### Next Action
→ Open `SETUP_GUIDE.md` for Phase 1 setup instructions

---

**Status**: ✅ Production Ready  
**Files**: 40+ complete  
**Time**: 24-35 hours estimated  
**Confidence**: 100%
