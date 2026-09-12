import pandas as pd

df = pd.read_csv("students.csv")

# Basic filtering
print("Students with Marks greater than 80:")
print(df[df["Marks"] > 80])

# AND condition
print("\nAge greater than 20 AND Marks greater than 80:")
print(df[(df["Age"] > 20) & (df["Marks"] > 80)])

# OR condition
print("\nAge equal to 20 OR Marks less than 80:")
print(df[(df["Age"] == 20) | (df["Marks"] < 80)])

# Selecting specific columns
print("\nStudents Age greater than 20 - Name and Age:")
print(df[df["Age"] > 20][["Name", "Age"]])

# loc - select rows and columns using conditions/labels
print("\nUsing loc:")
print(df.loc[df["Age"] > 20, ["Name", "Age"]])

# iloc - select using integer positions
print("\nUsing iloc:")
print(df.iloc[0:3, 0:2])

# Sorting
print("\nStudents sorted by Age - highest to lowest:")
print(df.sort_values("Age", ascending=False))

# Filtering + selecting columns + sorting
print("\nStudents with Marks >= 80 - highest to lowest:")
print(
    df.loc[df["Marks"] >= 80, ["Name", "Marks"]].sort_values("Marks", ascending=False)
)
