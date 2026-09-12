import pandas as pd

df = pd.read_csv("students.csv")

# Use this when the CSV file doesn't have a header
# df = pd.read_csv("students.csv", header=None)

# Use this to provide our own column names
# df = pd.read_csv("students.csv", header=None, names=["Name", "Age", "Marks"])

print(df)

print(df.shape)
df.info()
print(df.describe())
