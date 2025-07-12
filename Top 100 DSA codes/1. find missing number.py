def findnumber(arr):
    n= len(arr)
    sum1=0
    sum2=0
    max_num= max(arr)
    min_num= min(arr)
    #Calculating arraysum
    for i in range(n):
        sum1 += arr[i]
    for i in range(min_num,max_num+1):
        sum2 += i
    return sum2-sum1

arr=[2,3,4,6]
res= findnumber(arr)
print("The missing number is:", res)