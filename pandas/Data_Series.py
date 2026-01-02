# Series

import pandas as pd

def main():
    data = [101, 102, 103] # data_type list

    series = pd.Series(data) # constructor of series : pd.Series()

    print(series)
    print(f"data type of series is {type(series)}")  #  <class 'pandas.core.series.Series'>

    series = pd.Series(data, index=['a', 'b', 'c'])

    print(series)

    print(f"value of index a {series['a']}")
    print(f"Value of index a {series.loc['a']}")
    print(f"Value of index a {series.iloc[0]}")

    series.loc['a'] = 999
    print(f"Value of index a {series.loc['a']}")

if __name__ == "__main__":
    main()