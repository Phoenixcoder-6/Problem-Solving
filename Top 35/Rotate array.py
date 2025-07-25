def rotate(arr,idx):
    left= arr[:idx]
    right= arr[idx:]
    res= right + left
    return res

arr=[1,2,3,4,5]
res= rotate(arr,2)
print(res)