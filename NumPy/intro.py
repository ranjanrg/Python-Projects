import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))
print(np.__version__)

#Use a tuple to create a NumPy array:

arr = np.array((1, 2, 3, 4,5))

print(arr)

#Zero Dimensional array

arr = np.array(23)
print(arr)

#One Dimensional Array

arr = np.array([1, 2, 3, 4])
print(arr)
print(arr.ndim)


#Two dimensional array

arr = np.array([[1, 2], [3, 4]])
print(arr)
print(arr.ndim)

#Three dimensional array
arr = np.array([[[1, 2, 3,], [4, 5, 6],
               [7, 8, 8], [10, 11, 12],
               [13, 14, 15], [16, 17, 18]]])

print(arr)
print(arr.ndim)