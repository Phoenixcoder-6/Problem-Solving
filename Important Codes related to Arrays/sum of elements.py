# Using iteration
'''
arr=[2,4,5,7,8]
x=0
for i in arr:
    x +=i

print(x) '''

#Using recursion

def summation(arr,n):
    if n == 0:
        return 0
    else:
        return arr[n-1] + summation(arr,n-1)
arr= [10,20,45]
print(summation(arr,len(arr)))