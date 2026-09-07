# Restaurant Sales ETL Pipeline
This is a modular python and pandas ETL pipeline that processes a raw restaurant sales dataset into a cleaned, transformed, validated and analytics ready dataset.

## Project Overview
The project is an end-to-end ETL workflow for restaurant sales transaction data.
The pipeline processes the raw dataset through data quality analysis, cleaning, transformation, feature engineering and final validation and finally an analytics ready dataset.
This project was built with a focus on data engineering using python and pandas.

## ETL Workflow
Raw Dataset -> Data Quality Analysis -> Data Cleaning -> Data Transformation -> Feature engineering -> Final Validation -> Analytics Ready Dataset

Intermediate datasets are maintained through the workflow.

## Dataset and Attribution
This project uses the **Restaurant Sales - Dirty Data for Cleaning Training** dataset.
The dataset contains **17,534 restaurant sales transactions** and was designed to introduce realistic data inconsistencies for practicing data cleaning.
The dataset contains following 9 columns, `OrderID`, `CustomerID`,`Category`,`Item`,`Price`,`Quantity`,`Order Total`,`Order date`,`Payment Method`.
The dataset was obtained from Kaggle:
- **Author:** Ahmed Mohamed
- **Source:** Kaggle (https://www.kaggle.com/datasets/ahmedmohamed2003/restaurant-sales-dirty-data-for-cleaning-training)
-  **License:** This dataset is released under the CC BY-SA 4.0 License. (https://creativecommons.org/licenses/by-sa/4.0/)

The original dataset was cleaned, transformed and modified as part of the project. The original dataset creator is credited above, and the dataset is used in accordance with the CC BY-SA 4.0 license.

## Key Results
- Processed 17,534 raw restaurant sales transactions.
- Identified and handled significant missing value patterns and inconsistencies.
- Removed 430 highly incomplete transactions
- Reconstructed missing values where reliable relationships existed.
- Filled the records with frequent or related values.
- Created 4 attributes from Order Date during transformation.
- Created 3 row level analytics features during feature engineering phase.
- Performed a final validation on final dataframe created after feature engineering which covered consistency validation and features validation.
- Produced a final analytics ready dataset with 17,104 records.

## Project Structure
restaurant-sales-data-pipeline/
    - Data/
        - Raw/
            - restaurant_sales_data.csv
        - Interim/
            - cleaned.csv
            - transformed.csv
            - feature_engineered.csv
        - Processed/
            - Final_restaurant_sales.csv
    - src/
        - ingest.py
        - cleaning_analysis.py
        - clean.py
        - transform.py
        - feature_engineering.py
        - validate.py
        - pipeline.py
    - docs/
        - Data_Quality_Analysis.md
        - Cleaning_analysis_and_plan.md
        - Transformation.md
        - Feature_engineering.md
    - reports/
        - Project_report.md
    - Changelog.md
    - .gitignore
    - requirements.txt
    - README.md

## How To Run
1. Clone the repository
    git clone <repository-url>
    cd restaurant-sales-data-pipeline
2. Install dependencies
    pip install -r requirements.txt
3. Run the pipeline
    python src/pipeline.py

The processed datasets are produced in each stages and final dataset is exported to **Data/Processed/Final_restaurant_sales.csv**.

## Technologies Used 
- Python - programming language 
- Pandas - Data Processing and transformation
- Git - Version Control
- Github - Repository and Project management

## Documentation
The detailed project documentation is available in Docs/ and reports/ directories.
- [Data Quality Analysis](docs/Data_Quality_Analysis.md)
- [Cleaning Analysis](docs/Cleaning_analysis_and_plan.md)
- [Transformation](docs/Transformation.md)
- [Feature Engineering](docs/Feature_engineering.md)
- [Project Report](reports/Project_report.md)

## Future Scope 
The final dataset can be used as a foundation for future work including:
- Exploratory Data Analysis
- Restaurant sales analysis
- Machine learning
Machine learning specific preprocessing such as encoding, scaling and train test split can performed seperately when developing a future ml pipeline.
