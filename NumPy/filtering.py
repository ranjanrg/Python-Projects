import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = []

for element in arr:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)


arr1 = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr1 = []

for element in arr1:
  if element % 2 == 0:
    filter_arr1.append(True)
  else:
    filter_arr1.append(False)

newarr1 = arr1[filter_arr1]

print(filter_arr1)
print(newarr1)


arr2 = np.array([41, 42, 43, 44])

filter_arr2 = arr2 > 42

newarr2 = arr2[filter_arr2]

print(filter_arr2)
print(newarr2)