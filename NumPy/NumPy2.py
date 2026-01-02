# Important Attributes of a NumPy Array (ndarray)

import numpy as np

def main():
    # Create a 3x5 array with numbers from 0 to 14
    a = np.arange(15).reshape(3, 5)
    
    print("This is the numpy array: ")
    print(a)

    print("\nNumber of dimensions:", a.ndim) 

    print("\nShape of array:",a.shape)

    print("\nsize of array:",a.size)

    print("\nData type of the element:",a.dtype.name)

    print("\nSize(in bytes) of each element",a.itemsize)
    

if __name__ == "__main__":
    main()