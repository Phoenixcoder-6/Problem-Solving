def union(arr1,arr2):
    uni= list(set(arr1) | set(arr2))
    return uni
def intersection(arr1,arr2):
    inter= list(set(arr1)& set(arr2))
    return inter

arr1=[1,2,5,7,8,9]
arr2=[4,2,6,7,9,1]

result1= union(arr1,arr2)
result2= intersection(arr1,arr2)

print("Union:", result1)
print("Intersection:",result2)