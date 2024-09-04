def repeat(arr):
    freq={}
    repeats=[]
    for num in arr:
        if num in freq:
            if freq[num]==1:
                repeats.append(num)
            freq[num]+=1
        else:
            freq[num]=1
                
    return repeats
        
        

arr=[10,20,20,20,30,10]
result= repeat(arr)
print(result)
