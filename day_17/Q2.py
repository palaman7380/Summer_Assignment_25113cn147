import numpy as np

arr_1 = np.array([1, 2, 3,4])
arr_2 = np.array([4, 5, 6,5])
n1 = len(arr_1)
n2 = len(arr_2)
ans = []
for i in range(n1):
    for j in range(n2):
        if arr_1[i] == arr_2[j]:
            ans.append(arr_1[i])

print("the intersection of an array " ,ans)