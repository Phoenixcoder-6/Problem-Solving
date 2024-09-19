def kadane(arr):
    max_sum= float('-inf')
    for i in range(len(arr)):
        current_sum=0
        for j in range(i,len(arr)):
            current_sum+=arr[j]

            if current_sum> max_sum:
                max_sum= current_sum

    return max_sum


arr=[5,4,-1,7,8]
result= kadane(arr)
print(result)

