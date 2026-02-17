import time
import random
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup


# -------------------------
# CONFIG
# -------------------------

CONFIG_FILE = "scraper_config.json"
OUTPUT_FILE = "military_raw_data.csv"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}


# -------------------------
# STEP 1: LOAD CONFIG
# -------------------------

def load_links(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    return config["other_sources"]


# -------------------------
# STEP 2: SCRAPE ONE PAGE
# -------------------------

def scrape_metric(url, metric, data):
    print(f"Scraping {metric}")

    try:
        r = requests.get(url, headers=HEADERS, timeout=30)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return

    soup = BeautifulSoup(r.text, "html.parser")

    records = soup.select("div.recordsetContainer")
    print(f"Records found: {len(records)}")

    for rec in records:
        country_tag = rec.select_one(".longFormName span")
        value_tag = rec.select_one(".valueContainer span span")

        if not country_tag or not value_tag:
            continue

        country = country_tag.get_text(strip=True)
        value = value_tag.get_text(strip=True)

        if country not in data:
            data[country] = {}

        data[country][metric] = value

    # polite delay to avoid hammering server
    time.sleep(random.uniform(1.5, 3))


# -------------------------
# STEP 3: MAIN
# -------------------------

def main():
    links = load_links(CONFIG_FILE)
    data = {}

    for url, metric in links.items():
        scrape_metric(url, metric, data)

    df = pd.DataFrame.from_dict(data, orient="index")
    df.index.name = "country"
    df.reset_index(inplace=True)

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"\nSaved {OUTPUT_FILE}")
    print("Countries scraped:", len(df))


# -------------------------
# RUN
# -------------------------

if __name__ == "__main__":
    main()
