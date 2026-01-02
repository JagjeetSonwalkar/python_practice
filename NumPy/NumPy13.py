# Stacking array

import numpy as np

def main():
    # Row-->
    a = np.r_[1:4, 0,10,60]
    '''
    1:4 → generates 1, 2, 3
    0 → added as-is
    10 → added as-is
    60 → added as-is
    All combined into one 1D array
    '''

    print(f"Noraml Array using np.r_[]: {a}")

    # np.r_ with arrays (like vstack)
    a = np.arange(1,5)
    b = np.arange(5,10)

    x = np.r_[a,b]
    print(f"np.r_ with arrays (like vstack): {x}")

    # np.r_ with arrays (like vstack) --> If arrays are 2D:
    a = np.array([[1, 2], [1, 3]])
    b = np.array([[3, 4], [1, 3]])
    x = np.r_[a,b]

    print(f"np.r_ with arrays (like vstack):\n{x}")

    # Col-->
    a = np.c_[1:4, 3:6, 6:9]
    print(f"Noraml Array using np.c_[]:\n{a}")

if __name__ == "__main__":
    main()