import pandas as pd
import numpy as np

# creae a dataframe df from this dict data which has the index labels

data = {"animal": ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
"age" : [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
"visitors" : [1,3,2,3,2,3,1,1,2,1],
"priority" : ['y', 'y', 'n', 'y', 'n', 'n', 'n', 'y', 'n', 'n']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index=labels)
print(df)

# display the summary of the basic infromation of DF and its data
print("\n-- Basic info --")
df.info()

# return the first 3 rows of df
print(f"\nThe first the rows of DF is:\n{df.head(3)}")

# select just the animal & age coloums from the df
new_df = df[["animal", "age"]]
print(f"\nanimal & age coloums from the df:\n{new_df}")

# select the data in rows [3,4,8] and coloums ["animal","age"]
select_data = df[["animal", "age"]].iloc[[3,4,8]]
print(f"\ndata in rows [3,4,8] and coloums [animal,age] is:\n{select_data}")

# select the data only the rows where the no. of visits is grater than 3
select_data = df[df["visitors"] > 3]
print(f"\nrows where the no. of visits is grater than 3:\n{select_data}")

# select the rows where the age is missing
select_data = df[df["age"].isna()]
print(f"\nrows where the age is missing:\n{select_data}")

# select the rows where the animal is a cat and the age is less than 3
select_data = df[(df.animal == "cat") & (df.age < 3)]
print(f"\nrows where the animal is a cat and the age is less than 3:\n{select_data}")

# select the rows the age is b/w 2 and 4
select_data = df[(df.age <= 4) & (df.age >= 2)]
print(f"\nthe rows the age is b/w 2 and 4:\n{select_data}")

# change the age in row 'f' to 1.5
print(f"\nThe row 'f' before changing:\n{df.iloc[5]}")
df.loc["f", "age"] = 1.5
print(f"The row 'f' after changing:\n{df.iloc[5]}")
