
from sklearn.datasets import load_iris

def main():
    dataset = load_iris()
    line = '-' * 45

    print(line)
    for i in range(len(dataset.target)):
        print("ID %d , Features %s, Label : %s"%(i, dataset.data[i], dataset.target[i]))
    print(line)

if __name__ == '__main__':
    main()