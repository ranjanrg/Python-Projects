import numpy as np

# Make a copy, change the original array, and display both arrays:
arr = np.array([1, 2, 3, 4, 5])

newarr = arr.copy()

arr[0] = 12

print(arr)

print(newarr)

# Make a view, change the original array, and display both arrays:

arr1 = np.array([1, 2, 3, 4, 5])

newarr1 = arr1.view()

arr1[0] = 34
newarr1[0] = 10

print(arr1)
print(newarr1)

# Print the value of the base attribute to check if an array owns it's data or not:

x = np.array([1, 2, 3, 4, 5])

y = x.copy()
z = x.view()

print(y.base)
print(z.base)