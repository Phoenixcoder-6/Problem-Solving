def check(arr):
    new_arr= arr.copy()
    new_arr.sort()

    for i in range(len(arr)):
        for j in range(len(new_arr)):
            if arr[i]==new_arr[j]:
                arr[i] = j+1
                break

arr=[100,34,23,67,98]
check(arr)
print(arr)
