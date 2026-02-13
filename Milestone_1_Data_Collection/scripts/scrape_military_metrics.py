import os
import time
import random
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

LINKS_FILE = "../links_for_military_data.txt"
RAW_DATA_CSV = "../data/raw/military_raw_data.csv"
HTML_SAVE_DIR = "../data/raw/html_pages"


def ensure_directories():
    """Create folders if they don't exist."""
    os.makedirs(os.path.dirname(RAW_DATA_CSV), exist_ok=True)
    os.makedirs(HTML_SAVE_DIR, exist_ok=True)


def load_urls(filepath):
    """
    Read URLs from links_for_military_data.txt.

    File format example:
        base_url:'https://www.globalfirepower.com/countries-listing.php'
        other_sources: {
            'https://www.globalfirepower.com/total-population-by-country.php': 'total_population',
            ...
        }

    We only want the URL between the first pair of single quotes on each line.
    """
    urls = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if "http" not in line:
                continue  
            parts = line.split("'")
           
            if len(parts) >= 2 and parts[1].startswith("http"):
                url = parts[1]
                urls.append(url)
    return urls


def slug_from_url(url):
    """
    Convert a URL into a Windows-safe filename.

    Example:
        https://www.globalfirepower.com/countries-listing.php
        -> www_globalfirepower_com_countries_listing_php
    """
    url = url.strip().lower()
    url = url.replace("https://", "").replace("http://", "")
    url = url.split("?")[0]  
    slug = re.sub(r"[^a-z0-9]+", "_", url).strip("_")
    return slug


def fetch_html(url, timeout=15):
    """Download HTML from a URL and return text (or None on failure)."""
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        )
    }
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch {url}: {e}")
        return None


def save_html(html_text, slug):
    """Save raw HTML to a file for debugging."""
    filepath = os.path.join(HTML_SAVE_DIR, f"{slug}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_text)
    return filepath


def parse_ranking_page(html_text, url):
    """
    Parse a ranking page (e.g., 'Active Military Manpower by Country (2025)')
    and extract ALL countries with their values.

    Returns: list of dicts, one per country:
        {
            "country": "India",
            "rank": "4",
            "<metric_name>": "1,455,550",
            "source_url": url
        }
    """
    soup = BeautifulSoup(html_text, "html.parser")

    metric_name = url.split("/")[-1].replace(".php", "").replace("-", "_")

    records = []
    containers = soup.find_all("div", class_="recordsetContainer")

    for container in containers:
        try:
            # Rank
            rank_elem = container.find("div", class_="rankNumContainer")
            rank = rank_elem.get_text(strip=True) if rank_elem else None

            # Country name
            name_elem = container.find("div", class_="longFormName")
            country_name = name_elem.get_text(strip=True) if name_elem else None

            # Value
            value_container = container.find("div", class_="valueContainer")
            value = None
            if value_container:
                inner_span = value_container.find("span")
                if inner_span:
                    value = inner_span.get_text(strip=True)

            if country_name and value:
                records.append(
                    {
                        "country": country_name,
                        "rank": rank,
                        metric_name: value,
                        "source_url": url,
                    }
                )
        except Exception as e:
            print(f"  [WARN] Failed to parse one record on {url}: {e}")
            continue

    return records


def main():
    ensure_directories()
    urls = load_urls(LINKS_FILE)
    print(f"Loaded {len(urls)} URLs")

   
    all_country_records = {} 

    for i, url in enumerate(urls, start=1):
        print(f"[{i}/{len(urls)}] Fetching: {url}")
        html_text = fetch_html(url)

        if html_text is None:
            print("  [SKIP] fetch failed")
            continue

        slug = slug_from_url(url)
        save_html(html_text, slug)

       
        page_records = parse_ranking_page(html_text, url)
        print(f"  [OK] Extracted {len(page_records)} country rows")

        
        for rec in page_records:
            country = rec["country"]
            if country not in all_country_records:
                all_country_records[country] = {"country": country}

            
            metric_cols = [
                k for k in rec.keys() if k not in ["country", "rank", "source_url"]
            ]
            if not metric_cols:
                continue
            metric_col = metric_cols[0]

            all_country_records[country][metric_col] = rec[metric_col]
            all_country_records[country][f"{metric_col}_rank"] = rec.get("rank")

       
        time.sleep(random.uniform(1.0, 3.0))

   
    df = pd.DataFrame(list(all_country_records.values()))

    df.to_csv(RAW_DATA_CSV, index=False, encoding="utf-8")
    print(
        f"\n[SUCCESS] Saved {len(df)} countries with {len(df.columns) - 1} metrics to {RAW_DATA_CSV}"
    )


if __name__ == "__main__":
    main()