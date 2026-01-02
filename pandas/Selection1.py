# selection by column

import pandas as pd

def main():
    df = pd.read_csv("playPredictor.csv")

    #print the whether column only
    print(df["Whether"].to_string)

    #print the whether & Temperature column both
    print(df[["Whether", "Temperature"]].to_string)

    # <----------------- end of main ----------------->

if __name__ == "__main__":
    main()  