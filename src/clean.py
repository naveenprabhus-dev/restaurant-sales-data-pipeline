import pandas as pd
df=pd.read_csv(r"Data\Raw\restaurant_sales_data.csv")
print("Raw datasetloaded successfully")
#Created a copy to check once before working on the originl dataframe
df_copy1= df.copy()

#Missing value cleaning

#Selecting the records with missing price but available order total and quantity
dh=(df["Price"].isnull() & df["Order Total"].notnull() & df["Quantity"].notnull())
l=df.loc[dh]
print(l)

calcu=l["Order Total"]/l["Quantity"]
print(calcu)

print("Records selected=",len(l))

df.loc[dh,"Price"]=calcu

print(df["Price"].isnull().sum())

print(df.loc[dh].sample(1))