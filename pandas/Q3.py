# save the file

import pandas as pd
from sqlalchemy import create_engine

df = pd.read_json("other_files/titanic.json")

# to_csv()
df.to_csv("saved_files/df.csv", index = False, header = False, mode = 'a')

# to_excel()
df.to_excel("saved_files/titanic.xlsx", index = False)

df = pd.read_csv("csv_files/titanic.csv")

# to_json()
df.to_json("saved_files/titanics.json", index = False)

# to_sql()
engine = create_engine("mysql+pymysql://username:password@localhost:3306/database_name")

df.to_sql(
    name="employees",   # table name
    con=engine,
    if_exists="replace",  # or 'append'
    index=False
)

# Save Excel File into MySQL
df = pd.read_excel("employees.xlsx")
df.to_sql("employees", engine, if_exists="append", index=False)
