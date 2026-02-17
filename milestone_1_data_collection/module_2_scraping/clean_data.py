import pandas as pd

# Load raw data
df = pd.read_csv("military_raw_data.csv")

df.head()

# Clean numeric values
def clean_number(value):
    if pd.isna(value):
        return value
    value = str(value)
    value = value.replace(",", "")
    value = value.replace("$", "")
    value = value.replace("%", "")
    return value

for col in df.columns:
    if col != "country":
        df[col] = df[col].apply(clean_number)

# Convert to numeric
for col in df.columns:
    if col != "country":
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Handle missing values
df = df.fillna(0)

# Save cleaned data
df.to_csv("military_cleaned.csv", index=False)

df.head()

df.columns

