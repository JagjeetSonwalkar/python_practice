# I’m interested in some basic statistics of the numerical data of my data table

import pandas as pd 

def main():
    ages = pd.Series([10, 15, 18, 45], name="Age")

    x = ages.describe()
    
    print(x)

if __name__ == "__main__":
    main()