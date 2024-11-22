def max_frequency(arr):
    freq={}
    for num in arr:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1

    max_elem=[]
    max_freq=0
    for key,value in freq.items():
        if freq[key]>max_freq:
            max_freq= freq[key]
            max_elem=key
    return max_elem, max_freq
arr=[1,1,2,2,3,4,5,5,2,8]
res,bes= max_frequency(arr)
print("Most occurrent element:",res,"and it's frequency:",bes)