import numpy as np

#Slice elements from index 1 to index 5 from the following array:

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print("Element from index 1 - 5: ", arr[1:5])

# Slice elements from index 4 to the end of the array

print("Slice elements from index 4 to the end of the array: ", arr[4:])

#Slice elements from the beginning to index 4 (not included)
print("Slice elements from the beginning to index 4 (not included): ", arr[0:4])

#Negative slicing
print("Slice from the index 3 from the end to index 1 from the end: ", arr[-3:-1] )

#step
print("Step 1: ", arr[1: 5: 2])
print("Step 1: ", arr[: : 2])

#slicng 2 d arrays
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

#From the second element, slice elements from index 1 to index 4 (not included):
print(arr2[1, 1 : 4])
print(arr2[0:2, 2])
print(arr2[0:2, 1:4])