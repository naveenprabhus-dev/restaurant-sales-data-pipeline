# Retail Sales Data Pipeline - Project Report
#
## Dataset 
The project used a sales transaction dataset containing 17,534 transaction records and 9 columns.Namely, `Order ID`, `Customer ID`, `Category`, `Item`, `Price`,`Quantity`,`Order Total`,`Order Date`,`Payment Method`.
The dataset is processed through multiple stages to finally produce a clean, transformed and analytics ready dataset.
#
## Data Quality Analysis
The analysis was performed on the raw dataset to identify the data quality issues before performing any cleaning.
The found major findings include:
- 430 records having major fields like "Item, Price,Quantity and Order Total" missing.
- 446 records had missing Price values but available Quantity and Order total values.
- 14 unique combinations of "Category+Price" were identified that could be associated with a single item.
- Order ID was unique accross the dataset.
- Order date was storder as string.
The datail finding of the data quality is documented in **docs/data_quality_analysis.md**.
#
## Data Cleaning
The identified data quality issues were addressed based on the patterns found during cleaning analysis.
### Highly Incomplete Records
The 430 records with major fields missing were removed from the dataset.
### Price Reconstruction
446 missing Price values were reconstructed using available Order Total and Quantity information
### Item Reconstruction
The identified Category+Price relationships were used to reconstruct the missing item values where the relationship provides sufficient evidence.
This resulted in 771 individual "Item" values being constructed.
The remaining 557 values unresolved Item values were assigned as `unknown`.
### Payment Method
The missing Payment Method values were unable to be reconstructed using any realtionships.So,they were filled with the most frequent payment method.
### Date Conversion
The date column was converted from string to Datetime datatype.

The detailed Cleaning analysis and plan are documented in **docs/Cleaning_analysis_and_plan.md**.
#
## Data Transformation
The cleaned dataset was transformed without altering the original transaction level information.The Order date column was used to derive attributes like,
- Year
- Month
- Month name
- Day of Week
the detailed transformation is documented in **docs/Transformation.md**.
#
## Feature Engineering
The row level features were created from teh transformed dataset.
They include `Day Type`, `Order Total Category`,`Quantity Category`.
The detailed feature engineering is documented in **docs/Feature_engineering.md**.
#
## Final Validation
The validation process was performed after feature engineering verify the final dataset.
The final dataset was validated whether they preserved the transaction records as the initial dataset and also was checked whether it was consistent after feature engineering as the previous dataset after transformation.
#
## Final Dataset
The final dataset contained **17,104 records** and 13 columns which is cleaned, transformed and feature engineered.
The final output is exported to **Data/Processed/Final_restaurant_sales.csv**.
The fianl dataset is intended to be used as an analytics-ready dataset or as a foundation for future machine learning works.
#