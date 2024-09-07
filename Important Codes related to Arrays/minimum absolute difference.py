import sys
def sum(arr,n):
    result=sys.maxsize
    for i in range(0,n):
        sum=0
        for j in range(0,n):
            sum+= abs(arr[i]-arr[j])
        result= min(result,sum)
    return result

arr=[2,5,4,3]
n= len(arr)
result= sum(arr,n)
print(result)