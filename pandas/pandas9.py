# I’m interested in the passengers older than 35 years.
# I’m interested in the Titanic passengers from cabin class 2 and 3.

import pandas as pd

def main():
    df = pd.read_csv("csv_files/titanic.csv")

    # I’m interested in the passengers older than 35 years.
    old_passenger = df[df["Age"] > 35]

    print(old_passenger)
    
    result = df["Age"] > 35
    print(result)

    # I’m interested in the Titanic passengers from cabin class 2 and 3.
    passenger_class_2_3 = df[df["Pclass"].isin([2,3])]
    print(passenger_class_2_3)

    # I want to work with passenger data for which the age is known.
    known_age_passenger = df[df['Age'].notna()]
    print(known_age_passenger)

if __name__ == "__main__":
    main()