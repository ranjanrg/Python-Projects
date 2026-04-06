import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

newarr1 = arr.reshape(2, 3, 2)

print(newarr)
print(newarr1)
print(newarr1.ndim)

# Try converting 1D array with 8 elements to a 2D array with 3 elements in each dimension (will raise an error):

arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr3 = arr2.reshape(2, 2, -1)

print(newarr3)

# Convert the array into a 1D array:

arr3 = np.array([[1, 2, 3], [4, 5, 6]])

newarr2 = arr3.reshape(-1)

print(newarr2)