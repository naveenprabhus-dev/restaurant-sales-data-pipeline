import pandas as pd
df=pd.read_csv(r"Data\Interim\cleaned.csv")
print(df.head())

df["Order Date"]=pd.to_datetime(df["Order Date"],format="%Y-%m-%d")
print("The datatype of Order Date:",df["Order Date"].dtypes)

