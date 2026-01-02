# Add two NumPy arrays ([1,2,3], [4,5,6])
# Multiply an array by a scalar. (Multiply array [2,4,6] by 3.)
# Find the sum of [1,2,3,4].
# Access the element at index 2 in array [5,10,15,20].

import numpy as np

def main():
    a = np.array([1,2,3])
    b = np.array([4,5,6])

    # Add two NumPy arrays 
    result = a + b
    print(f"Add two NumPy arrays: {result}")

    # Multiply an array by a scalar.
    a = np.array([2,4,6])
    result = a * 3
    print(f"Multiply an array by a scalar: {result}")

    # Find the sum of [1,2,3,4].
    a = np.array([1,2,3,4])
    print(f"sum of [1,2,3,4] is '{a.sum()}'")

    # Access the element at index 2 in array [5,10,15,20]
    a = np.array([5,10,15,20])
    print(f"Access the element at index 2 in array [5,10,15,20]: {a[2]}")
   

if __name__ == "__main__":
    main()