# Feature Engineering 
Feature engineering was performed on the transformed dataset to create a small number of meaningful row level features for analysis.
#
## Features created 
Created three row level features during this stage.
### 1.Day Type
This feature classifies the each transaction based on the day of the week whether it is,
    - "Weekday" - Monday to Friday
    - "Weekend" - Saturday and Sunday
This feature helps in distinguishing between weekday and weekend sales with out further interpretation of the 'day of week' column

### 2.Order Total Category
- This feature groups the transaction based on the value of their Order Total.
- Used the distribution of the order total value accross the table and divided it into, Low, Medium and High valued transactions.
- These were done based on the quartiles of the Order Total column.

### 3.Quantity Category
- This feature groups the transaction based on the quantity ordered by the customer in that particular transaction
- The dataset contained quantity values ranging from 1 to 5, So we used quartiles to divide it as Low, Medium and High valued transactions based on the quantity value.
#
The created features were validated to ensure that they preserved the transaction count dring feature engineering, and also whether the final dataset remained consistent with the previous transformation stage.
#
## Output
The final cleaned and ready dataset was exported as **Final_restaurant_sales.csv** to Data/Processed/ folder. 
The final dataset lies as a foundation for future analytics and machine learning.
#
