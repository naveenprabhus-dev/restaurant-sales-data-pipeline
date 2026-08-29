# Cleaning Analysis
After the data quality analysis we have made earlier, now we will extend the analysis and find the patterns and insights we have for planning the cleaning process.
#
## Missing Value pattern analysis
- The 430 missing values in columns order total and quantity are in the exact same rows in both the columns.
- The missing values combining three columns Quantity, Order Total and Price is 430. So the three columns have exact same 430 records as missing.
- The price values are missing but the values are present in quantity and order total is totally 446.
- The item is available but the price value is missing is 0. 
- Within the 430 records where the price,quantity and order total are missing:
    - Item is missing all the 430 records
    - Payment method is missing 139 records
    - other 3 columns dont have any missing values.
- So the 430 records have substantial missing transaction information.
### Item and price relationship
- There are no records where item is available and the price is missing.
- the category+ price analysis was performed to determine whether these 2 columns can uniquely identify an 'Item'.
- the analysis identified **14 category + price** combinations that are associated with only one unique item.

#
## Cleaning Plan
- The **446** records with missing price but available 'quantity' and 'Order total' can be used to reconstruct the missing price values.
- The 430 records with multiple feilds missing requires seperate investigation before decision of removal or retention.
- The identified 14 unique category+price combinations can potentially help in reconstructing the missing item values.