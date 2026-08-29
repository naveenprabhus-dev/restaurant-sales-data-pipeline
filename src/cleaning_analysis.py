import pandas as pd
df=pd.read_csv(r"Data\Raw\restaurant_sales_data.csv")
#Missing value pattern analysis
print("\nQuantity and Order Total both missing:")
print((df["Quantity"].isnull()&df["Order Total"].isnull()).sum())

print("\nQuantity missing but order total is avilable:")
print((df["Quantity"].isnull()&df["Order Total"].notnull()).sum())

print("\nQuantity + Order Total + Price all three missing values:")
print((df["Quantity"].isnull()& df["Order Total"].isnull()& df["Price"].isnull()).sum())

print("\nQuantity and Order total is available but the Price is missing:")
print((df["Quantity"].notnull()& df["Order Total"].notnull()& df["Price"].isnull()).sum())

print("\nItem values are available but the price values are missing:")
print((df["Item"].notnull()& df["Price"].isnull()).sum())

print("\nMissing values in other columns withing those 430 missing rows:")
print(df.loc[df["Price"].isnull() & df["Quantity"].isnull() & df["Order Total"].isnull()].isnull().sum(),"\n")

print("\nNumber of unique items for each category+ price combination:\n0")
print(df.groupby(["Category", "Price"])["Item"].nunique().sort_values(ascending=False))

