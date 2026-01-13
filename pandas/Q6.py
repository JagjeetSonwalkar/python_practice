import pandas as pd
import numpy as np

data = {"animal": ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
"age" : [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
"visitors" : [1,3,2,3,2,3,1,1,2,1],
"priority" : ['y', 'y', 'n', 'y', 'n', 'n', 'n', 'y', 'n', 'n']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(data, index=labels)

####################################################################################################################

# calculate the sum of all visitors in df
total_visitors = df["visitors"].sum()
print(f"The total visitors are: {total_visitors}")

# calculate the mean age for each different animal in df
calculation = df.groupby(["animal"])[("age")].agg('mean').reset_index()
print(f"the mean age for each different animal: {calculation}")

# append a new row at 'k' to df with your choice of values for each column. Then delete that row to return the original DataFrame
df.loc['k'] = ['lion', 10, 25, 'y'] 
print(df)
df.drop(index=['k'], inplace= True)
print(df)

# count the number of each type of animal in df
df['count'] = 1
count = df.groupby("animal")["count"].sum().reset_index()
print(f"The count of animal is:\n{count}")

# in the animal column , change the snake entires to python
df['animal'].replace({"snake":"python"}, inplace=True)
print(df)