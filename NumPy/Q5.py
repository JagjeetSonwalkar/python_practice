# Stack [1,2] and [3,4] vertically
# Stack [1,2] and [3,4] horizontally
# Sort [5,2,8,1].
# Generate 5 random numbers between 0 and 1.

import numpy as np

def main():
    array = np.array([[1,2],[3,4]])

    print(f"the orignal array:\n{array}")

    # Stack [1,2] and [3,4] vertically
    print(f"Stack [1,2] and [3,4] vertically:\n{np.vstack(array)}")

    # Stack [1,2] and [3,4] horizontally
    print(f"Stack [1,2] and [3,4] horizontally:\n{np.hstack(array)}")

    # Sort [5,2,8,1].
    array = np.array([5,2,8,1])
    print(f"Sort [5,2,8,1]: {np.sort(array)}")

    # Generate 5 random numbers between 0 and 1.
    array = np.linspace(0,1,5)
    print(f"Generate 5 random numbers between 0 and 1: {array}")

if __name__ == "__main__":
    main()