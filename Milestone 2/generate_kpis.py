import pandas as pd
import numpy as np

df = pd.read_csv("military_cleaned.csv")

df["total_assets"] = (
    df["total_military_aircraft"] +
    df["tanks"] +
    df["total_naval_fleet"]
)

df["assets_per_capita"] = df["total_assets"] / df["total_population"]

df["budget_per_active_personnel"] = (
    df["defense_budget_usd"] / df["active_personnel"]
)

df["budget_to_gdp_ratio"] = (
    df["defense_budget_usd"] / df["purchasing_power_parity_usd"]
)

df["air_share"] = df["total_military_aircraft"] / df["total_assets"]
df["land_share"] = df["tanks"] / df["total_assets"]
df["naval_share"] = df["total_naval_fleet"] / df["total_assets"]

score_columns = [
    "active_personnel",
    "total_military_aircraft",
    "tanks",
    "total_naval_fleet",
    "defense_budget_usd"
]

for col in score_columns:
    df[col + "_norm"] = (
        (df[col] - df[col].min()) /
        (df[col].max() - df[col].min())
    )

df["composite_power_score"] = df[
    [c + "_norm" for c in score_columns]
].mean(axis=1)

df["power_rank"] = df["composite_power_score"].rank(
    ascending=False, method="dense"
)

df["power_rank_gap"] = df["power_rank"] - 1

global_assets = df["total_assets"].sum()

df["coalition_asset_share"] = df["total_assets"] / global_assets

kpi_columns = [
    "assets_per_capita",
    "budget_per_active_personnel",
    "budget_to_gdp_ratio",
    "air_share",
    "land_share",
    "naval_share",
    "composite_power_score"
]

df_long = df.melt(
    id_vars=["Country"],
    value_vars=kpi_columns,
    var_name="kpi_name",
    value_name="kpi_value"
)

nato_countries = [
    "United States","Canada","United Kingdom","France","Germany","Italy",
    "Spain","Portugal","Netherlands","Belgium","Luxembourg","Denmark",
    "Norway","Poland","Czech Republic","Slovakia","Hungary","Romania",
    "Bulgaria","Greece","Turkey","Estonia","Latvia","Lithuania",
    "Croatia","Slovenia","Albania","Montenegro","North Macedonia",
    "Finland","Sweden"
]

region_map = {
    "United States":"North America",
    "Canada":"North America",

    "Germany":"Europe","France":"Europe","United Kingdom":"Europe",
    "Italy":"Europe","Spain":"Europe","Poland":"Europe",

    "Russia":"Europe",

    "China":"Asia","India":"Asia","Japan":"Asia","South Korea":"Asia",
    "North Korea":"Asia","Pakistan":"Asia",

    "Saudi Arabia":"Middle East","Iran":"Middle East","Israel":"Middle East",
    "Turkey":"Middle East",

    "Brazil":"South America","Argentina":"South America","Chile":"South America",

    "South Africa":"Africa","Egypt":"Africa","Nigeria":"Africa",

    "Australia":"Oceania","New Zealand":"Oceania"
}

df["is_nato"] = df["Country"].apply(lambda x: 1 if x in nato_countries else 0)

df["region"] = df["Country"].map(region_map)

df["region"] = df["region"].fillna("Other")

df_wide = df.copy()

with pd.ExcelWriter("military_final.xlsx", engine="openpyxl") as writer:
    df_wide.to_excel(writer, sheet_name="Wide_Data", index=False)
    df_long.to_excel(writer, sheet_name="KPI_Long_Format", index=False)

