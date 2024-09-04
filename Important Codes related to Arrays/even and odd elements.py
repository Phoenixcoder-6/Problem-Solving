def check(arr):
    odd=[]
    even=[]
    for i in arr:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return len(even),len(odd)

arr=[1, 7, 8, 4, 5, 16, 8]
result= check(arr)
print(result)