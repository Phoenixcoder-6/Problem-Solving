def check(arr):
    s=set()
    for (x,y) in arr:
        s.add((x,y))
    if (y,x) in s:
        print((x,y))

arr=[(3,4),(6,7),(4,3)]
result= check(arr)
print(result)
        

