import pandas as pd
def clean_data():
    df=pd.read_csv(r"Data/Raw/restaurant_sales_data.csv")
    print("Raw datasetloaded successfully\n")
    print(df.head(10))
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

    incomplete = (df_copy1["Item"].isnull()& df_copy1["Price"].isnull()& df_copy1["Quantity"].isnull()& df_copy1["Order Total"].isnull())

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

    #Filling Items Column using Category+Price combination

    unique_item_mapping = (df.groupby(["Category", "Price"])["Item"].agg(["nunique", "first"]))

    print("\nCategory + Price mapping:")
    print(unique_item_mapping)

    unique_item_mapping = unique_item_mapping[unique_item_mapping["nunique"] == 1]

    print("\nUnique Category + Price -> Item mappings:")
    print(unique_item_mapping)

    item_mapping = unique_item_mapping["first"].to_dict()

    for index in df[df["Item"].isnull()].index:

        category = df.loc[index, "Category"]
        price = df.loc[index, "Price"]
        if (category, price) in unique_item_mapping.index:
            df.loc[index, "Item"] = unique_item_mapping.loc[(category, price), "first"]

    print("\nThe missing Item values after filling using 14 unique combination=")
    print(df['Item'].isnull().sum())

    #Filling the rest 557 records as unknown 
    df["Item"] = df["Item"].fillna("Unknown")
    print(df["Item"].isnull().sum())

    #Checking relation of payment methods to customer ID for reconstruction
    payment_missing = df["Payment Method"].isnull()

    print("\nCustomer IDs for records with missing Payment Method:")
    print(df.loc[payment_missing, "Customer ID"])

    print("\nCustomer IDs and Payment Methods for missing-payment records:")
    print(df.loc[payment_missing,["Customer ID", "Payment Method"]])

    print("\nNumber of different Payment Methods used by each Customer:")
    print(df.groupby("Customer ID")["Payment Method"].nunique())

    print("\nPayment Method frequency:")
    print(df["Payment Method"].value_counts())

    most_common_payment = df["Payment Method"].mode()[0]

    print("\nMost common Payment Method:")
    print(most_common_payment)

    df["Payment Method"] = df["Payment Method"].fillna(most_common_payment)

    print("\nRemaining missing Payment Method values:")
    print(df["Payment Method"].isnull().sum())

    #Changing the Order Date to datetime data type
    df["Order Date"]=pd.to_datetime(df["Order Date"],format="%d-%m-%Y")

    print("\nOrder Date data type:")
    print(df["Order Date"].dtype)

    print("\nMissing values after cleaning:")
    print(df.isnull().sum())

    #Exporting the cleaned interim dataset
    df.to_csv("data/interim/cleaned.csv",index=False)
    print("\n--Cleaned dataset exported successfully--\n")

    return df

if __name__ == "__main__":
    clean_data()
