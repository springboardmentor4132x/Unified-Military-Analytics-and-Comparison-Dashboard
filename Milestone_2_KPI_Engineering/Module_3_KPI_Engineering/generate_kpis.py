"""
Module 3: KPI Feature Engineering Script
=========================================
Generates derived KPIs and enriches data with metadata

Author: Project Team
Date: February 2026
Status: Template (Ready for implementation)

KPIs Generated:
1. Power Index Rank Gap - Ranking difference between consecutive countries
2. Assets per Capita - Military assets per person
3. Budget-to-GDP Ratio - Defense spending as % of GDP
4. Personnel Density - Active military per 1000 population
5. Equipment Density - Equipment count per 1000 km²
"""

import pandas as pd
import numpy as np
import json
import logging
from pathlib import Path
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('./logs/kpi_generation_log.txt'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class KPIGenerator:
    """Generate KPIs and enrich military metrics data"""
    
    def __init__(self, config_file='kpi_definitions.json'):
        """Initialize KPI generator"""
        self.config = self.load_config(config_file)
        self.df = None
        self.kpi_metrics = {}
        self.validation_report = {
            'total_kpis': 0,
            'kpis_calculated': 0,
            'kpis_valid': 0,
            'errors': []
        }
    
    def load_config(self, config_file):
        """Load KPI configuration"""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.warning(f"Config file not found: {config_file}. Using defaults.")
            return self.get_default_config()
    
    def get_default_config(self):
        """Return default KPI definitions"""
        return {
            'kpi_definitions': {
                'power_index_rank_gap': {
                    'description': 'Ranking difference between consecutive countries',
                    'formula': 'rank[i] - rank[i+1]',
                    'data_type': 'float'
                },
                'assets_per_capita': {
                    'description': 'Total military assets per person',
                    'formula': 'total_assets / population',
                    'data_type': 'float'
                },
                'budget_to_gdp_ratio': {
                    'description': 'Defense spending as % of GDP',
                    'formula': '(defense_budget / gdp) * 100',
                    'data_type': 'float'
                },
                'personnel_density': {
                    'description': 'Active military per 1000 population',
                    'formula': '(active_personnel / population) * 1000',
                    'data_type': 'float'
                },
                'equipment_density': {
                    'description': 'Total equipment per 1000 km²',
                    'formula': 'total_equipment / (land_area_km2 / 1000)',
                    'data_type': 'float'
                }
            },
            'metadata': {
                'regions': {
                    'Asia': ['China', 'India', 'Russia', 'Japan', 'South Korea', 'Indonesia'],
                    'Europe': ['Germany', 'France', 'United Kingdom', 'Italy', 'Spain'],
                    'Americas': ['United States', 'Canada', 'Brazil', 'Mexico', 'Argentina'],
                    'Africa': ['Nigeria', 'Egypt', 'South Africa', 'Kenya', 'Ethiopia'],
                    'Oceania': ['Australia', 'New Zealand']
                },
                'alliances': {
                    'NATO': ['United States', 'Germany', 'France', 'United Kingdom', 'Italy', 'Canada'],
                    'BRICS': ['Brazil', 'Russia', 'India', 'China', 'South Africa'],
                    'ASEAN': ['Indonesia', 'Thailand', 'Vietnam', 'Philippines', 'Malaysia']
                }
            }
        }
    
    def load_data(self, filepath):
        """Load cleaned data CSV"""
        try:
            self.df = pd.read_csv(filepath)
            logger.info(f"✓ Loaded data: {len(self.df)} rows, {len(self.df.columns)} columns")
            return True
        except FileNotFoundError:
            logger.error(f"File not found: {filepath}")
            return False
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            return False
    
    def calculate_power_index_rank_gap(self):
        """Calculate Power Index Rank Gap KPI"""
        try:
            # Rank countries by composite military score
            # This is a simplified version - you may want to use GlobalFirepower's actual ranking
            self.df['power_index_rank'] = range(1, len(self.df) + 1)
            
            # Calculate rank gap (difference with next ranked country)
            self.df['power_index_rank_gap'] = self.df['power_index_rank'].diff().fillna(0)
            
            logger.info("✓ Calculated Power Index Rank Gap")
            self.validation_report['kpis_calculated'] += 1
            return True
        except Exception as e:
            logger.error(f"Error calculating Power Index Rank Gap: {str(e)}")
            self.validation_report['errors'].append(str(e))
            return False
    
    def calculate_assets_per_capita(self):
        """Calculate Assets Per Capita KPI"""
        try:
            # Sum total military assets
            asset_columns = [col for col in self.df.columns if col in [
                'total_aircraft', 'tanks', 'submarines', 'destroyers'
            ]]
            
            self.df['total_assets'] = self.df[asset_columns].sum(axis=1, numeric_only=True)
            
            # Calculate per capita (avoid division by zero)
            self.df['assets_per_capita'] = (self.df['total_assets'] / self.df['population']).replace([np.inf, -np.inf], 0)
            self.df['assets_per_capita'].fillna(0, inplace=True)
            
            logger.info("✓ Calculated Assets Per Capita")
            self.validation_report['kpis_calculated'] += 1
            return True
        except Exception as e:
            logger.error(f"Error calculating Assets Per Capita: {str(e)}")
            self.validation_report['errors'].append(str(e))
            return False
    
    def calculate_budget_to_gdp_ratio(self):
        """Calculate Budget-to-GDP Ratio KPI"""
        try:
            # Calculate ratio (avoid division by zero)
            if 'defense_budget' in self.df.columns and 'gdp' in self.df.columns:
                self.df['budget_to_gdp_ratio'] = (self.df['defense_budget'] / self.df['gdp'] * 100).replace([np.inf, -np.inf], 0)
                self.df['budget_to_gdp_ratio'].fillna(0, inplace=True)
                
                logger.info("✓ Calculated Budget-to-GDP Ratio")
                self.validation_report['kpis_calculated'] += 1
                return True
            else:
                logger.warning("Missing required columns for Budget-to-GDP Ratio")
                return False
        except Exception as e:
            logger.error(f"Error calculating Budget-to-GDP Ratio: {str(e)}")
            self.validation_report['errors'].append(str(e))
            return False
    
    def calculate_personnel_density(self):
        """Calculate Personnel Density KPI"""
        try:
            if 'active_personnel' in self.df.columns and 'population' in self.df.columns:
                self.df['personnel_density'] = (self.df['active_personnel'] / self.df['population'] * 1000).replace([np.inf, -np.inf], 0)
                self.df['personnel_density'].fillna(0, inplace=True)
                
                logger.info("✓ Calculated Personnel Density")
                self.validation_report['kpis_calculated'] += 1
                return True
            else:
                logger.warning("Missing required columns for Personnel Density")
                return False
        except Exception as e:
            logger.error(f"Error calculating Personnel Density: {str(e)}")
            self.validation_report['errors'].append(str(e))
            return False
    
    def calculate_equipment_density(self):
        """Calculate Equipment Density KPI"""
        try:
            # Note: Requires land_area_km2 data - may need to be added separately
            if 'total_assets' in self.df.columns and 'land_area_km2' in self.df.columns:
                self.df['equipment_density'] = (self.df['total_assets'] / (self.df['land_area_km2'] / 1000)).replace([np.inf, -np.inf], 0)
                self.df['equipment_density'].fillna(0, inplace=True)
                
                logger.info("✓ Calculated Equipment Density")
                self.validation_report['kpis_calculated'] += 1
                return True
            else:
                logger.warning("Missing land_area_km2 column for Equipment Density")
                return False
        except Exception as e:
            logger.error(f"Error calculating Equipment Density: {str(e)}")
            self.validation_report['errors'].append(str(e))
            return False
    
    def add_region_metadata(self):
        """Add region classification to each country"""
        try:
            regions = self.config['metadata']['regions']
            
            # Create region mapping
            region_map = {}
            for region, countries in regions.items():
                for country in countries:
                    region_map[country.lower()] = region
            
            # Map regions to dataframe
            self.df['region'] = self.df['country'].str.lower().map(region_map)
            self.df['region'].fillna('Other', inplace=True)
            
            logger.info(f"✓ Added region metadata")
            return True
        except Exception as e:
            logger.error(f"Error adding region metadata: {str(e)}")
            return False
    
    def add_alliance_metadata(self):
        """Add alliance classification to each country"""
        try:
            alliances = self.config['metadata']['alliances']
            
            # Create alliance flags
            for alliance, members in alliances.items():
                column_name = f'is_{alliance.lower()}'
                self.df[column_name] = self.df['country'].isin(members).astype(int)
            
            logger.info(f"✓ Added alliance metadata")
            return True
        except Exception as e:
            logger.error(f"Error adding alliance metadata: {str(e)}")
            return False
    
    def create_wide_format(self, output_file):
        """Save data in wide format (each KPI as column)"""
        try:
            Path(output_file).parent.mkdir(parents=True, exist_ok=True)
            
            # Save to Excel for better compatibility with Tableau
            self.df.to_excel(output_file, index=False, engine='openpyxl')
            
            logger.info(f"✓ Saved wide format: {output_file}")
            return True
        except Exception as e:
            logger.error(f"Error saving wide format: {str(e)}")
            return False
    
    def create_long_format(self, output_file):
        """Save data in long format for Tableau/Power BI"""
        try:
            # Melt DataFrame for long format
            id_vars = [col for col in self.df.columns if col not in [
                'power_index_rank_gap', 'assets_per_capita', 'budget_to_gdp_ratio',
                'personnel_density', 'equipment_density'
            ]]
            
            kpi_columns = [
                'power_index_rank_gap', 'assets_per_capita', 'budget_to_gdp_ratio',
                'personnel_density', 'equipment_density'
            ]
            
            df_long = pd.melt(
                self.df,
                id_vars=id_vars,
                value_vars=kpi_columns,
                var_name='KPI',
                value_name='Value'
            )
            
            Path(output_file).parent.mkdir(parents=True, exist_ok=True)
            df_long.to_csv(output_file, index=False)
            
            logger.info(f"✓ Saved long format: {output_file}")
            return True
        except Exception as e:
            logger.error(f"Error saving long format: {str(e)}")
            return False
    
    def validate_kpis(self):
        """Validate KPI calculations"""
        try:
            logger.info("\n" + "=" * 60)
            logger.info("KPI VALIDATION REPORT")
            logger.info("=" * 60)
            
            kpi_columns = [
                'power_index_rank_gap', 'assets_per_capita', 'budget_to_gdp_ratio',
                'personnel_density', 'equipment_density'
            ]
            
            for col in kpi_columns:
                if col in self.df.columns:
                    non_null = self.df[col].notna().sum()
                    non_zero = (self.df[col] != 0).sum()
                    min_val = self.df[col].min()
                    max_val = self.df[col].max()
                    mean_val = self.df[col].mean()
                    
                    logger.info(f"\n{col}:")
                    logger.info(f"  Non-null: {non_null}")
                    logger.info(f"  Non-zero: {non_zero}")
                    logger.info(f"  Min: {min_val:.2f}")
                    logger.info(f"  Max: {max_val:.2f}")
                    logger.info(f"  Mean: {mean_val:.2f}")
                    
                    self.validation_report['kpis_valid'] += 1
            
            logger.info("\n" + "=" * 60)
            logger.info("✓ KPI Validation Complete")
            logger.info("=" * 60)
            return True
        except Exception as e:
            logger.error(f"Error validating KPIs: {str(e)}")
            return False
    
    def save_validation_report(self, report_path):
        """Save KPI validation report"""
        try:
            Path(report_path).parent.mkdir(parents=True, exist_ok=True)
            
            with open(report_path, 'w') as f:
                f.write("# KPI Generation and Validation Report\n\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write("## Summary\n")
                f.write(f"- KPIs Defined: {len(self.config['kpi_definitions'])}\n")
                f.write(f"- KPIs Calculated: {self.validation_report['kpis_calculated']}\n")
                f.write(f"- KPIs Valid: {self.validation_report['kpis_valid']}\n\n")
                
                if self.validation_report['errors']:
                    f.write("## Errors\n")
                    for error in self.validation_report['errors']:
                        f.write(f"- {error}\n")
                else:
                    f.write("## Status\n✓ No errors encountered\n")
            
            logger.info(f"✓ Report saved: {report_path}")
            return True
        except Exception as e:
            logger.error(f"Error saving report: {str(e)}")
            return False
    
    def run_kpi_generation(self, input_file, output_wide, output_long):
        """Execute full KPI generation pipeline"""
        logger.info("=" * 60)
        logger.info("Starting KPI Generation Pipeline")
        logger.info("=" * 60)
        
        # Load data
        if not self.load_data(input_file):
            return False
        
        # Calculate KPIs
        kpi_steps = [
            ("Power Index Rank Gap", self.calculate_power_index_rank_gap),
            ("Assets Per Capita", self.calculate_assets_per_capita),
            ("Budget-to-GDP Ratio", self.calculate_budget_to_gdp_ratio),
            ("Personnel Density", self.calculate_personnel_density),
            ("Equipment Density", self.calculate_equipment_density),
        ]
        
        for step_name, step_func in kpi_steps:
            try:
                step_func()
            except Exception as e:
                logger.error(f"✗ {step_name} error: {str(e)}")
        
        # Add metadata
        self.add_region_metadata()
        self.add_alliance_metadata()
        
        # Validate KPIs
        self.validate_kpis()
        
        # Save results
        self.create_wide_format(output_wide)
        self.create_long_format(output_long)
        
        # Save validation report
        report_file = output_wide.replace('.xlsx', '_kpi_validation_report.md')
        self.save_validation_report(report_file)
        
        logger.info("\n✓ KPI generation completed")
        return True


def main():
    """Main execution"""
    try:
        input_file = '../../../data/processed/military_cleaned.csv'
        output_wide = '../../../data/kpi/military_final.xlsx'
        output_long = '../../../data/kpi/military_final_long.csv'
        
        generator = KPIGenerator('kpi_definitions.json')
        success = generator.run_kpi_generation(input_file, output_wide, output_long)
        
        if success:
            logger.info("✓ KPI generation completed successfully")
        else:
            logger.warning("⚠ KPI generation completed with warnings")
            
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        raise


if __name__ == '__main__':
    main()
