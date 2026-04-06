import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

# joining 2-D arrays

arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4 = np.array([[7, 8, 9], [10, 11, 12]])

arr5 = np.stack((arr3, arr4), axis=1)

print(arr5)

# joining using stack()

arr6 = np.array([1, 2, 3])

arr7 = np.array([4, 5, 6])

arr8 = np.dstack((arr1, arr2))

print(arr8)