import pandas as pd

df = pd.read_csv("students.csv")

# if csv didn't have any header then we use this
# df = pd.read_csv("students.csv", header=None)

# It create our own header (column names)
# df = pd.read_csv("students.csv", header=None, names=["Name", "Age", "Marks"])

print(df)

print(df.shape)
df.info()
print(df.describe())
