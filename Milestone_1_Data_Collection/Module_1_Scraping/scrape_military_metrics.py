"""
Module 1: Web Scraping Script for Military Metrics
====================================================
Scrapes military data from GlobalFirepower.com for 140+ countries

Author: Project Team
Date: February 2026
Status: Template (Ready for implementation)
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time
import logging
from pathlib import Path
from datetime import datetime
import csv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('./logs/scraping_log.txt'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class MilitaryMetricsScraper:
    """Scrape military metrics from GlobalFirepower.com"""
    
    def __init__(self, config_file='scraper_config.json'):
        """Initialize scraper with configuration"""
        self.config = self.load_config(config_file)
        self.session = requests.Session()
        self.session.headers.update(self.config['scraping_config']['headers'])
        self.metrics = []
        self.failed_urls = []
        
    def load_config(self, config_file):
        """Load configuration from JSON file"""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Config file not found: {config_file}")
            raise
    
    def load_urls_from_file(self, filepath):
        """Load country URLs from links_for_military_data.txt"""
        try:
            with open(filepath, 'r') as f:
                urls = [line.strip() for line in f if line.strip()]
            logger.info(f"Loaded {len(urls)} URLs from {filepath}")
            return urls
        except FileNotFoundError:
            logger.error(f"URL file not found: {filepath}")
            raise
    
    def scrape_country(self, url):
        """Scrape data from a single country page"""
        retry_count = 0
        max_retries = self.config['scraping_config']['retry_attempts']
        
        while retry_count < max_retries:
            try:
                response = self.session.get(
                    url,
                    timeout=self.config['scraping_config']['timeout']
                )
                response.raise_for_status()
                
                soup = BeautifulSoup(response.content, 'html.parser')
                metrics = self.extract_metrics(soup, url)
                
                logger.info(f"✓ Successfully scraped: {url}")
                return metrics, response.content
                
            except requests.RequestException as e:
                retry_count += 1
                logger.warning(f"Attempt {retry_count} failed for {url}: {str(e)}")
                if retry_count < max_retries:
                    time.sleep(self.config['scraping_config']['retry_delay'])
        
        self.failed_urls.append(url)
        logger.error(f"✗ Failed to scrape after {max_retries} attempts: {url}")
        return None, None
    
    def extract_metrics(self, soup, url):
        """Extract military metrics from parsed HTML"""
        metrics = {}
        
        # Extract country name from URL or page
        metrics['country'] = self.extract_country_name(soup, url)
        
        # Extract each metric using configured selectors
        metric_selectors = self.config['parsing_config']['metric_selectors']
        
        for metric_name, selector in metric_selectors.items():
            try:
                element = soup.select_one(selector)
                if element:
                    metrics[metric_name] = element.get_text(strip=True)
                else:
                    metrics[metric_name] = None
            except Exception as e:
                logger.warning(f"Error extracting {metric_name}: {str(e)}")
                metrics[metric_name] = None
        
        return metrics
    
    def extract_country_name(self, soup, url):
        """Extract country name from page or URL"""
        # Implement country name extraction logic
        # This is a placeholder
        return url.split('/')[-1].replace('-', ' ').title()
    
    def run_scraping(self, url_file='../../../data/raw/links_for_military_data.txt'):
        """Execute full scraping pipeline"""
        logger.info("=" * 60)
        logger.info("Starting Military Metrics Scraping")
        logger.info("=" * 60)
        
        try:
            urls = self.load_urls_from_file(url_file)
        except FileNotFoundError:
            logger.error(f"URL file not found at {url_file}")
            logger.info("Please ensure 'links_for_military_data.txt' exists in data/raw/")
            return False
        
        total_urls = len(urls)
        successful = 0
        
        for idx, url in enumerate(urls, 1):
            logger.info(f"[{idx}/{total_urls}] Processing: {url}")
            metrics, html_content = self.scrape_country(url)
            
            if metrics:
                self.metrics.append(metrics)
                successful += 1
                
                # Save HTML for debugging (optional)
                if self.config['output_config']['save_html'] and html_content:
                    self.save_html(html_content, metrics.get('country', f'country_{idx}'))
            
            # Polite delay between requests
            time.sleep(2)
        
        # Calculate success rate
        success_rate = successful / total_urls if total_urls > 0 else 0
        logger.info(f"\n{'=' * 60}")
        logger.info(f"Scraping Complete: {successful}/{total_urls} successful ({success_rate*100:.1f}%)")
        logger.info(f"Failed URLs: {len(self.failed_urls)}")
        logger.info(f"{'=' * 60}\n")
        
        # Save results
        self.save_results()
        
        # Validate against config requirements
        return self.validate_results(success_rate)
    
    def save_results(self):
        """Save scraped data to CSV"""
        try:
            output_path = self.config['output_config']['output_directory']
            output_file = self.config['output_config']['output_filename']
            
            Path(output_path).mkdir(parents=True, exist_ok=True)
            
            df = pd.DataFrame(self.metrics)
            filepath = Path(output_path) / output_file
            
            df.to_csv(filepath, index=False)
            logger.info(f"✓ Data saved to: {filepath}")
            logger.info(f"  Records: {len(df)}")
            logger.info(f"  Columns: {len(df.columns)}")
            
            return True
        except Exception as e:
            logger.error(f"Error saving results: {str(e)}")
            return False
    
    def save_html(self, content, country_name):
        """Save HTML for debugging purposes"""
        try:
            html_dir = Path(self.config['output_config']['html_directory'])
            html_dir.mkdir(parents=True, exist_ok=True)
            
            filepath = html_dir / f"{country_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
            with open(filepath, 'wb') as f:
                f.write(content)
        except Exception as e:
            logger.warning(f"Could not save HTML: {str(e)}")
    
    def validate_results(self, success_rate):
        """Validate scraping results against config requirements"""
        min_countries = self.config['validation_config']['min_countries']
        min_success_rate = self.config['validation_config']['min_success_rate']
        
        validation_passed = True
        
        if len(self.metrics) < min_countries:
            logger.warning(f"⚠ Less than {min_countries} countries scraped: {len(self.metrics)}")
            validation_passed = False
        
        if success_rate < min_success_rate:
            logger.warning(f"⚠ Success rate {success_rate*100:.1f}% below minimum {min_success_rate*100:.1f}%")
            validation_passed = False
        
        if validation_passed:
            logger.info("✓ Validation PASSED")
        else:
            logger.warning("✗ Validation FAILED - Review results")
        
        return validation_passed


def main():
    """Main execution"""
    try:
        scraper = MilitaryMetricsScraper('scraper_config.json')
        success = scraper.run_scraping()
        
        if success:
            logger.info("✓ Scraping completed successfully")
        else:
            logger.warning("⚠ Scraping completed with warnings")
            
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        raise


if __name__ == '__main__':
    main()
