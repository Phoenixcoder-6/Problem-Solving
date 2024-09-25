def find_element(arr, k):
    n = len(arr)
    freq = {}
    result_set = set()
    
    # Count the frequency of each element
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    # Iterate through the frequency dictionary
    for i in freq:  # We use freq.keys() to avoid duplicates
        if freq[i] >= n // k:  # Use floor division to avoid floating-point errors
            result_set.add(i)

    return list(result_set)

arr = [1, 2, 2, 4, 3, 5]
result = find_element(arr,3)
print(result)
