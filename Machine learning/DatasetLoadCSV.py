# read a csv file

import pandas as pd

def main():
    data_frame = pd.read_csv("iris.csv")

    print(data_frame.head())

if __name__ == '__main__':
    main()

# python DatasetLoadCSV.py
# python DatasetLoadCSV.py < outputcsv