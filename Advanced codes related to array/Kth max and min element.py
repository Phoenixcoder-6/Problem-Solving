def min_element(arr,k):
    arr.sort()
    return arr[k]
arr=[2,3,6,1,8,9]
result1= min_element(arr,5)
print(arr)
print("Kth minimum element is:",result1)


def max_element(arr,k):
    return arr[k]

arr1=[2,3,6,1,8,9]
arr1= sorted(arr1,reverse= True)
print(arr1)
result2= max_element(arr1,3)
print("Kth maximum element is:",result2)
#print(result2)

