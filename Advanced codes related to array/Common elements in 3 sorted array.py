""" def check(arr1,arr2,arr3):
    lst=[]
    lst=list(set(arr1) & set(arr2) & set(arr3))
    return lst

arr1=[1,2,3,4,5]
arr2=[2,3,4,5]
arr3=[3,4,5,6]

result=check(arr1,arr2,arr3)
print(result)
"""

# More optimized approach 

def find_common_elements(arr1,arr2,arr3):
    i=0
    j=0
    k=0
    common_elements=[]
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        # If the current elements are the same, add to result and move all pointers
        if arr1[i] == arr2[j] == arr3[k]:
            common_elements.append(arr1[i])
            i += 1
            j += 1
            k += 1
        # If arr1[i] is smaller, increment i
        elif arr1[i] < arr2[j]:
            i += 1
        # If arr2[j] is smaller, increment j
        elif arr2[j] < arr3[k]:
            j += 1
        # If arr3[k] is smaller, increment k
        else:
            k += 1
            
    return common_elements

# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 5]
arr3 = [3, 4, 5, 6]

result = find_common_elements(arr1, arr2, arr3)
print(result)
