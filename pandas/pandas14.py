# Create a new column from an existing column

import pandas as pd 

def main():
    df = pd.read_csv("csv_files/air_quality.csv", index_col=0, parse_dates=True)

    print(df.head())

    # Create a new column from an existing column
    df["londom_mg_per_cubic"] = (
        df['station_london'] * 1.882
    )

    print(df.head())

    # I want to check the ratio of the values in Paris versus Antwerp and save the result in a new column.
    df["ratio_paris_antwerp"] = (
        df['station_paris'] / df['station_antwerp']
    )

    print(df.head())

    # I want to rename the data columns to the corresponding station identifiers used by OpenAQ.
    df = df.rename(
        columns =
        {
            "station_antwerp" : "Station_Antwerp",
            "station_paris" : "Station_paris"
        }
    )

    print(df.head())

    # coloumn name should be lower
    df = df.rename(columns=str.lower)

    print(df.head())


    


if __name__ == "__main__":
    main()