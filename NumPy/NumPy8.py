# Indexing, slicing and iterating - (2D array)

import numpy as np

def main():
    a = np.fromfunction(lambda x, y: 10*x + y, (5, 4), dtype = int)

    print(f"Noraml display:\n{a}\n")

    # ascess single element
    print(f"The element is: {a[4,3]}")

    # get first full column
    print(f"The first full column:\n{a[:,0]}")

    # get first full row
    print(f"The first row:\n{a[0, :]}")

    # using loop
    print("\nUsing loop: ")
    for i in a:
        if len(i) > 1:
            for j in i:
                print(j)
        else:
            print(i)


if __name__ == "__main__":
    main()