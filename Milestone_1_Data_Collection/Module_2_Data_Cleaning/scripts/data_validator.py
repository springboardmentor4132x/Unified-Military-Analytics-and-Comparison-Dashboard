"""
Utility script for data validation and quality checks
Module 2: Data Cleaning
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple

class DataValidator:
    """Validates data quality and completeness"""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
    
    def validate_csv(self, filepath: str) -> Dict:
        """Validate CSV file structure and content"""
        results = {
            'file': filepath,
            'valid': True,
            'rows': 0,
            'columns': 0,
            'missing_rate': 0.0,
            'errors': [],
            'warnings': []
        }
        
        try:
            df = pd.read_csv(filepath)
            results['rows'] = len(df)
            results['columns'] = len(df.columns)
            
            # Calculate missing data rate
            total_cells = df.shape[0] * df.shape[1]
            missing_cells = df.isnull().sum().sum()
            results['missing_rate'] = (missing_cells / total_cells * 100) if total_cells > 0 else 0
            
            # Check for issues
            if results['missing_rate'] > 5:
                results['warnings'].append(f"High missing data rate: {results['missing_rate']:.2f}%")
            
            if len(df) < 100:
                results['warnings'].append(f"Low row count: {len(df)}")
            
            if len(df.columns) < 30:
                results['warnings'].append(f"Low column count: {len(df.columns)}")
            
        except Exception as e:
            results['valid'] = False
            results['errors'].append(str(e))
        
        return results
    
    def check_numeric_columns(self, df: pd.DataFrame) -> Dict:
        """Check numeric column integrity"""
        results = {'valid_numeric': 0, 'invalid_numeric': 0, 'mixed_type': []}
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        results['valid_numeric'] = len(numeric_cols)
        
        for col in numeric_cols:
            if df[col].dtype == 'object':
                results['mixed_type'].append(col)
        
        return results
    
    def print_summary(self, filepath: str):
        """Print validation summary"""
        validation = self.validate_csv(filepath)
        
        print(f"\n{'='*60}")
        print(f"DATA VALIDATION REPORT")
        print(f"{'='*60}")
        print(f"File: {validation['file']}")
        print(f"Status: {'✅ VALID' if validation['valid'] else '❌ INVALID'}")
        print(f"Rows: {validation['rows']}")
        print(f"Columns: {validation['columns']}")
        print(f"Missing Data: {validation['missing_rate']:.2f}%")
        
        if validation['warnings']:
            print(f"\n⚠️ Warnings:")
            for w in validation['warnings']:
                print(f"   • {w}")
        
        if validation['errors']:
            print(f"\n❌ Errors:")
            for e in validation['errors']:
                print(f"   • {e}")
        
        print(f"{'='*60}\n")


if __name__ == "__main__":
    # Example usage
    validator = DataValidator()
    validator.print_summary('data/processed/military_cleaned.csv')
