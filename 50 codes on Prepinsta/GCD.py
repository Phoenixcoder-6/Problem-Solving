def gcd(a,b):
    result= min(a,b)
    while result:
        if  a%result==0 and b%result==0:
            break
        result-=1

    return result


a=98
b=56
res= gcd(a,b)
print("gcd is:",res)