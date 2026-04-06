import numpy as np

arr = np.array([1, 2, 3, 4, 5] , dtype = 'i4')
arr1 = np.array(['r', 'a', 'n'])
arr2 = np.array(['apple', 'banana', 'cherry'], dtype='U')

print(arr.dtype)

#converting data type

arr3 = np.array([-1, 0, 1])
newarr = arr3.astype(bool)
print(arr3.dtype)
print(newarr)
print(newarr.dtype)