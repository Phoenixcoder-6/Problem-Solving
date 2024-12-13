import numpy as np

diagonal_elements=[5,2,-3]
D= np.diag(diagonal_elements)
print("Diagonal matrix is:\n",D)

#Diagonal matrix multiplication
A=np.diag([1,2,3])
B= np.diag([7,8,9])

G= np.dot(A,B)
print("Multiplication of two diagonal matrix is:")
print(G)