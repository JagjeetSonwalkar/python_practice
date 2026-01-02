# Shape

import numpy as np

def main():
    a = np.array([(2,3,4), (5,6,7)])

    print(f"The orginal array:\n{a}")

    print(f"Shape of a is: {a.shape}")

    # ravel()
    print(f"The array is:{a.ravel()}")

    # reshape the array
    print(f"Now the shape of array is:\n{a.reshape(3,2)}")

    # T-transpose
    print(f"now using T-transpose:\n{a.T}")

    # resize the array
    a.resize(4,3)
    print(f"Now the array is:\n{a}")

    # reshape using -1
    a.reshape(3, -1)
    print(f"Now the array is:\n{a}")


if __name__ == "__main__":
    main()