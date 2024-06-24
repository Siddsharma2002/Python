import numpy as np

arr = list((1, 2, 3, 4, 5))

print(arr)


arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

arr = np.array([1, 2, 3, 4], ndmin=6)

print(arr)
print('number of dimensions :', arr.ndim)
arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4])
#Slicing in python means taking elements from one given index to another given index.
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])
#Make a copy, change the original array, and display both arrays
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)
#Convert the array into a 1D array:

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)
#
arr = np.array([1, 2, 3])

for x in arr:
  print(x)

for x in arr:
  print(x)

for x in arr:
  print(x)
#Join two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
#Join two 2-D arrays along rows (axis=1)
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)