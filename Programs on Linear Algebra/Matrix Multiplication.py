def matrix_multiplication(A,B):
    if len(A[0]) != len(B):
        raise ValueError("Invalid!!")
    
    m= len(A)
    n= len(B[0])
    p=len(B)

    result= [[0 for _ in range(n)]for _ in range(m)]

    for i in range(n):
        for j in range(m):
            for k in range(p):
                result[i][j]= A[i][k] * B [k][j]

    return result


def print_matrix(matrix):
    for row in matrix:
        print(row)


A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]
try:
    result = matrix_multiplication(A, B)
    print("\nResult of A x B:")
    print_matrix(result)
except ValueError as e:
    print(e)
