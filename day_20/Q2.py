# symmetry matrix 
import numpy as np
matrix_1 = np.array([[1,2,3],[3,4,5],[2,3,1]])
if (matrix_1 == matrix_1.T).all():
    print("symetry matrix")
else :
    print("not symetry")

