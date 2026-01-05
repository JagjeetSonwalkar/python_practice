# import a csv file

import pandas as pd

def main():
    df = pd.read_csv("csv_files/titanic.csv")

    print(df)

    # I want to see the first 8 rows of a pandas DataFrame.
    print(df.head(8))

if __name__ == "__main__":
    main()