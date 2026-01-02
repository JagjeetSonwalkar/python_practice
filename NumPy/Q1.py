# Create a NumPy array from a Python list.
# Create a NumPy array of zeros.
# Create a 2×3 NumPy array filled with ones.
# Find the shape of a NumPy array
# Get the data type of array elements
# Create an array using arange. (Generate numbers from 0 to 9 using NumPy.)

import numpy as np

def main():
    # Create a NumPy array from a Python list.
    list = [1, 2, 3, 4, 5, 6, 7]
    array = np.array(list)

    print(f"Type of array is {type(array)} & Array is: {array}")

    # Create a NumPy array of zeros.
    array = np.zeros((5), dtype = np.int32)
    print(f"NumPy array of zeros: {array}")

    # Create a 2×3 NumPy array filled with ones.
    array = np.ones((2, 3), dtype = np.int32)
    print(f"Array of 2x3 NumPy array filled with ones:\n{array}")

    # Find the shape of a NumPy array
    array = np.array([[1,2,3],[4,5,6]])
    print(f"the shape of a NumPy array: {array.shape}")

    # Get the data type of array elements
    array = np.array([10, 20, 30])
    print(f"data type of array elements: {array} is: {array.dtype}")

    # Generate numbers from 0 to 9 using NumPy.
    array = np.arange(0, 9+1)
    print(f"The array of Generate numbers from 0 to 9: {array}")

    

if __name__ == "__main__":
    main()