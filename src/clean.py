import pandas as pd
df=pd.read_csv(r"Data\Raw\restaurant_sales_data.csv")
print("Raw datasetloaded successfully")
#Created a copy to check once before working on the originl dataframe
df_copy1= df.copy()

#Missing value cleaning

#Reconstructing the 446 records with missing Price but available order Total and Quantity
dh=(df["Price"].isnull() & df["Order Total"].notnull() & df["Quantity"].notnull())
l=df.loc[dh]
print(l)

calcu=l["Order Total"]/l["Quantity"]
print(calcu)

print("Records selected=",len(l))

df.loc[dh,"Price"]=calcu

print(df["Price"].isnull().sum())

print(df.loc[dh].sample(1))

# Inspecting the 430 records with majority of the feilds missing

incomplete = (
    df_copy1["Item"].isnull()
    & df_copy1["Price"].isnull()
    & df_copy1["Quantity"].isnull()
    & df_copy1["Order Total"].isnull()
)

print("\n430 incomplete transaction records:")
h=df_copy1.loc[incomplete]
#h.to_excel("cleaned.xlsx",index=False)

print("\nCustomer IDs in the 430 incomplete records:")
print(df_copy1.loc[incomplete, "Customer ID"].value_counts())

print("\nCustomer IDs in the 430 incomplete records:")
print(df_copy1.loc[incomplete, "Category"].value_counts())

#Cleaning the 1728 missing values of items column
#Dropping the 430 records with majority of feilds missing

df = df.drop(df[incomplete].index)
print(df.shape)
print(df["Item"].isnull().sum())

missing_item = (
    df_copy1["Item"].isnull()
    & ~incomplete
)

print("\nRecords with Item missing excluding the 430 incomplete records:")
print(missing_item.sum())

print(df_copy1.loc[missing_item,["Category","Price"]].value_counts())

print(df.groupby(["Category","Price"])["Item"].nunique())

#df.to_excel("cleaned.xlsx",index=False)


