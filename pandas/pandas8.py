# select specific columns from a DataFrame & I’m interested in the age and sex of the Titanic passengers.

import pandas as pd

def main():
    df = pd.read_csv("csv_files/titanic.csv")

    age_sex_col = df[['Age', 'Sex']]

    print(age_sex_col)

    # data type of age_sex_col
    print(f"The data type of age & sex column is: {type(age_sex_col)}")

    # shape
    print(f"The shape of age sex column is: {age_sex_col.shape}")

if __name__ == "__main__":
    main()