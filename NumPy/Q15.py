import numpy as np

# 44. consider a random 10x2 matrix representing cartesian corrdinates, convert them to polar corrdinates
arr = np.random.randint(0,10,10*2).reshape(10,2)
print(f"The corrdinates:\n{arr}")

# 45. create a random vector of size 10 and replace the maximum values by 0
arr = np.random.randint(0,10, 10)
print("The array before replcae the max value by 0:",arr)
arr = np.where(arr == arr.max(), 0, arr)
print("The array after replcae the max value by 0:",arr)



np.meshgrid()
