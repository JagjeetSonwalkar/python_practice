# Basic operations

import numpy as np

def main():
    a = np.array([(10, 20), (30, 40)])
    b = np.ones([2,2], dtype=np.int64)

    print(f"a:{a}\nb:{b}\n")

    result = a.min()
    print(f"min of a & b is: {result}")

    result = a.max()
    print(f"max of a & b is: {result}")

    result = a @ b
    print(f"\nResult of a@b: {result}")

    result = a.dot(b)
    print(f"\nResult of a.dot(b): {result}")

    # Note: A.dot(B) = A @ B
    a += 2
    print(f"\nresult of a+=2: {a}")
    

if __name__ == "__main__":
    main()