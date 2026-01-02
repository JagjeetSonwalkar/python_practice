import numpy as np

colors = np.array([1, 2, 3])  # 1=Red, 2=Blue, 3=Green
sizes  = np.array([7, 8])

# Make all combinations
c_idx, s_idx = np.ix_(colors, sizes)

# Show result
print(c_idx * s_idx)
# Output:
# [[ 7  8]
#  [14 16]
#  [21 24]]
