def factorial(num):
    res=1
    for i in range(1,num+1):
        res *= i
    return res

print("The factorial is:",factorial(5))