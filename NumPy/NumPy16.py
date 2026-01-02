# Advanced Indexing

import numpy as np

def main():
    a = np.arange(12)**2
    i = np.array([1, 1, 3, 8, 5])

    print(f"The original array is: {a}")

    # Indexing with Integer Arrays
    print(f"The elements present on index i are: {a[i]}")

    # Multidimensional Index Arrays
    j = np.array([[3,4],
                [9,7]])
    
    print("The element of a[j] is:\n",a[j])



if __name__ == "__main__":
    main()