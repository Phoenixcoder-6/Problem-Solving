def fibonacci(n):
    first=0
    second=1
    fibb=[first,second]
    for i in range(2,n):
        next= first + second
        fibb.append(next)
        first = second
        second = next
    return fibb

n=9
res=fibonacci(n)
print(res)


    


