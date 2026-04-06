import numpy as np

arr = np.array([[1, 2, 3, 4, 5 ] ,[6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])

print(arr.shape)

# Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:

arr1 = np.array([1, 2, 3, 4], ndmin= 5 )
print(arr1)
print(arr1.shape)