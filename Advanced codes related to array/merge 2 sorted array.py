def find(arr1,arr2,n1,n2):
    for i in arr2:
        arr1.append(i)
    arr1=list(set(sorted(arr1)))

    arr2=arr1[len(arr1)-n2:]
    arr1= arr1[:len(arr1)-n2]

    print("After:")
    print("Array1:",arr1,"Array2:",arr2)


arr1=[1,2,3,5,8,9,10,13,15,20]
arr2= [2,3,8,13]

print("Before:")
print("Array1:",arr1)
print("Array2:",arr2)

find(arr1,arr2,len(arr1),len(arr2))