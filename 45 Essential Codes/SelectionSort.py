def SelectionSort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]= arr[min_index],arr[i]
    return arr

arr=[22,4,6,1,89,34,69]
res= SelectionSort(arr)
print("Original array:",arr)
print("Sorted array:",res)
