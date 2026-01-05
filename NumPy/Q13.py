import numpy as np

# 18. create a 5x5 matrix with values 1,2,3,4 just below the diagonal
size = 5
matrix = np.diag(np.arange(1,size), k=-1)
print(f"5x5 matrix with values 1,2,3,4,n of just below the  diagonal:\n{matrix}")

# 19. create a 8x8 matrix and fill it with a checkerboard pattern
size = 8
matrix = np.zeros((size,size), dtype = np.int16)

matrix[::2, 1::2] = 1
matrix[1::2, ::2] = 1
print(f"8x8 matrix and fill it with a checkerboard pattern:\n{matrix}")

# 20. consdier a (6,7,8) shape array, what is the index (x,y,z) of the 100th element
arr = np.arange(0,6*7*8).reshape((6,7,8))
result = np.unravel_index(99, (6,7,8))
print(f"a (6,7,8) shape array, what is the index (x,y,z) of the 100th element is: {np.array(result)}")

# 21. create a checkboard of 8x8 matrix using the tile function
checkboard = np.tile(np.array([[0,1],[1,0]]), (4,4))
print(f"A checkboard of 8x8 matrix using the tile function:\n{checkboard}")

# 22. Normalize a 5x5 random matrix 
random_matrix = np.random.randint(0,10 ,(5,5))
normalize = (random_matrix - np.mean(random_matrix)) / np.std(random_matrix)

print(f"the matrix of 5x5 is:\n{random_matrix} & its normalize is:\n{normalize}")

# 24. multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
mat1 = np.arange(0, 5*3).reshape(5,3)
mat2 = np.arange(0, 3*2).reshape(3,2)
matrix_product = np.dot(mat1, mat2)
print(f"real matrix product:\n{matrix_product}")

# 25. given 1D array, negate all elements which are between 3 and 8, in place
arr = np.random.randint(0, 10, (10))
print(f"The array: {arr}")
arr = np.where((arr >= 3) & (arr <= 8), arr.__neg__(), arr) 
print(f"negate all elements which are between 3 and 8, in place: {arr}")

# 26. how to find common values between 2 arrays
arr1 = np.arange(0, 10)
arr2 = np.arange(5, 10)
common_value = np.intersect1d(arr1, arr2)
print(f"The common values from the array'{arr1,arr2}' is: {common_value}")

# 27. how to igonre all numpy warning (not recommended)
default = np.seterr(all="ignore")
z = np.ones(1) / 0

# how to get the dates of yesterday, today & tomorrow 
today = np.datetime64('today')
tomorrow = today - np.timedelta64(1, 'D')
yesterday = today + np.timedelta64(1, 'D')

print(f"yesterday: {yesterday}, today: {today}, tomorrow: {tomorrow}")