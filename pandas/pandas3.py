# You can create a Series from scratch as well:

import pandas as pd 

def main():
    ages = pd.Series([10, 15, 18, 45], name="Age")

    print(ages)

if __name__ == "__main__":
    main()