# create the series and dataframe

import pandas as pd 
import numpy as np

# Creating Series: From lists
age_series = pd.Series([12, 23, 34, 45, 56])
print(f"create a series from list:\n{age_series}\n")

# Creating Series: From dictionaries
age_series = pd.Series({"rohit": 45, "virat": 18, "mahesh": 25})
print(f"Create a series from dict:\n{age_series}\n")

# Creating Series: From NumPy arrays
age = np.array([14, 24, 47])
age_series = pd.Series(age)
print(f"Create a series from numpy:\n{age_series}\n")

# Creating DataFrames: From lists
student_df = pd.DataFrame(
    [
    [1, "rohit", 245, 'R'],
    [2,"tilak", 89, 'L'],
    [3,"Sky",100, "R"]
], columns=["ID", "Name", "Runs", "Hand"]
)
print(f"The dataframe of student:\n{student_df}\n")

# Creating DataFrames: From dictionaries
student_df = pd.DataFrame(
    {
        "Names": ["Rohit", "Virat", "Sky"],
        "Ages": [51, 42, 38],
        "position": [1,3,4]
    }
)
print(f"Dataframe of dict:\n{student_df}\n")

# Creating DataFrames: From NumPy arrays
arr = np.array([
    [1, 23],
    [2, 25],
    [3, 22]
])
age_df = pd.DataFrame(arr, columns=["ID", "Age"])
print(age_df)