# Pandas Practice 🐼

This repository contains my hands-on Pandas practice as part of a focused 7-day learning sprint.

The goal is to build practical skills for working with structured data using Python and Pandas.

## Learning Progress

### Day 1 - Pandas Basics ✅

- Introduction to Pandas
- Series and DataFrames
- Rows, columns, and indexes
- Creating DataFrames from dictionaries
- Selecting single and multiple columns
- Understanding `shape`
- Viewing column names with `columns`
- Checking data types with `dtypes`
- Using `head()` and `tail()`
- Hands-on practice with a product dataset

### Day 2 - Working with CSV Files ✅

- Understanding CSV files
- Reading CSV files using `read_csv()`
- Understanding CSV headers
- Using `header=None`
- Assigning custom column names with `names`
- Inspecting datasets using `info()`
- Understanding non-null values and missing data
- Statistical summaries using `describe()`
- Hands-on practice with student and employee datasets

### Day 3 - Selecting, Filtering & Sorting

- Filtered rows using comparison conditions
- Combined multiple conditions using `&` (AND) and `|` (OR)
- Selected specific columns from filtered data
- Learned `.loc[]` for selecting data using labels and conditions
- Learned `.iloc[]` for selecting data using integer positions
- Used slicing with `.iloc[]`
- Sorted DataFrames using `sort_values()`
- Practiced combining filtering, column selection, and sorting

### Day 4 - Data Cleaning

- Identified missing values using `isnull()` and `isnull().sum()`
- Learned how Pandas represents missing data using `NaN`
- Removed rows containing missing values using `dropna()`
- Filled missing numerical values using `fillna()` and the column mean
- Detected duplicate rows using `duplicated()`
- Counted duplicates using `duplicated().sum()`
- Removed duplicate rows using `drop_duplicates()`
- Learned why duplicates should be handled before calculating statistics such as the mean
- Verified the dataset after cleaning for remaining missing values and duplicates

### Day 5 - Columns, Calculations & GroupBy

- Added new columns to a DataFrame
- Created calculated columns using existing data
- Rounded numerical values using `round()`
- Removed columns using `drop()`
- Learned vectorized calculations without writing loops
- Grouped data using `groupby()`
- Calculated group statistics using `mean()`, `min()`, and `max()`
- Used `agg()` to perform multiple aggregate calculations
- Performed aggregation on multiple columns

### Day 6 - Practical Data Analysis

- Loaded and inspected a real-style CSV dataset
- Checked DataFrame shape and structure
- Identified missing values and duplicate rows
- Removed duplicate records using `drop_duplicates()`
- Filled missing numerical values using `fillna()` and column mean
- Verified data after cleaning
- Sorted products by Price using `sort_values()`
- Grouped data by Category using `groupby()`
- Calculated average Price for each Category
- Created a calculated `Total_Value` column using Price × Quantity
- Practiced combining concepts learned from previous Pandas days

## Progress

**Day 6/7 Completed ✅**

## Tools

- Python
- Pandas
- VS Code
- Git & GitHub
