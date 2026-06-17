import numpy as np

A = np.array([[1,2,3],[3,4,5],[2,3,1]])
n = len(A)
sum_value = 0
for i in range(n):
    for j in range(i):
        if (A[i] == A[j]).any():
            print("Match:", A[i], A[j])
            sum_value += np.sum(A[j])

print(sum_value)
