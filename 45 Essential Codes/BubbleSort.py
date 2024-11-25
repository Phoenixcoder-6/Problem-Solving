def bubble_sort(arr):
    n= len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                temp= arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr

arr=[4,1,7,9,40,3,2]
res= bubble_sort(arr)
print("The original array:",arr)
print("Sorted array is:",res)