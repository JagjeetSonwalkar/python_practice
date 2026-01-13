import pandas as pd 

df = pd.read_csv("csv_files/data.csv")
print(df.head(5))

# Filter rows where Age > 25 and City == 'Delhi'.
result = df[(df["Age"] > 25) & (df["City"] == "Delhi")].reset_index()
print("rows where Age > 25 and City == 'Delhi': ")
print(result)

# Select rows with Name starting with 'A'.
result = df[df.Name.str.startswith("A")].reset_index()      
print("rows with Name starting with 'A': ")
print(result)

# Select rows with Name ending with 'e'.
result = df[df.Name.str.endswith('e')].reset_index()
print("rows with Name ending with 'e'.")
print(result)

# Select rows with Age between 20 and 30.
result = df[(df.Age >= 20) & (df.Age <= 30)].reset_index()
print("rows with Age between 20 and 30: ")
print(result)

# Use query method to filter Age > 25.
result = df.query("Age > 25").reset_index()
print("using query method to filter Age > 25: ")
print(result)
