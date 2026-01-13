import pandas as pd 

df = pd.read_csv("csv_files/data.csv")

# Convert Name column to uppercase.
result = df['Name'].str.upper()
print("Convert Name column to uppercase: ")
print(result)

# Check which rows contain 'Alice' in Name.
result = df[df.Name.str.contains("Alice")]
print("Check which rows contain 'Alice' in Name: ")
print(result)

# Replace 'Delhi' with 'New Delhi' in City.
df["City"] = df['City'].str.replace("Delhi", "New Delhi")
print("Replace 'Delhi' with 'New Delhi' in City: ")
print(df)

# Get first character of Name column.
result = df.Name.str.get(0)
print("Get first character of Name column: ")
print(result)