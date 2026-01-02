# Compute moving average of website trafficInput: [100, 150, 200, 250], window 2 Output: [125, 175, 225]
# Find correlation between two products’ sales Input: productA = [100,200,150], productB = [120,210,160] Output: Correlation coefficient 0.998

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




if __name__ == "__main__":
    main()