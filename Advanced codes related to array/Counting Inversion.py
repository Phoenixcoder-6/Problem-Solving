def pairs(arr):
    n= len(arr)
    list=[]
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                list.append((arr[i],arr[j]))
    return list

arr=[6,3,5,2,7]
rsult= pairs(arr)
print(rsult)