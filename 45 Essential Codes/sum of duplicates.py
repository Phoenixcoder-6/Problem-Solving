def sumduplicates(arr):
    freq={}
    for num in arr:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1

    
    sorted_set=0
    for i in freq:
        if freq[i]>1:
            sorted_set+= i* freq[i]

    return freq,sorted_set

arr=[1,3,2,4,1,1,3,2,5]
res,summation= sumduplicates(arr)
print("The frequencies are:",res,"The summation of duplicates are:",summation)
        