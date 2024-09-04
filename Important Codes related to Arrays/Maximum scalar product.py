arr1=[1,3,-5]
arr2 = [-2,4,1]
arr3=[]

arr1=sorted(arr1)
arr2=sorted(arr2, reverse=True)
print(arr1,arr2)

for i in range(len(arr1)):
    arr3.append(arr1[i]*arr2[i])

print("new vector:",arr3)

print("Sum:",sum(arr3))

#for i in range(len(arr1)):
    #arr3= arr1[i]*arr2[i]

#print(arr3)
#print(sum(arr3))