def check(arr1,arr2):
    for i in arr1:
        for j in arr2:
            if i==j:
                print("Not disjoint")
                return

        
    print("Disjoint")

arr1=[1,2,3,4]
arr2=[1,6,7,8]
check(arr1,arr2)


