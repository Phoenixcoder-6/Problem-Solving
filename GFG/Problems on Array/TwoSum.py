def twosum(arr,num):
    n=len(arr)
    arr1=[]
    for i in range(n):
        for j in range(i+1,n):
            if i!=j and arr[i]+ arr[j] == num:
                arr1.append((arr[i],arr[j]))
    return arr1

arr=[2,3,4,5,1,3,4]
result= twosum(arr,6)
print(result)