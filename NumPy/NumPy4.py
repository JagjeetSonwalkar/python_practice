# printing Array

import numpy as np
import sys

def main():
    a = np.arange(10, 51, 10) # 1D Array (Printed as a row)
    print(f"1D Array (Printed as a row)\n{a}")


    a = np.arange(10, 30, 1).reshape(4,5) # 2D Array (Printed as a matrix)
    print(f"\n2D Array (Printed as a matrix)\n{a}")

    a = np.arange(10, 50, 1).reshape(2,4,5) # 3D Array (Printed as a list of matrices)
    print(f"\n3D Array (Printed as a list of matrices):\n{a}")

    a = np.arange(1000000) # large array
    print(f"\nlarge range array:\n{a}")

    # Print the FULL array (disable hiding)
    np.set_printoptions(threshold=sys.maxsize) # Disable skipping of middle values
    a = np.arange(10000) # large array    
    print(f"\nlarge range array:\n{a}")
    


if __name__ == "__main__":
    main()