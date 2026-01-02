# Series

import pandas as pd

def main():
    series = pd.Series([101, 102, 103, 200, 202], index = ['a', 'b', 'c', 'd', 'e']) 

    print("Orignal Series:\n",series)

    # print series which elements are >= 200
    print(f"The elements are greter or equals to 200 \n{series[series >= 200]}")

    # series using dict
    calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}
    series = pd.Series(calories)
    print(f"Series:\n{series}")

    series.loc["Day 1"] += 300

    print(f"Calories burn on day1 {series.loc["Day 1"]}")

if __name__ == "__main__":
    main()