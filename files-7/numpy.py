import numpy as np

arr = np.array([[1, 4, 3], [7, 6, 5], [2, 3, 1]])
print(arr)
print(np.sort(arr, 0))  # Sort along axis 0 (columns)
print(np.sort(arr, 1))  # Sort along axis 1 (rows)


arr = np.full((5,5), 7)
new_arr = np.insert(arr, 2, 9, 1)
print(arr)

arr = np.array([1,2,3], [4,5,6], [7,8,9])
arr_1 = arr.delete(arr, 1, 0)
arr_2 = arr.delete(arr, 0, 1)

arr = np.array([[1,2], [2,3]])
print(type(arr))
print(arr.shape)
print(arr)
