# Assigning new columns using assign() method 

import pandas as pd 

def main():
    df = pd.read_csv("csv_files/iris.csv")

    print(df.head(5))

    # add new column
    x = df.assign(sepial_ratio = lambda x:  (x["sepal.width"] / x["sepal.length"]))
    print(x.head(5))

if __name__ == "__main__":
    main()