# select specific columns from a DataFrame & I’m interested in the age of the Titanic passengers.

import pandas as pd

def main():
    df = pd.read_csv("csv_files/titanic.csv")

    age_series = df["Age"]
    print(age_series)

    # types of age_series 
    print(f"Type of age column is: {type(age_series)}")

    # shape of age_series
    print(f"The shape of age_series is: {age_series.shape}")

if __name__ == "__main__":
    main()