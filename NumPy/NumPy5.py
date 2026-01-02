# Basic operations

import numpy as np

def main():
    a = np.array([(10, 20), (30, 40)])
    b = np.ones([2,2], dtype=np.int64)

    print(f"a:{a}\nb:{b}")

    result = a + b
    print(f"\nResult of a + b: {result}")

    result = b - a
    print(f"\nResult of b - a: {result}")

    result = a * b
    print(f"\nResult of a*b is: {result}")

    result = a > 15
    print(f"\nResult of a>15 is: {result}")

    result = a ** 2
    print(f"\nResult of a**2 is: {result}")


if __name__ == "__main__":
    main()