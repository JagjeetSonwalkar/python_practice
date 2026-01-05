import numpy as np


# 12. create a 3x3x3 array with random values
arr = np.random.random((3,3,3))
print(f"The 3x3x3 array is:\n{arr}")

# 13. create 10x10 array with random values and find max & min values
arr = np.random.randint(1, 51, (10,10))
print("the arr is:\n",arr)
print(f"The max is: {arr.max()} & The min is: {arr.min()}")

# 14. create a random vector of size 30 and find the mean value of each coloum
arr = np.random.rand(30).reshape((10, 3))
print(f"The arr is:\n{arr}")
print(f"The mean is: {arr.mean(axis = 0)}")

# 15. create a 2d array with borader 1 and inside 0
size = 5
one = np.ones((size, size))
zero = np.zeros((size-2, size-2))

one[1:one.shape[0]-1, 1:one.shape[1]-1] = zero
print(one)

print()
# 16. how to add a border (filled with 0's) around an existing array
size = 5
arr = np.ones((size,size))
arr[:, [0, -1]] = 0
arr[[0,-1], :] = 0
print(arr)
