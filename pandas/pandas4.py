# I want to know the maximum Age of the passengers
# We can do this on the DataFrame by selecting the Age column and applying max():

import pandas as pd 

def main():
    ages = pd.Series([10, 15, 18, 45], name="Age")

    max_age = ages.max()
    print("The max age is:",max_age)

    x = ages.describe()
    
    print(x)

if __name__ == "__main__":
    main()