import numpy as np

def inverse_mat(matrix):
    try:
        inverse=  np.linalg.inv(matrix)
        return inverse
    except np.linalg.LinAlgError:
        return "Invalid!!"
    
A=np.array([[3,4],
   [5,6]])

res= inverse_mat(A)
print(res)
