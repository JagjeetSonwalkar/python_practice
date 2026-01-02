# Replace values less than 5 with 0 in [2,6,3,8].
# Count non-zero values in [0,1,2,0,3].
# Compute cumulative sum.
# Extract unique elements from [1,2,2,3,3,3].

import numpy as np

def main():
    array = np.array([2,6,3,8])

    # Replace values less than 5 with 0 in [2,6,3,8]
    array[array < 5] = 0
    print(f"Replace values less than 5 with 0 in [2,6,3,8]:{array}")

    # Count non-zero values in [0,1,2,0,3].
    array = np.array([0,1,2,0,3])
    result = array[array != 0].size
    print(f"array: {array} ,The count of non zero values is: {result}")

    # Compute cumulative sum.
    array = np.arange(1,5)
    cum_sum = np.zeros_like(array)

    current_sum = 0
    for i in range(len(array)):
        current_sum += array[i]
        cum_sum[i] = current_sum
    print(f"The cumulative sum of array: {array} is {cum_sum}")

    # Extract unique elements from [1,2,2,3,3,3].
    arr = np.array([1,2,2,3,3,3])
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    result = np.array(result)
            
    print(f"Extract unique elements from [1,2,2,3,3,3] is {result}")



if __name__ == "__main__":
    main()