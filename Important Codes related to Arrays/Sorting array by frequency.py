from collections import Counter

def sort_by_frequency(arr):
    freq= Counter(arr)
    sorted_arr= sorted(arr,key=lambda x:(-freq[x],x))
    return sorted_arr

arr=[]
n= int(input("Enter range:"))
for i in range(n):
    ele= int(input(f"Enter element at position {i}:"))
    arr.append(ele)

print(sort_by_frequency(arr))
