import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_path):
    df = pd.read_csv(file_path)
    print("Data set gets loaded in memory sucessfully")
    return df

def get_information(df):
    print("information about the loaded dataset is: ")
    print("Shape of dataset: ",df.shape)
    print("Columns: ",df.columns)
    print("Missing values: ",df.isnull().sum())

def encode_data(df):
    df["variety"] = df["variety"].map({"Setosa": 0, "Versicolor": 1, "Virginica": 2})
    return df

def split_feature_target(df):
    x = df.drop("variety", axis = 1)
    y = df["variety"]
    return x,y

def split(X,Y,size=0.2):
    return train_test_split(X,Y,test_size=size)

def main():
    data = load_data("iris.csv")
    print(data.head())

    get_information(data)

    print("Data after encoding: ")
    data = encode_data(data)
    print(data.head())

    print("Splitting feature & labels")
    independent, dependent = split_feature_target(data)
    print(independent.head())
    print(dependent.head())

    x_train, x_test, y_train, y_test = split(independent, dependent, 0.3)
    print(x_train.shape)
    print(x_test.shape)
    print(y_train.shape)
    print(y_test.shape)

if __name__ == "__main__":
    main()