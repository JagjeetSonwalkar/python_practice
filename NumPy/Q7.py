# Split [1,2,3,4,5,6] into 3 equal parts.
# Compute sum of each row in [[1,2],[3,4]].
# Compute column-wise mean.

import numpy as np

def main():
    arr = np.array([1,2,3,4,5,6])

    # Split [1,2,3,4,5,6] into 3 equal parts.
    result = arr.reshape(3,2)

    print(f"Split [1,2,3,4,5,6] into 3 equal parts is:\n{result}")

    # Compute sum of each row in [[1,2],[3,4]].
    arr = np.array([[1,2],[3,4]])
    result = []
    for row in arr:
        result.append(row.sum())
    print("Sum of rows: ", np.array(result))

    # Compute column-wise mean.
    arr = np.array([[1,2],[3,4]])
    result = []
    for col in np.vstack(arr):
        result.append(col.min())
    print(f"column-wise mean is {np.array(result)}")

if __name__ == "__main__":
    main()