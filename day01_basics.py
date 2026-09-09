import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "Price": [55000, 700, 1500, 12000, 2500],
    "Quantity": [5, 20, 10, 7, 15],
}

df = pd.DataFrame(data)

print(df)

print(df.shape)

print(df.columns)

print(df.dtypes)

print(df["Price"])

print(df[["Product", "Quantity"]])

print(df.head(3))

print(df.tail(2))
