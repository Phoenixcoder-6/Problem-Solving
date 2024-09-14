def largest_sum(arr):
    max_sum=max_current= arr[0]
    for i in range(1,len(arr)):
        max_sum= max(arr[i],max_sum+ arr[i])
        if max_sum< max_current:
            max_sum= max_current
    return max_sum

arr=[2,4,5,6,8]
result= largest_sum(arr)
print(result)
