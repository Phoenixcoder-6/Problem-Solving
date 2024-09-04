arr1=[1,2,3]
arr2=[4,5,6]
arr3=[]
for i in range(len(arr1)):
    arr3.append(arr1[i]*arr2[i])

print("New Vector:",arr3)
print("product is:",sum(arr3))