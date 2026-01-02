import pandas as pd

def main():
    dataframe = pd.read_csv("iris.csv")

    print("Data set loaded successfully")
    print(f"Dimension of data set is: {dataframe.shape}")

    print(dataframe["variety"])
    # print(dataframe["sepal.length"].head())

    dataframe["variety"] = dataframe["variety"].map({"Setosa":0, "Versicolor":1, "Virginica":2}) # encoding
    print(dataframe["variety"])

    X = dataframe.drop("variety", axis="columns")
    Y = dataframe["variety"]

    print(f"Independent variables dimension : {X.shape}")
    print(f"Dependent variables dimension : {Y.shape}")

# -------------- end of main ------------ #

if __name__ == '__main__':
    main()