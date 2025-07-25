def twosum(arr,target):
    res=[]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == target:
                res.append([arr[i],arr[j]])         
    return res


arr=[1,2,3,4,5]
target=7
res= twosum(arr,target)
print(res)
