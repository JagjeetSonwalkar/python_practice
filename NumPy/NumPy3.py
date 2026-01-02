# Array creation

import numpy as np

def main():
    # 1. By using a python list or tuple
    a = np.array([1,2,3,4,2,3,4]) # or a = np.array((1,2,3,4,2,3,4))
    print(f"Array using list: {a}")

    # 2. Creating 2D & 3D Array
    b = np.array([(1,2,3,4), (5,6,7,8)]) # 2D
    print(f"\n2D Array:\n{a}") 

    c = np.array([(1,2,3), (4,5,6.5), (3, 3, None) ]) # 3D
    print(f"\n3D Array:\n{c}")

    # 3. Specify data type manually
    d = np.array([[1,2,3], [4,5,6]], dtype=np.complex64)
    print(f"\nSpecfic datatype Array:\n{d}")

    # 4. Creating arrays with known size but unknown values
    a = np.zeros((3, 4))    # zeros() → all values are 0
    print(f"\ncreated a array with all values '0' of dimension 3,4:\n{a}")

    a = np.ones((3,4,5), dtype = np.int16)  # ones() → all values are 1
    print(f"\ncreated a array with all values '1' of dimension 3,4,5:\n{a}")

    a = np.empty((2,4), dtype = np.int8) # empty() → random garbage values (fast, uninitialized)
    print(f"\ncreated a array with random values of dimension 2,4:\n{a}")

    # 5. Creating sequences of numbers - arange() → works like range()
    a = np.arange(10, 20, 1)
    print(f"\nArray of range:\n{a}")

    a = np.arange(10, 0, -0.5)
    print(f"\nArray of range:\n{a}")

    # 6. linspace() (BETTER for floats)
    a = np.linspace(0, 3, 9)
    print(f"\nusing linespace:\n{a}")

if __name__ == "__main__":
    main()