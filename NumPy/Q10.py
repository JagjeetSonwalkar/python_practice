# Find indices where value > 5. Input: [3,7,2,9]
# Reverse [1,2,3,4].
# Normalize [10,20,30] to range 0–1.
# Compute covariance of a 2D dataset. Input: [[2,4,6],[1,3,5]]
# Solve Ax = B. Input: A=[[3,1],[1,2]], B=[9,8]

import numpy as np

def main():
    # Find indices where value > 5. Input: [3,7,2,9]
    arr = np.array([3,7,2,9])
    result = np.where(arr > 5)

    print(f"indices where value > 5: {result}")

    # Reverse [1,2,3,4].
    arr = np.array([1,2,3,4])
    print(f"Reverse [1,2,3,4]: {arr[::-1]}")

    # Normalize [10,20,30] to range 0–1.
    arr = np.array([10,20,30])
    result = (arr - min(arr)) / (max(arr) - min(arr))
    print(f"Normalize [10,20,30] to range 0-1: {result}")

    # Compute covariance of a 2D dataset.
    arr = np.array([[2,4,6],[1,3,5]])
    result = np.cov(arr)
    print(result)

    # Solve Ax = B. Input: A=[[3,1],[1,2]], B=[9,8]
    A = np.array([[3,1],[1,2]])
    B = np.array([9,8])
    result = np.linalg.inv(A).dot(B)
    print(f"Solve Ax = B. Input: A=[[3,1],[1,2]], B=[9,8]: {result}")

    



if __name__ == "__main__":
    main()