def reverse(arr):
    res=[]
    for i in range(len(arr)-1,-1,-1):
        res.append(arr[i])
    return res

arr=[1,2,3,4,5]
res= reverse(arr)
print(res)