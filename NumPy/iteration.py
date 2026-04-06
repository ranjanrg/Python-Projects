import numpy as np

# Iterating on 1-D array
arr = np.array([1, 2, 3, 4, 5])

for x in arr:
  print(x)

# Iterating on 2-D array

arr1 = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr1:
  for y in x:
    print(y)

# Iterating on 3-D array

arr2 = np.array([[[1, 2, 3], [4, 5, 6]]])

for x in arr2:
  for y in x:
    for z in y:
      print(z)


# iterating using nditer() function

arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr3):
  print(x)


# iterating array with differernt data type

arr4 = np.array([1, 2, 3])

for x in np.nditer(arr4, flags=["buffered"], op_dtypes= ['S']):
  print(x)


arr5 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr5[:, ::2]):
  print(x)


# ndenumerate() function

arr6 = np.array([1, 2, 3, 4])

for idx, x in np.ndenumerate(arr6):
  print(idx, x)

arr7 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr7):
  print(idx, x)