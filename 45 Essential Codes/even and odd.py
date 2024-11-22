def evenodd(arr):
    even=[]
    odd=[]
    n=len(arr)
    for i in range(n):
        if arr[i] %2 ==0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
        
    return even,odd

arr=[4,23,6,9,98,64,1,13]
even,odd= evenodd(arr)
print(even,odd)
