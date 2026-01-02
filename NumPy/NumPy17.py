# ix_()

import numpy as np

def main():
    a = np.array([2, 3])
    b = np.array([4, 5])
    c = np.array([10, 20])

    # We want to compute the result of this formula for all possible combinations: a + b * c

    # Apply ix_() to prepare combinations
    A, B, C = np.ix_(a, b, c)

    '''
    What happens here?
    A shape → (2, 1, 1)
    B shape → (1, 2, 1)
    C shape → (1, 1, 2)
    These shapes allow NumPy to broadcast automatically.
    '''
    
    result = A + B * C

    print(result)




if __name__ == "__main__":
    main()