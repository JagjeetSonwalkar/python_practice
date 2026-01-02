# Indexing, slicing and iterating - (1D array)

import numpy

def main():
    a = numpy.arange(1, 20)

    print(f"normal print: {a}")

    i = int(input("Enter the index to get element: "))
    print(f"The element at index '{i}' is {a[i]}") # Indexing

    print(f"The element from 5 to 10: {a[5:10]}") # Slicing (get a range)

    a[0: 3] = 100 # Slice + step + assignment
    print(f"new a after Slice + step + assignment: {a}")

    # Iterating (loop through elements)
    for i in a:
        print("Element:",i)


if __name__ == "__main__":
    main()