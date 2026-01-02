# check pandas version

import pandas as pd

def main():
    print("Current version of pandas: ")
    print(pd.__version__)
    print(help(pd))

if __name__ == "__main__":
    main()