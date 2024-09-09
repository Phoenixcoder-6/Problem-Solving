def rotation(arr,n):
    rot= arr[-n:]+arr[:-n]
    return rot

arr=[10,20,30,40,50]
result= rotation(arr,1)
print(result)