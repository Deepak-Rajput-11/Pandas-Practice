import pandas as pd

df = pd.read_csv("sales.csv")

print(df.isnull().sum())

df = df.drop_duplicates()

print(df)

df["Price"] = df["Price"].fillna(df["Price"].mean())

print(df)

print(df[(df["Category"] == "Electronics") & (df["Price"] > 2000)])

df["Total_Value"] = df["Price"] * df["Quantity"]

print(df["Total_Value"])

print(df.groupby("Category")["Price"].agg(["mean", "min", "max"]))
