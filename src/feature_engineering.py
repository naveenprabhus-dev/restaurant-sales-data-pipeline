import pandas as pd
df=pd.read_csv(r"Data/Interim/transformed.csv")
print("Dataset loaded successfully\n")
print(df.head())
print(df.columns)

df["Order Date"]=pd.to_datetime(df["Order Date"],format="%d-%m-%Y")

#Day type feature
df["Day Type"]=df["Day of week"].apply(lambda x:"Weekend" if x in["Saturday","Sunday"] else "Weekday")
print(df[["Day of week","Day Type"]].head(10))

#Order Value category feature
print("\nOrder Total Statistics:")
print(df["Order Total"].describe())

df["Order Total Category"]="Medium"

df.loc[df["Order Total"]<=7.5,"Order Total Category"]="Low"
df.loc[df["Order Total"]>25,"Order Total Category"]="High"

print(df[["Order Total","Order Total Category"]].sample(10))

#Quantity Category
print("Quantity Statistics:")
print(df["Quantity"].describe())

df["Quantity Category"]="Medium"
df.loc[df["Quantity"]<=2,"Quantity Category"]="Low"
df.loc[df["Quantity"]>4,"Quantity Category"]="High"

print(df[["Quantity","Quantity Category"]].sample(10))

df.to_csv("Data/Interim/feature_engineered.csv",index=False)