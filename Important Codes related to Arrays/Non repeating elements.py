def count(arr):
    freq={}
    non_repeat=[]
    for num in arr:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1

    for num in arr:
        if freq[num]==1:
            non_repeat.append(num)

    return non_repeat
arr=[10,20,30,10,10,40,40]
result= count(arr)
print(set(result))