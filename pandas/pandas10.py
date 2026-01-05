# I’m interested in the names of the passengers older than 35 years.

import pandas as pd 

def main():
    df = pd.read_csv("csv_files/titanic.csv")

    # I’m interested in the names of the passengers older than 35 years.
    passenger = df.loc[df["Age"] > 35, "Name"]

    print(passenger)

    # I’m interested in rows 10 till 25 and columns 3 to 5.
    passenger = df.iloc[9:25, 2:5]
    print(passenger)


if __name__ == "__main__":
    main()