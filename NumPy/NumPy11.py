# Stacking array

import numpy as np

def main():
    a1 = np.array([(1,2), (2,3)])
    a2 = np.array([(100, 200), (200, 300)])

    print(f"Orignal stack:\n{a1}\n{a2}")

    # vstack() → stack vertically (row-wise)
    x = np.vstack((a1, a2))
    print(f"vstack()->\n{x}")

    # hstack() → stack horizontally (column-wise)
    x = np.hstack((a1, a2))
    print(f"hstack() →\n{x}")

    # column_stack() → stack as columns
    x = np.column_stack((a1, a2))
    print(f"column_stack() →\n{x}")


if __name__ == "__main__":
    main()