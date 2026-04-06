import numpy as np

arr = np.array([1, 6, 3, 0])

x = np.sort(arr)

print(x)

# sorting array fo strings

arr1 = np.array(['banana', 'apple', 'mango'])

y = np.sort(arr1)

print(y)

# sorting boolean array

arr2 = np.array([True, False, True])

print(np.sort(arr2))

# sorting 2-D arrays

arr3 = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr3))