def summation(A,B):
    n=len(A)
    max_sum=0

    for front_count in range(min(B,n)+1):
        back_count= B-front_count

        sum_front= sum(A[:front_count]) if front_count > 0 else 0
        sum_back= sum(A[-back_count:]) if back_count > 0 else 0

        max_sum= max(max_sum,(sum_front+sum_back))

    return max_sum


A=[5, -2, 3 , 1, 2]
B=3
result= summation(A,B)
print(result)