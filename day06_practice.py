import pandas as pd

df = pd.read_csv("sales.csv")

print("Original data:")
print(df)

print("\nShape:")
print(df.shape)

print("\nDataFrame information:")
df.info()

print("\nMissing values before cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows before cleaning:")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing numerical values using column mean
df["Price"] = df["Price"].fillna(df["Price"].mean())
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())

print("\nCleaned data:")
print(df)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows after cleaning:")
print(df.duplicated().sum())

print("\nProducts sorted by Price - highest to lowest:")
print(df.sort_values("Price", ascending=False))

print("\nAverage Price by Category:")
print(df.groupby("Category")["Price"].mean())

# Create a calculated column
df["Total_Value"] = df["Price"] * df["Quantity"]

print("\nAfter adding Total_Value:")
print(df)
