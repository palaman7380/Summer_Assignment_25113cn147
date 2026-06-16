import numpy as np

arr_1 = np.array([1, 2, 3, 4])
arr_2 = np.array([4, 5, 6, 5])

union = np.union1d(arr_1, arr_2)

print("The union of arrays:", union)