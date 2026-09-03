# Changelog
## Day 1 - Project initialization, Setup and planning
- Created a new Github repository
- Cloned the repository and connected it to vs code
- Created a initial project structure
- Downloaded and added the raw dataset to the data folder 
- Created and completed the Project Plan 
- Committed and pushed the initial project setup and plan to github

## Day 2 - Data Ingestion and Quality Analysis
- Created ingest.py file under src folder
- Loaded the raw restaurant sales dataset and created a dataframe
- Implemented basic dataset profiling
- Created and completed the Data-quality analysis and documented the identified findings in reports\Data_Quality_Analysis.md file
- committed and pushed the src\ingest.py and report\Data_Quality_Analysis file to github

## Day 3 - Cleaning analysis and Plan
- Created cleaning_analysis.py for cleaning stage investigations.
- Created Cleaning_analysis_and_plan.md file to write the investigations.
- Investigated missing feild patterns.
- Documented the missing value findings for future cleaning decisions.
- Committed and pushed today's work to github.

## Day 4 - Cleaning Analysis and Plan 
- Continued and completed the cleaning analysis
- performed outliers analysis
- Checked categorical Inconsistencies across Item,Category and payment method columns.
- Documented the initial cleaning plan based on the extended analysis.
- Created file **clean.py** and initiated cleaning process.
- Committed and pushed the completed files cleaning_analysis_and_plan.md and cleaning_analysis.py, clean.py to github

## Day 5 - Cleaning 
- Started the cleaning process
- Created a copy of the original dataframe to work without making changes in the main data frame.
- completed 446 missing **Price** values using order total and quantity.
- committed and pushed the work to github.

## Day 6 - Cleaning
- Removed 430 records with majority of fields missing
- Identified and filled 14 unique category + Price-> Item mappings
- Reconstructed 771 records using unique mapping
- Replaced the rest 557 Item records as unknown
- Investigated the payment method with customer Id 
- Confirmed customer Id couldn't help
- Filled the missing payment methods with the most frequent payment method (cash)
- Converted the Orderdate to datetime datatype in dd-mm-yyyy format
- Completed the cleaning process
- Exported an interim file Cleaned.csv
- Commited and pushed to github

## Day 7 - Transformation started
- Checked the data quality of the created csv file cleaned.csv
- Analysed the dataset and figured out possible transformation ideas in the cleaned dataset
- Created a python file transform.py for doing transformation tasks
- Initialized work in transform.py by adding the cleaned.py and created a dataframe
- Converted the date to datetime datatype which is present as string datatype.
- Committed and pushed the work to github.