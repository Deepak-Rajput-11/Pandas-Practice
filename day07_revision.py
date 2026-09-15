import pandas as pd

df = pd.read_csv("sales.csv")

print(df[["Product", "Price"]])

print(df[df["Price"] > 5000])

print(df[df["Quantity"] > 4])

print(df[(df["Category"] == "Electronics") & (df["Price"] > 2000)])

print(df[(df["Category"] == "Furniture") & (df["Quantity"] > 2)])

print(df.iloc[0:3, 0:2])

print(df.groupby("Category")["Price"].agg(["mean", "min", "max"]))
