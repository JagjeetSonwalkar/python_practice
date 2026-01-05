# What is the average age for male versus female Titanic passengers?

import pandas as pd

def main():
    df = pd.read_csv("csv_files/titanic.csv")

    print(df.head())

    avg_age = df[["Sex","Age"]].groupby("Sex").mean()

    print(f"The avg age is:\n{avg_age}")

if __name__ == "__main__":
    main()