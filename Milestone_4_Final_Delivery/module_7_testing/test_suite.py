"""
Test Suite for Military Analytics Dashboard
Module 7: Testing & Quality Assurance
"""

import unittest
import pandas as pd
import numpy as np
from pathlib import Path

class TestDataValidation(unittest.TestCase):
    """Test data validation and quality checks"""
    
    def setUp(self):
        """Setup test fixtures"""
        self.sample_data = pd.DataFrame({
            'country': ['USA', 'China', 'Russia'],
            'rank': [1, 2, 3],
            'military_expenditure_usd': [820000, 292000, 72000],
            'active_military_personnel': [1300000, 2035000, 1010000],
            'total_military': [2160000, 2585000, 1260000]
        })
    
    def test_data_shape(self):
        """Test data shape"""
        self.assertEqual(self.sample_data.shape[0], 3)
        self.assertEqual(self.sample_data.shape[1], 5)
    
    def test_no_missing_values(self):
        """Test for missing values"""
        self.assertEqual(self.sample_data.isnull().sum().sum(), 0)
    
    def test_column_names(self):
        """Test column names are standardized"""
        expected_cols = ['country', 'rank', 'military_expenditure_usd', 
                        'active_military_personnel', 'total_military']
        self.assertEqual(list(self.sample_data.columns), expected_cols)
    
    def test_numeric_types(self):
        """Test numeric columns have correct types"""
        numeric_cols = ['rank', 'military_expenditure_usd', 'active_military_personnel', 'total_military']
        for col in numeric_cols:
            self.assertTrue(pd.api.types.is_numeric_dtype(self.sample_data[col]))
    
    def test_positive_values(self):
        """Test all numeric values are positive"""
        numeric_df = self.sample_data.select_dtypes(include=[np.number])
        self.assertTrue((numeric_df >= 0).all().all())
    
    def test_no_duplicates(self):
        """Test for duplicate countries"""
        self.assertEqual(self.sample_data.duplicated(subset=['country']).sum(), 0)

class TestKPICalculations(unittest.TestCase):
    """Test KPI calculations"""
    
    def setUp(self):
        """Setup test data"""
        self.kpi_data = pd.DataFrame({
            'country': ['USA', 'China'],
            'rank': [1, 2],
            'military_expenditure_usd': [820000, 292000],
            'population_millions': [338.3, 1425.9],
            'gdp_billions_usd': [27360, 17734],
            'total_military': [2160000, 2585000]
        })
    
    def test_budget_to_gdp_ratio(self):
        """Test budget-to-GDP ratio calculation"""
        self.kpi_data['budget_to_gdp'] = (
            self.kpi_data['military_expenditure_usd'] / 1000 / 
            self.kpi_data['gdp_billions_usd'] * 100
        )
        
        # USA: 820/27360 * 100 = 3%
        self.assertAlmostEqual(self.kpi_data.loc[0, 'budget_to_gdp'], 3.0, places=1)
    
    def test_personnel_per_capita(self):
        """Test personnel per capita calculation"""
        self.kpi_data['personnel_per_million'] = (
            self.kpi_data['total_military'] / 
            self.kpi_data['population_millions']
        )
        
        # All values should be positive
        self.assertTrue((self.kpi_data['personnel_per_million'] > 0).all())

class TestFileOperations(unittest.TestCase):
    """Test file I/O operations"""
    
    def setUp(self):
        """Setup test files"""
        self.test_dir = Path('data/test')
        self.test_dir.mkdir(exist_ok=True)
    
    def test_csv_write_read(self):
        """Test CSV file write/read"""
        test_file = self.test_dir / 'test_data.csv'
        
        # Write
        df_write = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        df_write.to_csv(test_file, index=False)
        
        # Read
        df_read = pd.read_csv(test_file)
        
        # Assert
        pd.testing.assert_frame_equal(df_write, df_read)
        
        # Cleanup
        test_file.unlink()

class TestDashboardMetrics(unittest.TestCase):
    """Test dashboard metric calculations"""
    
    def test_top_countries_ranking(self):
        """Test ranking of countries by budget"""
        df = pd.DataFrame({
            'country': ['USA', 'China', 'Russia'],
            'budget': [820, 292, 72]
        })
        
        top_3 = df.nlargest(3, 'budget')
        self.assertEqual(list(top_3['country']), ['USA', 'China', 'Russia'])
    
    def test_regional_aggregation(self):
        """Test regional data aggregation"""
        df = pd.DataFrame({
            'country': ['USA', 'Canada', 'China', 'Japan'],
            'region': ['Americas', 'Americas', 'Asia', 'Asia'],
            'military': [2160, 100, 2585, 201]
        })
        
        regional = df.groupby('region')['military'].sum()
        self.assertEqual(regional['Americas'], 2260)
        self.assertEqual(regional['Asia'], 2786)

class TestDataIntegrity(unittest.TestCase):
    """Test overall data integrity"""
    
    def test_minimum_requirements(self):
        """Test minimum data requirements met"""
        # Create sample dataset
        df = pd.DataFrame({
            'country': [f'Country{i}' for i in range(140)],
            'rank': range(1, 141),
            'budget': np.random.randint(1000, 1000000, 140)
        })
        
        # Minimum 140 countries
        self.assertGreaterEqual(len(df), 140)
        
        # No missing countries
        self.assertEqual(df['country'].nunique(), 140)

def run_tests():
    """Run all tests"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    suite.addTests(loader.loadTestsFromTestCase(TestDataValidation))
    suite.addTests(loader.loadTestsFromTestCase(TestKPICalculations))
    suite.addTests(loader.loadTestsFromTestCase(TestFileOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestDashboardMetrics))
    suite.addTests(loader.loadTestsFromTestCase(TestDataIntegrity))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result

if __name__ == '__main__':
    result = run_tests()
    
    # Print summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    print(f"Tests Run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped)}")
    print(f"Success Rate: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.1f}%")
    print("="*60)
