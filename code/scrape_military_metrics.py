import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
all_data = []
with open("links_for_military_data.txt", "r") as f:
    raw_urls = [line.strip() for line in f if line.strip()]
cleaned_urls = []
for item in raw_urls:
    match = re.search(r"(https?://[^\s']+)", item)
    if match:
        cleaned_urls.append(match.group(1))
print("Total metric links:", len(cleaned_urls))
for url in cleaned_urls:
    if "countries-listing.php" in url:
        continue
    print("Scraping:", url)
    try:
        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=15
        )
        soup = BeautifulSoup(response.text, "html.parser")
        rows = soup.find_all("div", class_="topRow")
        if not rows:
            print("No rows found:", url)
            continue
        metric = url.split("/")[-1].replace(".php", "")
        for row in rows:
            spans = [s.get_text(strip=True) for s in row.find_all("span")]
            if len(spans) < 3:
                continue
            country_name = None
            value = None
            for text in spans:
                if country_name is None and any(c.isalpha() for c in text):
                    country_name = text
                elif country_name is not None and any(c.isdigit() for c in text):
                    value = text
                    break
            if not country_name or not value:
                continue
            all_data.append({
                "country_name": country_name,
                "metric": metric,
                "value": value
            })
        time.sleep(1)
    except Exception as e:
        print("Failed:", url, e)
print("Scraping completed")
print("Total rows scraped:", len(all_data))
raw_df = pd.DataFrame(all_data)
raw_df.to_csv("military_raw_data.csv", index=False)
print("Saved military_raw_data.csv")
pivot_df = raw_df.pivot_table(
    index="country_name",
    columns="metric",
    values="value",
    aggfunc="first"
).reset_index()
rank_calc = pivot_df.copy()
for col in rank_calc.columns:
    if col == "country_name":
        continue
    rank_calc[col] = (
        rank_calc[col]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.extract(r"([\d\.]+)")
        .astype(float)
        .fillna(0)
    )
metric_cols = [c for c in rank_calc.columns if c != "country_name"]
for col in metric_cols:
    max_val = rank_calc[col].max()
    rank_calc[col] = rank_calc[col] / max_val if max_val > 0 else 0
rank_calc["global_rank"] = (
    rank_calc[metric_cols]
    .sum(axis=1)
    .rank(ascending=False, method="dense")
    .astype(int)
)
pivot_df = pivot_df.merge(
    rank_calc[["country_name", "global_rank"]],
    on="country_name",
    how="left"
)
pivot_df = pivot_df[
    ["global_rank", "country_name"] +
    [c for c in pivot_df.columns if c not in ["global_rank", "country_name"]]
]
pivot_df = pivot_df.sort_values("global_rank")
pivot_df.to_csv("military_pivot_data.csv", index=False)
print("Saved military_pivot_data.csv (with rank)")
