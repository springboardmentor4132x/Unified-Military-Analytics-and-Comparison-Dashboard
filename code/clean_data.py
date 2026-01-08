import pandas as pd
import numpy as np
import re

data = pd.read_csv("military_pivot_data.csv")

def clean_value(v):
    if pd.isna(v):
        return np.nan
    v = str(v)
    v = re.sub(r"[,%+]", "", v)
    v = re.sub(r"[^\d.-]", "", v)
    return v

for c in data.columns:
    if c.lower() not in ["country", "country_name", "nation"]:
        data[c] = data[c].apply(clean_value)

for c in data.columns:
    if c.lower() not in ["country", "country_name", "nation"]:
        data[c] = pd.to_numeric(data[c], errors="coerce")

nums = data.select_dtypes(include=["int64", "float64"]).columns

for c in nums:
    data[c] = data[c].fillna(data[c].median())

data.to_csv("military_cleaned.csv", index=False)

print("Data cleaning completed and military_cleaned.csv file created successfully")
