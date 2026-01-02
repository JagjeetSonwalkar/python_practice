# Stacking array

import numpy as np

def main():
    a = np.array([1,2,3,4])
    b = np.array([100, 200, 200, 300])

    print(f"Orignal stack:\n{a}\n{b}\n")

    # newaxis – convert 1D to 2D column
    x = a[:, np.newaxis]
    print(x)

    x = np.concatenate((a, b), axis=0)
    print(x,"\n")

    a = np.array([(1,2,3,4),(1,2,3,4)])
    b = np.array([(100, 200, 200, 300), (100, 200, 200, 300)])

    print(f"Orignal stack 2D:\n{a}\n{b}\n")
    
    x = np.concatenate((a, b), axis=1)
    print(x)


if __name__ == "__main__":
    main()