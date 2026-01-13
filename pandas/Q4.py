# Quick Data Inspection

import pandas as pd 

def main():
    df = pd.read_json("other_files/titanic.json")

    print(df.head())
    print(df.tail())

    print()
    print(df.sample())
    print(df.info())

    print()
    print(df.describe())

    print("Shape is:",df.shape)
    print("Data type is:",df.dtypes)


if __name__ == "__main__":
    main()