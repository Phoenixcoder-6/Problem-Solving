def sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]

arr=[2,4,6,8]
result= sum(arr,10)
print(result)
