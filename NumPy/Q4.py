# Find the mean of [10,20,30,40]
# Find the standard deviation of [2,4,6,8]
# Add two 2×2 matrices : [[1,2],[3,4]], [[5,6],[7,8]]
# Multiply two matrices using dot product.
# Transpose a 2×3 matrix. [[1,2,3],[4,5,6]]
# Convert a 2D array into 1D.

import numpy as np

def main():
    array = np.array([10,20,30,40])

    # Find the mean of [10,20,30,40]
    print(f"'{array.mean()}' is the mean of [10,20,30,40]")

    # Find the standard deviation of [2,4,6,8]
    array = np.array([2, 4, 6, 8])
    print(f"{array.std()} is the standard deviation of [2,4,6,8]")

    # Add two 2×2 matrices
    a = np.array([[1,2],[3,4]])
    b = np.array([[5,6],[7,8]])
    result = a + b
    print(f"Add two 2x2 matrices:\n{result}")

    # Multiply two matrices using dot product: [[1,2],[3,4]], [[2,0],[1,2]]
    a = np.array([[1,2],[3,4]])
    b = np.array([[2,0],[1,2]])
    result = np.dot(a,b)
    print(f"Multiply two matrices using dot product [[1,2],[3,4]] & [[2,0],[1,2]]:\n{result}")

    # Transpose a 2×3 matrix. [[1,2,3],[4,5,6]]
    array = np.array([[1,2,3],[4,5,6]])
    result = np.column_stack(array)
    print(f"Transpose a 2x3 matrix. [[1,2,3],[4,5,6]]:\n{result}")

    # Convert a 2D array into 1D.
    array = np.array([[1,2],[3,4]])
    print(f"Converting this 2D array:\n{array}\nINTO 1D Array:\n{array.flatten()}")

    
   

if __name__ == "__main__":
    main()