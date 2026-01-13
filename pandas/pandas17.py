# Indexing / selection

import pandas as pd 

def main():
    df = pd.read_csv("csv_files/iris.csv")

    # select the sepal.length col only
    result = df['sepal.length']
    print(result.head(5))

    # select the row by label 
    result = df.loc[0]
    print(result)

    # Select row by integer location
    result = df.iloc[0]
    print(result)

    # Slice rows 5 - 10
    result = df[5:10]
    print(result)

    

if __name__ == "__main__":
    main()