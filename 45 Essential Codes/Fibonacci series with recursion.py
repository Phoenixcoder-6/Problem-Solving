def fibonacci(n):
    if(n<=1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n= int(input("Enter the term:"))
for i in range(0,n):
    print(fibonacci(i))
