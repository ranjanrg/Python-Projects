import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Get the first element
print("The first element is: ", arr[0])

# Get the second element
print("The first element is: ", arr[1])

# Get third and fourth elements from the following array and add them.
print("Sum of 3rd and 4th element is: ", arr[2] + arr[3])

# 2 Dimensional

arr1 = np.array([[1, 2, 3, 4, 5], 
                 [6, 7, 8, 9, 0]])

# Print the last element from the 2nd dim:
print("the last element from the 2nd dim: ", arr1[1, -1])

# Access the element on the first row, second column:
print("the element on the first row, second column: ", arr1[0, 1])

#  Access the element on the 2nd row, 5th column:
print("the element on the 2nd row, 5th column:", arr1[1, 4])

## Dimensional

arr2 = np.array([[[1, 2, 3], [4, 5, 6],[7, 8, 9], 
                  [0, 1 , 2], [3, 4, 5], [6, 7, 8]]])

# Access the third element of the second array of the first array:
print("the third element of the second array of the first array: ", arr2[0, 1, 2])