def subset(arr1,arr2):
    for elem in arr1:
        if elem in arr2:
            return "Subset"
    else:
        return "Not Subset"
    
arr1=[1,2,3,4,5]
arr2=[1,2,3,4,5,6,7]
res=subset(arr1,arr2)
print(res)