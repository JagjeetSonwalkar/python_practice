import pandas as pd 

df = pd.read_csv("csv_files/data.csv")

# Show the shape of a DataFrame.
print(f"The shape of DF is: {df.shape}")

# Show column names of a DataFrame.
result = df.columns
print(f"The names of column are: {result}")

# Select a single column Age from a DataFrame.
result = df.Age
print(f"The single column of age: \n{result}")

# Select multiple columns Name and City.
result = df[["Age", "City"]]
print(f"The multiple columns Name and City: \n{result}")

# Select the first row using iloc.
result = df.iloc[0]
print(f"The first row is:\n{result}")

# Select the first row using loc.
result = df.loc[df["ID"]==1]
print(f"The first row is:\n{result}")

# Check for missing values in a DataFrame.
result = df.columns[df.isnull().any()]    # OR-> df.isnull().values.sum()
print(f"missing values in a DataFrame:{result}")

# Fill missing values in a column with 0.
df = df.fillna(0)
print(df)

# drop City column from DF
result = df.drop(["City"], axis = 1)
print("drop City column from DF:")
print(result)

# Add a new column Country with value India
df["Country"] = "India"
print("Add a new column Country with value India")
print(df)

# Sort DataFrame by Age ascending.
result = df.sort_values("Age")
print("Sort DataFrame by Age ascending.")
print(result)

# Filter rows where Age > 25.
result = df[df["Age"] > 25]
print("Filter rows where Age > 25.")
print(result)

# Calculate the mean of Age.
result = df.Age.mean()
print(f"The mean of age column is: {result}")

# Calculate the sum of Age.
result = df.Age.sum()
print(f"The sum of age column is: {result}")

# Get the maximum and minimum value of Age.
print(f"The max Age is: {df.Age.max()} & The min Age is: {df.Age.min()} ")