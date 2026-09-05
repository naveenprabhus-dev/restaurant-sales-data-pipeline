import pandas as pd
df=pd.read_csv(r"Data\Interim\feature_engineered.csv")
print("Dataset loaded successfully")
print(df.head())

#Final Validation Checks
print("\nDataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("Missing Values:")
print(df.isnull().sum())

print("Duplicate Records:")
print(df.duplicated().sum())

print("Data types:")
print(df.dtypes)

print("Final Row count:")
print(len(df))

#Order total validation
calc_total=df["Price"]*df["Quantity"]
print("\nPrice * Quantity = Order total:",calc_total.equals(df["Order Total"]))

#Features engineered validation
#Day Types
print("\nDay type values:")
print(df["Day Type"].value_counts())

#Order category
print("\nOrder Category values:")
print(df["Order Total Category"].value_counts())

#Quantity category
print("Quantity Category Values:")
print(df["Quantity Category"].value_counts())

df.to_csv("Data/Processed/Final_restaurant_sales.csv",index=False)