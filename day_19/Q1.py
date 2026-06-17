import numpy as np
def matrix_add(A , B):
    return A + B

A = np.array([[1,2,3],[3,4,5],[2,3,1]])
B = np.array([[2,1,3],[2,4,5],[3,7,1]])
print(f"matrix A = {A} \n b is {B} \n sum of matrix is = \n {matrix_add(A , B)}")

