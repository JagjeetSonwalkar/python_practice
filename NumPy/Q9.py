# Compute moving average of website trafficInput: [100, 150, 200, 250], window 2 Output: [125, 175, 225]
# Find correlation between two products’ sales Input: productA = [100,200,150], productB = [120,210,160] Output: Correlation coefficient 0.998
# Split [1,2,3,4,5,6] into 3 equal parts.
# Compute sum of each row in [[1,2],[3,4]].
# Compute mean of each column.
# Find the difference between consecutive elements. [10,15,20]
# Repeat each element twice. Input: [1,2,3]



def moving_avg(arr, k = 2):
    avg_list = []

    for i in range(len(arr)-k+1):
        window = arr[i:i+k]
        avg_window = sum(window) / k
        avg_list.append(avg_window)
    return np.array(avg_list, dtype = np.int16)
        

import numpy as np

def main():
    # Compute moving average of website traffic
    arr = np.array([100, 150, 200, 250])
    result = moving_avg(arr)
    print(result)

    # Find correlation between two products’ sales
    arr = np.array([100, 200, 150])
    brr = np.array([120, 210, 160])

    result = np.correlate(arr, brr)
    print(result)

    # Split [1,2,3,4,5,6] into 3 equal parts.
    arr = np.array([1,2,3,4,5,6])
    result = np.split(arr, 3)

    print(f"Split [1,2,3,4,5,6] into 3 equal parts: {np.array(result)}")

    # Compute sum of each row in [[1,2],[3,4]]
    arr = np.array([[1,2],[3,4]])
    result = []
    for row in arr:
        result.append(sum(row))
    result = np.array(result)
    print(f"Compute sum of each row in [[1,2],[3,4]]: {result}")

    # Compute mean of each column.
    arr = np.array([[1,2],[3,4]])
    result = []
    for col in arr.T:
        result.append(np.mean(col))
    print(f"Compute mean of each column: {np.array(result)}")

    # Clip values of [1,5,10] between 2 and 8.
    arr = np.array([1,5,10])
    result = np.clip(arr,2,8)
    print(f"Clip values of [1,5,10] between 2 and 8.: {result}")

    # Find the difference between consecutive elements.
    arr = np.array([10,15,20])
    result = []
    for i in range(len(arr)-1):
        value = arr[i] - arr[i+1]
        if value < 0:
            value = -value
        result.append(value)
    print(f"Find the difference between consecutive elements: {np.array(result)}")

    # Repeat each element twice. Input: [1,2,3]
    arr = np.array([1,2,3])
    result = np.repeat(arr, 2)
    print(f"Repeat each element twice: {result}")

    # Tile [1,2] three times
    arr = np.arange(1,3)
    result = np.tile(arr,3)
    print(f"Tile [1,2] three times: {result}")

    # Check if [1,2,3] and [1,2,3] are equal.
    arr = np.arange(1,4)
    brr = np.arange(1,4)
    print(arr,"\t",brr)
    result = np.all(arr == brr)
    print(f"check equality: {result}")



if __name__ == "__main__":
    main()