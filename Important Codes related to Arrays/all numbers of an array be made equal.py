def check(arr1,length):
    for i in range(0,length):
        while arr1[i] % 2 ==0:
            arr1[i] //=2
        while arr1[i] % 3 ==  0:
            arr1[i] //=3

    if arr1[i] % 3 == 0:
        return False
    return True

array= [ 50,200,75]
n= len(array)

if check(array, n):
     print("Yes, all the elements of an array can be made equal")
else:
     print("No, all the elements of an array cannot be made equal")


