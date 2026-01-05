# Read data

import pandas as pd
# from sqlalchemy import create_engine as sql

# read_csv()
df = pd.read_csv("csv_files/titanic.csv")
print(df.head())

# read_excel()
# Need of: pip install openpyxl
exel_df = pd.read_excel("other_files/titanic.xlsx")
print(exel_df.head())

# read_json()
json_df = pd.read_json("other_files/titanic.json")
print(json_df.head())

# read_sql()
'''
sql_engine = create_engine("mysql+pymysql://username:password@localhost:3306/database_name")
sql_df = pd.read_sql("Select * from table", sql_engine)
'''

# read_url()
url_link = "https://raw.githubusercontent.com/pandas-dev/pandas/refs/heads/main/doc/data/titanic.csv"
url_df = pd.read_csv(url_link)
print(url_df.head())