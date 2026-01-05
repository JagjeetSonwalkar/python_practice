import numpy as np

# 35. How to compute ((A+B)*(-A/2)) in place (without copy)
A = np.array([1,2,3,4])
B = np.array([1,1,1,1])
result = (np.add(A,B)) * (np.divide(-A,2))

print(f"compute ((A+B)*(-A/2)): {result}")

# 36. Extract the integer part of a random array of positive numbers using 4 different methods
arr = np.random.random(10)*5
print(f"\nExtract the integer part of a random array of positive numbers using 4 different methods:\n{arr}")
print(f"""1. {arr//1}
2. {np.floor(arr)}
3. {np.ceil(arr)-1}
4. {np.trunc(arr)}
""")

# 37. create a 5x5 matrix with row values ranging from 0 to 4
row = np.arange(5, dtype = np.int16)
matrix = np.repeat(row, 5).reshape(5,5).T
print(f"5x5 matrix with row values ranging from 0 to 4:\n{matrix}") 

# 38. consider a generator function that generate 10 integers and use it to build an array
def generator():
    for x in range(10):
        yield x
arr = np.fromiter(generator(), dtype = int)
print(f"A generator function that generate 10 integers: {arr}")

# 39. create a vector of size 10 with values ranging from 0 to 1, both excluded
arr = np.linspace(0.1, 0.9,10, endpoint=False)
print(f"vector of size 10 with values ranging from 0 to 1: {arr}")

# 40. create a random array of size 10 and sort it
arr = np.random.randint(0,50, 10)
print(f"The array with sort is: {np.sort(arr)}")

# 41. how to sum a small array faster than np.sum
arr = np.array([10,20,30,40])
sum = np.add.reduce(arr)
print(f"Sum of arr: {sum}")

# 42. consider two random array A and B, check if they are equal.
A = np.random.random(10)
B = np.random.random(10)
check = np.array_equal(A,B)
print(f"Both are equal: {check}")

# 43. make an array immutable (read only)
immutable_arr = np.array([1,2,3,4,5])
immutable_arr.flags.writeable = False
# immutable_arr[0] = 10 # ERROR