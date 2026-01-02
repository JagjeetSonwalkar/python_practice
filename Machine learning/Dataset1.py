
from sklearn.datasets import load_iris

def main():
    dataset = load_iris()

    print(f"Independent (Feature) variable names are: {dataset.feature_names}")
    print(f"Dependent (label) variable names are: {dataset.target_names}")

if __name__ == '__main__':
    main()