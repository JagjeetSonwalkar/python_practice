''' I want to store passenger data of the Titanic. For a number of passengers, 
 I know the name (characters), age (integers) and sex (male/female) data. '''

import pandas as pd

def main():
    df = pd.DataFrame(
        {
            "Name":["Rohit", "pooja", "Virat"],
            "Age": [45, 25, 81],
            "Gender": ["male", "female", "male"]
        }
    )

    print(df)

    # I'm just interested in working with the data in the column Age
    age_coloum = df["Age"]

    print(age_coloum)

if __name__ == "__main__":
    main()