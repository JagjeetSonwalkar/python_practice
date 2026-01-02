# selection by row

import pandas as pd 

def main():
    df = pd.read_csv("PlayPredictor.csv", index_col="Whether")

    print(df.loc["Sunny"])




if __name__ == "__main__":
    main()