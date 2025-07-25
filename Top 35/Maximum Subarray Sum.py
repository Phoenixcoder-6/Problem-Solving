def kadane(arr):
    max_sum= float('-inf')
    start_index= end_index =0
    for i in range(len(arr)):
        current_sum=0
        for j in range(i,len(arr)):
            current_sum += arr[j]

            if current_sum > max_sum:
                max_sum = current_sum
                start_index=i
                end_index=j
    
    return max_sum, start_index,end_index

arr= [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result,start,end = kadane(arr)
print("Max Sum:", result, " Starting Index:", start, " End Index:", end)


