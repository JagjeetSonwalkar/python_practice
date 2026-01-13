import pandas as pd 

df = pd.read_csv("csv_files/data.csv")

# Select the first 3 rows and first 2 columns using iloc.
result = df.iloc[0:3, 0:2]
print("the first 3 rows and first 2 columns using iloc: ")
print(result)

# Select rows 2 to 5 and columns Name and Age using loc.
result = df.loc[2:5, ["Name", "Age"]]
print("rows 2 to 5 and columns Name and Age using loc.")
print(result)

# Reset DataFrame index.
result = df.reset_index()
print(result.head(5))

# Set Name as the index.
result = df.set_index(df["Name"])
print("Name as the index: ")
print(result)

# Sort DataFrame by index.
result = result.sort_index()
print("Sort DataFrame by index.")
print(result)