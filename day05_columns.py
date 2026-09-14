import pandas as pd

df = pd.read_csv("students.csv")

print("Original data:")
print(df)

# Add a new column
df["Result"] = "Pass"

print("\nAfter adding Result column:")
print(df)

# Add a calculated column
df["Percentage"] = ((df["Marks"] / 120) * 100).round(2)

print("\nAfter adding Percentage column:")
print(df)

# Remove a column
df = df.drop(columns=["Result"])

print("\nAfter removing Result column:")
print(df)

# Group data by Course and calculate average Marks
print("\nAverage Marks by Course:")
print(df.groupby("Course")["Marks"].mean())

# Multiple summary calculations on Marks
print("\nMarks summary by Course:")
print(df.groupby("Course")["Marks"].agg(["mean", "min", "max"]))

# Multiple-column aggregation
print("\nAge and Marks summary by Course:")
print(df.groupby("Course")[["Age", "Marks"]].agg(["mean", "min", "max"]))
