The objective of this phase is to collect raw military strength data for 140+ countries from GlobalFirepower.com, clean and standardize the dataset, and prepare it for analytical processing in later milestones.
**Data Source**
GlobalFirepower.com
Country-specific military profile pages
Ranking and metric listing pages

URLs were collected using a predefined file:
links_for_military_data.txt

**Methodology**
Extract country level military data from structured web pages
**Tools Used**
-Python
-Requests
-BeautifulSoup
-Pandas
**Output File**
military_raw_data.csv
**Module 2: Data Cleaning and Structuring**
Transform raw scraped data into structured numerical format.
**Tools Used**
-Pandas
-NumPy
**Cleaning Steps**
-Removed commas, dollar signs,%, and special characters.
-Converted numerical columns to int64 or float64.
-Standardized column names.
-Handled missing or duplicate data.
-Ensured uniform formatting across all countries.
**Data Quality Checks**
-Verified numeric conversion of all quantitatives fields.
-Ensured no structural column mismatches.
-Checked for missing/null values
-validated row count for 140+ countries.
**Output files**
Cleaned_Military_Data2.csv
**Key Observation**
-Large disparity in defense budgets between top and lower ranked countries.
-Significant variation in manpower and asset distribution.
-Raw data required extensive cleaning due to inconsistent formatting.
-Some smaller countries had missing values in some specific metrics.
