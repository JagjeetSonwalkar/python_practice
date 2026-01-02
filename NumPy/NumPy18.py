# Depth Stacking — dstack()

import numpy as np

if __name__ == "__main__":
    x = np.arange(0, 10, 2)
    y = np.arange(5)

    print("x:",x)
    print("y:",y)

    result = np.dstack([x,y])

    print(result)
