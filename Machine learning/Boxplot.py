import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def main():
    df = pd.read_csv("iris.csv")

    sb.boxplot(x = "variety", y = "petal.length", data = df)

    plt.title("Jaggi Histogram for IRIS")

    plt.show()

if __name__ == "__main__":
    main()              