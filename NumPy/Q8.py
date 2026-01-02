# Calculate average temperature from sensor data
# Find minimum and maximum stock prices [120, 150, 130, 160]
# Generate a sequence of days in a month Number of days 30
# Check which sales exceed target using boolean mask Input: [100, 200, 150, 50], target 150
# Reshape a flat array of 12 hourly readings into 3x4 (3 days, 4 readings/day) Input: [10, 12, 14, 16, 11, 13, 15, 17, 10, 12, 14, 16]
# Normalize customer purchase amounts between 0 and 1 Input: [100, 200, 300] Output: [0, 0.5, 1]
# Compute moving average of website trafficInput: [100, 150, 200, 250], window 2 Output: [125, 175, 225]


import numpy as np

def main():
    # Calculate average temperature from sensor data [22.5, 23.0, 21.8, 22.9]
    arr = np.array([22.5, 23.0, 21.8, 22.9])
    print(f"The average temperature is: {np.average(arr).round(2)}")

    # Find minimum and maximum stock prices [120, 150, 130, 160]
    arr = np.array([120, 150, 130, 160])
    print(f"The max stock price is {arr.max()} & the min {arr.min()}")

    # Generate a sequence of days in a month Number of days 30
    arr = np.arange(1, 31)
    print(f"Generate a sequence of days in a month Number of days 30: {arr}")

    # Check which sales exceed target using boolean mask
    arr = np.array([100, 200, 150, 50])
    target = 150
    result = np.array(arr == target)
    print(f"Check which sales exceed target using boolean mask: {result}")
    
    # Reshape a flat array of 12 hourly readings into 3x4 (3 days, 4 readings/day)
    arr = np.array([10, 12, 14, 16, 11, 13, 15, 17, 10, 12, 14, 16])
    result = arr.reshape(3,4)
    print(f"Reshape a flat array of 12 hourly readings into 3x4:\n{result}")

    # Normalize customer purchase amounts between 0 and 1
    purchase_amount = np.array([100, 200, 300])
    normalize = (purchase_amount - purchase_amount.min()) / (purchase_amount.max() - purchase_amount.min())
    print(f"Normalize customer purchase amounts between 0 and 1: {normalize}")

    # Compute moving average of website traffic
    arr = np.array([100, 150, 200, 250])
    window = 2
    sum = 0
    result = []
    for i in range(len(arr)):
        sum += arr[i]
        for j in range(window-1):
            if j >= window - 1:
                break
            sum += arr[i+1] 
        result.append(sum)
        

    print(result)





if __name__ == "__main__":
    main()