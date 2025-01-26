def repeate_elements(arr):
    n=len(arr)
    duplicates=[]
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] ==arr[j]:
                duplicates.append(arr[j])
    return duplicates

arr=[1,2,3,4,2,3,1,6,5,7,4]
res= repeate_elements(arr)
print(res)