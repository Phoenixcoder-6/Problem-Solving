def multiply_numbers(arr):
    n=len(arr)
    res=[1]*n
    prefix=1
    for i in range(n):
        res[i] = prefix
        prefix*= arr[i]

    suffix = 1
    for i in range(n-1,-1,-1):
        res[i] *= suffix
        suffix *= arr[i]
    return res

arr=[10,3,5,2,1]
res= multiply_numbers(arr)
print(res)