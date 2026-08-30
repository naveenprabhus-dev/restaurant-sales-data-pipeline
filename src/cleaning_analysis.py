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

print("\nNumber of unique items for each category + price combination:\n0")
print(df.groupby(["Category", "Price"])["Item"].nunique().sort_values(ascending=False))

#Outlier Analysis
#Order total
print("\nPotential Order Total outliers using IQR:")

Q1=df["Order Total"].quantile(0.25)
Q3=df["Order Total"].quantile(0.75)
IQR=Q3-Q1
lower_limit1=Q1-1.5*IQR
upper_limit1=Q3+1.5*IQR

print("Lower limit:",lower_limit1)
print("Upper limit:",upper_limit1)

print("Number of potential outliers:")
print(((df["Order Total"] < lower_limit1) | (df["Order Total"] > upper_limit1)).sum())

#Unique values
print("Total number of unique values in column OrderID:")
print(df["Order ID"].nunique())

# Categorical Value Consistency 
print("\nUnique Category values:")
print(df["Category"].unique())
print("\nCategory value counts:")
print(df["Category"].value_counts(dropna=False))

print("\nUnique Payment Method values:")
print(df["Payment Method"].unique())
print("\nPayment Method value counts:")
print(df["Payment Method"].value_counts(dropna=False))

print("\nUnique Item values:")
print(df["Item"].unique().tolist())
print("\nItem value counts:")
print(df["Item"].value_counts(dropna=False))

#Order date Check
print(df["Order Date"].head(20))
print("\nNumber of unique Order Date values:")

print(df["Order Date"].nunique())
dates = pd.to_datetime(df["Order Date"])

print("\nInvalid Order Date values:")
print(dates.isnull().sum())
