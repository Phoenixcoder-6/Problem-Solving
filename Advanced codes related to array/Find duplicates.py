def duplicates(arr):
    arr1=[]

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                arr1.append(arr[i])
                break
    return arr1
    
arr=[1,3,2,5,1,2,3]
duplicates= duplicates(arr)
print(duplicates)