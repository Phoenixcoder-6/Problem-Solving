def fibonacci(n):
    first,second=0,1
    print("The fibonacchi series is:",first,second,end=" ")
    for i in range(2,n):
        third= first+second
        first=second
        second=third
        print(third,end=" ")
    return

n=7
res= fibonacci(n)
print(res)
