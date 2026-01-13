import pandas as pd 

df = pd.read_csv("csv_files/data.csv")

# Drop rows with any missing value.
result = df.dropna()
print("Drop rows with any missing value: ")
print(result)

# Forward fill missing values.
result = df.fillna(method="ffill")
print("Forward fill missing values: ")
print(result)

# Backward fill missing values.
result = df.fillna(method="bfill")
print("Backward fill missing values: ")
print(result)

# Interpolate missing values.
result = df.interpolate()
print("Interpolate missing values: ")
print(result)

# Count missing values per column.
result = df.isna().sum()
print("Count missing values per column: ")
print(result)
