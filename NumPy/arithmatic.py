import numpy as np

# Addition
arr1 = np.array([12, 13, 14, 15, 16])
arr2 = np.array([1, 2, 3, 4, 5])

x = np.add(arr1, arr2)
print(x)

# subtraction


arr3 = np.array([12, 13, 14, 15, 16])
arr4 = np.array([1, 2, 3, 4, 5])

y = np.subtract(arr3, arr4)
print(y)

# multiplication


arr5 = np.array([12, 13, 14, 15, 16])
arr6 = np.array([1, 2, 3, 4, 5])

z = np.multiply(arr5, arr6)
print(z)

# divition


arr7 = np.array([12, 13, 14, 15, 16])
arr8 = np.array([1, 2, 3, 4, 5])

a = np.divide(arr7, arr8)
print(a)

# power


arr9 = np.array([12, 13, 14, 15, 16])
arr10 = np.array([1, 2, 3, 4, 5])

b = np.power(arr9, arr10)
print(b)

# mod or reminder

import numpy as np

arr11 = np.array([10, 20, 30, 40, 50, 60])
arr12 = np.array([3, 7, 9, 8, 2, 33])

c = np.mod(arr11, arr12)

print(c)

# Quetient or mod

import numpy as np

arr13 = np.array([10, 20, 30, 40, 50, 60])
arr14 = np.array([3, 7, 9, 8, 2, 33])

d = np.divmod(arr13, arr14)

print(d)

# absolute values

import numpy as np

arr15 = np.array([-1, -2, 1, 2, 3, -4])

e = np.absolute(arr15)

print(e)