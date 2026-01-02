import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    dataframe = pd.read_csv("iris.csv")

    print("Data set loaded successfully")

    print(dataframe["variety"])

    dataframe["variety"] = dataframe["variety"].map({"Setosa":0, "Versicolor":1, "Virginica":2}) # encoding
    print(dataframe["variety"])

    X = dataframe.drop("variety", axis="columns")
    Y = dataframe["variety"]

    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

    print(f"Dimension of x_train : {x_train.shape}")
    print(f"Dimesion of x_test : {x_test.shape}")
    print(f"Dimesion of y_train : {y_train.shape}")
    print(f"Dimesion of y_test : {y_test.shape}")

# -------------- end of main ------------ #

if __name__ == '__main__':
    main()