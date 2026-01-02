
import numpy as np
import matplotlib.pyplot as plt

# Create some simple data
data = [10, 12, 13, 15, 16, 18, 20, 20, 22, 25]

# Create a histogram using Matplotlib
plt.hist(data, bins=5)
plt.show()