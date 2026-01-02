# import .csv file

import pandas as pd

def main():
    # import csv file
    df = pd.read_csv("iris.csv")

    print(df) # it will print 1st & last 5 row's

    print(df.to_string())   # it will print whole .csv file

    # import json file
    # df = pd.read_json("file_name")

if __name__ == "__main__":
    main()