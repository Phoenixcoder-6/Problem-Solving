def InsertionSort(arr):
    n= len(arr)
    arr=arr.copy()
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>arr[i]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]=key
    return arr

arr=[34,1,3,2,89,45]
res= InsertionSort(arr)
print("Original Array:",arr)
print("Sorted array:",res)