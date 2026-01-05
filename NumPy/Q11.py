

# 1. import the numpy package under the name np
import numpy as np

# 2. print the numpy version and the configuration
print(f"current downladed version of numpy is:{np.__version__} & the configuration: {np.show_config()}")

# 3. create a null vector of size 10
null_vector = np.zeros(10)
print("Null vector:",null_vector)

# 4. find th e memory size of array
null_vector.size * null_vector.itemsize # memory size of just the array
null_vector.__sizeof__() # total memeory[array setup + array]
print(f"memory size of just the array: {null_vector.size * null_vector.itemsize} & total memeory[array setup + array]: {null_vector.__sizeof__()}")

# 5. how to get the documentation of numpy add function from the command line
documentation = np.info(np.add)
print(f"The documention of add is: {documentation}")

# 6. create a null vector of size 10 but the fifth value which is 1
null_vector = np.zeros(10)
null_vector[4] = 1
print(f"The null vector is: {null_vector}")

# 7. create a vector with values ranging from 10 to 49
vector = np.arange(10, 50)
print(f"The vector is: {vector}")

# 8. reverse a vector (first element becomes the last)
reverse_vector = vector[::-1]
print(f"The reverse vector is: {reverse_vector}")

# 9. create a 3x3 matrix with values ranging from 0 to 8
matrix = np.arange(0,9).reshape((3,3))
print(f"The matrix is: {matrix}")

# 10. find the indices of non zeroes elements from [1,2,0,0,4,0]
arr = np.array([1,2,0,0,4,0])
index = np.where(arr != 0)
print(f"The non zero element index is: {index}")

# 11. create a 3x3 identity matrix
identity_matrix = np.eye(3,3)
print(f"The matrix is: {identity_matrix}")