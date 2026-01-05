
import pandas as pd 
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("csv_files/air_quality.csv", index_col=0, parse_dates=True)

    print(df)

    # I want to plot only the columns of the data table with the data from Paris.
    df["station_paris"].plot()
    plt.show()


if __name__ == "__main__":
    main()