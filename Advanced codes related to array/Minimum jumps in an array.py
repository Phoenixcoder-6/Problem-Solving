def jump(arr):
    ans = 0
    i = 0
    while i < len(arr) - 1:
        if i + arr[i] < len(arr):
            ans += 1
            if arr[i] == 1:
                i += arr[i]
            else:
                i += arr.index(max(arr[i + 1:arr[i] + i + 1])) - i
        else:
            ans += 1
            i += arr[i]

    return ans


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print("Minimum no of jumps required to reach end of the array : ", jump(arr))