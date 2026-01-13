import pandas as pd

df = pd.read_csv("csv_files/data.csv")
print(df.head(5))

# Group by City and get mean of Age.
result = df.groupby("City")["Age"].mean()
print("Group by City and get mean of Age: ")
print(result)

# Group by City and count number of people.
result = df.groupby("City")["Name"].count()
print("Group by City and count number of people: ")
print(result)

# Group by City and aggregate Age (mean, max).
result = df.groupby("City").agg({'Age':['mean','max']})
print("Group by City and aggregate Age (mean, max): ")
print(result)

# Get cumulative sum of Age.
result = df["Age"].cumsum()
print("Get cumulative sum of Age: ")
print(result)

# Rank Age values.
result = df.Age.rank()
print("Rank Age values: ")
print(result)