# Broadcasting

import numpy as np

def main():
    a = np.array([1,2,3])

    print(f"The orignal array: {a}")
   
    # Scalar + Array
    a = a + 10
    print(f"Scalar + Array: {a}")

    # Row vector + Matrix
    A = np.array([[1, 2, 3],[4, 5, 6]])
    B = np.array([10, 20, 30])
    result = A + B
    print(f"The result of row vector + matrix:\n{result}")

    # Column vector
    C = np.array([[1],
              [2],
              [3]])

    D = np.array([10, 20, 30])
    result = C + D

    print(f"The result of coloum vector is:\n{result}")

    # Broadcasting fails
    A = np.array((3, 4))
    B = np.array((2, 4))
    A + B   # Error 
    # First dimension: 3 ≠ 2

if __name__ == "__main__":
    main()