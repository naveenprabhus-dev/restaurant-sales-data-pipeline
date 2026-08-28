# Dataset Quality Analysis
#
## Shape of the dataset
- Number of columns : 09
- Number of rows    : 17534
#
## Columns
- We have totally 9 columns in the dataset they are, OrderId, CustomerId, Category, Item, Price, Quantity, Order Total, Order Date and Payment method.
- It seems like the price and quantity column will constitute the order total, we will verify the relationship in later steps.
#
- From head() and tail() function we were able to look into the structure of the dataset in the starting and the ending, and verify is there any end of file issues.
#
## Datatypes 
- Among the 9 columns, 3 columns( Price,Quantity and Order total) is of float datatype.
- Rest all the 6 columns have the string datatype.
#
## Missing values
- By using the info and isnull statements, we were able to find the missing values in the dataset.
- We have missing values in Item,Price, Quantity, Order Total and Payment method columns.
        1. Item - 1758
        2. Price - 876
        3. Quantity - 430
        4. Order Total - 430 
        5. Payment Method - 1082
- Item, price and payment method has higher missing values, relatively Quantity and Order total has lesser missing values than those 3.
#
## Duplicate Values
- The exact duplicate values were found accross the records in the dataset.
#
- Using describe function we have obtained the numerical statistics of the numerical value columns present in the dataset.
  
|      |     Price |   Quantity  |   Order Total |
|----: |-------|-----|-----|
|count  |16658.000000  |17104.000000 | 17104.000000|
|mean   |   6.586325   |  3.014149   | 19.914494   |
|std    |   4.834652   |  1.414598   | 18.732549   |
|min    |   1.000000   |  1.000000   |  1.000000   |
|25%    |   3.000000   |  2.000000   |  7.500000   |
|50%    |   5.000000   |  3.000000   | 15.000000   |
|75%    |   7.000000   |  4.000000   | 25.000000   |
|max    |   20.000000  |   5.000000  | 100.000000  |

-  We can clearly see the ranges for each and every numerical value columns in the dataset,Quantity ranges from 1 to 5, Price ranges from 1 to 20 and Order total ranges from 1 to 100.
- The minimum values of all the three numerical value columns are positive values, no negative or values are there.
- Order total has potential outliers, as the 3rd quartile is 25 while the max is 100.
#
## Unique Values
- We can see category, quantity and payment mathods have lower number of unique values in the overall column, whreras all the other columns have higher number of unique values present, that is they have different values across the different records.
- The OrderId is unique for each and every record, and we can also infer that there are totally 100 unique customers accross the whole dataset.
#

## Final summary of the Data Quality Findings
- There are missing values present in columns Item, Price, Quantity, Order Total, Payment Method.
- No exact duplicate records were identified.
- Order date is stored as string which is an important observation.
- No negative or zero values are identified from the numerical summary,so all the values are under a positive range of values.
- The order total has potential high value outliers.
