import pandas as pd 

df = pd.read_csv("csv_files/data.csv")

print(df.dtypes)

# Convert a column Date to datetime.
df['Date'] = pd.to_datetime(df["Date"], errors='coerce')
print("Convert a column Date to datetime.")
print(df.dtypes)

# Extract year from Date.
df["year"] = df["Date"].dt.year
print(df.head(5))

# Extract month from Date.
df["month"] = df["Date"].dt.month
print(df.head(5))

# Extract day from Date.
df["Day"] = df["Date"].dt.day 
print(df.head(5))

# Extract weekday name from Date.
df["weekday"] = df["Date"].dt.weekday
print(df.head(5))