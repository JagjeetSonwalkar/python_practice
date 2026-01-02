# Indexing, slicing and iterating - (3D array)

import numpy as np

def main():
    a = np.fromfunction(lambda x, y,z: 10*x + y + z, (3, 4, 6), dtype = int)

    print(f"Noraml display:\n{a}\n")

    # INDEXING 
    value = a[2,0, 3]
    print("The value is:",value)

    for i in a.flat:
        print("Element:",i)


if __name__ == "__main__":
    main()