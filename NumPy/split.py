import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)

# Split the array in 4 parts

arr1 = np.array([1, 2, 3, 4, 5, 6])

newarr1 = np.array_split(arr1, 4)

print(newarr1[0])
print(newarr1[1])
print(newarr1[2])

# splitiing the 2-D array

arr2 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr2 = np.array_split(arr2, 3)

print(newarr2)

arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr3 = np.array_split(arr3, 3, axis=1)

print(newarr3)

