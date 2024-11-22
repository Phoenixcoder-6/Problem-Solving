def average(arr):
    n=len(arr)
    summation=0
    for i in range(len(arr)):
        summation+=arr[i]

    return summation/n


arr=[1,4,3,6,5]
res= average(arr)
print(res)
