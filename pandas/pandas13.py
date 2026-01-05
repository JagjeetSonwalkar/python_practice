# I want to visually compare the No2 values measured in London versus Paris

import pandas as pd 
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("csv_files/air_quality.csv", index_col=0, parse_dates=True)

    print(df)

    df.plot.scatter(x = "station_london", y = "station_paris", alpha = 0.5)
    plt.show()

if __name__ == "__main__":
    main()