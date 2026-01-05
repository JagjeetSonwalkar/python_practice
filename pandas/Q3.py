# save the file

import pandas as pd

df = pd.read_json("other_files/titanic.json")

# to_csv()
df.to_csv("saved_files/df.csv", index = False, header = False, mode = 'a')

# to_excel()
# to_json()

df = pd.read_csv("csv_files/titanic.csv")

# to_sql()
