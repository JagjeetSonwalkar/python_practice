# Split

import numpy as np

def main():
    # Case 1: Split into equal parts
    a = np.array([
    [6, 7, 6, 9, 0, 5, 4, 0, 6, 8, 5, 2],
    [8, 5, 5, 7, 1, 8, 6, 7, 1, 8, 1, 0]
    ])

    x = np.hsplit(a, 3)
    print(x)

    # Case 2: np.vsplit() – split vertically (rows)
    b = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
    ])

    x = np.vsplit(b, 2)
    print(x)

    # np.array_split() – flexible splitting
    a = np.array([
    [6, 7, 6, 9, 0, 5, 4, 0, 6, 8, 5, 2],
    [8, 5, 5, 7, 1, 8, 6, 7, 1, 8, 1, 0]
    ])

    x = np.array_split(a, 5, axis=1)
    print(x)


if __name__ == "__main__":
    main()