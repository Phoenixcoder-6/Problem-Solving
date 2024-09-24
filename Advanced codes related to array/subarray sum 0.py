def subarray(arr,sum):
    n= len(arr)
    lst=[]
    for i in range(n):
        current_sum=0
        for j in range(i,n):
            current_sum+=arr[j]

            if current_sum==sum:
                lst.append((arr[i:j+1]))

    return lst

arr=[1,2,-3,3,1]
result= subarray(arr,0)
print(result)
            