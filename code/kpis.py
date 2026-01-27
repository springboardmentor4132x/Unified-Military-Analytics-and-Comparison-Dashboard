import pandas as pd
import numpy as np

df = pd.read_csv("military_cleaned.csv").fillna(0)

for c in df.columns:
    if c != "country_name":
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0)

avg_rank = df["global_rank"].mean()
df["power_index_rank_gap"] = df["global_rank"] - avg_rank

asset_cols = [
    "aircraft-total",
    "armor-apc-total",
    "armor-mlrs-total",
    "armor-self-propelled-guns-total",
    "armor-tanks-total",
    "navy-ships",
    "navy-submarines",
    "navy-destroyers",
    "navy-frigates",
    "navy-corvettes"
]

df["total_assets"] = df[asset_cols].sum(axis=1)

df["assets_per_capita"] = np.where(
    df["total-population-by-country"] > 0,
    df["total_assets"] / df["total-population-by-country"],
    0
)

df["budget_to_gdp_ratio"] = np.where(
    df["purchasing-power-parity"] > 0,
    df["defense-spending-budget"] / df["purchasing-power-parity"],
    0
)

nato_members = {
    "United States", "United Kingdom", "France", "Germany", "Italy",
    "Canada", "Spain", "Poland", "Netherlands", "Belgium",
    "Norway", "Denmark", "Sweden", "Finland", "Turkey"
}

df["alliance"] = np.where(
    df["country_name"].isin(nato_members),
    "NATO",
    "None"
)

asia = {
    "India", "China", "Japan", "South Korea", "North Korea",
    "Pakistan", "Bangladesh", "Sri Lanka", "Nepal",
    "Indonesia", "Vietnam", "Thailand", "Philippines",
    "Iran", "Iraq", "Saudi Arabia", "Israel", "UAE", "Qatar"
}

europe = {
    "United Kingdom", "France", "Germany", "Italy", "Spain",
    "Poland", "Netherlands", "Belgium", "Norway", "Sweden",
    "Finland", "Russia", "Ukraine"
}

americas = {
    "United States", "Canada", "Mexico",
    "Brazil", "Argentina", "Chile", "Colombia"
}

africa = {
    "Egypt", "Algeria", "Morocco", "Nigeria",
    "South Africa", "Ethiopia", "Kenya"
}

oceania = {"Australia", "New Zealand"}

def continent_mapper(country):
    if country in asia:
        return "Asia"
    if country in europe:
        return "Europe"
    if country in americas:
        return "Americas"
    if country in africa:
        return "Africa"
    if country in oceania:
        return "Oceania"
    return "Unknown"

df["continent"] = df["country_name"].apply(continent_mapper)

with pd.ExcelWriter("kpi_building.xlsx") as writer:
    df.to_excel(writer, sheet_name="wide_format", index=False)
