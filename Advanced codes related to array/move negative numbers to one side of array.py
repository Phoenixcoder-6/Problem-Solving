def sorted_arr(arr):
    left=[]
    right=[]
    for i in arr:
        if i<0:
            left.append(i)
        else:
            right.append(i)
        
    return left+right


arr=[1,3,-1,4,-3,-5,-6,3,7]
result= sorted_arr(arr)
print(result)
