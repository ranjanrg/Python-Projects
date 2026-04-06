import numpy as np

arr = np.array([1, 2, 3, 4, 4, 5, 4])

x = np.where(arr%2 == 0)

print(x)

# Find the indexes where the value 7 should be inserted:

arr1 = np.array([1, 2, 3, 4, 5])

y = np.searchsorted(arr1, 2, side= "right")

print(y)

#Find the indexes where the values 2, 4, and 6 should be inserted:

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)