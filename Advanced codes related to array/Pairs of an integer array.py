def pairs(arr,sum):
    n= len(arr)
    lst=[]
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j] == sum:
                lst.append((arr[i],arr[j]))
    return lst

arr=[5,2,3,4,1,6,7]
result= pairs(arr,7)
print(result)
