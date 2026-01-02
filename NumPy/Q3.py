# Reshape array [1,2,3,4,5,6] into a 2×3 matrix.
# Create a 3×3 identity matrix
# Find the maximum element in [10,25,5,40].
# Find the index of the maximum element. ([10,25,5,40])
# Perform element-wise multiplication : Multiply [1,2,3] and [4,5,6].
# Boolean masking: Extract elements greater than 5 from [2,6,8,3,10].

import numpy as np

def main():
    array = np.array([1,2,3,4,5,6])

    # Reshape array [1,2,3,4,5,6] into a 2×3 matrix.
    print(f"Reshape array [1,2,3,4,5,6] into a 2x3 matrix:\n{array.reshape((2,3))}")

    # Create a 3×3 identity matrix
    array = np.identity(3, dtype=np.int32)
    print(f"Create a 3x3 identity matrix:\n{array}")

    # Find the maximum element in [10,25,5,40].
    array = np.array([10,25,5,40])
    print(f"{array.max()} is the maximum element in [10,25,5,40].")

    # Find the index of the maximum element.
    array = np.array([10,25,5,40])
    result = np.where(array == np.max(array))           # array.argmax()
    print(f"'{result}' is the index of the maximum element [10,25,5,40]")

    # Multiply [1,2,3] and [4,5,6]
    a = np.array([1,2,3])
    b = np.array([4,5,6])
    result = a * b
    print(f"Perform element-wise multiplication: {result}")

    # Extract elements greater than 5 from [2,6,8,3,10].
    array = np.array([2,6,8,3,10])
    result = np.array(array > 5)
    print(f"Extract elements greater than 5 from [2,6,8,3,10] are: {result}")
    
   

if __name__ == "__main__":
    main()