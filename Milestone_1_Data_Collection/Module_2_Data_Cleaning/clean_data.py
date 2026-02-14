"""
Module 2: Data Cleaning & Standardization Script
=================================================
Cleans and standardizes raw military metrics data

Author: Project Team
Date: February 2026
Status: Template (Ready for implementation)
"""

import pandas as pd
import numpy as np
import json
import logging
from pathlib import Path
from datetime import datetime
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('./logs/cleaning_log.txt'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class MilitaryDataCleaner:
    """Clean and standardize raw military metrics data"""
    
    def __init__(self, config_file='data_mapping.json'):
        """Initialize cleaner with configuration"""
        self.config = self.load_config(config_file)
        self.df = None
        self.cleaning_report = {
            'rows_initial': 0,
            'rows_final': 0,
            'columns_initial': 0,
            'columns_final': 0,
            'missing_before': {},
            'missing_after': {},
            'cleaning_steps': []
        }
    
    def load_config(self, config_file):
        """Load column mapping configuration"""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning(f"Config file not found: {config_file}. Using defaults.")
            return self.get_default_config()
    
    def get_default_config(self):
        """Return default column mapping"""
        return {
            'column_mapping': {
                'country': 'country',
                'total_aircraft': 'total_aircraft',
                'active_personnel': 'active_personnel',
                'reserve_personnel': 'reserve_personnel',
                'defense_budget': 'defense_budget',
                'tanks': 'tanks',
                'submarines': 'submarines',
                'destroyers': 'destroyers',
                'population': 'population',
                'gdp': 'gdp'
            },
            'numeric_columns': [
                'total_aircraft',
                'active_personnel',
                'reserve_personnel',
                'defense_budget',
                'tanks',
                'submarines',
                'destroyers',
                'population',
                'gdp'
            ],
            'required_columns': ['country']
        }
    
    def load_data(self, filepath):
        """Load raw data CSV"""
        try:
            self.df = pd.read_csv(filepath)
            self.cleaning_report['rows_initial'] = len(self.df)
            self.cleaning_report['columns_initial'] = len(self.df.columns)
            logger.info(f"✓ Loaded data: {len(self.df)} rows, {len(self.df.columns)} columns")
            return True
        except FileNotFoundError:
            logger.error(f"File not found: {filepath}")
            return False
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            return False
    
    def standardize_column_names(self):
        """Rename columns to standard format (snake_case)"""
        try:
            # Convert to lowercase and replace spaces with underscores
            self.df.columns = [col.lower().replace(' ', '_').replace('-', '_') 
                               for col in self.df.columns]
            logger.info("✓ Standardized column names")
            self.cleaning_report['cleaning_steps'].append("Standardized column names")
            return True
        except Exception as e:
            logger.error(f"Error standardizing column names: {str(e)}")
            return False
    
    def remove_special_characters(self):
        """Remove special characters from numeric columns"""
        try:
            numeric_cols = self.config['numeric_columns']
            
            for col in numeric_cols:
                if col in self.df.columns:
                    # Remove commas, %, +, and other special characters
                    self.df[col] = self.df[col].astype(str).str.replace(r'[,\%\+\$]', '', regex=True)
                    self.df[col] = self.df[col].str.strip()
            
            logger.info("✓ Removed special characters from numeric columns")
            self.cleaning_report['cleaning_steps'].append("Removed special characters")
            return True
        except Exception as e:
            logger.error(f"Error removing special characters: {str(e)}")
            return False
    
    def convert_to_numeric(self):
        """Convert text columns to numeric formats"""
        try:
            numeric_cols = self.config['numeric_columns']
            
            for col in numeric_cols:
                if col in self.df.columns:
                    # Try to convert to numeric, coercing errors to NaN
                    self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
            
            logger.info("✓ Converted columns to numeric format")
            self.cleaning_report['cleaning_steps'].append("Converted to numeric format")
            return True
        except Exception as e:
            logger.error(f"Error converting to numeric: {str(e)}")
            return False
    
    def handle_missing_values(self, strategy='mean'):
        """Handle missing/null values"""
        try:
            # Record missing values before
            self.cleaning_report['missing_before'] = self.df.isnull().sum().to_dict()
            
            numeric_cols = self.config['numeric_columns']
            
            # Fill numeric columns based on strategy
            if strategy == 'mean':
                for col in numeric_cols:
                    if col in self.df.columns:
                        self.df[col].fillna(self.df[col].mean(), inplace=True)
            elif strategy == 'median':
                for col in numeric_cols:
                    if col in self.df.columns:
                        self.df[col].fillna(self.df[col].median(), inplace=True)
            elif strategy == 'zero':
                for col in numeric_cols:
                    if col in self.df.columns:
                        self.df[col].fillna(0, inplace=True)
            
            # Forward fill country names if any missing
            if 'country' in self.df.columns:
                self.df['country'].fillna(method='ffill', inplace=True)
            
            # Record missing values after
            self.cleaning_report['missing_after'] = self.df.isnull().sum().to_dict()
            
            logger.info(f"✓ Handled missing values using '{strategy}' strategy")
            self.cleaning_report['cleaning_steps'].append(f"Handled missing values ({strategy})")
            return True
        except Exception as e:
            logger.error(f"Error handling missing values: {str(e)}")
            return False
    
    def remove_duplicates(self):
        """Remove duplicate rows"""
        try:
            initial_rows = len(self.df)
            self.df.drop_duplicates(subset=['country'], keep='first', inplace=True)
            removed = initial_rows - len(self.df)
            
            if removed > 0:
                logger.info(f"✓ Removed {removed} duplicate rows")
                self.cleaning_report['cleaning_steps'].append(f"Removed {removed} duplicates")
            else:
                logger.info("✓ No duplicates found")
            
            return True
        except Exception as e:
            logger.error(f"Error removing duplicates: {str(e)}")
            return False
    
    def validate_data_quality(self):
        """Validate data quality"""
        try:
            total_cells = self.df.shape[0] * self.df.shape[1]
            missing_cells = self.df.isnull().sum().sum()
            missing_percent = (missing_cells / total_cells) * 100 if total_cells > 0 else 0
            
            logger.info(f"\n{'=' * 60}")
            logger.info("DATA QUALITY REPORT")
            logger.info(f"{'=' * 60}")
            logger.info(f"Total cells: {total_cells}")
            logger.info(f"Missing cells: {missing_cells}")
            logger.info(f"Missing percentage: {missing_percent:.2f}%")
            logger.info(f"Rows: {len(self.df)}")
            logger.info(f"Columns: {len(self.df.columns)}")
            
            if missing_percent < 2:
                logger.info("✓ Quality Check PASSED (<2% missing data)")
                return True
            else:
                logger.warning(f"⚠ Quality Check WARNING ({missing_percent:.2f}% missing)")
                return False
        except Exception as e:
            logger.error(f"Error validating data: {str(e)}")
            return False
    
    def save_cleaned_data(self, output_path):
        """Save cleaned data to CSV"""
        try:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            self.df.to_csv(output_path, index=False)
            self.cleaning_report['rows_final'] = len(self.df)
            self.cleaning_report['columns_final'] = len(self.df.columns)
            
            logger.info(f"✓ Cleaned data saved to: {output_path}")
            logger.info(f"  Final rows: {self.cleaning_report['rows_final']}")
            logger.info(f"  Final columns: {self.cleaning_report['columns_final']}")
            return True
        except Exception as e:
            logger.error(f"Error saving cleaned data: {str(e)}")
            return False
    
    def save_report(self, report_path):
        """Save cleaning report"""
        try:
            Path(report_path).parent.mkdir(parents=True, exist_ok=True)
            
            with open(report_path, 'w') as f:
                f.write("# Data Cleaning Report\n\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write("## Summary\n")
                f.write(f"- Initial rows: {self.cleaning_report['rows_initial']}\n")
                f.write(f"- Final rows: {self.cleaning_report['rows_final']}\n")
                f.write(f"- Initial columns: {self.cleaning_report['columns_initial']}\n")
                f.write(f"- Final columns: {self.cleaning_report['columns_final']}\n\n")
                
                f.write("## Cleaning Steps\n")
                for i, step in enumerate(self.cleaning_report['cleaning_steps'], 1):
                    f.write(f"{i}. {step}\n")
                
                f.write("\n## Missing Values\n")
                f.write("### Before Cleaning\n")
                for col, count in self.cleaning_report['missing_before'].items():
                    if count > 0:
                        f.write(f"- {col}: {count}\n")
                
                f.write("\n### After Cleaning\n")
                for col, count in self.cleaning_report['missing_after'].items():
                    if count > 0:
                        f.write(f"- {col}: {count}\n")
            
            logger.info(f"✓ Report saved to: {report_path}")
            return True
        except Exception as e:
            logger.error(f"Error saving report: {str(e)}")
            return False
    
    def run_cleaning_pipeline(self, input_file, output_file):
        """Execute full cleaning pipeline"""
        logger.info("=" * 60)
        logger.info("Starting Data Cleaning Pipeline")
        logger.info("=" * 60)
        
        # Load data
        if not self.load_data(input_file):
            return False
        
        # Execute cleaning steps
        steps = [
            ("Standardizing column names", self.standardize_column_names),
            ("Removing special characters", self.remove_special_characters),
            ("Converting to numeric", self.convert_to_numeric),
            ("Handling missing values", self.handle_missing_values),
            ("Removing duplicates", self.remove_duplicates),
            ("Validating data quality", self.validate_data_quality),
        ]
        
        for step_name, step_func in steps:
            try:
                if not step_func():
                    logger.error(f"✗ {step_name} failed")
                    return False
            except Exception as e:
                logger.error(f"✗ {step_name} error: {str(e)}")
                return False
        
        # Save results
        if not self.save_cleaned_data(output_file):
            return False
        
        # Save report
        report_file = output_file.replace('.csv', '_cleaning_report.md')
        if not self.save_report(report_file):
            logger.warning("Could not save cleaning report")
        
        logger.info("\n✓ Cleaning pipeline completed successfully")
        return True


def main():
    """Main execution"""
    try:
        # Define file paths
        input_file = '../../../data/raw/military_raw_data.csv'
        output_file = '../../../data/processed/military_cleaned.csv'
        
        cleaner = MilitaryDataCleaner('data_mapping.json')
        success = cleaner.run_cleaning_pipeline(input_file, output_file)
        
        if success:
            logger.info("✓ Cleaning completed successfully")
        else:
            logger.warning("⚠ Cleaning completed with errors")
            
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        raise


if __name__ == '__main__':
    main()
