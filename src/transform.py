import pandas as pd
def transform_data():
    df=pd.read_csv(r"Data/Interim/cleaned.csv")
    print(df.head())

    df["Order Date"]=pd.to_datetime(df["Order Date"],format="%Y-%m-%d")
    print("The datatype of Order Date:",df["Order Date"].dtypes)

    #Year wise sales
    print("\nCreating Year column:")
    df["Year"] = df["Order Date"].dt.year

    print(df[["Order Date", "Year"]].sample(5))

    #Month wise sales segregation
    print("\nCreating Month column:")
    df["Month"]=df["Order Date"].dt.month
    df["Month_Name"]=df["Order Date"].dt.month_name()

    print(df[["Order Date","Month","Month_Name"]].sample(5))

    # Day of week wise sales
    print("\nCreating day of week column:")
    df["Day of week"]=df["Order Date"].dt.day_name()
    print("\n",df[["Order Date","Day of week"]].sample(5))

    print("\nTransformed dataset dimensions:",df.shape)

    df.to_csv("data/interim/transformed.csv",index=False)
    print("\n--Transformed dataset exported successfully.--\n")

    return df

if __name__ =="__main__":
    transform_data()
